"""Điều phối một phiên tự ôn theo thứ tự học liệu mẫu."""

import re
from dataclasses import dataclass

from tools import get_key_points, list_concept_titles

EXPLAINED = "Đã giải thích được"
REVISIT = "Nên ôn lại"
UNCHECKED = "Chưa kiểm tra"
_ENOUGH = "[ĐỦ Ý]"
_NEEDS_WORK = ("[THIẾU Ý]", "[HIỂU SAI]")
_NO_SOURCE = "[CHƯA ĐỦ CĂN CỨ]"
_OUT_OF_SCOPE = "[NGOÀI PHẠM VI]"
_UNVERIFIED = (
    "[CHƯA ĐỦ CĂN CỨ] Chưa nhận được phản hồi đối chiếu hợp lệ cho ý đang ôn."
)
_SOURCE_CODE = re.compile(r"\[([A-Za-z]\d{2}-P\d{2})\]")
_MAX_HINTS = 2


@dataclass
class StudyItem:
    concept_id: str
    title: str
    points: list
    status: str = UNCHECKED

    @property
    def source_codes(self):
        return list(dict.fromkeys(point["code"] for point in self.points))


def load_lessons():
    """Gom các mục theo mã ngày trong mã đoạn, giữ thứ tự của học liệu."""
    lessons = {}
    for concept_id, title in list_concept_titles():
        points = get_key_points(concept_id)
        if points:
            day = points[0]["code"].split("-", 1)[0]
            lessons.setdefault(day, []).append(StudyItem(concept_id, title, points))
    return lessons


class StudySession:
    def __init__(self, items):
        self.items = items
        self.index = 0
        self.hints = 0
        self.reviewed = False

    @property
    def current(self):
        return self.items[self.index] if self.index < len(self.items) else None

    def _advance(self, status):
        self.current.status = status
        self.index += 1
        self.hints = 0
        self.reviewed = False

    def defer(self):
        self._advance(REVISIT)

    def review(self):
        """Hiện phần kiến thức chuẩn đã có sẵn cho đúng mục đang ôn."""
        self.reviewed = True
        lines = ["[XEM LẠI KIẾN THỨC]"]
        lines.extend(f"- [{point['code']}] {point['point']}" for point in self.current.points)
        lines.append("Thử diễn đạt lại ý này một lần bằng lời của bạn.")
        return "\n".join(lines)

    def explain(self, text, answer):
        """Đối chiếu lời giải thích mới rồi cập nhật đúng mục hiện tại."""
        item = self.current
        query = f"Ý đang ôn: {item.concept_id}\nLời giải thích: {text}"
        output = answer(query)["output"].strip()
        if output.startswith(_OUT_OF_SCOPE):
            return f"{output}\nMời bạn tiếp tục với ý đang ôn: {item.title}."
        if output.startswith("[câu trả lời giả"):
            return f"{output}\nHãy chọn xem lại hoặc để ôn sau để tiếp tục dùng thử."
        if output.startswith(_NO_SOURCE):
            self._advance(UNCHECKED)
            return output

        cited = set(_SOURCE_CODE.findall(output))
        if not cited or cited.difference(item.source_codes):
            self._advance(UNCHECKED)
            return _UNVERIFIED
        if output.startswith(_ENOUGH):
            self._advance(EXPLAINED)
            return output
        if output.startswith(_NEEDS_WORK):
            if self.reviewed:
                self._advance(REVISIT)
                return "Ý này vẫn còn điểm cần ôn. Xem mã đoạn ở phần tổng hợp."
            if self.hints >= _MAX_HINTS:
                return self.review()
            self.hints += 1
            return output
        if output.startswith("[XEM LẠI KIẾN THỨC]") and not self.reviewed:
            return self.review()

        self._advance(UNCHECKED)
        return _UNVERIFIED
