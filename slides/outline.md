# Dàn slide — HelloWorld (Track A · A4) → xuất `demo-slides.pdf` ở thư mục gốc repo

> Làm ở guide bước 5.1. Luật: **không có bằng chứng thì không có slide** — mỗi trang ≥1 con số / trích dẫn có nguồn / kết quả đo.
> Xuất PDF thành `demo-slides.pdf` ở thư mục gốc repo, nộp tại **CP4 14:30 Thứ Bảy 28/11**.

## Tổng quan 8 trang & nguồn số liệu

| # | Trang | Nội dung cốt lõi + Số liệu / Trích dẫn có nguồn | Nguồn file | Trạng thái |
|---|---|---|---|---|
| **1** | **Người dùng & Pain** | **Người dùng:** Học viên AI20K L3 (`L3A`, `L3B`) vừa xong pre-class, chuẩn bị làm lab.<br/>**Pain (ảo tưởng hiểu bài):** Đọc lướt slide (`13/22 = 59.1%`) thấy quen nên tưởng đã hiểu đủ, tới lúc code lab mới lộ sai bản chất.<br/>**2 nguồn kiểm chéo:**<br/>• *Khảo sát (`n=22` L3 / 25 phiếu):* **`14/22 (63.6%)`** nghĩ mình hiểu đủ nhưng vào lab mới phát hiện sai; mất trung vị **`20 phút/lần`** (`15–60 phút`). Trích dẫn #21 L3B: *"đọc slide thấy quen nên chủ quan, lúc code CrossEntropyLoss lỡ cho qua softmax trước nên kết quả lệch hẳn"*.<br/>• *Data thật `data/preclass/` (`436` HV hoạt động):* **`98.9%`** lời bạn học AI xen giữa video bị phớt lờ (`151/13.975 = 1.1%` phản hồi); **`69/77 (89.6%)`** HV làm `pre_post_post` sai lần đầu (`399/1.968 = 20.3%`); chỉ **`18/436 (4.1%)`** tự giải thích. | `evidence/summary.md`, `evidence/survey/report.md`, `evidence/data-mining.md` | ☑ Đủ số thật |
| **2** | **Vì sao chọn bài này (Impact)** | **Hướng chọn (A4 tự giải thích trước lab):** `14 người × 3 lần/tháng × 20 phút/lần = 840 phút/tháng (14 giờ/tháng)` trong mẫu khảo sát (`~60 phút/người/tháng`, ước tính ~277 giờ/tháng nếu áp tỷ lệ lên 436 HV hoạt động *(tự ước tính)*).<br/>**2 hướng ĐÃ LOẠI (có số):**<br/>• *Can thiệp khi bỏ qua quiz giữa video:* chỉ **`21/2.153 (1.0%)`** lượt bỏ qua (`0/4.322` tua vượt) → bác bỏ giả thuyết ban đầu.<br/>• *Nhiều bạn học AI xen giữa video:* **`98.9%`** bị phớt lờ, `0/228` thưởng `phan_hoi_xay_dung`, tốn token nhân theo số vai và không kịp 10 giờ. | `spec.md` §2 | ☑ Đủ số thật |
| **3** | **Giải pháp AI** | Học viên chủ động chọn ngày và dạy lại từng mục. Giám khảo đối chiếu ngầm từng ý với học liệu, còn AI người học chỉ hỏi một câu về chỗ vướng. Khi đủ ý hoặc hết lượt, giám khảo mở phần đối chiếu kèm nguồn. Học liệu mô phỏng gồm 52 mục trên 15 ngày. | [Thiết kế](../spec.md) · [Học liệu](../data/DATA_CARD.md) | Đã có bản chạy thử |
| **4** | **Demo live** | Chạy `python run.py`, nhập `ôn lại ngày 1`, thử nói công cụ tạo ảnh cũng là LLM. AI hỏi lại về ví dụ tạo ảnh. Phân biệt GenAI với LLM và giải thích AI, ML, Deep Learning để giám khảo hiện `[D01-P51]` rồi chuyển mục. Dùng `/thoat` để xem tổng hợp. | [Ca thử thật](../eval/report.md#7-kiểm-tra-phiên-dạy-lại-hai-vai) | Đã xác nhận luồng bằng model thật |
| **5** | **Đánh giá thế nào** | CP3 đã nộp từ main đạt 26/30. CP4 trên 15dayspreclass có 37/38 nhãn đúng và 23/24 ca gợi mở đạt tiêu chí trên bộ giả lập. Phát lại 30 câu cũ với cùng model cho 27/29 nhãn khớp trên main và 24/29 trên 15dayspreclass. B18 và M34 chỉ rõ rủi ro xác nhận đủ ý sớm. | [Đối chiếu CP3 đến CP4](../eval/teachback-cp3-cp4.md) · [Bộ 38 ca](../eval/study-15days-report.md) | Đã đo bằng model thật |
| **6** | **Chi phí khi dùng thật** | Luồng mới xử lý 38 lượt giả lập bằng 47 lần gọi model, 16.227 token vào và 605 token ra. Đây là số dùng API của các lượt đầu, chưa đủ để suy ra chi phí một phiên trọn bài. | [Số đo API](../eval/study-15days-report.md) · [Mô phỏng chi phí](../cost/cost-estimate.md) | Cần đo theo phiên |
| **7** | **Kết luận** | Tiếp tục thử có giám sát. Học liệu đã có mục mẫu trên 15 ngày, 23/24 ca cần gợi mở đạt tiêu chí. Sai sót còn lại là giám khảo xác nhận đủ ý quá sớm ở ca M34. Cần đo học viên tự sửa được gì sau gợi mở. | [Báo cáo 15 ngày](../eval/study-15days-report.md) · [Nhật ký dùng thử](../validation/log.md) | Chưa kết luận hiệu quả học |
| **8** | **Nếu có thêm 1 tuần** | Khôi phục ý người duyệt ở B18, bổ sung ca hồi quy cho M34 và B06, kiểm câu gợi mở qua nhiều lượt rồi đo học viên tự sửa được gì trước khi xem đáp án. | [Hướng phát triển và cách nghiệm thu](../eval/teachback-cp3-cp4.md) | Chờ thử với học viên |

---

## Checklist trước khi lên demo (guide 5.2 & 5.3)
- [ ] Tải repo về thư mục sạch, chạy theo `README.md` trong 3 phút; `.env` trên máy demo đã test gọi thật trong vòng 1 giờ trước demo.
- [ ] Video demo dự phòng mở được bằng cửa sổ ẩn danh.
- [ ] Kiểm `demo-slides.pdf` nằm ở **thư mục gốc repo** (`K5-Day15-L3B-HelloWorld/demo-slides.pdf`).
- [ ] Không có API key / `.env` / dữ liệu cá nhân thật trong repo.
- [ ] Cả 4 thành viên trả lời trôi chảy 4 câu hỏi giám khảo: *(1) Vì sao chọn workflow cố định? (2) Lỗi nguy hiểm nhất là gì? (3) Chi phí / task thành công tính thế nào? (4) Phần bạn làm là gì?*

## Phân công thuyết trình (mỗi thành viên trình bày 2 trang)

| Trang | Nội dung | Người trình bày |
|---|---|---|
| **Trang 1–2** | Người dùng, Pain (2 nguồn) & Bảng Impact / Hướng loại | **Nguyễn Hoàng Trung** |
| **Trang 3–4** | Giải pháp AI (sơ đồ, công cụ, chặn rủi ro) & **Demo live** | **Nguyễn Duy Mạnh** |
| **Trang 5** | Đánh giá: Dataset, 30 câu thử, 4 metric, Lượt 1 → Lượt 2 & Lỗi chính | **Vũ Xuân Bách** |
| **Trang 6–8** | Mô phỏng chi phí 3 kịch bản, Người dùng thử, Kết luận & Kế hoạch 1 tuần | **Đỗ Triệu Đức Phương** |
