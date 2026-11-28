# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Chi tiết theo từng việc:

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Coding agent (Antigravity / LLM) | Gợi ý khung `codebase/tools.py`, `codebase/agent.py` theo sơ đồ `spec.md` §4 | Kiểm chạy thật qua `python run.py`, đối chiếu hợp đồng tool và chốt logic chặn rủi ro | Nguyễn Hoàng Trung |
| Prompt / thiết kế lời gọi mô hình | Coding agent / LLM | Nháp `SYSTEM` prompt, rà cấu trúc nhánh phản hồi `[THIẾU Ý]`, `[HIỂU SAI]`, `[ĐỦ Ý]` | Hiệu chỉnh phạm vi theo `spec.md` §4, thử nghiệm trên câu thử | Nguyễn Hoàng Trung, Đỗ Triệu Đức Phương |
| Đào data (viết script đếm, gợi ý nhãn) | Coding agent | Viết script thuần Python `evidence/count_preclass.py` và tóm tắt bảng kết quả | Chạy lại script trên `data/preclass/` của BTC, kiểm mẫu số `436` HV hoạt động và 6 ví dụ ẩn danh | Nguyễn Hoàng Trung, Nguyễn Duy Mạnh |
| Rà câu hỏi phỏng vấn / khảo sát | LLM | Chỉ rà câu hỏi tránh dẫn dắt theo Mom Test | Tự tạo form, gửi thu 25 phiếu thật ngoài nhóm (`evidence/KhaoSat.csv`), tự tính trung vị và Impact §2 | Nguyễn Duy Mạnh, Vũ Xuân Bách |
| Viết câu thử (benchmark) | Coding agent / LLM | Gợi ý biến thể câu chữ theo lưới input và 4 lớp chỗ khó | Tự duyệt đủ 24 câu, gắn rõ `source` (`9/24` từ `data_that`, `15/24` `tu_viet`), chạy `python run.py check` | Vũ Xuân Bách, Nguyễn Duy Mạnh |
| Sinh data `synthetic` (nếu có) | Coding agent / LLM | Hỗ trợ biên soạn cô đọng 6 khái niệm mẫu trong `data/sample_lessons.json` | Kiểm tay 12/12 đoạn học liệu và 18/18 ý chính chuẩn, không chép nguyên tài liệu khoá | Nguyễn Hoàng Trung |
| Chấm cột `pass` bằng LLM (nếu có) | Không dùng (dự kiến chấm tay + code) | — | Hai thành viên tự chấm chéo 5 output thật trước CP3 | Vũ Xuân Bách, Nguyễn Duy Mạnh |
| Slide, văn bản | Coding agent / LLM | Gợi ý bố cục `spec.md`, `canvas.md`, `eval/README.md`, `evidence/summary.md` | Toàn nhóm đối chiếu số liệu thật, chỉnh sửa theo thiết kế §3–§4 và chịu trách nhiệm từng mục | Cả nhóm |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
