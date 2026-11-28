# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Khi có lượt đo mới, chạy `python run.py simulate --rate-from eval/run-2.csv` rồi lấy bảng trong `cost/simulate-N-summary.md`.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

> Luồng hai vai đã ghi số đo API cho 38 lượt đầu tại [báo cáo 15 ngày](../eval/study-15days-report.md). Chi phí cho một phiên nhiều mục và tỷ lệ học viên tự sửa vẫn cần đo.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): dùng ít **42,2% · 2 phiên/tháng · 3 lượt/phiên**, dùng vừa **39,7% · 5 · 6**, dùng nhiều **18,1% · 10 · 10**. Tỷ trọng lấy từ `evidence/data-mining.md`. Tần suất và số lượt là tự ước tính cho bài mẫu ba ý.
- **Quy mô người dùng/tháng:** thấp **250** *(tự ước tính)*, cơ sở **436** và cao **721** *(kịch bản lấy mốc từ dữ liệu pre-class, xem `spec.md` §8)*.
- **Giá Standard trả phí (USD / 1 triệu token vào / ra):** `gemini-3.1-flash-lite` **0,25 / 1,50**, `gemini-4-hydrogen` **1,50 / 7,50**. [Bảng giá Gemini API, xem 27/11/2026](https://aistudio.google.com/docs/pricing).
- **Tỉ lệ đạt và model đo token:** **26/30 (86,7%)**, từ `eval/run-2.csv` (`run-2@20261128-001731`, model `cx/gpt-6-luna`). Bảng áp đơn giá hai model Gemini từ `cost/personas.yaml` lên token thực đo của Lượt 2. Lượng token và tỷ lệ đạt có thể đổi nếu triển khai bằng một trong hai model Gemini.

## 2. Kết quả mô phỏng

### Ước tính từ token của Lượt 2

Tạo lịch **50 phiên, seed 42** bằng khung mô phỏng hiện tại. Với từng đầu vào được chọn, dùng lại token và số lần gọi ghi trong `eval/run-2.csv` rồi cộng theo phiên. Lịch gồm **253 lượt gửi**, tương ứng **180 lần gọi model**, **261.519 token vào** và **15.934 token ra** theo số đã ghi. Những lần cùng một câu được chọn dùng chung số token Lượt 2 của câu đó. Chưa có lượt gọi API mới cho toàn bộ 50 phiên.

| Nhóm | Số phiên trong lịch | Lượt gửi / phiên | Token vào / phiên | Token ra / phiên |
|---|---:|---:|---:|---:|
| Dùng ít | 25 | 3 | 3.093 | 185 |
| Dùng vừa | 18 | 6 | 6.278 | 385 |
| Dùng nhiều | 7 | 10 | 10.170 | 627 |

| Đơn giá áp dụng | Chi phí / phiên | Chi phí / task thành công | / tháng — 250 người | / tháng — 436 người | / tháng — 721 người | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|
| `gemini-3.1-flash-lite` | $0.0018 | $0.0021 | $2.86 | $4.99 | $8.26 | $0.0115 |
| `gemini-4-hydrogen` | $0.0102 | $0.0118 | $16.41 | $28.61 | $47.32 | $0.0656 |

Chi phí mỗi task thành công là chi phí trung bình mỗi phiên chia cho tỷ lệ **26/30**. Tỷ lệ này đo trên từng câu thử. Lịch chi phí lấy từng lượt độc lập từ benchmark, nên chưa đo được tỷ lệ thành công hoặc mức dùng token trên trọn một phiên ôn thật. Để tham chiếu, ca D01 trong [báo cáo eval](../eval/report.md) có **8 lần gọi**, **10.005 token vào** và **774 token ra** với `gpt-4.1-mini`; ca này dùng model khác.

## 3. So với impact

- Impact (`spec.md` §2): khoảng **60 phút mất thêm/người/tháng** *(tự ước tính trong nhóm khảo sát gặp vấn đề)*.
- Chi phí API dự kiến ở kịch bản cơ sở là khoảng **$0.0115–$0.0656/người/tháng** theo hai đơn giá trên.
- **Kết luận:** Ước tính này đủ để bàn về quy mô thử nghiệm. Quyết định triển khai còn phụ thuộc vào kết quả §7 và thời gian học viên thực sự tiết kiệm khi ôn trước lab.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
