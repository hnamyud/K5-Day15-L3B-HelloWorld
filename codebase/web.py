"""Giao diện web cho phiên tự ôn (bản demo). Chạy bằng `python codebase/web.py` rồi mở http://localhost:8765.

Chỉ dùng thư viện chuẩn. Server một luồng, giữ một phiên ôn trong bộ nhớ (đủ cho demo trên một máy).
Luồng ôn dùng nguyên `StudySession` (session.py) và `answer` (agent.py) như `app.py`; file này chỉ thay lớp nhập/xuất.
Kết thúc phiên thì xoá trạng thái tạm, không ghi lời giải thích ra file (spec.md §9).
"""
import csv
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import tracing  # noqa: E402
from agent import answer  # noqa: E402
from guardrails import ENOUGH, NEEDS_WORK, NO_SOURCE, OUT_OF_SCOPE  # noqa: E402
from session import StudySession, load_lessons  # noqa: E402

PORT = int(os.environ.get("PORT", "8765"))
PAGE = os.path.join(HERE, "web", "index.html")

# Câu mẫu cho chế độ trình bày: lấy nguyên văn từ eval/benchmark.csv theo mã câu, không chép vào code.
# Khoá None = dùng được ở mọi ý (thử chặn ngoài phạm vi / thiếu căn cứ).
PRESETS = {
    "chatbot_vs_model": [("B01", "Giải thích đủ ý"), ("B17", "Giải thích thiếu ý")],
    "temperature_sampling": [("B02", "Giải thích đủ ý"), ("B11", "Hiểu sai bản chất")],
    "rag_grounding": [("B04", "Giải thích thiếu ý"), ("B05", "Hiểu sai bản chất")],
    "workflow_vs_agent": [("B23", "Hiểu sai bản chất")],
    None: [("B12", "Tấn công đổi vai"), ("B25", "Khái niệm ngoài học liệu")],
}


def _load_passages():
    with open(os.path.join(ROOT, "data", "sample_lessons.json"), encoding="utf-8") as f:
        data = json.load(f)
    return {p["code"]: p["text"] for c in data["concepts"] for p in c["passages"]}


def _load_benchmark():
    path = os.path.join(ROOT, "eval", "benchmark.csv")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8", newline="") as f:
        return {row["id"]: row["input"] for row in csv.DictReader(f)}


def _kind(text):
    """Nhãn mở đầu phản hồi → loại hiển thị trên giao diện."""
    text = text.strip()
    for label, kind in ((ENOUGH, "enough"), (OUT_OF_SCOPE, "scope"), (NO_SOURCE, "nosource"),
                        ("[XEM LẠI KIẾN THỨC]", "review")):
        if text.startswith(label):
            return kind
    if text.startswith(NEEDS_WORK[0]):
        return "missing"
    if text.startswith(NEEDS_WORK[1]):
        return "wrong"
    return "info"


class Demo:
    def __init__(self):
        self.lessons = load_lessons()
        self.passages = _load_passages()
        self.benchmark = _load_benchmark()
        self.reset()

    def reset(self):
        self.day = None
        self.session = None
        self.phase = "choose"  # choose → study → recall → summary
        self.recall = ""
        self.totals = {"model_calls": 0, "tool_calls": 0, "tokens_in": 0, "tokens_out": 0}
        self.models = set()

    # ---- trạng thái gửi cho giao diện ----
    def lessons_view(self):
        return [{"day": day, "items": [{"concept_id": i.concept_id, "title": i.title} for i in items]}
                for day, items in self.lessons.items()]

    def presets_view(self):
        item = self.session.current if self.session else None
        keys = ([item.concept_id] if item else []) + [None]
        return [{"id": bid, "label": label, "text": self.benchmark[bid]}
                for key in keys for bid, label in PRESETS.get(key, []) if bid in self.benchmark]

    def state(self):
        s = self.session
        return {
            "phase": self.phase,
            "day": self.day,
            "index": s.index if s else 0,
            "hints": s.hints if s else 0,
            "max_hints": 2,
            "reviewed": s.reviewed if s else False,
            "items": [{"concept_id": i.concept_id, "title": i.title, "status": i.status,
                       "codes": i.source_codes, "points": i.points} for i in (s.items if s else [])],
            "presets": self.presets_view() if self.phase == "study" else [],
            "recall": self.recall,
            "totals": self.totals,
            "models": sorted(self.models),
        }

    # ---- hành động ----
    def start(self, day):
        if day not in self.lessons:
            raise ValueError("Không có bài %s" % day)
        self.reset()
        # Mỗi phiên dùng bản sao trạng thái mới để phiên trước không ảnh hưởng.
        self.lessons = load_lessons()
        self.day = day
        self.session = StudySession(self.lessons[day])
        self.phase = "study"

    def _after_step(self):
        if self.session.current is None and self.phase == "study":
            self.phase = "recall"

    def send(self, text):
        item = self.session.current
        tracing.begin("web")
        error = None
        try:
            reply = self.session.explain(text, answer)
        except Exception as e:  # giữ nguyên ý hiện tại để học viên thử lại
            error = type(e).__name__
            reply = ("Lỗi khi đối chiếu (%s). Ý đang ôn vẫn giữ nguyên: bạn có thể gửi lại "
                     "hoặc chọn Xem lại kiến thức." % error)
        finally:
            stats, events = tracing.end()
        for key in self.totals:
            self.totals[key] += stats[key]
        self.models.update(stats["models"])
        moved = self.session.current is not item
        self._after_step()
        return {
            "reply": reply,
            "kind": "error" if error else _kind(reply),
            "item_title": item.title,
            "status_after": item.status if moved else None,
            "trace": {"stats": stats, "events": events},
        }

    def review(self):
        item = self.session.current
        reply = self.session.review()
        return {"reply": reply, "kind": "review", "item_title": item.title, "status_after": None,
                "trace": {"stats": {"model_calls": 0, "tool_calls": 0, "tokens_in": 0, "tokens_out": 0,
                                    "models": [], "errors": []},
                          "events": [{"kind": "note", "text": "Xem lại kiến thức: hiện ý chuẩn có sẵn, không gọi model"}]}}

    def defer(self):
        item = self.session.current
        self.session.defer()
        self._after_step()
        return {"reply": None, "kind": "defer", "item_title": item.title, "status_after": item.status, "trace": None}

    def finish(self):
        self.phase = "recall" if self.session.current is None and self.phase == "study" else "summary"

    def submit_recall(self, text):
        self.recall = text
        self.phase = "summary"


DEMO = Demo()


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):  # chỉ in lỗi, không in nội dung học viên gõ
        if args and str(args[1]).startswith(("4", "5")):
            sys.stderr.write("%s\n" % (fmt % args))

    def _json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path in ("/", "/index.html"):
            with open(PAGE, "rb") as f:
                body = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
        elif path == "/api/bootstrap":
            self._json({"lessons": DEMO.lessons_view(), "passages": DEMO.passages, "state": DEMO.state()})
        else:
            self._json({"error": "Không có đường dẫn này"}, 404)

    def do_HEAD(self):
        self.send_response(200 if self.path.split("?", 1)[0] in ("/", "/index.html") else 404)
        self.end_headers()

    def do_POST(self):
        path = self.path.split("?", 1)[0]
        try:
            length = int(self.headers.get("Content-Length") or 0)
            data = json.loads(self.rfile.read(length) or b"{}") if length else {}
            needs_study = path in ("/api/send", "/api/review", "/api/defer")
            if needs_study and (DEMO.phase != "study" or DEMO.session.current is None):
                return self._json({"error": "Phiên ôn chưa bắt đầu hoặc đã hết ý"}, 409)
            turn = None
            if path == "/api/start":
                DEMO.start(data.get("day"))
            elif path == "/api/send":
                text = (data.get("text") or "").strip()
                if not text:
                    return self._json({"error": "Lời giải thích đang trống"}, 400)
                turn = DEMO.send(text)
            elif path == "/api/review":
                if DEMO.session.reviewed:
                    return self._json({"error": "Đã xem lại ý này. Bạn có thể diễn đạt lại hoặc để ôn sau."}, 409)
                turn = DEMO.review()
            elif path == "/api/defer":
                turn = DEMO.defer()
            elif path == "/api/finish":
                DEMO.finish()
            elif path == "/api/recall":
                DEMO.submit_recall((data.get("text") or "").strip())
            elif path == "/api/reset":
                DEMO.reset()
            else:
                return self._json({"error": "Không có đường dẫn này"}, 404)
            self._json({"turn": turn, "state": DEMO.state()})
        except ValueError as e:
            self._json({"error": str(e)}, 400)


def main():
    server = HTTPServer(("127.0.0.1", PORT), Handler)
    print("Mở http://localhost:%d  (thêm ?trinhbay=1 hoặc nhấn phím T để bật chế độ trình bày). Ctrl+C để dừng." % PORT)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print()
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
