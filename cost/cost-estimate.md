# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Khi có lượt đo mới, chạy `python run.py simulate` (mặc định lấy tỷ lệ đạt từ lượt eval mới nhất, hoặc chỉ định bằng `--rate-from eval/run-N.csv`) rồi lấy bảng trong `cost/simulate-N-summary.md`. Bản tóm tắt chỉ tính hai giá Gemini trong `personas.yaml`, còn dòng `gpt-6-luna` ở §2 phải tính tay.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): dùng ít **42,2% · 2 phiên/tháng · 3 lượt/phiên**, dùng vừa **39,7% · 5 · 6**, dùng nhiều **18,1% · 10 · 10**. Tỷ trọng lấy từ `evidence/data-mining.md`. Tần suất và số lượt là tự ước tính cho bài mẫu ba ý.
- **Quy mô người dùng/tháng:** thấp **250** *(tự ước tính)*, cơ sở **436** và cao **721** *(kịch bản lấy mốc từ dữ liệu pre-class, xem `spec.md` §8)*.
- **Đơn giá (USD / 1 triệu token vào / ra):**
  - `gpt-6-luna` **0,10 / 0,50**. Đây là model nhóm đang dùng: bản chạy thử gọi `cx/gpt-6-luna` qua proxy OpenAI-compatible. Giá lấy từ bảng Standard, cột ngữ cảnh ngắn (mỗi phiên dưới 14.000 token vào). [Bảng giá OpenAI API, xem 28/11/2026](https://developers.openai.com/api/docs/pricing). Giá này là giá gọi thẳng API của OpenAI, chưa tính phí của proxy nếu có.
  - `gemini-3.1-flash-lite` **0,25 / 1,50** và `gemini-4-hydrogen` **1,50 / 7,50**, theo `cost/personas.yaml`. [Bảng giá Gemini API, xem 27/11/2026](https://aistudio.google.com/docs/pricing).
- **Tỷ lệ đạt và nguồn token:** Lượt 2 đạt **26/30 (86,7%)**, Run ID `run-2@20261128-001731`. Lượt 3 đạt **28/30 (93,3%)**, Run ID `run-3@20261128-122313`. Cột `pass` của Lượt 3 hiện là điểm chấm sơ bộ. Cả hai lượt dùng `cx/gpt-6-luna`. Với `gpt-6-luna`, token đo và đơn giá cùng một model. Với hai model Gemini, token đo trên `cx/gpt-6-luna` rồi tính theo giá Gemini, nên khi triển khai thật bằng Gemini, lượng token và tỷ lệ đạt có thể khác. [Lượt 2](../eval/run-2.csv) · [Lượt 3](../eval/run-3.csv)

## 2. Kết quả mô phỏng

### Đo thật: `simulate-1` gọi API cho cả 50 phiên

Chạy `python run.py simulate` với code Lượt 3 và model `cx/gpt-6-luna`: Run ID `simulate-1@20261128-134208`, **50 phiên, seed 42**, mỗi lượt gửi gọi API thật. Kết quả ghi ở [`simulate-1.csv`](simulate-1.csv), [`simulate-1-summary.md`](simulate-1-summary.md) và [`traces/simulate-1.jsonl`](../traces/simulate-1.jsonl).

- **Lỗi:** 1/50 phiên lỗi (`S001`, nhóm dùng vừa, 2 lượt `TimeoutError`). Phiên này không được tính vào trung bình, nên nhóm dùng vừa còn 17 phiên.
- **49 phiên hợp lệ:** **247 lượt gửi**, **180 lần gọi model**, **333.943 token vào** và **17.261 token ra**.

| Nhóm | Số phiên tính | Lượt gửi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên |
|---|---:|---:|---:|---:|---:|
| Dùng ít | 25 | 3 | 3.955 | 212 | 2,1 |
| Dùng vừa | 17 | 6 | 8.226 | 435 | 4,5 |
| Dùng nhiều | 7 | 10 | 13.601 | 653 | 7,3 |

| Đơn giá áp dụng | Chi phí / phiên | Chi phí / task thành công | / tháng — 250 người | / tháng — 436 người | / tháng — 721 người | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|
| **`gpt-6-luna` (model đang dùng)** | **$0.00086** | **$0.00092** | **$1.39** | **$2.42** | **$3.99** | **$0.0055** |
| `gemini-3.1-flash-lite` | $0.0022 | $0.0024 | $3.60 | $6.28 | $10.39 | $0.0144 |
| `gemini-4-hydrogen` | $0.0129 | $0.0138 | $20.78 | $36.24 | $59.92 | $0.0831 |

- **Nguồn từng dòng:** hai dòng Gemini chép từ `simulate-1-summary.md`. Dòng `gpt-6-luna` tính theo đúng công thức của `cost/simulate.py` (chi phí mỗi phiên, trung bình theo từng nhóm, nhân số người × tỷ trọng × số phiên/tháng) trên cùng 49 phiên. Áp công thức này cho hai model Gemini ra đúng số trong bản tóm tắt.
- **Chi phí mỗi task thành công** = chi phí / phiên ÷ **28/30**.
- **So với ước tính bên dưới:** số đo thật thấp hơn ước tính từ token của Lượt 3 khoảng 4%.

### Ước tính cho bản mới từ token của Lượt 3 (trước khi có `simulate-1`)

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
- **Chi phí API đo thật** (`simulate-1`, kịch bản cơ sở 436 người):
  - với model đang dùng `gpt-6-luna`: khoảng **$0.0055/người/tháng**, tức **$2.42/tháng**;
  - nếu chuyển sang Gemini: **$0.0144–$0.0831/người/tháng**.
- **Kết luận:**
  - Bản mới đạt thêm câu thử và tốn thêm token, nhưng chi phí API vẫn rất nhỏ so với khoảng 60 phút học viên có thể mất mỗi tháng.
  - Giữ `gpt-6-luna` là phương án rẻ nhất trong ba mức giá.
  - Để biết có đáng triển khai hay không, vẫn cần đo xem học viên tự giải thích lại đúng và tiết kiệm được bao nhiêu thời gian trước lab.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
