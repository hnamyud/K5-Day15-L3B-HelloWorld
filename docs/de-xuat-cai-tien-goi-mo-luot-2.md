# Cải thiện câu gợi mở cho lượt 2

Nhóm chốt sửa câu gợi mở để học viên tự nhận ra chỗ hiểu sai trước khi vào lab. Lượt 1 đạt 26/30. Ba câu khó bị trượt đều dẫn đúng mã học liệu nhưng gặp lỗi khi gợi mở. [Kết quả lượt 1](../eval/run-1.csv)

- **B06.** AI nói sẵn ứng dụng là bên thực thi hàm rồi hỏi lại ai chạy hàm.
- **B08.** Học viên nhầm truy xuất tài liệu với gửi email hoặc cập nhật dữ liệu. AI hỏi sang chuyện thay đổi trọng số mô hình.
- **B23.** AI nêu sẵn bên điều khiển luồng và giới hạn số bước trong câu hỏi có/không.

Sửa `SYSTEM` trong `codebase/agent.py`. Ở nhánh `[THIẾU Ý]` và `[HIỂU SAI]`, AI bám vào lời giải thích mới nhất, hỏi đúng một câu mở về chỗ còn vướng và dẫn mã đoạn liên quan. Phần giải thích chuẩn dành cho nhánh **Xem lại kiến thức**.

Chạy `python run.py eval` với cùng model `cx/gpt-6-luna`, đủ 30 câu và tiêu chí chấm đã chốt. Đối chiếu B06, B08, B23 và ghi các câu tệ đi nếu có. [Cách chấm và đối chiếu](../eval/report.md)
