"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI. NHÓM VIẾT phần gọi model thật.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng

Hỗ trợ sẵn (thuần thư viện chuẩn Python, không cần pip install):
    MODEL_PROVIDER=fake       chế độ giả mặc định khi chưa điền .env
    MODEL_PROVIDER=gemini     Google Gemini API (generativelanguage.googleapis.com)
    MODEL_PROVIDER=openai     OpenAI API hoặc nhà cung cấp tương thích (đặt thêm API_BASE_URL nếu khác OpenAI)
    MODEL_PROVIDER=anthropic  Anthropic Claude API
    MODEL_PROVIDER=ollama     Ollama chạy cục bộ (http://localhost:11434/api/chat)

Không dán API key vào file này — điền trong .env (đã nằm trong .gitignore).
"""
import json
import os
import urllib.error
import urllib.parse
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOW_RAW = False  # Đổi thành True khi cần in phản hồi JSON gốc để kiểm tên trường usage


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có. Khung — không cần sửa."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()
API_BASE_URL = (os.environ.get("API_BASE_URL") or "").strip()

URL_OPENAI = "https://api.openai.com/v1/chat/completions"
URL_CLAUDE = "https://api.anthropic.com/v1/messages"
URL_OLLAMA = "http://localhost:11434/api/chat"


def post_json(url: str, headers: dict, body: dict, timeout: int = 60) -> dict:
    """Gửi POST JSON, trả về dict phản hồi. Chỉ dùng thư viện chuẩn (urllib)."""
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers=dict({"Content-Type": "application/json"}, **headers),
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:400]
        raise RuntimeError("HTTP %d: %s" % (e.code, detail))
    if SHOW_RAW:
        print(json.dumps(data, ensure_ascii=False, indent=2)[:3000])
    return data


def _require_key_and_model():
    if not MODEL_NAME:
        raise RuntimeError("Thiếu MODEL_NAME trong .env (ví dụ gemini-3.1-flash-lite hoặc gpt-5.4-nano).")
    if MODEL_PROVIDER != "ollama" and not API_KEY:
        raise RuntimeError("Thiếu API_KEY trong .env cho MODEL_PROVIDER=%s." % MODEL_PROVIDER)


def call_gemini(system: str, user: str) -> dict:
    _require_key_and_model()
    model_enc = urllib.parse.quote(MODEL_NAME, safe="")
    base = API_BASE_URL.rstrip("/") if API_BASE_URL else "https://generativelanguage.googleapis.com/v1beta"
    url = f"{base}/models/{model_enc}:generateContent"
    body = {
        "contents": [{"role": "user", "parts": [{"text": user}]}],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 1024},
    }
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    data = post_json(url, {"x-goog-api-key": API_KEY}, body)
    candidates = data.get("candidates") or []
    if not candidates:
        raise RuntimeError("Gemini không trả về candidates: %s" % json.dumps(data, ensure_ascii=False)[:300])
    parts = (candidates[0].get("content") or {}).get("parts") or []
    text = "".join(p.get("text", "") for p in parts if not p.get("thought"))
    usage = data.get("usageMetadata") or {}
    tokens_in = int(usage.get("promptTokenCount", 0))
    # Bao gồm cả token suy luận (thoughtsTokenCount) nếu model tính riêng
    tokens_out = int(usage.get("candidatesTokenCount", 0)) + int(usage.get("thoughtsTokenCount", 0))
    return {"text": text, "tokens_in": tokens_in, "tokens_out": tokens_out}


def call_openai(system: str, user: str) -> dict:
    _require_key_and_model()
    url = API_BASE_URL or URL_OPENAI
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json(
        url,
        {"Authorization": "Bearer " + API_KEY},
        {"model": MODEL_NAME, "messages": messages, "temperature": 0.2},
    )
    usage = data.get("usage") or {}
    text = data["choices"][0]["message"]["content"]
    return {
        "text": text,
        "tokens_in": int(usage.get("prompt_tokens", 0)),
        "tokens_out": int(usage.get("completion_tokens", 0)),
    }


def call_claude(system: str, user: str) -> dict:
    _require_key_and_model()
    url = API_BASE_URL or URL_CLAUDE
    data = post_json(
        url,
        {"x-api-key": API_KEY, "anthropic-version": "2023-06-01"},
        {
            "model": MODEL_NAME,
            "max_tokens": 1024,
            "temperature": 0.2,
            "system": system or "",
            "messages": [{"role": "user", "content": user}],
        },
    )
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    usage = data.get("usage") or {}
    return {
        "text": text,
        "tokens_in": int(usage.get("input_tokens", 0)),
        "tokens_out": int(usage.get("output_tokens", 0)),
    }


def call_ollama(system: str, user: str) -> dict:
    _require_key_and_model()
    url = API_BASE_URL or URL_OLLAMA
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json(url, {}, {"model": MODEL_NAME, "messages": messages, "stream": False}, timeout=300)
    return {
        "text": data["message"]["content"],
        "tokens_in": int(data.get("prompt_eval_count", 0)),
        "tokens_out": int(data.get("eval_count", 0)),
    }


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {
            "text": "[câu trả lời giả — chưa nối model] " + last[:60],
            "model": "fake",
            "tokens_in": 0,
            "tokens_out": 0,
        }

    if MODEL_PROVIDER == "gemini":
        r = call_gemini(system, user)
    elif MODEL_PROVIDER in ("openai", "openai_compatible", "deepseek", "groq", "openrouter"):
        r = call_openai(system, user)
    elif MODEL_PROVIDER in ("anthropic", "claude"):
        r = call_claude(system, user)
    elif MODEL_PROVIDER == "ollama":
        r = call_ollama(system, user)
    else:
        raise NotImplementedError(
            "Chưa hỗ trợ MODEL_PROVIDER=%s trong codebase/ai.py — chọn gemini / openai / anthropic / ollama (xem docs/connect-model.md)."
            % MODEL_PROVIDER
        )

    return {
        "text": r["text"],
        "model": MODEL_NAME,
        "tokens_in": int(r["tokens_in"]),
        "tokens_out": int(r["tokens_out"]),
    }
