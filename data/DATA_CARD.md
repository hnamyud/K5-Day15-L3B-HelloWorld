# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Học liệu mô phỏng cho phiên dạy lại 15 ngày

| | |
|---|---|
| Dataset hiện dùng | [teachback_lessons.json](teachback_lessons.json) phục vụ cả chọn bài trong phiên và tra cứu đơn lượt. |
| Nguồn và ngày học | Biên soạn theo [đề cương công khai](https://e-learning-production.vercel.app/ngay/ngay-01). Số ngày bám đề cương này. |
| Cấu trúc | Mỗi ngày có URL nguồn. Mỗi mục có mã `[DXX-PYY]`, tham chiếu phần trong đề cương và các ý phải giải thích được. Mỗi ý đi kèm một câu hỏi gợi mở. |
| Quy mô | 15 ngày, 52 mục. D01 có 10 mục, mỗi ngày còn lại có 3 mục mẫu. |
| Phiên bản và nhãn | `teachback-outline-v1`, `synthetic`. |
| Sử dụng | Giám khảo dùng các ý chuẩn và lời học viên để nhận định từng ý. AI người học chỉ nhận lời giảng mới và các câu hỏi phù hợp. |
| Giới hạn | Bản biên soạn phục vụ chạy thử. Các ý cần người dạy rà chuyên môn và thử với học viên trước khi dùng làm căn cứ chính thức. |

Bộ học liệu CP3 với 6 khái niệm được giữ trong [sample_lessons.json](sample_lessons.json) để đối chiếu mã nguồn của hai lượt đã lưu. Phiên CP4 dùng mã đoạn từ bộ 15 ngày.

## Dataset 2 · Nhật ký hành vi pre-class (`data/preclass/` do BTC cấp)

| | |
|---|---|
| Dùng để làm gì | Đào bằng chứng pain hành vi thật (`evidence/data-mining.md`), lấy tỷ trọng 3 nhóm tần suất người dùng (`42% / 40% / 18%`) và quy mô `436 / 721` học viên cho `cost/personas.yaml`, và làm nguồn tình huống cho 4/30 câu thử `data_that` trong `eval/benchmark.csv` |
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
