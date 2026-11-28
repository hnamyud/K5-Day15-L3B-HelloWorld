"""Giao diện web cho phiên học viên dạy lại (bản demo). Chạy bằng `python codebase/web.py` rồi mở http://localhost:8765.

Chỉ dùng thư viện chuẩn. Server một luồng, giữ một phiên trong bộ nhớ (đủ cho demo trên một máy).
Luồng dùng nguyên `TeachbackSession` (teachback.py) và `call_model` (ai.py) như `app.py`; file này chỉ thay lớp nhập/xuất.
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
from ai import MODEL_PROVIDER, call_model  # noqa: E402
from teachback import MAX_HINTS, TeachbackSession  # noqa: E402
from tools import load_days  # noqa: E402

PORT = int(os.environ.get("PORT", "8765"))
PAGE = os.path.join(HERE, "web", "index.html")

LEARNER = "AI người học · "
JUDGE = "Giám khảo · "
KINDS = {"ĐỦ Ý": "enough", "THIẾU Ý": "missing", "HIỂU SAI": "wrong"}

# Câu mẫu cho chế độ trình bày: lấy nguyên văn từ eval/benchmark.csv theo mã câu, không chép vào code.
# Khoá None = dùng được ở mọi mục (thử chặn ngoài phạm vi / ngoài mục đang ôn).
PRESETS = {
    "D01-P52": [("B01", "Giải thích đủ ý"), ("B17", "Giải thích thiếu ý")],
    "D01-P53": [("B02", "Giải thích đủ ý"), ("B11", "Hiểu sai bản chất")],
    "D08-P51": [("B04", "Giải thích thiếu ý"), ("B05", "Hiểu sai bản chất")],
    "D03-P51": [("B23", "Hiểu sai bản chất")],
    None: [("B12", "Tấn công đổi vai"), ("B25", "Khái niệm ngoài học liệu")],
}


def _load_benchmark():
    path = os.path.join(ROOT, "eval", "benchmark.csv")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8-sig", newline="") as f:
        return {row["id"]: row["input"] for row in csv.DictReader(f)}


def _sources(days):
    """Mã mục → tham chiếu đề cương. Không chứa ý chuẩn để không lộ đáp án trước khi học viên dạy."""
    return {
        item["code"]: "%s · mục %s trong đề cương %s %s. Nguồn: %s"
        % (item["title"], item["section"], day["day"], day["title"], day["source"])
        for day in days for item in day["items"]
    }


def _classify(reply):
    """Tách lời của AI người học / giám khảo / hệ thống thành (kind, speaker, text)."""
    if reply.startswith(LEARNER):
        return "learner", "learner", reply[len(LEARNER):]
    if reply.startswith(JUDGE):
        head, _, body = reply.partition("\n")
        label = head[len(JUDGE):].strip().strip("[]")
        return KINDS.get(label, "review"), "judge", body
    return "scope", "system", reply


def _empty_stats(note):
    return {"stats": {"model_calls": 0, "tool_calls": 0, "tokens_in": 0, "tokens_out": 0, "models": [], "errors": []},
            "events": [{"kind": "note", "text": note}]}


class Demo:
    def __init__(self):
        self.days = {day["day"]: day for day in load_days()}
        self.sources = _sources(self.days.values())
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
        return [{"day": d["day"], "title": d["title"], "items": [{"code": i["code"], "title": i["title"]} for i in d["items"]]}
                for d in self.days.values()]

    def presets_view(self):
        item = self.session.current if self.session else None
        keys = ([item["code"]] if item else []) + [None]
        return [{"id": bid, "label": label, "text": self.benchmark[bid]}
                for key in keys for bid, label in PRESETS.get(key, []) if bid in self.benchmark]

    def state(self):
        s = self.session
        items = self.days[self.day]["items"] if s else []
        return {
            "phase": self.phase,
            "day": self.day,
            "day_title": self.days[self.day]["title"] if s else "",
            "index": s.index if s else 0,
            "hints": s.hints if s else 0,
            "max_hints": MAX_HINTS,
            "reviewed": s.revealed if s else False,
            "opening": s.opening() if s and s.current else "",
            "items": [{"code": i["code"], "title": i["title"], "section": i["section"], "status": status,
                       "codes": [i["code"]]} for i, status in zip(items, s.statuses if s else [])],
            "presets": self.presets_view() if self.phase == "study" else [],
            "recall": self.recall,
            "totals": self.totals,
            "models": sorted(self.models),
            "fake": MODEL_PROVIDER == "fake",
        }

    # ---- hành động ----
    def start(self, day):
        if day not in self.days:
            raise ValueError("Không có bài %s" % day)
        self.reset()
        self.day = day
        self.session = TeachbackSession(self.days[day])
        self.phase = "study"

    def _after_step(self):
        if self.session.current is None and self.phase == "study":
            self.phase = "recall"

    def _turn(self, item, index, reply, kind, speaker, trace, judge=None):
        moved = self.session.index != index
        return {
            "reply": reply,
            "kind": kind,
            "speaker": speaker,
            "judge": judge,
            "item_title": item["title"],
            "status_after": self.session.statuses[index] if moved else None,
            "trace": trace,
        }

    def send(self, text):
        s = self.session
        item, index = s.current, s.index
        tracing.begin("web")
        try:
            reply = s.explain(text, call_model)
            kind, speaker, body = _classify(reply)
        except Exception as e:  # giữ nguyên mục hiện tại để học viên thử lại
            kind, speaker = "error", "system"
            detail = str(e) if isinstance(e, ValueError) else type(e).__name__
            body = ("Chưa đối chiếu được lời giải thích (%s). Mục đang ôn vẫn giữ nguyên: bạn có thể gửi lại "
                    "hoặc chọn Xem lại kiến thức." % detail)
        finally:
            stats, events = tracing.end()
        for key in self.totals:
            self.totals[key] += stats[key]
        self.models.update(stats["models"])
        turn = self._turn(item, index, body, kind, speaker, {"stats": stats, "events": events}, s.last_label)
        self._after_step()
        return turn

    def review(self):
        s = self.session
        item, index = s.current, s.index
        _, _, body = _classify(s.reveal())
        return self._turn(item, index, body, "review", "judge",
                          _empty_stats("Xem lại kiến thức: hiện ý chuẩn có sẵn, không gọi model"))

    def defer(self):
        s = self.session
        item, index = s.current, s.index
        s.skip()
        turn = self._turn(item, index, None, "defer", "system", None)
        self._after_step()
        return turn

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
            self._json({"lessons": DEMO.lessons_view(), "passages": DEMO.sources, "state": DEMO.state()})
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
                return self._json({"error": "Phiên chưa bắt đầu hoặc đã hết mục"}, 409)
            turn = None
            if path == "/api/start":
                DEMO.start(data.get("day"))
            elif path == "/api/send":
                text = (data.get("text") or "").strip()
                if not text:
                    return self._json({"error": "Lời giải thích đang trống"}, 400)
                turn = DEMO.send(text)
            elif path == "/api/review":
                if DEMO.session.revealed:
                    return self._json({"error": "Đã xem ý chuẩn của mục này. Bạn có thể dạy lại một lần hoặc để ôn sau."}, 409)
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
