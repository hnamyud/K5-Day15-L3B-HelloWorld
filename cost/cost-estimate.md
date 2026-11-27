# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): dùng ít **42,2% · 2 phiên/tháng · 3 lượt/phiên**, dùng vừa **39,7% · 5 · 6**, dùng nhiều **18,1% · 10 · 10**. Tỷ trọng lấy từ `evidence/data-mining.md`. Tần suất và số lượt là tự ước tính cho bài mẫu ba ý.
- **Quy mô người dùng/tháng:** thấp **250** *(tự ước tính)*, cơ sở **436** và cao **721** *(kịch bản lấy mốc từ dữ liệu pre-class, xem `spec.md` §8)*.
- **Giá Standard trả phí (USD / 1 triệu token vào / ra):** `gemini-3.1-flash-lite` **0,25 / 1,50**, `gemini-4-hydrogen` **1,50 / 7,50**. [Bảng giá Gemini API, xem 27/11/2026](https://aistudio.google.com/docs/pricing).
- **Tỉ lệ đạt và model đo token:** Chờ lượt 2 đã chấm và mô phỏng chạy bằng model thật. Nếu áp giá của model khác lên token đã đo, ghi rõ hai model trong báo cáo.

## 2. Kết quả mô phỏng

Kế hoạch: **50 phiên, seed 42**. Chưa có lượt mô phỏng bằng model thật.

Khung lấy từng lượt độc lập từ benchmark. Khi luồng ôn nhiều ý đã chạy, đo thêm một phiên xuyên suốt để đối chiếu số lượt và token thực tế.

*(dán bảng từ `cost/simulate-N-summary.md`)*

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp | / tháng — cơ sở | / tháng — cao | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**.

## 3. So với impact

- Impact (`spec.md` §2): khoảng **60 phút mất thêm/người/tháng** *(tự ước tính trong nhóm khảo sát gặp vấn đề)*.
- Chi phí / người / tháng ở kịch bản cơ sở: chờ mô phỏng bằng model thật.
- **Kết luận:** Đáng thử. Quyết định triển khai dựa trên kết quả §7, chi phí đo được và thời gian học viên thực sự tiết kiệm khi ôn trước lab.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
