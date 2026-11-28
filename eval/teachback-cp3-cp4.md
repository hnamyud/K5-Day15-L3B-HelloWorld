# Từ bản CP3 trên main đến bản CP4 trên 15dayspreclass

CP3 đã nộp từ `main`, theo xác nhận của nhóm. Điểm gốc là [lượt 1](run-1.csv) **26/30**, chấm chéo **4/5**. PR `15dayspreclass → main` đề xuất bản CP4 với học liệu và phiên hai vai. Lượt 2 **26/30** đã lưu trên `main` là lần sửa prompt của luồng cũ. [Chấm chéo CP3](cross-check-trung.md) · [Hai lượt lịch sử](report.md)

## 1. Lỗi ở CP3 và thay đổi đề xuất cho CP4

Ở lượt gốc, B06 và B23 trượt vì AI nói sẵn phần cần gợi. B08 hỏi lệch điểm vướng. B03 trượt vì độ dài. Bản CP4 tập trung vào **giữ cơ hội để học viên tự sửa**. Giám khảo đối chiếu ngầm từng ý và AI người học hỏi từ danh sách của mục đang ôn. Hệ thống công bố đáp án khi đủ ý, hết lượt gợi mở hoặc học viên chọn xem lại. Học liệu mô phỏng đưa phạm vi chọn bài lên 15 ngày, với 52 mục.

## 2. Cách kiểm trước khi chạy đối chiếu

- Phép kiểm tương thích đưa nguyên văn 30 đầu vào CP2 vào `answer(text)` của hai bản. Dùng cùng model `gpt-4.1-mini`, cùng thứ tự câu trong bộ dữ liệu, và đo trên cùng tệp benchmark đã chốt.
- Bản nền kỹ thuật là `main@6ea10b4`. Bản này đã chứa lần sửa prompt cũ. Điểm CP3 đã nộp vẫn lấy từ lượt 1 lưu trong repo.
- Phép kiểm tự động ghi độ khớp nhãn mở đầu, mã nguồn thực tế và lỗi kỹ thuật. Tiêu chí đầy đủ của từng câu vẫn cần chấm theo rubric. B01–B30 tham chiếu mã đoạn và phạm vi học liệu cũ. Ca B09 là ví dụ cần đọc lại theo ngữ cảnh vì chọn model đã có trong học liệu CP4.
- Phép kiểm phiên CP4 chạy riêng 38 lời giảng có mã mục mới và đo chất lượng câu gợi mở, điều kiện chuyển mục và độ chính xác của giám khảo. [Kết quả phiên 15 ngày](study-15days-report.md)

## 3. Kết quả phát lại bộ CP2

Chạy `main@6ea10b4` và `3fb671d` với `gpt-4.1-mini`. Tệp đầu vào có SHA-256 `43d1f1decf7a8623261cf8ff7bfea0305e416ac0c6f36f80768bf14795ec0c04`. Hai bản dùng cùng đầu vào gốc. [Phản hồi theo từng ID](cp4-compatibility.json)

| Phép kiểm | main | CP4 15dayspreclass |
|---|---:|---:|
| Có phản hồi, không gặp lỗi kỹ thuật | 30/30 | 30/30 |
| Khớp nhãn mở đầu được yêu cầu rõ trong rubric | 27/29 | 24/29 |
| Lần gọi model | 19 | 20 |
| Token vào / ra | 20.832 / 2.120 | 7.313 / 275 |

B08 được đọc riêng vì rubric không yêu cầu nhãn mở đầu cụ thể. Các số khớp nhãn chỉ đo một phần tiêu chí. Thay đổi mã đoạn khiến bộ cũ cần đối chiếu nội dung nguồn trước khi diễn giải. Số điểm gốc CP3 vẫn là **26/30**. Số token ở đây đo đường đơn lượt của 30 ca, chưa đại diện cho chi phí trọn phiên.

| Ca | Điều quan sát được | Hướng xử lý |
|---|---|---|
| **B02** | `main` nhận đủ. CP4 hỏi thêm vòng lặp sau khi chọn token. | Rà điểm bắt buộc của mục sinh token. Giữ một ca diễn đạt tương đương để kiểm giám khảo có đòi cụm từ quá cụ thể hay không. |
| **B06** | CP4 gắn thiếu ý dù học viên khẳng định model tự chạy hàm. Câu hỏi hướng sang đường trả kết quả. | Kiểm xem giám khảo có xác định được mâu thuẫn về bên thực thi trước khi hỏi phần còn thiếu không. |
| **B07** | Cả hai bản lệch nhãn thiếu ý. CP4 coi câu “Agent tự làm hết” là hiểu sai. | Thêm ví dụ thiếu chi tiết và ví dụ khẳng định sai một cách rõ ràng để hiệu chuẩn ranh giới hai nhãn. |
| **B08** | CP4 giữ chủ đề RAG nhưng hỏi về dẫn nguồn. Chỗ học viên đang lẫn là truy xuất tài liệu với hành động gửi tin hoặc sửa dữ liệu. | Kiểm tuyến chọn mục và câu hỏi theo chính điểm lẫn trong lời giảng. |
| **B09** | CP4 tra được mục chọn model `[D01-P60]`. Rubric cũ yêu cầu thiếu căn cứ. | Giữ rubric CP2 nguyên trạng, ghi đây là thay đổi phạm vi học liệu khi đọc kết quả. |
| **B18** | CP4 xác nhận đủ cơ chế gọi hàm, dù lời giảng chưa nói đến bước người duyệt. | Bổ sung lại ý phân biệt công cụ chỉ đọc với công cụ gây tác động và bước duyệt vào mục phù hợp. Tạo một cặp ca giống nhau ngoài phần người duyệt. |
| **B19** | CP4 đổi từ đủ ý sang thiếu ý theo rubric. Câu hỏi hướng vào cách giữ bộ câu thử qua các phiên bản. | Xem đây là ca cải thiện trong phép phát lại này. |

Chạy lại phép phát lại với `MODEL_NAME=gpt-4.1-mini python eval/run_checkpoint_comparison.py --baseline 6ea10b4 --output /tmp/cp4-compatibility-new.json`. Chương trình đọc bộ câu đã khóa và lấy mã `main` qua bản lưu Git, giữ trạng thái nhánh làm việc.

## 4. Kết quả riêng của phiên CP4

Trên bộ **38 lời giảng mới**, giám khảo gắn đúng **37/38 nhãn** và **23/24 ca cần gợi mở** đạt tiêu chí. M34 phát biểu sai về trạng thái giữa các tiến trình nhưng được cho qua. Mốc này đo trực tiếp luồng hai vai của CP4. [Kết quả và ca trượt](study-15days-report.md)

Bộ mở rộng kiểm cả cách diễn đạt và ứng xử qua nhiều lượt. Kết quả là **54/66 ca**, với 6 lượt xác nhận đủ ý quá sớm. Hai bộ dùng tiêu chí và phạm vi khác nhau. [Báo cáo bộ mở rộng](teachback-variants-report.md)

## 5. Việc phát triển tiếp và cách nghiệm thu

| Thứ tự | Việc phát triển từ PR | Cách nghiệm thu |
|---|---|---|
| 1 | **Khôi phục ý về người duyệt** và rà các ý bắt buộc chuyển từ học liệu CP3 sang CP4. Bắt đầu từ B18. | Hai lời giảng có và thiếu bước người duyệt phải dẫn tới hai trạng thái khác nhau. Người dạy rà mục và mã nguồn. |
| 2 | **Giảm xác nhận đủ ý quá sớm.** Dùng M34 và B06 làm ca hồi quy. | Thử cả lời khẳng định sai, lời giải thích thiếu và lời tự sửa. Ghi nhãn, câu hỏi và thời điểm ứng dụng chuyển mục. |
| 3 | **Kiểm giữ đúng chỗ vướng qua nhiều lượt.** Bắt đầu bằng ca trộn khái niệm B08. | Ghi lời giảng đầu, câu hỏi, lời học viên tự sửa và trạng thái cuối. Chấm người để kiểm câu hỏi có tiết lộ đáp án hay hỏi sang ý khác. |
| 4 | **Đo học và chi phí theo phiên.** | Cập nhật A4 từ học viên ngoài nhóm, ghi token API theo trọn phiên, chốt slide và video dự phòng. [Nhật ký dùng thử](../validation/log.md) · [Chi phí](../cost/cost-estimate.md) · [Slide](../slides/outline.md) |
