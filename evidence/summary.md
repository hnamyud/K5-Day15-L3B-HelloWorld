# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2 (bản tổng hợp đã đạt ngưỡng ở CP2, hoàn thiện bổ sung trước CP3 10:00 Thứ Bảy 28/11). Chấm ở rubric R1.
> Nhóm đã đạt ngưỡng ở **2 nguồn độc lập kiểm chéo nhau**: đào dữ liệu thật `data/preclass/` và khảo sát hành vi thật `evidence/KhaoSat.csv`.

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ Đạt | `evidence/data-mining.md` · `evidence/count_preclass.py` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ *(tuỳ chọn bổ sung trước CP3)* | `evidence/interviews/` |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☑ Đạt (`25` phiếu tổng · `22` phiếu L3) | `evidence/survey/report.md` · `evidence/KhaoSat.csv` |

## 2. Số chính

- **Khảo sát (`evidence/KhaoSat.csv`, `n = 25` phiếu ngoài nhóm, lọc đúng người dùng chính lớp L3: `n = 22` — gồm `12` L3B, `10` L3A; `3` phiếu `Khác` giữ log nhưng tách khỏi mẫu số L3):**
  - Cách tự kiểm tra trước lab (chọn nhiều đáp án): xem lại học liệu `13/22 (59.1%)` · làm câu hỏi/bài thử `8/22 (36.4%)` · tự giải thích `7/22 (31.8%)` · dùng công cụ AI `6/22 (27.3%)` · hỏi bạn/trợ giảng `5/22 (22.7%)`.
  - **Ảo tưởng hiểu bài trước lab:** `14/22 (63.6%)` chọn *"Nghĩ mình hiểu đủ để áp dụng"* trước lần phát hiện hiểu sai gần nhất trong lab (`5/22 = 22.7%` còn phân vân, `3/22 = 13.6%` biết mình chưa hiểu).
  - Tần suất trong 30 ngày qua: `12/22 (54.5%)` gặp *"Dưới 5 lab"*, `5/22 (22.7%)` gặp *"Trên 5 lab"*, `5/22 (22.7%)` *"Không nhớ"* (`17/22 = 77.3%` nhớ rõ số lượng lab bị phát hiện hiểu sai).
  - Xử lý sau khi phát hiện sai trong lab: xem lại học liệu `7/22`, sửa bài lab `6/22`, hỏi người khác `5/22`, hỏi công cụ AI `3/22`, dừng bài lab `1/22`.
  - **Thời gian tốn thêm mỗi lần:** trung vị **`20 phút/lần`** trên `21/22` phiếu L3 có ghi số phút (`5–60 phút`); riêng nhóm `14` phiếu *"Nghĩ mình hiểu đủ"* có `13` phiếu ghi số phút (`15–60 phút`), trung vị vẫn **`20 phút/lần`**.
- **Đào data thật (`data/preclass/`, `evidence/data-mining.md`, `436/721 = 60.5%` HV hoạt động, `107.709` events):**
  - Bỏ qua quiz giữa video: chỉ `21/2.153 (1.0%)` (tua vượt `0/4.322 = 0.0%`) → **bác bỏ giả thuyết 1**.
  - **Bạn học AI xen giữa video bị phớt lờ:** `director_decided` xen vào `385/761 (50.6%)` đoạn bài (`13.975` lượt `agent_message_shown`, TB `48.9` lượt/HV), nhưng chỉ `151/13.975 (1.1%)` có phản hồi trong khung thảo luận (`34/286 = 11.9%` HV), và `0/228 (0.0%)` đạt thưởng `phan_hoi_xay_dung`.
  - **Vẫn hiểu sai & ít tự giải thích:** `399/1.968 (20.3%)` lượt trả lời `pre_post_post` lần 1 bị sai (`69/77 = 89.6%` HV làm bài kiểm tra sau học từng sai ít nhất 1 câu); chỉ `18/436 (4.1%)` từng viết tự giải thích (`giai_thich`), và `909/1.223 (74.3%)` lượt chat với AI bị chấm `rubric_y_moi = 0` *(chưa nêu ý riêng)*.

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

1. *"đọc slide thấy quen nên chủ quan, lúc code CrossEntropyLoss lỡ cho qua softmax trước nên kết quả lệch hẳn"* — Phiếu khảo sát #21 (`L3B`, `evidence/KhaoSat.csv` dòng 21, mất `15 phút`).
2. *"tưởng fit_transform dùng luôn cho tập test, chạy xong thấy điểm cao bất thường mới biết bị rò dữ liệu"* — Phiếu khảo sát #12 (`L3B`, `evidence/KhaoSat.csv` dòng 12, mất `20 phút`).
3. *"đinh ninh hiểu cách split train/test rồi, làm lab tới bước tiền xử lý bị leak từ tập test sang mới sửa"* — Phiếu khảo sát #10 (`L3B`, `evidence/KhaoSat.csv` dòng 10, mất `20 phút`).
4. *"Mình nghĩ hàm CrossEntropyLoss nhận đầu vào đã qua softmax rồi, lúc chạy lab thấy loss hội tụ rất chậm và kết quả sai lệch so với test mẫu mới phát hiện mình áp softmax hai lần."* — Phiếu khảo sát #3 (`L3B`, `evidence/KhaoSat.csv` dòng 3, mất `60 phút`).
5. *"Mình tưởng shuffle dữ liệu lúc nào cũng tốt, làm bài time series shuffle bừa ra kết quả ảo quá mới nhận ra sai."* — Phiếu khảo sát #18 (`L3A`, `evidence/KhaoSat.csv` dòng 18, mất `20 phút`).
6. *"em cứ nghĩ train loss giảm là xong rồi, nộp thử test ẩn điểm thấp mới quay lại xem lại phần đánh giá"* — Phiếu khảo sát #19 (`L3A`, `evidence/KhaoSat.csv` dòng 19, mất `30 phút`).
7. **Ví dụ dữ liệu hành vi ẩn danh (`data/preclass/`):** Học viên `L0213` nhắn AI `C00983` (`A02628`, 29 ký tự) bị chấm `rubric_bam_bai=0`, `rubric_y_moi=0`; 15 phút sau làm `pre_post_post` câu `chatbot_is_app_around_model` (`A00611`) trả lời sai ngay ở lần 1 (`evidence/data-mining.md`).

## 4. Các nguồn có khớp nhau không

- **Data nói:** Học viên không bỏ qua câu hỏi giữa video (`1.0%`), nhưng phớt lờ tới `98.9%` lời bạn học AI xen ngang giữa video; phần lớn ít tự giải thích (`4.1%`), chat thiếu ý riêng (`74.3%` có `rubric_y_moi = 0`), và vẫn sai `20.3%` câu kiểm tra sau bài (`89.6%` HV làm bài kiểm tra sau học từng sai).
- **Người dùng nói (khảo sát):** Học viên chủ yếu xem lại slide (`59.1%`), cảm thấy quen mắt nên nghĩ mình đã hiểu đủ (`63.6%`), chỉ khi vào lab chạy sai/lệch kết quả mới nhận ra lỗ hổng bản chất và mất trung vị `20 phút/lần` để đọc lại và sửa bài.
- **Khớp và bổ sung nhau:** Log pre-class cho thấy *cơ chế xen vào giữa video thất bại* và *tỉ lệ tự giải thích rất thấp*, còn khảo sát giải thích *vì sao* (ảo tưởng hiểu bài khi chỉ đọc slide thụ động trước giờ lab).

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **đúng một phần và đã điều chỉnh lát cắt cho CP2** — giả thuyết 1 (*bỏ qua quiz giữa video ≥30%*) **sai** (`1.0%`), nhưng giả thuyết 2 (*tương tác bạn học AI xen vào bị phớt lờ <5% và học viên ít tự giải thích dẫn tới hiểu sai*) **đúng mạnh** (`1.1%` phản hồi, `4.1%` tự giải thích, `14/22` ảo tưởng hiểu bài trước lab).
- **Điều vẫn chưa biết:** Khi triển khai phiên tự giải thích chủ động sau pre-class và trước lab, học viên L3 thực tế có sẵn sàng dành 3–5 phút dùng trước buổi lab không và tỉ lệ tự sửa được hiểu sai sau ≤2 vòng gợi mở đạt bao nhiêu % → sẽ kiểm chứng trực tiếp qua người dùng thử (`validation/log.md`) trước CP4.
