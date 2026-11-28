# Người dùng thử *(bonus)*

> Điền ở guide bước 4.3 — 2–3 người ngoài nhóm, ~10 phút / người, theo 5 nhịp: làm quen · bối cảnh · giao việc · quan sát · hỏi sau. Ôn lại: ngày 5, ngày 13. Chấm ở rubric Bonus.
> Không ghi tên: ghi vai. Hành vi quan sát được nặng hơn lời nói; toàn lời khen = phiên chưa đạt, giao việc khó hơn.
> Người dùng thử **không thay được** bằng chứng pain ở `evidence/`.

## Kịch bản dùng thử

- Mời 2–3 học viên L3 ngoài nhóm, khoảng 10 phút/người. Nói rõ người tham gia đang thử công cụ và có thể dừng bất cứ lúc nào. Hỏi trước lab bạn thường kiểm tra mình đã hiểu bài bằng cách nào.
- Giao việc: “Bạn vừa học xong bài pre-class về chatbot và temperature. Hãy dạy lại cho AI một ý bạn vừa học, rồi dùng câu hỏi của AI để tự làm rõ chỗ còn vướng trước khi vào lab.” Mở `python run.py` và để người thử tự chọn bài D01, thao tác và diễn đạt. Quan sát họ làm gì trước, chỗ do dự và lúc chọn xem lại hoặc để ôn sau.
- Hỏi sau: “Ý nào bạn vừa làm rõ? Bạn sẽ áp dụng nó thế nào trong lab?”. Cho người thử tự nói bằng lời của mình sau khi đóng gợi ý, rồi đối chiếu với học liệu. Hỏi thêm câu về mức tiếc nuối bên dưới.

| Người thử (vai) | Việc giao (theo kết quả, không theo nút) | Quan sát (làm gì đầu tiên, chỗ do dự, chỗ hiểu sai) | Trích nguyên văn | Mức nghiêm trọng (cao / vừa / thấp) |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

Câu hỏi sau: *"Nếu mai không được dùng nữa, bạn thấy: rất tiếc / hơi tiếc / không sao?"* → __ / __ / __

## Chỉ số tự giải thích lại (A4)

Ghi mỗi ý có điểm thiếu hoặc sai và đã nhận câu gợi mở hoặc phần **Xem lại kiến thức**. Đối chiếu lời diễn đạt mới với điểm còn thiếu/sai và mã đoạn tương ứng. Ghi rõ số lượt gợi mở, có xem lại hay không và trường hợp người thử bỏ qua hoặc dừng sớm.

| Người thử (mã ẩn danh) | Ý và mã đoạn | Điểm thiếu/sai ban đầu | Số lượt gợi mở / đã xem lại? | Lời diễn đạt mới | Tự giải thích đúng? |
|---|---|---|---|---|---|
| | | | | | |

- Kết quả thực tế: **chưa đo được**. Chưa có phiên với học viên L3 ngoài nhóm để tính tỷ lệ theo ngưỡng §7 (≥75%).

## Kiểm thử theo vai học viên trên bản dòng lệnh

Ba kịch bản dưới đây chạy qua giao diện `codebase/app.py` và workflow tại commit `6ea10b4`. Câu nhập của học viên được soạn cho kịch bản. Các phản hồi model được cấp sẵn để kiểm tra cách ứng dụng xử lý từng nhánh. Kết quả ghi từ màn hình Terminal.

| Kịch bản | Thao tác | Quan sát khi chạy |
|---|---|---|
| A. Ôn hết hai mục D01 | Giải thích rằng LLM tự giữ lịch sử, sửa lời giải thích sau gợi mở. Sang Temperature, tiếp tục nhầm giữa lấy mẫu và độ chính xác qua hai lượt, rồi tự diễn đạt lại sau khi xem học liệu. | Hai mục được xử lý lần lượt. Temperature hiện đúng hai câu gợi mở trước phần xem lại. Cuối phiên có lời mời tự nhắc lại, rồi tổng hợp cả hai mục **Đã giải thích được** theo phản hồi mẫu. |
| B. Cần xem nhanh trước khi vào lab | Mở D01, chọn `/xem`, để mục đầu ôn sau bằng `/sau`, rồi kết thúc ở mục tiếp theo bằng `/thoat`. | Học liệu của mục đầu hiện kèm mã đoạn. Tổng hợp ghi mục đầu **Nên ôn lại**, mục sau **Chưa kiểm tra**. |
| C. Lẫn hai khái niệm | Ở mục Chatbot và LLM, nhập lời giải thích lẫn với RAG. Cấp phản hồi mẫu dẫn `[D07-P01]` của bài RAG, rồi chọn để ôn sau. | Phản hồi lệch nguồn bị chặn. Giao diện nhắc tiếp tục ở mục hiện tại và vẫn cho để ôn sau. |

Giữ cách hiển thị trạng thái cuối phiên để người học biết mục nào cần xem tiếp. Ở buổi dùng thử với học viên thật, cần quan sát xem người học có nhận ra bước tiếp theo khi gặp thông báo thiếu căn cứ hay không. Mục này chỉ cung cấp bằng chứng kiểm thử luồng. Tỷ lệ A4 vẫn cần quan sát từ học viên thật.

## Tổng hợp

- Chủ đề lặp nhiều nhất: __
- Sửa gì trước demo (ghi `spec.md` §10): __
- Giữ gì và vì sao: __
- Để dành sau: __
