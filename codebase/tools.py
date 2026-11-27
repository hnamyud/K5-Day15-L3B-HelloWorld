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
}

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


def _score_concept(query: str, concept: dict) -> float:
    q_norm = _normalize(query)
    if not q_norm:
        return 0.0
    q_toks = _tokens(query)
    score = 0.0

    cid_norm = _normalize(concept["concept_id"].replace("_", " "))
    if concept["concept_id"].lower() in q_norm or (cid_norm and cid_norm in q_norm):
        score += 10.0

    for alias in concept.get("aliases", []):
        a_norm = _normalize(alias)
        if not a_norm:
            continue
        if f" {a_norm} " in f" {q_norm} ":
            score += 6.0 if " " in a_norm else 4.5

    title_toks = _tokens(concept.get("title", ""))
    score += 2.0 * len(q_toks & title_toks)

    passage_text = " ".join(p["text"] for p in concept.get("passages", []))
    passage_toks = _tokens(passage_text)
    score += 0.6 * len(q_toks & passage_toks)

    return score


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
    return best_id if best_score >= 3.5 else ""


@tool
def search_lesson(query: str) -> list:
    """search_lesson · Input: tên khái niệm + lời giải thích của học viên (str) · Output: danh sách đoạn học liệu {"code", "text"}, rỗng nếu không có đoạn khớp · Tác động ra ngoài: Không (chỉ đọc)."""
    data = _load_lessons()
    scored = []
    for concept in data.get("concepts", []):
        s = _score_concept(query, concept)
        if s >= 3.5:
            scored.append((s, concept))
    if not scored:
        return []
    scored.sort(key=lambda item: item[0], reverse=True)
    # Lấy các đoạn học liệu của khái niệm khớp nhất (mỗi phiên 1 khái niệm theo spec.md §4)
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
    # Dự phòng: nếu truyền tên khái niệm tự do thay vì mã chuẩn
    resolved = resolve_concept_id(concept_code)
    if resolved:
        for concept in data.get("concepts", []):
            if concept["concept_id"] == resolved:
                return [{"code": kp["code"], "point": kp["point"]} for kp in concept.get("key_points", [])]
    return []
