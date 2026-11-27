# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Học liệu chuẩn tóm tắt theo khái niệm (`data/sample_lessons.json`)

| | |
|---|---|
| Dùng để làm gì | Nguồn sự thật cho công cụ `search_lesson` và `get_key_points` trong `codebase/tools.py`, và làm căn cứ đối chiếu mã đoạn khi chấm bộ câu thử `eval/benchmark.csv` (24 câu) |
| Từ đâu | Nhóm tự viết lại cô đọng từ các khái niệm cốt lõi AI20K L3 (Day01, Day03, Day07, Day09) — không sao chép nguyên văn tài liệu khoá |
| Xử lý những bước gì | Chuẩn hoá cấu trúc JSON gồm 6 khái niệm (`concept_id`, `title`, `aliases`, `passages` gắn mã `[DXX-PYY]`, `key_points` gắn mã đoạn); rà tay 100% nội dung và mã đoạn bởi nhóm |
| Số dòng / số đoạn | 6 khái niệm · 12 đoạn học liệu (`D01-P01` → `D09-P02`) · 18 ý chính chuẩn |
| Phiên bản / ngày lấy | `1.0-cp2` · 27/11/2026 |
| Nhãn | `synthetic` (bản viết lại cô đọng do nhóm biên soạn; không dùng làm bằng chứng pain) |
| Giới hạn | Mới phủ 6 khái niệm nền tảng của L3 (chưa phủ hết toàn bộ 15 ngày học); mọi câu hỏi nằm ngoài 6 khái niệm này (vd `B09`, `B13`) sẽ chủ động rơi vào nhánh `[CHƯA ĐỦ CĂN CỨ]` theo nguyên tắc G10 |

**Data `synthetic` (nhóm tự biên soạn):** 6 khái niệm và 12 đoạn học liệu do nhóm tự viết lại theo kiến thức cốt lõi các ngày học L3 (không dùng script sinh ngẫu nhiên); người kiểm: Nguyễn Hoàng Trung (đã kiểm tay 12/12 đoạn và 18/18 ý chính). Data tự dựng **không phải bằng chứng pain**.

## Dataset 2 · Nhật ký hành vi pre-class (`data/preclass/` do BTC cấp)

| | |
|---|---|
| Dùng để làm gì | Đào bằng chứng pain hành vi thật (`evidence/data-mining.md`), lấy tỷ trọng 3 nhóm tần suất người dùng (`42% / 40% / 18%`) và quy mô `436 / 721` học viên cho `cost/personas.yaml`, và làm nguồn `data_that` cho 9/24 câu thử trong `eval/benchmark.csv` |
| Từ đâu | Data BTC cấp trong repo đề (`data/preclass/`, nhật ký thật đã ẩn danh trên `preclass-online.com`) |
| Xử lý những bước gì | Đếm bằng script chuẩn Python `evidence/count_preclass.py` (chọn mẫu số 436 học viên hoạt động, lọc `lan_thu=1` cho `answers.csv`, đếm `agent_message_shown` và `video_discussion_reply`, phân 3 nhóm theo số phiên `session_started`); **không** commit file CSV gốc vào repo |
| Số dòng / số đoạn | 721 tài khoản (436 HV hoạt động) · 107.709 `events` · 3.776 `answers` · 1.260 `chat` · 849 `class_events` · 228 `rewards` |
| Phiên bản / ngày lấy | Bản phát hành hackathon 27/11/2026 (dữ liệu từ `05/11/2026` đến `25/11/2026`, Day01–Day13) |
| Nhãn | thật (đã ẩn danh bởi BTC) |
| Giới hạn | Không có nội dung chữ học viên gõ (chỉ có độ dài ký tự và điểm rubric); `video_quiz` trong `answers.csv` và `learning_mode` chỉ ghi từ `25/11/2026`; cần đối chiếu thêm bằng khảo sát học viên L3 |

## Dataset 3 · Khảo sát tự đánh giá trước lab của học viên AI20K L3 (bằng chứng bổ trợ ở `spec.md` §2)

| | |
|---|---|
| Dùng để làm gì | Kiểm chứng pain "ảo tưởng hiểu bài" trước lab và ước tính thời gian mất thêm mỗi lần hiểu sai (`20 phút/lần`, `3 lần/người/tháng`) để tính Impact ở `spec.md` §2 và so sánh chi phí ở `spec.md` §8 |
| Từ đâu | Khảo sát trực tiếp học viên AI20K L3 ngoài nhóm do nhóm triển khai ngày 27/11/2026 (đã ẩn danh, không lưu tên hay mã học viên) |
| Xử lý những bước gì | Lọc đúng phiếu học viên L3 (`n = 22`), đếm nhóm từng chọn *"Nghĩ mình hiểu đủ để áp dụng"* trước khi phát hiện hiểu sai trong lab (`14/22` phiếu), tính trung vị số phút tự báo cáo (`20 phút`, khoảng `15–60 phút` trên 13/14 phiếu có số phút) |
| Số dòng / số đoạn | 22 phiếu hợp lệ (trong đó 14 phiếu rơi vào nhóm pain A4) |
| Phiên bản / ngày lấy | Đợt thu thập CP1–CP2 · 27/11/2026 |
| Nhãn | thật (đã ẩn danh) |
| Giới hạn | Cỡ mẫu nhỏ (`n = 22`), số phút và tần suất là học viên tự nhớ lại nên con số tần suất `3 lần/người/tháng` và Impact `840 phút/tháng` được đánh dấu rõ *(tự ước tính)* trong `spec.md` §2 |
