# Reflection — Đỗ Triệu Đức Phương

## 1. Vai trò và phần tôi làm

Ở CP2, tôi góp phần chốt cách đánh giá và giả định chi phí trong [`spec.md` §7–§8](../spec.md) (`bb10809`).\
Ở CP3, tôi triển khai luồng ôn nhiều ý trong [`codebase/session.py`](../codebase/session.py) và tích hợp vào [`codebase/app.py`](../codebase/app.py) (`25422ff`). Luồng giữ trạng thái từng ý, giới hạn hai câu gợi mở và tổng hợp phần cần ôn lại.\
Ở CP4, tôi kiểm thử giao diện web, quay video dự phòng với một câu thường và một câu khó, rồi cập nhật [báo cáo chi phí](../cost/cost-estimate.md) theo kết quả Lượt 3 (`d558cf4`). Tôi cũng ghi các ca kiểm thử theo vai học viên trong [nhật ký dùng thử](../validation/log.md) (`8df6290`).

## 2. AI hỗ trợ tôi thế nào?

Tôi dùng Codex để viết phần quản lý phiên, thử các nhánh xem lại kiến thức và kết thúc sớm, rồi chuẩn bị kịch bản quay video web.\
Khi repo có Lượt 3, tôi yêu cầu tính lại chi phí từ token mới và giữ Lượt 2 làm mốc so sánh. Bảng của tôi ghi rõ đây là ước tính từ token eval đã lưu. Nhóm bổ sung số đo từ lượt `simulate-1` sau đó.\
Trong nhật ký, tôi ghi rõ những phiên nào dùng phản hồi mẫu để kiểm tra giao diện. Chỉ số A4 từ học viên L3 thật vẫn chưa đo được.

## 3. Một câu thử trượt và điều tôi học được

Tôi chọn [B11 ở Lượt 3](../eval/run-3.csv) vì đây là hiểu lầm về Temperature mà tôi dùng khi quay demo. Học viên cho rằng tăng Temperature giúp mô hình suy luận sâu và trả lời chính xác hơn.\
AI nhận đúng chỗ hiểu sai và dẫn `[D01-P04]`, nhưng mở đầu câu hỏi bằng “Nếu temperature chỉ thay đổi cách lấy mẫu token”, nên đã nói trước điều học viên cần tự nhận ra. Câu này bị chấm trượt.\
Tôi học được rằng khi kiểm thử luồng ôn, tôi cần đọc cả câu gợi mở và xem học viên còn phải tự suy ra điều gì. Với ca này, tôi sẽ hỏi “Khi tăng Temperature, cách mô hình chọn token thay đổi thế nào?” rồi đợi học viên tự diễn đạt trước khi mở học liệu.
