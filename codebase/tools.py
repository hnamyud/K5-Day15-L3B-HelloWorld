"""Tra cứu học liệu mô phỏng theo mã đoạn hoặc tên mục."""

from functools import lru_cache
import json
from pathlib import Path
import re

from guardrails import normalize_input
from tracing import tool

LESSONS_PATH = Path(__file__).resolve().parents[1] / "data" / "teachback_lessons.json"


@lru_cache(maxsize=1)
def load_days():
    """Nạp 15 ngày theo đề cương và kiểm mã đoạn, nguồn, câu hỏi."""
    days = json.loads(LESSONS_PATH.read_text(encoding="utf-8"))["days"]
    if [day["day"] for day in days] != [f"D{day:02d}" for day in range(1, 16)]:
        raise ValueError("Học liệu cần đủ D01 đến D15 theo thứ tự.")
    seen = set()
    for day in days:
        if not day["items"] or not day["source"].startswith("https://"):
            raise ValueError(f"Ngày {day['day']} thiếu mục ôn hoặc nguồn.")
        for item in day["items"]:
            code = item["code"]
            if code in seen or not re.fullmatch(day["day"] + r"-P\d{2}", code):
                raise ValueError(f"Mã mục trùng hoặc không thuộc ngày: {code}")
            seen.add(code)
            if not item["checkpoints"] or not item["section"]:
                raise ValueError(f"Mục {code} thiếu ý chuẩn hoặc tham chiếu.")
            for point in item["checkpoints"]:
                question = point["question"]
                if not point["answer"] or question.count("?") != 1 or not question.endswith("?"):
                    raise ValueError(f"Mục {code} có ý chuẩn hoặc câu hỏi chưa hợp lệ.")
    return days


def _normalize(text):
    return " ".join(re.findall(r"[a-z0-9]+", normalize_input(text)))


def _find_lesson(query):
    body = _normalize(query)
    header, separator, _ = query.partition(":")
    prefix = _normalize(header) if separator else ""
    matches = []
    for day in load_days():
        for item in day["items"]:
            if f' {_normalize(item["code"])} ' in f" {body} ":
                return day, item
            names = (item["title"], *item.get("aliases", ()))
            lengths = [
                (f" {name} " in f" {prefix} ", len(name))
                for name in map(_normalize, names)
                if name and f" {name} " in f" {body} "
            ]
            if lengths:
                matches.append((max(lengths), day, item))
    if not matches:
        return None
    matches.sort(key=lambda match: match[0], reverse=True)
    if len(matches) > 1 and matches[0][0] == matches[1][0]:
        return None
    return matches[0][1:]


@tool
def search_lesson(query: str):
    """search_lesson · Input: tên, bí danh hoặc mã đoạn.
    Output: bài và mục phù hợp nhất, hoặc None. Tác động: chỉ đọc.
    """
    return _find_lesson(query)


@tool
def get_key_points(lesson_code: str):
    """get_key_points · Input: mã đoạn đã chọn.
    Output: các checkpoint có ý chuẩn và câu hỏi. Tác động: chỉ đọc.
    """
    for day in load_days():
        for item in day["items"]:
            if item["code"] == lesson_code:
                return item["checkpoints"]
    return []
