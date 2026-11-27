# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Script đếm lưu tại `evidence/count_preclass.py` (chỉ dùng thư viện chuẩn Python), chạy lại trên thư mục `data/preclass/` của BTC sẽ ra đúng các số bên dưới.
> Repo chỉ chứa số đã tổng hợp và ví dụ ẩn danh — không commit nguyên các file CSV gốc của BTC.

## 1. Cách đếm — viết TRƯỚC khi chạy

- **Data dùng:** Bộ `data/preclass/` do BTC cấp (nhật ký hành vi thật đã ẩn danh trên `preclass-online.com`, từ `05/11/2026` đến `25/11/2026`, Day01 → Day13): `learners.csv` (721 dòng), `events.csv` (107.709 dòng), `class_events.csv` (849 dòng), `answers.csv` (3.776 dòng), `chat.csv` (1.260 dòng), `completed_items.csv` (2.472 dòng), `rewards.csv` (228 dòng).
- **Đếm gì · trên tập nào · lọc gì:**
  1. Tỉ lệ học viên có hoạt động: số `hv` duy nhất trong `events.csv` / tổng `hv` trong `learners.csv`.
  2. Tỉ lệ bỏ qua câu hỏi giữa video: `events.csv` lọc `type = quiz_item_dismissed` và `data.skipped_stop = true` / tổng `quiz_item_opened`; và số `hv` từng bỏ qua / số `hv` từng mở quiz.
  3. Tỉ lệ làm sai ở lần thử đầu: `answers.csv` lọc `lan_thu = 1`, `was_correct ∈ {True, False}` theo từng `nguon` (`pre_post_post`, `thuc_hanh`, `video_quiz`).
  4. Mức độ học chủ động (tự giải thích & nêu ý riêng): số `hv` có `nguon = giai_thich` / 436 `hv` hoạt động; tỉ lệ `rubric_y_moi = 0` trong `answers.csv` (`nguon = chat`, `trang_thai_cham = da_cham`); phân bổ hành vi thưởng trong `rewards.csv`.
  5. Mức độ hiệu quả của lớp học AI (bạn học AI xen vào): tỉ lệ `director_decided` có `inserted = true` trong `class_events.csv`; tỉ lệ lượt học viên thực sự nhắn trả lời (`chat.csv` có `channel = video_discussion_reply` hoặc có `intervention_id`) / tổng lượt hiển thị `agent_message_shown` trong `events.csv`; tỉ lệ `hv` từng trả lời / `hv` thấy `agent_message_shown`.
  6. Phân nhóm tần suất hoạt động (`session_started` / `hv` trong 21 ngày) để làm đầu vào cho `cost/personas.yaml`.
- **Mẫu số là gì:** Dùng **436 học viên có hoạt động** (không dùng 721 tài khoản tạo sẵn) khi tính trên toàn tập học viên hoạt động; dùng đúng tập con tương ứng (vd 189 học viên từng mở quiz, 286 học viên từng thấy bạn học AI, 13.975 lượt `agent_message_shown`, 1.968 lượt `pre_post_post` lần 1, 1.223 lượt `chat` đã chấm) cho từng chỉ số.
- **Script / công thức:** `python evidence/count_preclass.py <duong_dan_toi_data_preclass>` (xem [count_preclass.py](count_preclass.py)).

## 2. Đọc trước, đếm sau

Đã đọc từ điển cột (`column_dictionary.csv`, `event_types.csv`, `data/preclass/README.md`) và các dòng đầu của 6 bảng CSV. Các *kiểu* hành vi thấy được trước khi đếm:
- Bộ điều phối lớp học AI (`director_decided`) cho 4 vai bạn học AI (`note_taker`, `deep_thinker`, `inquisitive`, `clown`) xen vào theo từng đoạn bài giảng (`summarize`, `ask_check`, `prompt_reflection`…), hiển thị qua sự kiện `agent_message_shown`.
- Học viên làm bài kiểm tra sau học (`pre_post_post`), thực hành (`thuc_hanh`), hỏi trợ giảng AI (`video_question`), trả lời bạn học AI (`video_discussion_reply`), hoặc tự giải thích (`giai_thich`, `so_hieu_bai`).
- Hệ thống chấm chất lượng tương tác chat theo 3 rubric (`rubric_bam_bai`, `rubric_y_moi`, `rubric_dung_ngu_canh`, thang 0–2) và thưởng hành vi học tốt trong `rewards.csv`.

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---:|---:|---|
| Học viên có hoạt động trên pre-class | 436 / 721 | 60.5% | Mẫu số toàn bài = 436 HV hoạt động |
| Bỏ qua câu hỏi giữa video (`skipped_stop=true` / `quiz_item_opened`) | 21 / 2.153 | **1.0%** | **Bác bỏ giả thuyết 1:** chỉ 17/189 (9.0%) HV từng bỏ qua; tua vượt quiz `crossed_stop=true` = 0/4.322 (0.0%) |
| Bộ điều phối cho bạn học AI xen vào (`director_decided` `inserted=true`) | 385 / 761 | **50.6%** | Can thiệp rất dày: tạo ra 13.975 lượt `agent_message_shown` trên 286 HV (TB 48.9 lượt/HV, trung vị 19, max 455) |
| Lượt học viên phản hồi lại trong khung thảo luận bạn học AI (`video_discussion_reply` / `agent_message_shown`) | 151 / 13.975 | **1.1%** | Gắn đúng `intervention_id`: 144/13.975 (1.0%). **~98.9% lượt bạn học AI xen vào bị phớt lờ** |
| Học viên từng nhắn trả lời bạn học AI / HV thấy `agent_message_shown` | 34 / 286 | **11.9%** | 88.1% học viên thấy bạn học AI xen vào nhưng không bao giờ phản hồi |
| Thưởng `phan_hoi_xay_dung` & `giai_thich` trong `rewards.csv` | 0 / 228 | **0.0%** | `rewards.csv` chỉ có 219 `du_doan` và 9 `sua_sai` (trên tổng 90 HV) |
| Trả lời SAI lần đầu ở câu kiểm tra sau học (`pre_post_post`, `lan_thu=1`) | 399 / 1.968 | **20.3%** | Có tới **69/77 (89.6%)** học viên làm `pre_post_post` từng trả lời sai ít nhất 1 câu ở lần đầu |
| Học viên từng viết tự giải thích (`nguon=giai_thich` / HV hoạt động) | 18 / 436 | **4.1%** | Tổng cộng chỉ có 20 lượt tự giải thích trong suốt 21 ngày |
| Lượt chat với AI **chưa có ý riêng** (`rubric_y_moi=0` / `chat` `da_cham`) | 909 / 1.223 | **74.3%** | Chỉ 226/1.223 (18.5%) đạt `rubric_y_moi=2`; 261/1.223 (21.3%) bị `rubric_bam_bai=0` |
| Sổ hiểu bài được AI nhận xét / số lần mở (`so_hieu_bai_reviewed` / `opened`) | 56 / 228 | **24.6%** | Phần lớn mở xem nhưng không hoàn tất viết để nhận xét |
| Phân nhóm tần suất HV hoạt động (số phiên `session_started` trong 21 ngày) | 184 / 173 / 79 trên 436 | 42.2% / 39.7% / 18.1% | Dùng ít (0–1 phiên) · vừa (2–4 phiên) · nhiều (≥5 phiên); TB 3.20 phiên/HV (dùng cho `cost/personas.yaml`) |

### Kết luận đối chiếu với giả thuyết (`evidence/hypothesis.md`)
- **Giả thuyết 1 (bỏ qua quiz ≥30%) bị bác bỏ:** Học viên hầu như không bỏ qua câu hỏi giữa video (`21/2.153 = 1.0%`).
- **Giả thuyết 2 được chứng minh rất rõ — và làm lộ ra pain lớn hơn của lớp học AI:** Bộ điều phối hiện tại xen vào quá dày đặc (`385/761 = 50.6%` đoạn bài → `13.975` lượt hiển thị), nhưng **98.9% bị học viên phớt lờ** (`151/13.975 = 1.1%` có phản hồi, `0` lượt đạt thưởng `phan_hoi_xay_dung`). Cùng lúc đó, **69/77 (89.6%)** học viên làm kiểm tra sau bài vẫn sai ở lần đầu (`399/1.968 = 20.3%` câu sai), chỉ **4.1%** tự giải thích và **74.3%** tin nhắn chat với AI không có ý riêng (`rubric_y_moi = 0`).
- **Hàm ý cho lát cắt A4 (cập nhật cho CP2):** Không nên can thiệp đại trà theo từng đoạn video hay theo sự kiện "bỏ qua quiz", mà cần **bộ điều phối can thiệp chọn lọc đúng lúc có tín hiệu hiểu sai hoặc trả lời nông** (sai câu kiểm tra hoặc nhắn câu chưa có ý riêng) để kéo học viên vào việc tự giải thích lại và sửa đúng câu kiểm tra tương đương.

## 4. ≥5 ví dụ cụ thể (mã dòng / mã đã ẩn danh, không đoán ai là ai)

1. **Học viên `L0213` — sai câu kiểm tra sau bài & nhắn AI không có ý riêng:** ngày `05/11/2026`, `L0213` nhắn `C00983` (`A02628`, `program-day01:ai-llm-foundation`) chỉ dài 29 ký tự, bị chấm `rubric_bam_bai=0`, `rubric_y_moi=0`; 15 phút sau làm `pre_post_post` câu `chatbot_is_app_around_model` (`A00611`) trả lời sai ở lần 1.
2. **Học viên `L0057` — tương tác ngắn & sai câu kiểm tra:** ngày `06/11/2026`, `L0057` trả lời `classmate_deep_thinker` (`C00352`, gắn `intervention_id` của `day02:module-7:chunk-8`) chỉ 18 ký tự, và làm sai lần 1 câu `chatbot_is_app_around_model` (`A02467`, `pre_post_post`), đồng thời có lượt chat `C01056` (`A03361`) bị chấm `rubric_y_moi=0`.
3. **Học viên `L0510` — sai câu kiểm tra sau học về chọn tầng model:** ngày `06/11/2026`, `A00288` (`pre_post_post`, `program-day01:ai-llm-foundation`, KC `model_tier_selection`) trả lời sai ngay ở lần 1.
4. **Học viên `L0247` — sai `video_quiz` lần 1 nhưng không làm lại:** ngày `25/11/2026` (`program-day13:launch-economics`), trả lời sai ở cả 2 câu `A01200` (`bounded_retry_cost`) và `A01809` (`adoption_vs_outcome_metrics`) ở `lan_thu=1` và không có lần làm lại (`lan_thu ≥ 2`).
5. **Học viên `L0384` — phản hồi ngắn cho bạn học AI xen vào:** ngày `05/11/2026`, trong 19 giây liên tiếp phản hồi `classmate_deep_thinker` ở `day01:module-2:chunk-15` với độ dài rất ngắn (`C00869`: 43 ký tự; `C00128`: 24 ký tự), và có lượt chat `C00979` (`A01435`) bị chấm `rubric_y_moi=0`.
6. **Học viên `L0503` — bỏ qua câu hỏi giữa video ở 2 ngày học khác nhau:** `skipped_stop=true` tại `day01-ai-llm-foundation:m01:s007` (`05/11/2026`) và `day02-ai-problem-definition:m01:s006` (`09/11/2026`).

## 5. Giới hạn của data

- **Không có nội dung câu chữ học viên viết** (chỉ có độ dài ký tự và điểm rubric do giám khảo AI chấm), nên data cho biết học viên *phớt lờ 98.9% lời xen vào* và *sai 20.3% câu kiểm tra*, nhưng **không cho biết vì sao** (do bạn học AI nói nhiều gây phiền, do nội dung không đúng chỗ đang bí, hay do học viên muốn xem nhanh).
- **Lệch thời điểm ghi log:** `nguon = video_quiz` trong `answers.csv` chỉ có 7 dòng ghi từ `25/11/2026` (không đủ mẫu để kết luận riêng cho `video_quiz`, nên dùng `pre_post_post` với 1.968 lượt lần 1 làm chỉ số sai lần đầu); `learning_mode` (`maic`/`tutor`) cũng chỉ ghi từ `25/11/2026` nên không so sánh hai chế độ trên bộ này.
- **Tự chọn lọc:** Chỉ 77/436 học viên làm `pre_post_post` và 286/436 thấy `agent_message_shown` — không tự suy rộng tỉ lệ của nhóm con ra toàn bộ 721 tài khoản.
- **→ Kiểm lại bằng khảo sát nào:** Khảo sát Google Form của nhóm (do Mạnh & Bách triển khai cho ≥20 học viên lớp L3 ngoài nhóm) + phỏng vấn ngắn để giải thích **vì sao** học viên phớt lờ bạn học AI xen vào và thường làm gì sau khi trả lời sai câu hỏi trên pre-class.
