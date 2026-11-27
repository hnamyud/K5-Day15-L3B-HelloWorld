# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Học liệu chuẩn tóm tắt theo khái niệm (`data/sample_lessons.json`)

| | |
|---|---|
| Dùng để làm gì | Nguồn sự thật cho công cụ `search_lesson` và `get_key_points` trong `codebase/tools.py`, và làm căn cứ chấm bộ câu thử `eval/benchmark.csv` |
| Từ đâu | Nhóm tự viết lại cô đọng từ các khái niệm cốt lõi AI20K L3 (Day01, Day03, Day07, Day09) — không sao chép nguyên văn tài liệu khoá |
| Xử lý những bước gì | Chuẩn hoá cấu trúc JSON gồm 6 khái niệm (`concept_id`, `title`, `aliases`, `passages` có mã `[DXX-PYY]`, `key_points` gắn mã đoạn); kiểm tay 100% nội dung và mã đoạn bởi nhóm |
| Số dòng / số đoạn | 6 khái niệm · 12 đoạn học liệu (`D01-P01` → `D09-P02`) · 18 ý chính chuẩn |
| Phiên bản / ngày lấy | `1.0-cp2` · 27/11/2026 |
| Nhãn | `synthetic` (bản viết lại cô đọng do nhóm biên soạn; không dùng làm bằng chứng pain) |
| Giới hạn | Mới phủ 6 khái niệm nền tảng của L3 (chưa đủ toàn bộ 15 ngày); các câu hỏi ngoài 6 khái niệm này sẽ chủ động rơi vào nhánh "chưa đủ căn cứ" (G10) |

**Data `synthetic` (nhóm tự biên soạn):** 6 khái niệm và 12 đoạn học liệu do nhóm tự viết lại theo kiến thức cốt lõi các ngày học L3 (không dùng script sinh ngẫu nhiên); người kiểm: Nguyễn Hoàng Trung (đã kiểm tay 12/12 đoạn và 18/18 ý chính). Data tự dựng **không phải bằng chứng pain**.

## Dataset 2 · Nhật ký hành vi pre-class (`data/preclass/` do BTC cấp)

| | |
|---|---|
| Dùng để làm gì | Đào bằng chứng pain hành vi thật (`evidence/data-mining.md`), tính phân nhóm tần suất sử dụng cho `cost/personas.yaml`, và làm nguồn cho các câu thử `data_that:` trong `eval/benchmark.csv` |
| Từ đâu | Data BTC cấp trong repo đề (`data/preclass/`, nhật ký thật đã ẩn danh trên `preclass-online.com`) |
| Xử lý những bước gì | Lọc bằng script `evidence/count_preclass.py` (chọn mẫu số 436 học viên hoạt động, đếm `lan_thu=1` cho `answers.csv`, đếm `agent_message_shown` và `video_discussion_reply`); **không** commit file CSV gốc vào repo |
| Số dòng / số đoạn | 721 tài khoản (436 HV hoạt động) · 107.709 `events` · 3.776 `answers` · 1.260 `chat` · 849 `class_events` · 228 `rewards` |
| Phiên bản / ngày lấy | Bản phát hành hackathon 27/11/2026 (dữ liệu từ `05/11/2026` đến `25/11/2026`, Day01–Day13) |
| Nhãn | thật (đã ẩn danh bởi BTC) |
| Giới hạn | Không có nội dung chữ học viên gõ (chỉ có độ dài và điểm rubric); `video_quiz` trong `answers.csv` và `learning_mode` chỉ ghi từ `25/11/2026`; cần đối chiếu thêm bằng khảo sát học viên L3 |
