# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Khi có lượt đo mới, chạy `python run.py simulate --rate-from eval/run-2.csv` rồi lấy bảng trong `cost/simulate-N-summary.md`.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): dùng ít **42,2% · 2 phiên/tháng · 3 lượt/phiên**, dùng vừa **39,7% · 5 · 6**, dùng nhiều **18,1% · 10 · 10**. Tỷ trọng lấy từ `evidence/data-mining.md`. Tần suất và số lượt là tự ước tính cho bài mẫu ba ý.
- **Quy mô người dùng/tháng:** thấp **250** *(tự ước tính)*, cơ sở **436** và cao **721** *(kịch bản lấy mốc từ dữ liệu pre-class, xem `spec.md` §8)*.
- **Đơn giá dùng cho hai kịch bản (USD / 1 triệu token vào / ra):** `gemini-3.1-flash-lite` **0,25 / 1,50**, `gemini-4-hydrogen` **1,50 / 7,50**. Tính theo đơn giá đã ghi trong `cost/personas.yaml` để so sánh hai phiên bản trên cùng giả định. [Nguồn được ghi trong cấu hình, ngày 27/11/2026](https://aistudio.google.com/docs/pricing).
- **Tỷ lệ đạt và nguồn token:** Lượt 2 đạt **26/30 (86,7%)**, Run ID `run-2@20261128-001731`. Lượt 3 đạt **28/30 (93,3%)**, Run ID `run-3@20261128-122313`. Cả hai lượt dùng `cx/gpt-6-luna`. Bảng chi phí dùng token của model này với đơn giá Gemini. Kết quả triển khai thực tế bằng Gemini có thể khác về lượng token và tỷ lệ đạt. [Lượt 2](../eval/run-2.csv) · [Lượt 3](../eval/run-3.csv)

## 2. Kết quả mô phỏng

### Ước tính cho bản mới từ token của Lượt 3

Tạo lịch **50 phiên, seed 42** bằng `plan_sessions` trong `cost/simulate.py`. Với mỗi đầu vào được chọn, lấy token và số lần gọi đã ghi trong `eval/run-3.csv` rồi cộng theo phiên. Lịch gồm **253 lượt gửi**, tương ứng **192 lần gọi model**, **357.308 token vào** và **19.524 token ra**. Khi cùng một câu xuất hiện nhiều lần, mỗi lần dùng lại số token đã ghi của câu đó. Đây là ước tính từ dữ liệu eval đã có. Chưa có lượt gọi API mới cho toàn bộ 50 phiên.

| Nhóm | Số phiên trong lịch | Lượt gửi / phiên | Token vào / phiên | Token ra / phiên |
|---|---:|---:|---:|---:|
| Dùng ít | 25 | 3 | 4.268 | 228 |
| Dùng vừa | 18 | 6 | 8.632 | 495 |
| Dùng nhiều | 7 | 10 | 13.602 | 702 |

| Đơn giá áp dụng | Chi phí / phiên | Chi phí / task thành công | / tháng — 250 người | / tháng — 436 người | / tháng — 721 người | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|
| `gemini-3.1-flash-lite` | $0.0024 | $0.0025 | $3.75 | $6.54 | $10.82 | $0.0150 |
| `gemini-4-hydrogen` | $0.0136 | $0.0146 | $21.60 | $37.66 | $62.28 | $0.0864 |

Chi phí mỗi task thành công là chi phí trung bình mỗi phiên chia cho tỷ lệ **28/30**. Tỷ lệ đạt được đo trên từng câu thử. Lịch này lấy từng lượt độc lập từ benchmark, nên chưa đo được tỷ lệ thành công hoặc mức dùng token trên trọn một phiên ôn. Phiên D01 trong báo cáo eval có **8 lần gọi**, **10.005 token vào** và **774 token ra** với `gpt-4.1-mini`. [Báo cáo eval](../eval/report.md)

### Mốc Lượt 2 theo yêu cầu §8

Dùng cùng lịch 50 phiên và cùng đơn giá để đối chiếu. Lượt 2 có **180 lần gọi model**, **261.519 token vào**, **15.934 token ra** và tỷ lệ đạt **26/30**.

| Đơn giá áp dụng | Chi phí / phiên | Chi phí / task thành công | / tháng — 250 người | / tháng — 436 người | / tháng — 721 người | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|
| `gemini-3.1-flash-lite` | $0.0018 | $0.0021 | $2.86 | $4.99 | $8.26 | $0.0115 |
| `gemini-4-hydrogen` | $0.0102 | $0.0118 | $16.41 | $28.61 | $47.32 | $0.0656 |

Lượt 3 tăng **2 câu đạt**, đồng thời chi phí ước tính mỗi tháng ở quy mô 436 người tăng khoảng **31–32%**. Mức tăng chi phí mỗi task thành công vẫn dương theo cả hai đơn giá.

## 3. So với impact

- Impact (`spec.md` §2): khoảng **60 phút mất thêm/người/tháng** *(tự ước tính trong nhóm khảo sát gặp vấn đề)*.
- Chi phí API ước tính theo Lượt 3 ở kịch bản cơ sở là **$0.0150–$0.0864/người/tháng** theo hai đơn giá trên.
- **Kết luận:** Bản mới đạt thêm câu thử và tốn thêm token. Để biết chi phí tăng có đáng hay không, cần đo xem học viên tự giải thích lại đúng và tiết kiệm được bao nhiêu thời gian trước lab.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
