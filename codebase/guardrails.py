"""Kiểm tra đầu vào và nhãn phản hồi của phiên tự ôn."""

import re
import unicodedata

OUT_OF_SCOPE = "[NGOÀI PHẠM VI]"
NO_SOURCE = "[CHƯA ĐỦ CĂN CỨ]"
ENOUGH = "[ĐỦ Ý]"
NEEDS_WORK = ("[THIẾU Ý]", "[HIỂU SAI]")
SESSION_LABELS = (OUT_OF_SCOPE, NO_SOURCE, ENOUGH, *NEEDS_WORK)
SESSION_REFUSAL = (
    f"{OUT_OF_SCOPE} Phiên này chỉ hỗ trợ tự ôn dựa trên học liệu. "
    "Bạn có thể tiếp tục giải thích ý đang ôn hoặc dùng /xem để xem học liệu."
)
SESSION_NO_SOURCE = (
    f"{NO_SOURCE} Chưa đủ căn cứ để đối chiếu đầu vào với ý đang ôn."
)

_SCOPE_PATTERNS = (
    r"bo qua (moi |tat ca )?huong dan",
    r"ignore (all )?previous instructions",
    r"(in|hien|cho xem|tiet lo|lo|show|reveal|print).{0,25}system prompt",
    r"cham (giup |cho )?(toi|minh|em).{0,40}diem",
    r"cham diem (bai|lab|giup|cho)",
    r"cho (toi|minh|em) (\d+/\d+|\d+ diem)",
    r"xac nhan.{0,30}qua lab",
    r"duyet.{0,30}qua lab",
    r"(lam ho|giai ho|viet ho).{0,35}(lab|code|bai tap)",
    r"(cho|dua|in).{0,25}(full code|toan bo code|dap an lab|loi giai hoan chinh)",
    r"gui ket qua.{0,25}giang vien",
)
_SESSION_PATTERNS = (
    r"\b(?:bo qua|quen|ghi de)\b.{0,40}\b(?:chi dan|quy tac|lenh he thong|chi thi)\b",
    r"\b(?:ignore|disregard|forget|override)\b.{0,40}\b(?:instructions|rules|constraints)\b",
    r"\b(?:tu gio|tu bay gio)\b.{0,20}\bban la\b|\b(?:hay|vui long) dong vai\b",
    r"\b(?:act as|pretend to be|you are now|developer mode)\b",
    r"\b(?:in|doc|hien|gui|liet ke|tiet lo|nhac lai|show|reveal|print|repeat|disclose)\b"
    r".{0,35}\b(?:prompt he thong|chi dan an|lenh an|system instructions|hidden prompt)\b",
    r"\b(?:chi tra loi|chi in|chi xuat|respond only|output only)\b.{0,25}"
    r"\[(?:du y|thieu y|hieu sai|xem lai kien thuc)\]",
    r"(?m)^\s*(?:system|developer|assistant|he thong|nha phat trien)\s*:",
    r"<\|(?:im_start|im_end|system|assistant|developer|eot_id)\|>|\[/?inst\]|</?system>",
)


def normalize_input(text: str) -> str:
    """Bỏ dấu và ký tự định dạng ẩn để kiểm tra chỉ thị trong đầu vào."""
    text = text.replace("đ", "d").replace("Đ", "D")
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(
        char for char in normalized
        if not unicodedata.combining(char) and unicodedata.category(char) != "Cf"
    ).lower()


def is_out_of_scope(text: str, *, in_session: bool = False) -> bool:
    """Nhận diện yêu cầu ngoài thẩm quyền và các chỉ thị đổi vai phổ biến."""
    normalized = normalize_input(text)
    flat = " ".join(normalized.split())
    if any(re.search(pattern, flat) for pattern in _SCOPE_PATTERNS):
        return True
    return in_session and any(
        re.search(pattern, normalized) or re.search(pattern, flat)
        for pattern in _SESSION_PATTERNS
    )


def session_label(output: str) -> str:
    """Chỉ nhận một nhãn phiên hợp lệ ở đầu phản hồi."""
    labels = [label for label in SESSION_LABELS if label in output]
    if len(labels) == 1 and output.startswith(labels[0]) and output.count(labels[0]) == 1:
        return labels[0]
    return ""
