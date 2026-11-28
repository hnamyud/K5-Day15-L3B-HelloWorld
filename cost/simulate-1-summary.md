# Tóm tắt mô phỏng simulate-1@20261128-134208

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 25 | 3 | 3955 | 212 | 2.1 | 5.1 |
| dung_vua | 17 | 6 | 8226 | 435 | 4.5 | 10.4 |
| dung_nhieu | 7 | 10 | 13601 | 653 | 7.3 | 17.0 |

Tỉ lệ đạt dùng để tính: 28/30 (93%) — lượt run-3@20261128-122313

- Tự chọn: lượt run-N mới nhất đã chấm xong, chạy bằng đúng model đang đo (run-3.csv). Muốn dùng lượt khác (vd lượt 2): thêm `--rate-from eval/run-2.csv`.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (250 người) | Chi phí / tháng — cơ sở (436 người) | Chi phí / tháng — cao (721 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.0022 | $0.0024 | $0.00047 | $3.60 | $6.28 | $10.39 | $0.0144 |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0129 | $0.0138 | $0.0027 | $20.78 | $36.24 | $59.92 | $0.0831 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (5.0) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: cx/gpt-6-luna. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 1/50.
