# Reflection — Nguyễn Duy Mạnh

> Làm ở guide bước 5.3. Mỗi câu ngắn gọn, trỏ tới file và commit thật của nhóm.

## 1. Vai trò + phần mình làm

**Thành viên** (mã `2A202603806`). Ở CP1–CP2, tôi làm cặp Bằng chứng & Eval với Bách: triển khai khảo sát học viên L3 (`evidence/KhaoSat.csv`, 25 phiếu, 22 phiếu L3), tính bảng Impact §2 và góp phần thiết kế tương tác AI ở `spec.md` §4, §9 (commits `8fb8b5a`, `e983a6d`, `f7599ec`).
Từ CP3, sau khi đổi vai với Trung, tôi phụ trách `codebase/`. Tôi nối model thật qua API OpenAI-compatible trong `codebase/ai.py` và chạy Lượt 1 (`eval/run-1.csv`, commit `246dc63`). Ở CP4, tôi sửa câu gợi mở cho Lượt 2 (`287a862`), khóa ý đang ôn và chặn yêu cầu ngoài phạm vi (`c8754f2`), làm giao diện web demo `codebase/web.py` (`b777ee9`). Cuối cùng, tôi chuyển nhánh đối chiếu sang phản hồi JSON có code kiểm tra và chạy Lượt 3 (`eval/run-3.csv`, commit `c773ae1`, PR #4).

## 2. AI hỗ trợ mình thế nào

Tôi dùng Claude Code (bản desktop) để dựng giao diện web, tìm nguyên nhân model trả lời chậm (khoảng 5 giây mỗi lượt gọi, do độ trễ cố định của proxy, không do prompt dài), đề xuất và code bộ kiểm JSON của Lượt 3, chạy eval rồi chấm sơ bộ.
Có mấy chỗ tôi phải chỉnh lại:
- Claude định chạy eval bằng Gemini cho nhanh. Tôi dừng lại và yêu cầu dùng đúng `cx/gpt-6-luna` như Lượt 1–2, để so sánh công bằng.
- Bản giao diện đầu bị lệch bố cục, tin nhắn dài không được thu gọn, và tự nhảy sang màn tự nhắc lại trước khi tôi kịp đọc phản hồi cuối. Tôi yêu cầu làm lại cả ba chỗ.
- Khi tôi muốn xóa `run-2` để chạy lại cùng tên, Claude từ chối vì `AGENTS.md` cấm sửa lượt đã chạy. Tôi đồng ý chạy thành `run-3`.
- Cột `pass` của `run-3` hiện vẫn là điểm Claude chấm sơ bộ, cần người chấm của nhóm xác nhận.

## 3. Một câu thử trượt của nhóm và mình học được gì từ nó

Tôi chọn **`B11`**. Học viên cho rằng tăng temperature giúp mô hình "suy luận sâu hơn và chính xác hơn".
- Lượt 1: đạt.
- Lượt 2: trượt, vì AI giảng sẵn cách lấy mẫu và độ đa dạng rồi mới hỏi.
- Lượt 3: dù đã thêm bộ kiểm chặn các cụm như "thực chất", "thực ra", "chứ không", "nghĩa là", câu hỏi vẫn mở đầu bằng *"Nếu temperature chỉ thay đổi cách lấy mẫu token…"*, tức vẫn lộ đáp án qua một mệnh đề giả định. `B23` cũng trượt theo đúng kiểu này. Lượt 3 đạt 28/30 (chấm sơ bộ), cả hai câu trượt đều vì lý do đó.

Tôi học được rằng kiểm bằng code chỉ bắt được *hình thức*, không bắt được *ý nghĩa*: model luôn tìm được cách diễn đạt khác đi vòng qua danh sách từ khóa. Muốn biết câu hỏi có thật sự để học viên tự nghĩ hay không vẫn phải có người đọc theo `pass_criterion`, và phải chạy lại cả bộ sau mỗi lần sửa. Ở Lượt 2, sửa prompt cứu được `B06`, `B23` nhưng lại làm hỏng `B05`, `B11`.
