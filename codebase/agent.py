"""Đưa đầu vào đơn lượt của khung eval và simulate vào luồng dạy lại."""

import re

from ai import MODEL_PROVIDER, call_model
from guardrails import NO_SOURCE, OUT_OF_SCOPE, is_out_of_scope, normalize_input
from teachback import TeachbackSession
from tools import search_lesson

_REVIEW = re.compile(
    r"\b(?:xem lai kien thuc|xem lai bai|giai thich lai giup|"
    r"(?:da dung|da het|het|sau) (?:2|hai) (?:cau|luot) (?:hoi )?(?:goi mo|lam ro))\b"
)


def answer(text: str) -> dict:
    """Giữ hợp đồng answer(text) của khung và tạo một phiên cho mục tìm được."""
    text = (text or "").strip()
    if is_out_of_scope(text, in_session=True):
        return {"output": f"{OUT_OF_SCOPE} Bạn có thể quay lại giải thích một ý trong bài đang ôn."}

    match = search_lesson(text)
    if match is None:
        return {
            "output": (
                f"{NO_SOURCE} Chưa tìm được một mục phù hợp. "
                "Bạn có thể nhập tên mục hoặc chạy python run.py để chọn bài theo ngày."
            )
        }

    day, item = match
    study = TeachbackSession({**day, "items": [item]})
    if _REVIEW.search(normalize_input(text)):
        return {"output": "[XEM LẠI KIẾN THỨC]\n" + study.reveal()}
    if MODEL_PROVIDER == "fake":
        reply = call_model("Chế độ giả của phiên dạy lại.", study.opening())
        return {"output": f'{reply["text"]} [{item["code"]}]'}
    output = study.explain(text, call_model)
    if not study.last_label:
        return {"output": f"{NO_SOURCE} Lời giải thích chưa cho thấy căn cứ để đối chiếu mục này."}
    if output.startswith("AI người học · "):
        output = output.removeprefix("AI người học · ") + f' [{item["code"]}]'
    else:
        output = output.split("\n", 1)[1]
    return {"output": f"[{study.last_label}] {output}"}
