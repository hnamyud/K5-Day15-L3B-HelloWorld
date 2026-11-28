# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Chi tiết theo từng việc đến mốc CP4:

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử & giao diện | Coding agent (Antigravity, Claude, Codex) | Gợi ý khung `codebase/tools.py`, `agent.py`, `ai.py`, `guardrails.py`, `session.py`, `app.py`, `web.py` và cấu trúc hậu kiểm JSON Lượt 3 | Kiểm định tuyến 30/30 câu, sửa lỗi chặn nhầm `B01` & từ khoá chung, test CLI/Web với API thật (`cx/gpt-6-luna`, `gpt-4.1-mini`) và kiểm `git status` không lộ `.env` | Nguyễn Hoàng Trung (CP2), Nguyễn Duy Mạnh & Đỗ Triệu Đức Phương (CP3–CP4) |
| Prompt / thiết kế lời gọi mô hình | Coding agent / LLM | Nháp `SYSTEM` prompt, đề xuất cải tiến gợi mở Lượt 2 và schema JSON kiểm tra Lượt 3 | Đối chiếu sơ đồ `spec.md` §4, đo trước/sau qua `eval/run-1.csv` → `run-2.csv` → `run-3.csv` | Nguyễn Duy Mạnh, Nguyễn Hoàng Trung, Đỗ Triệu Đức Phương |
| Đào data (viết script đếm, gợi ý nhãn) | Coding agent (Antigravity) | Viết script thuần Python `evidence/count_preclass.py` và tóm tắt bảng kết quả | Chạy lại script trên `data/preclass/` của BTC, kiểm mẫu số `436` HV hoạt động, bác bỏ giả thuyết 1 (`1.0%` bỏ qua quiz) và kiểm 6 ví dụ ẩn danh | Nguyễn Hoàng Trung, Nguyễn Duy Mạnh |
| Rà câu hỏi phỏng vấn / khảo sát | LLM | Chỉ rà câu hỏi tránh dẫn dắt theo Mom Test | Tự tạo form, gửi thu 25 phiếu thật ngoài nhóm (`evidence/KhaoSat.csv`, lọc `22` phiếu L3), tự tính trung vị `20 phút` và Impact §2 | Nguyễn Duy Mạnh, Vũ Xuân Bách, Nguyễn Hoàng Trung |
| Viết câu thử (benchmark) | Coding agent / LLM | Gợi ý biến thể câu chữ theo lưới input 4 chiều và 4 lớp chỗ khó | Tự rà soát & phân loại lại trung thực đủ **30 câu** (`10/30 = 33.3%` nguồn thật: `6 nguoi_dung` từ `KhaoSat.csv`, `4 data_that` từ `answers.csv`; `20 tu_viet`), chạy `python run.py check` sạch | Vũ Xuân Bách, Nguyễn Hoàng Trung, Nguyễn Duy Mạnh |
| Sinh data `synthetic` (học liệu mẫu) | Coding agent / LLM | Hỗ trợ biên soạn cô đọng 6 khái niệm mẫu trong `data/sample_lessons.json` | Kiểm tay 12/12 đoạn học liệu (`D01-P01` → `D09-P02`) và 18/18 ý chính chuẩn, không chép nguyên tài liệu khoá (`data/DATA_CARD.md`) | Nguyễn Hoàng Trung |
| Hỗ trợ rà chấm cột `pass` & kiểm thử phiên | Codex (không chấm tự động thay người) | Tóm tắt checklist 30 `pass_criterion`, rà phản hồi với trace và gợi ý lý do chấm | Vũ Xuân Bách tự đọc phản hồi & chốt từng điểm `pass` (vd giữ `B04 = 1` dù Codex gợi ý `0`); chấm chéo độc lập với Nguyễn Hoàng Trung khớp **4/5 (80%)** (`eval/cross-check-trung.md`, `eval/README.md`) | Vũ Xuân Bách, Nguyễn Hoàng Trung |
| Slide, báo cáo & văn bản | Coding agent (Antigravity, Codex) | Gợi ý bố cục `spec.md`, `canvas.md`, `eval/report.md`, `cost/cost-estimate.md`, tạo `slides/demo-slides.html` xuất `demo-slides.pdf` | Toàn nhóm đối chiếu trực tiếp từng con số về file nguồn, loại bỏ số không truy vết được, kiểm trực quan cả 8 trang PDF và chịu trách nhiệm từng phần | Cả nhóm (Nguyễn Hoàng Trung tổng hợp `spec.md` & `demo-slides.pdf`) |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
