# Reflection — Vũ Xuân Bách

## 1. Vai trò và phần tôi làm

Tôi phụ trách đánh giá bản chạy thử của nhóm trên bộ 30 câu ở `eval/benchmark.csv`.\
Ở CP3, tôi chấm Lượt 1 và đối chiếu 5 câu với Trung. Hai bảng khớp 4/5, khác ở B04.\
Ở CP4, tôi chấm Lượt 2, so sánh các câu cải thiện và tệ đi, rồi tổng hợp kết quả kiểm thử phiên D01. Phần việc được ghi trong `eval/README.md` và `eval/report.md`, ở các commit `3d8b581`, `6ea10b4` và `988f222`.

## 2. AI hỗ trợ tôi thế nào?

Tôi dùng Codex để tóm tắt tiêu chí đạt của từng câu thành một checklist 30 câu, rà phản hồi với trace và gợi ý cách ghi lý do chấm.\
Ở B04, Codex đề xuất điểm 0 vì câu hỏi đã nêu một phần nội dung trước khi hỏi. Sau khi đọc lại phản hồi và tiêu chí, tôi chốt 1 vì câu trả lời nhận ra học viên còn thiếu ý, dẫn đúng đoạn học liệu về cách RAG tìm và sử dụng tài liệu, rồi hỏi một câu phù hợp để học viên bổ sung.\
Codex cũng giúp tôi kiểm thử luồng D01 và tổng hợp bốn ca mô phỏng. Chỉ số A4 từ học viên thật vẫn được ghi là chưa đo được.

## 3. Một câu thử trượt và điều tôi học được

Ở B08, học viên nhầm việc RAG truy xuất tài liệu với việc gọi công cụ gửi email và cập nhật cơ sở dữ liệu.\
Phản hồi Lượt 2 dẫn đúng đoạn học liệu giải thích cách RAG tìm tài liệu và đưa tài liệu vào ngữ cảnh để trả lời. Tuy nhiên, AI lại hỏi thêm về trọng số, nên chưa giúp học viên phân biệt hai thao tác đang bị lẫn.\
Tôi học được rằng kiểm xem AI có dẫn đúng đoạn học liệu chỉ là một phần của việc chấm. Khi đánh giá câu gợi mở, tôi còn phải xem học viên cần tự nhận ra điều gì và câu hỏi có dẫn họ tới đúng chỗ đó không.
