# Reflection — Nguyễn Hoàng Trung

> Làm ở guide bước 5.3. Mỗi câu ngắn gọn, trỏ thẳng tới file và commit thật của nhóm.

## 1. Vai trò + phần mình làm

Tôi làm **Đội trưởng** (mã `2A202603826`), điều phối chung, giữ quyền gộp `spec.md` từ sau CP2 để tránh xung đột Git và nộp các checkpoint CP1–CP4.
Ở chặng CP1–CP2, tôi viết giả thuyết (`evidence/hypothesis.md`), viết và chạy script đào dữ liệu thật `data/preclass/` (`evidence/count_preclass.py`, `evidence/data-mining.md` — commit `54c55ac`), hoàn thiện `spec.md` §0–§2, §5–§6, §10, bổ sung metric về học A4 trong `eval/metric_spec.yaml`, dựng học liệu mẫu `data/sample_lessons.json` + `data/DATA_CARD.md` và khung ban đầu cho `codebase/tools.py`, `codebase/agent.py` (commits `d95ca86`, `8036782`, `82f514c`, `f32cc8a`, `f919dd1`).
Từ CP3–CP4 sau khi đổi vai với Mạnh, tôi lập hồ sơ khảo sát `evidence/survey/report.md`, chụp và che tên trên 2 ảnh `preclass-online.com` (`assets/preclass-video-ai.png`, `assets/preclass-ontap.png`), chấm chéo độc lập 5 mẫu lượt 1 (`eval/cross-check-trung.md`, khớp 4/5 với Bách), đồng bộ số liệu thật vào `spec.md` §7–§8 và thiết kế xuất `demo-slides.pdf` 8 trang tại thư mục gốc (commits `42e2d44`, `424ba09`, `3cb4eb1`, `1372132`).

## 2. AI hỗ trợ mình thế nào

Tôi dùng coding agent (Antigravity / LLM) hỗ trợ viết script thuần Python đếm log `data/preclass/`, dựng khung `codebase/tools.py`, `agent.py`, `ai.py`, biên soạn cô đọng 6 khái niệm mẫu trong `data/sample_lessons.json`, và tạo bản trình bày HTML để xuất `demo-slides.pdf`.
Có ba chỗ tôi phải trực tiếp kiểm và sửa lại đầu ra của AI thay vì tin nguyên bản:
- Khi kiểm định tuyến trên toàn bộ 30 câu thử trước khi nối API, khung lọc ban đầu do AI viết đã **chặn nhầm câu `B01`** vì bắt từ khoá trần `"system prompt"` và **khớp nhầm các câu ngoài học liệu (`B09`, `B13`, `B25`–`B30`)** vì từ khoá chung chung như `"mô hình"`, `"LLM"`, `"dữ liệu"` — phải sửa lại bộ khớp đặc trưng và kiểm chạy đạt 30/30 câu mới giao Mạnh nối API.
- Khi làm báo cáo bằng chứng, tôi tự đối chiếu lại mẫu số (`436` HV hoạt động trên `721` tài khoản, `22` phiếu L3 trên `25` phiếu khảo sát) và bỏ giả thuyết cũ về *"bỏ qua quiz giữa video"* ngay khi số thật chỉ ra `1.0%`.
- Khi rà `demo-slides.pdf`, phải bỏ các con số ước quy đổi tiền Việt ngoài bảng `cost/cost-estimate.md` để mọi con số trên 8 trang đều truy vết trực tiếp về file trong repo.

## 3. Một câu thử trượt của nhóm và mình học được gì từ nó

Câu thử để lại bài học rõ nhất cho tôi là **`B06` (`eval/run-1.csv`, `run-1@20261127-230315`)** — học viên hiểu sai rằng *"LLM tự chạy thẳng hàm truy vấn cơ sở dữ liệu"*.
Ở Lượt 1, hệ thống nhận đúng nhãn `[HIỂU SAI]` và trích đúng mã đoạn `[D03-P03]`, nhưng lại viết: *"ứng dụng mới thực thi rồi đưa kết quả lại cho mô hình [D03-P03]. Ai là bên thực sự chạy hàm trong quy trình này?"* — tức là **nói toẹt luôn đáp án ngay trước khi đặt câu hỏi gợi mở**, làm mất mục tiêu tự suy luận của học viên trong Track A4.
Tôi học được hai điều: (1) một phản hồi đúng nhãn và đúng mã nguồn vẫn có thể **thất bại về mục tiêu người dùng** nếu không có `pass_criterion` đủ chặt để bắt lỗi sư phạm; và (2) sửa prompt tự do ở Lượt 2 giúp `B06` đạt nhưng lại làm `B05`, `B11` hồi quy, chỉ khi chuyển sang **phản hồi JSON có cấu trúc kèm bước hậu kiểm bằng code ở Lượt 3** thì chất lượng mới bật lên `28/30 (93%)` — chứng tỏ luôn phải chạy lại trọn bộ câu thử sau mỗi lần sửa.
