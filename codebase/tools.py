"""Công cụ của bài toán — NHÓM VIẾT. Điền ở guide bước 2.2 (thiết kế) và 3.2 (code).

Mỗi công cụ là một hàm Python có @tool. Docstring ghi đúng 4 ý như sơ đồ ở spec.md §4:
    tên · input · output · có tác động ra ngoài không (gửi tin, sửa dữ liệu, chấm điểm…)
Khung tự ghi mỗi lần gọi công cụ vào trace (tên, input, output rút gọn, thời gian, lỗi).

Dữ liệu công cụ đọc: data/sample_lessons.json (mô tả tại data/DATA_CARD.md).
"""
import json
import os
import re
import unicodedata

from tracing import tool, TOOLS  # noqa: F401

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSONS_PATH = os.path.join(ROOT, "data", "sample_lessons.json")

_STOPWORDS = {
    "la", "va", "cua", "cho", "khi", "thi", "co", "khong", "duoc", "trong",
    "nhu", "voi", "mot", "cac", "nhung", "nay", "do", "de", "tu", "den",
    "ve", "bang", "hay", "hoac", "giua", "tai", "sao", "gi", "nao", "the",
    "toi", "minh", "em", "ban", "khai", "niem", "giai", "thich", "bai",
    "hoc", "lab", "pre", "class", "preclass", "xem", "lai", "kien", "thuc",
    "chi", "can", "phai", "neu", "vi", "nen", "se", "da", "dang", "con",
    "dung", "sai", "ro", "hon", "them", "nua", "vong", "cau", "tra", "loi",
    # Từ vựng ML/AI quá chung chung — không tự đại diện riêng cho một khái niệm cụ thể
    "ai", "llm", "model", "mo", "hinh", "ngon", "ngu", "du", "lieu", "dau",
    "vao", "ra", "ham", "so", "ket", "qua", "phan", "tich", "huan", "luyen",
    "tap", "chay", "cach", "he", "thong", "danh", "gia", "tham", "truoc",
    "sau", "moi", "tinh", "toan", "su", "biet", "hieu", "nham", "tuong",
    "nghi", "thu", "kiem", "chinh", "xac", "tot", "hon", "gioi", "han",
}

_TOPIC_PREFIX_RE = re.compile(
    r"^(?:y\s+dang\s+on|khai\s+niem|chu\s+de|tinh\s+huong\s+kiem\s+thu\s*:\s*y\s+dang\s+on\s+la)\s*[:\-]?\s*([^\.\n;]+)",
    re.IGNORECASE,
)

_CACHE = None


def _load_lessons() -> dict:
    global _CACHE
    if _CACHE is None:
        with open(LESSONS_PATH, encoding="utf-8") as f:
            _CACHE = json.load(f)
    return _CACHE


def _normalize(text: str) -> str:
    text = text.replace("đ", "d").replace("Đ", "D")
    nfkd = unicodedata.normalize("NFKD", text)
    ascii_text = "".join(ch for ch in nfkd if not unicodedata.combining(ch))
    ascii_text = ascii_text.lower()
    ascii_text = re.sub(r"[^a-z0-9_]+", " ", ascii_text)
    return re.sub(r"\s+", " ", ascii_text).strip()


def _tokens(text: str) -> set:
    return {t for t in _normalize(text).split() if len(t) >= 2 and t not in _STOPWORDS}


def _extract_declared_topic(query: str) -> str:
    """Tách tên khái niệm nếu đầu vào ghi rõ tiêu đề (vd 'Ý đang ôn: ...' hoặc '<Khái niệm>: ...')."""
    norm_raw = query.replace("đ", "d").replace("Đ", "D")
    norm_raw = "".join(ch for ch in unicodedata.normalize("NFKD", norm_raw) if not unicodedata.combining(ch))
    m = _TOPIC_PREFIX_RE.match(norm_raw.strip())
    if m:
        return m.group(1).strip()
    if ":" in norm_raw:
        head = norm_raw.split(":", 1)[0].strip()
        if 2 <= len(head) <= 45 and len(head.split()) <= 7:
            return head
    return ""


def _alias_score(text_norm: str, concept: dict) -> float:
    score = 0.0
    cid_norm = _normalize(concept["concept_id"].replace("_", " "))
    if concept["concept_id"].lower() in text_norm or (cid_norm and f" {cid_norm} " in f" {text_norm} "):
        score += 10.0

    for alias in concept.get("aliases", []):
        a_norm = _normalize(alias)
        if not a_norm:
            continue
        if f" {a_norm} " in f" {text_norm} ":
            score += 6.0 if " " in a_norm else 5.0
    return score


def _score_concept(query: str, concept: dict) -> float:
    q_norm = _normalize(query)
    if not q_norm:
        return 0.0

    # 1. Điểm khớp từ khoá đặc trưng (concept_id / aliases) trong toàn văn bản
    base_alias = _alias_score(q_norm, concept)

    # 2. Nếu người học ghi rõ tiêu đề khái niệm ở đầu câu (vd "Ý đang ôn: RAG..."), ưu tiên cao hơn
    declared = _extract_declared_topic(query)
    declared_bonus = 0.0
    if declared:
        d_norm = _normalize(declared)
        declared_bonus = 1.5 * _alias_score(d_norm, concept)

    # 3. Nếu không có bất kỳ từ khoá đặc trưng nào của khái niệm khớp, không cộng điểm nhiễu từ nội dung chung
    if base_alias == 0.0 and declared_bonus == 0.0:
        return 0.0

    q_toks = _tokens(query)
    title_toks = _tokens(concept.get("title", ""))
    passage_text = " ".join(p["text"] for p in concept.get("passages", []))
    passage_toks = _tokens(passage_text)

    return base_alias + declared_bonus + 1.5 * len(q_toks & title_toks) + 0.4 * len(q_toks & passage_toks)


def list_concept_titles() -> list:
    """Helper nội bộ (không phải @tool): trả danh sách (concept_id, title) để nhắc phạm vi học liệu."""
    data = _load_lessons()
    return [(c["concept_id"], c["title"]) for c in data.get("concepts", [])]


def resolve_concept_id(query: str) -> str:
    """Helper nội bộ: tìm mã khái niệm khớp tốt nhất với query, rỗng nếu dưới ngưỡng."""
    data = _load_lessons()
    best_id = ""
    best_score = 0.0
    for concept in data.get("concepts", []):
        s = _score_concept(query, concept)
        if s > best_score:
            best_score = s
            best_id = concept["concept_id"]
    return best_id if best_score >= 4.5 else ""


@tool
def search_lesson(query: str) -> list:
    """search_lesson · Input: tên khái niệm + lời giải thích của học viên (str) · Output: danh sách đoạn học liệu {"code", "text"}, rỗng nếu không có đoạn khớp · Tác động ra ngoài: Không (chỉ đọc)."""
    data = _load_lessons()
    scored = []
    for concept in data.get("concepts", []):
        s = _score_concept(query, concept)
        if s >= 4.5:
            scored.append((s, concept))
    if not scored:
        return []
    scored.sort(key=lambda item: item[0], reverse=True)
    # Lấy các đoạn học liệu của khái niệm khớp nhất (mỗi phiên 1 ý cốt lõi theo spec.md §4)
    top_concept = scored[0][1]
    return [{"code": p["code"], "text": p["text"]} for p in top_concept.get("passages", [])]


@tool
def get_key_points(concept_code: str) -> list:
    """get_key_points · Input: mã khái niệm (str) · Output: danh sách ý chính chuẩn kèm mã đoạn {"code", "point"}, rỗng nếu không có · Tác động ra ngoài: Không (chỉ đọc)."""
    if not concept_code:
        return []
    data = _load_lessons()
    target = concept_code.strip().lower()
    for concept in data.get("concepts", []):
        if concept["concept_id"].lower() == target:
            return [{"code": kp["code"], "point": kp["point"]} for kp in concept.get("key_points", [])]
    resolved = resolve_concept_id(concept_code)
    if resolved:
        for concept in data.get("concepts", []):
            if concept["concept_id"] == resolved:
                return [{"code": kp["code"], "point": kp["point"]} for kp in concept.get("key_points", [])]
    return []
