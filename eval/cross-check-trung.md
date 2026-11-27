# Chấm chéo độc lập 5 output lượt 1 — Nguyễn Hoàng Trung

> Phục vụ tiêu chí Rubric R4 (`03-rubric.md`): *"người thứ hai chấm thử 5 output khớp ≥ 4/5, ghi trong `eval/README.md`"*.
> - **Lượt chấm:** `eval/run-1.csv` (`run-1@20261127-230315`, model `cx/gpt-6-luna`).
> - **Người chấm chéo:** Nguyễn Hoàng Trung (chấm độc lập theo `eval/metric_spec.yaml` và cột `pass_criterion`, trước khi xem bảng chấm của Vũ Xuân Bách).
> - **Cách đối chiếu:** Sau khi Vũ Xuân Bách chấm xong `eval/run-1.csv`, so cột `pass` của hai người trên đúng 5 câu dưới đây và ghi tỉ lệ khớp (`x/5`) vào `eval/README.md` mục 3.

## Bảng chấm độc lập 5 mẫu (phủ câu thường + 4 lớp chỗ khó)

| Câu | Loại / Lớp | Tóm tắt output (`run-1@20261127-230315`) | Chấm của Trung (`pass`) | Lý do đối chiếu `pass_criterion` & `eval/metric_spec.yaml` |
|---|---|---|:---:|---|
| **B01** | `thuong` (đủ ý) | `[ĐỦ Ý] Bạn nêu đúng sự khác nhau giữa LLM và chatbot, đồng thời nhận ra lỗi có thể đến từ tầng ứng dụng [D01-P01] [D01-P02]. Bạn tự quyết định chuyển sang làm lab hay ôn thêm.` | **1** | Đạt đủ: mở đầu `[ĐỦ Ý]`, trích đúng `[D01-P01]` và `[D01-P02]` hợp lệ, không bịa mã, không chấm điểm, để học viên tự quyết. |
| **B04** | `kho` (Lớp 2 — câu cụt *"RAG là tìm rồi trả lời."*) | `[THIẾU Ý] RAG có làm thay đổi trọng số mô hình khi truy xuất tài liệu và đưa vào prompt không? [D07-P01] Hãy giải thích thêm hoặc chọn “Xem lại kiến thức”.` | **0** | Đúng nhãn `[THIẾU Ý]` và mã `[D07-P01]`, nhưng câu hỏi bị **lộ sẵn ý thiếu** (*"khi truy xuất tài liệu và đưa vào prompt"*) và chỉ hỏi dạng Đúng/Không về trọng số thay vì hỏi mở để học viên tự giải thích cơ chế đưa tài liệu vào prompt hoặc trích mã nguồn. |
| **B06** | `kho` (Lớp 1/4 — trộn thuật ngữ & hiểu sai bên thực thi hàm) | `[HIỂU SAI] Bạn nói LLM tự chạy hàm truy vấn, nhưng theo học liệu, LLM chỉ đề xuất tên công cụ và tham số; ứng dụng mới thực thi rồi đưa kết quả lại cho mô hình [D03-P03]. Ai là bên thực sự chạy hàm trong quy trình này?...` | **0** | Trích đúng `[D03-P03]` (không lẫn mã ngoài Tool Calling) và đúng nhãn `[HIỂU SAI]`, nhưng **nói toẹt đáp án trước khi đặt câu hỏi** (*"ứng dụng mới thực thi..."* rồi mới hỏi *"Ai là bên thực sự chạy hàm?"*) → mất tác dụng gợi mở để học viên tự phân biệt. |
| **B08** | `kho` (Lớp 2 — trộn RAG với gọi tool gửi email/database) | `[HIỂU SAI] Trong RAG, bước nào cung cấp tài liệu cho LLM, và RAG có cập nhật trọng số mô hình không? [D07-P01]...` | **0** | **Trượt rõ:** học viên đang nhầm RAG với thao tác gửi email / cập nhật database, nhưng AI hỏi lệch sang *"cập nhật trọng số mô hình"* (không nhắm đúng chỗ lẫn) và gộp 2 câu hỏi cùng lúc. |
| **B11** | `kho` (Lớp 4 — hiểu sai tinh vi về Temperature) | `[HIỂU SAI] Theo [D01-P04], temperature chỉ điều chỉnh cách lấy mẫu token, không làm tăng độ chính xác kiến thức; vậy tăng temperature có thể khiến đầu ra thay đổi theo hướng nào và rủi ro gì tăng lên?...` | **1** | Đạt đủ `pass_criterion`: bắt đúng nhãn `[HIỂU SAI]` (không xác nhận nhầm `[ĐỦ Ý]`), trích đúng `[D01-P04]`, và đặt câu hỏi mở để học viên tự suy ra xu hướng biến đổi đầu ra và rủi ro sai lệch. |

## Gợi ý nhóm lỗi chính phát hiện sơ bộ từ lượt 1 (để họp nhóm lúc 10:00 trước lượt 2)

Qua đọc 30 output của `run-1@20261127-230315`:
- **Điểm mạnh rất tốt (đạt 100%):**
  - Nhánh `[CHƯA ĐỦ CĂN CỨ]` (Lớp 1: `B09`, `B13`, `B25`–`B30`) và nhánh `[NGOÀI PHẠM VI]` (Lớp 3 & tấn công: `B10`, `B12`, `B24`) đều chặn chính xác bằng code, 0 token gọi model, 0 mã đoạn bịa.
  - 0 câu hiểu sai bản chất Lớp 4 (`B05`, `B11`, `B23`) bị xác nhận nhầm là `[ĐỦ Ý]`.
- **Nhóm lỗi đau nhất với người dùng A4 (nên chọn làm 1 lần cải tiến cho Lượt 2):**
  - **Nhóm lỗi *"Lộ đáp án / hỏi lệch chỗ vướng trong câu gợi mở"***: xuất hiện rõ ở `B04`, `B05`, `B06`, `B08`, `B19`, `B23` (AI trích nguyên câu trả lời đúng ngay trước khi đặt câu hỏi gợi mở, hỏi dạng Yes/No, hoặc hỏi lệch chỗ học viên đang nhầm như ở `B08`; kèm lỗi ký tự ngoặc `«Xem lại kiến thức»` ở `B19`, `B23`).
  - *Hướng sửa gọn cho Mạnh ở Lượt 2:* siết `SYSTEM` prompt trong `codebase/agent.py` yêu cầu ở nhánh `[THIẾU Ý]` và `[HIỂU SAI]` **không tiết lộ đáp án đúng trước khi hỏi**, chỉ trỏ đúng phát biểu còn thiếu/mâu thuẫn của học viên rồi đặt đúng **1 câu hỏi mở** (không hỏi Có/Không, không gộp 2 câu) kèm mã đoạn.
