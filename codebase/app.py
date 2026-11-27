"""Giao diện dòng lệnh cho phiên tự ôn. Chạy bằng `python run.py`."""
from collections import Counter
import os
import sys

for _stream in (sys.stdout, sys.stderr, sys.stdin):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def _where(e):
    """File (trong codebase/) gây lỗi khi nạp: SyntaxError có e.filename, lỗi khác lấy khung cuối của traceback."""
    import traceback
    path = getattr(e, "filename", None) or (traceback.extract_tb(e.__traceback__)[-1].filename if e.__traceback__ else "")
    if not path:
        return "codebase/"
    p = os.path.abspath(path)
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.relpath(p, base).replace(os.sep, "/") if p.startswith(base) else path

def _choose_lesson(lessons):
    choices = dict(enumerate(lessons.items(), start=1))
    print("Chọn bài pre-class để tự ôn:")
    for number, (day, items) in choices.items():
        print(f"  {number}. {day} · " + " / ".join(item.title for item in items))
    while True:
        selected = input("Số bài (Enter để thoát): ").strip()
        if not selected:
            return None
        for number, lesson in choices.items():
            if selected == str(number):
                return lesson
        print("Chọn một số trong danh sách.")


def _run_session(day, session, answer, tracing):
    totals = Counter()
    models = set()
    last_item = None
    try:
        while (item := session.current) is not None:
            if item is not last_item:
                print(f"\nÝ {session.index + 1}/{len(session.items)} · {item.title}")
                last_item = item
            commands = "/sau: để ôn sau · /thoat: kết thúc phiên"
            if not session.reviewed:
                commands = f"/xem: xem lại kiến thức · {commands}"
            print(f"Nhập lời giải thích bằng lời của bạn. {commands}")
            text = input("> ").strip()
            if text == "/thoat":
                break
            if text == "/sau":
                session.defer()
            elif text == "/xem":
                print("Bạn có thể diễn đạt lại hoặc để ôn sau." if session.reviewed else session.review())
            elif text:
                tracing.begin("app")
                try:
                    print(session.explain(text, answer))
                except Exception as e:  # giữ nguyên ý hiện tại để học viên có thể thử lại
                    print(f"Lỗi khi đối chiếu ({type(e).__name__}). Bạn có thể thử lại hoặc chọn xem học liệu.")
                finally:
                    stats, _ = tracing.end()
                    for key in ("model_calls", "tool_calls", "tokens_in", "tokens_out"):
                        totals[key] += stats[key]
                    models.update(stats["models"])

        if session.current is None:
            print("\nTự nhắc lại. Ý nào bạn vừa làm rõ? Bạn sẽ áp dụng nó thế nào trong lab?")
            input("Tự trả lời hoặc nhấn Enter để bỏ qua: ")
    except (EOFError, KeyboardInterrupt):
        print()

    print(f"\nTổng hợp phiên ôn {day}")
    for item in session.items:
        codes = ", ".join(f"[{code}]" for code in item.source_codes)
        print(f"- {item.title} · {item.status} · {codes}")
    print("Bạn tự quyết định ôn thêm hay sang lab.")
    print("Model: %s · gọi model %d lần · công cụ %d lần · token vào %d / ra %d" % (
        ", ".join(sorted(models)) or "—", totals["model_calls"], totals["tool_calls"],
        totals["tokens_in"], totals["tokens_out"],
    ))


def main() -> int:
    try:
        import tracing
        from agent import answer
        from session import StudySession, load_lessons

        lessons = load_lessons()
    except Exception as e:
        print("Không nạp được học liệu hoặc code ở %s: %s: %s" % (_where(e), type(e).__name__, e))
        return 1

    if not lessons:
        print("Chưa có bài pre-class với ý cốt lõi để tự ôn.")
        return 1
    try:
        selected = _choose_lesson(lessons)
    except (EOFError, KeyboardInterrupt):
        print()
        return 0
    if selected:
        day, items = selected
        _run_session(day, StudySession(items), answer, tracing)
    return 0


if __name__ == "__main__":
    sys.exit(main())
