"""Giao diện phiên học viên dạy lại. Chạy bằng python run.py."""

import re
import sys

from ai import MODEL_PROVIDER, call_model
from guardrails import normalize_input
from teachback import TeachbackSession
from tools import load_days
import tracing


def _choose_lesson(days):
    print("Chọn bài để dạy lại cho AI")
    for lesson in days:
        print(f'  {lesson["day"]} · {lesson["title"]} ({len(lesson["items"])} mục)')
    while True:
        selection = input('Nhập số ngày hoặc gõ “ôn lại ngày 4” (Enter để thoát)\n> ').strip()
        if not selection:
            return None
        selected = re.search(
            r"(?:^|\bngay\s+|\bd\s*)(\d{1,2})\s*$", normalize_input(selection)
        )
        if selected and 1 <= int(selected.group(1)) <= len(days):
            return days[int(selected.group(1)) - 1]
        print("Chọn một ngày từ 1 đến 15.")


def _run_session(lesson):
    session = TeachbackSession(lesson)
    print("Bạn là người dạy. AI sẽ hỏi để hiểu bài.")
    print("Dùng /xem để đối chiếu, /sau để chuyển mục, /thoat để kết thúc.")
    tracing.begin("app-teachback")
    try:
        while session.current is not None:
            index = session.index
            print(f'\nMục {index + 1}/{len(lesson["items"])} · {session.current["title"]}')
            print("AI người học · " + session.opening())
            while session.index == index:
                text = input("> ").strip()
                if text == "/thoat":
                    return
                if text == "/sau":
                    session.skip()
                    continue
                if text == "/xem":
                    if session.revealed:
                        print("Bạn có thể dạy lại một lần hoặc chọn /sau.")
                    else:
                        print(session.reveal())
                elif text:
                    try:
                        print(session.explain(text, call_model))
                    except Exception:
                        print("Chưa đối chiếu được lời giải thích. Thử lại hoặc dùng /xem để mở học liệu.")
        print("\nBạn áp dụng điều vừa làm rõ vào tình huống nào trong lab?")
        input("Nhập để tự nhắc lại hoặc Enter để bỏ qua\n> ")
    except (EOFError, KeyboardInterrupt):
        print()
    finally:
        stats, _ = tracing.end()
        print(f'\nTổng hợp phiên {lesson["day"]}')
        for item, status in zip(lesson["items"], session.statuses):
            print(f'- {item["title"]} · {status} · [{item["code"]}]')
        models = ", ".join(stats["models"]) or "—"
        print(
            f'Model {models} · {stats["model_calls"]} lượt gọi · '
            f'token vào {stats["tokens_in"]} / ra {stats["tokens_out"]}'
        )


def main():
    try:
        lessons = load_days()
        selected = _choose_lesson(lessons)
    except (EOFError, KeyboardInterrupt):
        return 0
    except (OSError, ValueError, KeyError) as error:
        print(f"Không nạp được học liệu mô phỏng: {error}")
        return 1
    if selected:
        if MODEL_PROVIDER == "fake":
            print("Chế độ mô phỏng. /xem mở học liệu; giám khảo cần model thật để đối chiếu.")
        _run_session(selected)
    return 0


if __name__ == "__main__":
    sys.exit(main())
