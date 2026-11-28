# Bàn giao hackathon theo CP3 và CP4

Dùng bảng này để cập nhật hồ sơ và chuẩn bị PR `15-day → main`. **CP3 đã nộp từ `main`; CP4 dùng luồng hai vai trên `15-day`.** Mốc giờ và phân công lấy theo §10. “Có” nghĩa là repo có bằng chứng tương ứng. [Spec](../spec.md) · [Đối chiếu từ CP3 đến CP4](../eval/teachback-cp3-cp4.md)

## CP3 · Bản chạy thử và lượt gốc

Mốc theo spec là **10:00 ngày 28/11**. Mục tiêu là chốt lát cắt, có demo chạy model thật và một lượt đánh giá gốc để chọn lỗi cần cải tiến.

| Hạng mục | Người phụ trách theo spec | Bằng chứng hoặc trạng thái |
|---|---|---|
| Bằng chứng, impact và thiết kế | Nguyễn Hoàng Trung | Có [tổng hợp bằng chứng](../evidence/summary.md), [khảo sát](../evidence/survey/report.md) và [spec §0–§7](../spec.md). |
| Học liệu và chuẩn đánh giá đã chốt | Nguyễn Duy Mạnh, Vũ Xuân Bách | Có [benchmark 30 câu](../eval/benchmark.csv) và [4 metric](../eval/metric_spec.yaml). Dùng chuẩn §7 của CP2. Học liệu 6 khái niệm của mốc này nằm trong revision CP3. |
| Model thật và lượt gốc | Nguyễn Duy Mạnh | Có [run-1](../eval/run-1.csv) và [trace](../traces/run-1.jsonl). Lượt chạy `run-1@20261127-230315`, model `cx/gpt-6-luna`, ghi ở commit `246dc63`. |
| Chấm chéo và chấm hết bộ | Vũ Xuân Bách, Nguyễn Hoàng Trung | Có [chấm chéo 4/5](../eval/cross-check-trung.md) và điểm lượt 1 **26/30**. Bản chấm ở commit `3d8b581`. Lỗi đưa sang CP4 là gợi mở lộ đáp án hoặc hỏi lệch. |
| Video 30 giây | Đỗ Triệu Đức Phương | Repo đã ghi [link video CP3](https://drive.google.com/file/d/103SH3vI9oHgr-xipk7X_N-tLoN23WWxd/view?usp=sharing). Quyền xem cần nhóm kiểm trước khi nộp. |
| Thử mô phỏng chi phí 10 phiên | Đỗ Triệu Đức Phương | Repo có cấu hình và lệnh `python run.py simulate --try`. Hồ sơ chưa có kết quả để xác nhận thử chi phí CP3. [Chi phí](../cost/cost-estimate.md) |

## CP4 · Phiên hai vai trên 15-day

Mốc theo spec là **14:30 ngày 28/11**. PR bổ sung phần chênh lệch từ `main`: học liệu 15 ngày, vòng dạy lại hai vai, báo cáo và kịch bản demo tương ứng. Hồ sơ kết quả CP3 đã nộp được giữ để đối chiếu.

| Hạng mục | Người phụ trách theo spec | Bằng chứng hoặc trạng thái |
|---|---|---|
| Chọn lỗi và cải tiến có chủ đích | Nguyễn Duy Mạnh | CP3 ghi nhận AI lộ đáp án và hỏi lệch. CP4 tách giám khảo ngầm và AI người học, giữ câu hỏi trong mục đang ôn và mở đáp án ở bước đối chiếu. [Lỗi CP3 và thay đổi CP4](../eval/teachback-cp3-cp4.md) |
| Đối chiếu bộ cũ và đo luồng mới | Nguyễn Duy Mạnh, Vũ Xuân Bách | Bộ 30 dùng làm kiểm tương thích. [Kết quả phiên mới](../eval/study-15days-report.md) gồm **37/38** nhãn đúng và **23/24** ca gợi mở đạt tiêu chí trên bộ 38 lời giảng. [Run-2 26/30](../eval/run-2.csv) là lượt sửa prompt của luồng cũ trên `main`. |
| Kiểm thử phiên nhiều ý và đo A4 | Vũ Xuân Bách, Đỗ Triệu Đức Phương | Có [ca thử D01 của luồng hai vai](../eval/report.md#7-kiểm-tra-phiên-dạy-lại-hai-vai). Chỉ số A4 từ học viên ngoài nhóm vẫn chưa có số đo trong [nhật ký](../validation/log.md). |
| Mô phỏng chi phí dùng thật | Đỗ Triệu Đức Phương | Cần lưu lượt **≥50 phiên** và bảng tóm tắt đủ ba kịch bản vào [báo cáo chi phí](../cost/cost-estimate.md). Số token của 38 lượt đầu là số đo kỹ thuật bổ sung. Chỉ tính chi phí mỗi tác vụ thành công khi có tỷ lệ đạt phù hợp với model và tác vụ đang đo. |
| Slide, demo trực tiếp và video dự phòng | Nguyễn Hoàng Trung, Nguyễn Duy Mạnh, Đỗ Triệu Đức Phương | Có [dàn 8 slide](../slides/outline.md) và kịch bản demo. Repo chưa có `demo-slides.pdf` hoặc link video dự phòng CP4. Video 30 giây ở trên thuộc hồ sơ CP3. |
| Rà và nộp hồ sơ CP4 | Nguyễn Hoàng Trung | Đội trưởng duyệt phần cập nhật `spec.md`, số liệu, slide và quyền mở bằng chứng trước khi nộp. |

## Phần chênh lệch của PR CP4

- **Sản phẩm.** 52 mục học liệu mô phỏng theo đề cương công khai. AI người học hỏi một câu, giám khảo đối chiếu từng ý ở hậu trường rồi giải thích kèm nguồn khi chốt. [Data card](../data/DATA_CARD.md)
- **Kiểm chạy.** `python run.py` mở phiên dạy lại. `python run.py eval --try` kiểm đường đơn lượt chạy model. Năm bài kiểm thử trạng thái và vai trò chạy bằng `python -m unittest discover -s tests`.
- **Số đo trên nhánh.** Giám khảo gắn đúng 37/38 lời giảng giả lập. 23/24 ca cần gợi mở đạt tiêu chí. Ca M34 bị xác nhận đủ ý quá sớm. Điểm lượt gốc đã nộp là 26/30 trên bộ CP2. [Báo cáo 15 ngày](../eval/study-15days-report.md)
- **Phần chờ xác nhận.** Nhóm rà học liệu và chấm người trên mẫu gợi mở. Sau đó dùng [kịch bản A4](../validation/log.md) để đo học viên tự sửa được phần nào, và đo chi phí theo phiên trước khi chốt kết luận.

Khi cập nhật PR, mở đầu bằng lỗi quan sát ở CP3, rồi nêu thay đổi trên `15-day`, kết quả tương thích và số đo phiên CP4. Ghi đủ model, bộ câu, mẫu số và ca trượt để người đọc đối chiếu.
