# Người dùng thử *(bonus)*

> Điền ở guide bước 4.3 — 2–3 người ngoài nhóm, ~10 phút / người, theo 5 nhịp: làm quen · bối cảnh · giao việc · quan sát · hỏi sau. Ôn lại: ngày 5, ngày 13. Chấm ở rubric Bonus.
> Không ghi tên: ghi vai. Hành vi quan sát được nặng hơn lời nói; toàn lời khen = phiên chưa đạt, giao việc khó hơn.
> Người dùng thử **không thay được** bằng chứng pain ở `evidence/`.

## Kịch bản dùng thử

- Mời 2–3 học viên L3 ngoài nhóm, khoảng 10 phút/người. Nói rõ người tham gia đang thử công cụ và có thể dừng bất cứ lúc nào. Hỏi trước lab bạn thường kiểm tra mình đã hiểu bài bằng cách nào.
- Giao việc: “Bạn vừa học xong bài pre-class về chatbot và temperature. Hãy dùng bản chạy thử để chọn ý mình cần ôn thêm trước khi vào lab.” Mở `python run.py` và để người thử tự chọn bài D01, thao tác và diễn đạt. Quan sát họ làm gì trước, chỗ do dự và lúc chọn xem lại hoặc để ôn sau.
- Hỏi sau: “Ý nào bạn vừa làm rõ? Bạn sẽ áp dụng nó thế nào trong lab?”. Cho người thử tự nói bằng lời của mình sau khi đóng gợi ý, rồi đối chiếu với học liệu. Hỏi thêm câu về mức tiếc nuối bên dưới.

| Người thử (vai) | Việc giao (theo kết quả, không theo nút) | Quan sát (làm gì đầu tiên, chỗ do dự, chỗ hiểu sai) | Trích nguyên văn | Mức nghiêm trọng (cao / vừa / thấp) |
|---|---|---|---|---|
| S1 · Học viên L3 ngoài nhóm (ôn dồn trước lab) | Chọn ý cần ôn thêm ở D01 | Gõ giải thích ngay, không đọc dòng lệnh `/xem` `/sau` `/thoat`. Nhầm "LLM tự nhớ lịch sử chat". Sau hai gợi mở và `/xem`, gõ lại ngắn/sát từ khóa học liệu nhưng vẫn thiếu ý. Sau thông báo "vẫn còn điểm cần ôn" thì hỏi lại điểm nào thiếu. | "Mình thiếu điểm nào?" | Vừa |
| S2 · Học viên L3 ngoài nhóm (tự tin, diễn đạt trôi chảy) | Kiểm tra ý Temperature trước lab | Giải thích trôi chảy nhưng hiểu sai bản chất ("temperature là độ chính xác"). Bấm `/xem` sớm, đọc xong tự diễn đạt lại được bằng lời mình. | "Ra là nó chỉ chỉnh độ ngẫu nhiên khi lấy mẫu." | Thấp |
| S3 · Học viên L3 ngoài nhóm (ít thời gian) | Xem nhanh rồi quyết định ôn gì | Dùng `/xem`, đặt mục đầu `/sau`, thoát ở mục tiếp theo bằng `/thoat`. Gặp thông báo `[CHƯA ĐỦ CĂN CỨ]` không nói bước tiếp theo thì gõ lại câu cũ, rồi dừng. | "Giờ mình làm gì tiếp?" | Vừa |

Câu hỏi sau: *"Nếu mai không được dùng nữa, bạn thấy: rất tiếc / hơi tiếc / không sao?"* → **1 / 2 / 0** (1 rất tiếc · 2 hơi tiếc · 0 không sao)

## Chỉ số tự giải thích lại (A4)

Ghi mỗi ý có điểm thiếu hoặc sai và đã nhận câu gợi mở hoặc phần **Xem lại kiến thức**. Đối chiếu lời diễn đạt mới với điểm còn thiếu/sai và mã đoạn tương ứng. Ghi rõ số lượt gợi mở, có xem lại hay không và trường hợp người thử bỏ qua hoặc dừng sớm.

| Người thử (mã ẩn danh) | Ý và mã đoạn | Điểm thiếu/sai ban đầu | Số lượt gợi mở / đã xem lại? | Lời diễn đạt mới | Tự giải thích đúng? |
|---|---|---|---|---|---|
| S1 | Chatbot và LLM — `D01-P01`, `D01-P02` | Nhầm LLM tự nhớ lịch sử; thiếu vai trò công cụ | 2 gợi mở / có xem lại | "Thêm prompt và công cụ" | Chưa (còn thiếu, ghi **Nên ôn lại**) |
| S2 | Temperature — `D01-P03`, `D01-P04` | Nhầm temperature là độ chính xác | 0 gợi mở (xem ngay) / có xem lại | "Temperature chỉ chỉnh cách lấy mẫu xác suất, không làm kiến thức đúng hơn" | Đúng |
| S3 | Bài D01 (ý 1 đặt `/sau`, ý 2 `/thoat`) | Không tự giải thích trước; dừng sớm sau thông báo `[CHƯA ĐỦ CĂN CỨ]` | 0 gợi mở / có xem lại ở ý 1, sau đó `/sau` và `/thoat` | *(dừng sớm, không có lượt tự diễn đạt lại)* | Không tính (dừng sớm) |

- Kết quả trên 3 phiên ghi nhận (`S1–S3`): **1/2** lượt hoàn thành bước tự diễn đạt lại đạt yêu cầu (`S2` đúng, `S1` còn thiếu nên gắn **Nên ôn lại**), và **1/3** phiên dừng sớm (`S3`). Do cỡ mẫu nhỏ (`n = 3`, không ghi `%` theo quy ước `02-guide.md`), kết quả này dùng để rút lỗi UX và chưa đủ đại diện để kết luận ngưỡng `≥75%` của §7 trên toàn lớp.

## Kiểm thử luồng & diễn tập trước buổi dùng thử thật

### 1. Kiểm thử theo vai học viên trên bản dòng lệnh

Ba kịch bản dưới đây chạy qua giao diện `codebase/app.py` và workflow tại commit `6ea10b4`. Câu nhập của học viên được soạn cho kịch bản. Các phản hồi model được cấp sẵn để kiểm tra cách ứng dụng xử lý từng nhánh. Kết quả ghi từ màn hình Terminal.

| Kịch bản | Thao tác | Quan sát khi chạy |
|---|---|---|
| A. Ôn hết hai mục D01 | Giải thích rằng LLM tự giữ lịch sử, sửa lời giải thích sau gợi mở. Sang Temperature, tiếp tục nhầm giữa lấy mẫu và độ chính xác qua hai lượt, rồi tự diễn đạt lại sau khi xem học liệu. | Hai mục được xử lý lần lượt. Temperature hiện đúng hai câu gợi mở trước phần xem lại. Cuối phiên có lời mời tự nhắc lại, rồi tổng hợp cả hai mục **Đã giải thích được** theo phản hồi mẫu. |
| B. Cần xem nhanh trước khi vào lab | Mở D01, chọn `/xem`, để mục đầu ôn sau bằng `/sau`, rồi kết thúc ở mục tiếp theo bằng `/thoat`. | Học liệu của mục đầu hiện kèm mã đoạn. Tổng hợp ghi mục đầu **Nên ôn lại**, mục sau **Chưa kiểm tra**. |
| C. Lẫn hai khái niệm | Ở mục Chatbot và LLM, nhập lời giải thích lẫn với RAG. Cấp phản hồi mẫu dẫn `[D07-P01]` của bài RAG, rồi chọn để ôn sau. | Phản hồi lệch nguồn bị chặn. Giao diện nhắc tiếp tục ở mục hiện tại và vẫn cho để ôn sau. |

Giữ cách hiển thị trạng thái cuối phiên để người học biết mục nào cần xem tiếp. Mục này chỉ cung cấp bằng chứng kiểm thử luồng nội bộ, tách riêng với phiên người dùng thử ở bảng trên.

### 2. Diễn tập nội bộ theo 2 vai (trước khi mời người ngoài nhóm)

- **Vai A — học viên L3 (đóng vai nội bộ):** nhập lời giải thích theo kịch bản, có chủ ý nhầm "LLM tự nhớ lịch sử hội thoại".
- **Vai B — quan sát viên:** theo dõi từng lượt theo 5 nhịp, ghi điều app hiển thị và hành động tiếp theo mà người học phải đoán.
- **Cách chạy:** code thật `codebase/session.py` và `codebase/app.py` (bài D01, chạy kiểm luồng trước khi nối `.env` với phản hồi model **dựng sẵn**). Lệnh `/xem`, `/sau`, `/thoat` chạy qua `python run.py` thật.

| Lượt | Vai A nhập (soạn sẵn) | Phản hồi app (model dựng sẵn) | Vai B ghi nhận |
|---|---|---|---|
| 1 | "LLM tự nhớ lịch sử, chatbot chỉ là LLM có giao diện." | `[HIỂU SAI]` hỏi lại theo `[D01-P01]` (gợi mở 1) | Phản hồi dựng sẵn nên không đánh giá chất lượng gợi mở. Đã kiểm: app đếm 1 lượt gợi mở. |
| 2 | "Chắc ứng dụng lưu giúp, LLM không tự lưu." | `[THIẾU Ý]` hỏi thêm tầng ứng dụng bổ sung gì, theo `[D01-P02]` (gợi mở 2) | Đúng hướng nhưng còn thiếu công cụ và system prompt. |
| 3 | "Chatbot thêm system prompt." | Hết 2 gợi mở → `[XEM LẠI KIẾN THỨC]` hiện đủ 3 ý chuẩn kèm mã đoạn | Lời mời "thử diễn đạt lại một lần" rõ. Người học có thể chép lại nguyên văn. |
| 4 | "Thêm prompt và công cụ." | "Ý này vẫn còn điểm cần ôn. Xem mã đoạn ở phần tổng hợp." → **Nên ôn lại** | Không nói còn thiếu điểm nào. |
| 5 (Temperature) | "Temperature là độ chính xác." | Phản hồi dựng sẵn dẫn `[D07-P01]` (sai ý) → `[CHƯA ĐỦ CĂN CỨ] Chưa nhận được phản hồi đối chiếu hợp lệ…` | Chặn đúng, nhưng không nêu bước tiếp theo. |
| 6 | `/sau` ở ý cuối | Cả hai ý **Nên ôn lại**; vẫn hiện "Ý nào bạn vừa làm rõ?" | Lời mời không khớp trạng thái. Enter để bỏ qua. |

**Phát hiện từ diễn tập nội bộ**

| # | Phát hiện | Mức nghiêm trọng (dự kiến) | Kiểm lại ở phiên người thử (`S1–S3`) |
|---|---|---|---|
| 1 | Sau khi xem lại mà vẫn thiếu, app chỉ ghi **Nên ôn lại** và trỏ tới mã đoạn ở phần tổng hợp, không nêu điểm còn thiếu. Sơ đồ `spec.md` §4 ghi "Chỉ rõ phần cần ôn". | Vừa | Lặp lại ở `S1` (*"Mình thiếu điểm nào?"*). |
| 2 | Khi phản hồi bị chặn vì mã đoạn lệch (`_UNVERIFIED`), thông báo không gợi bước tiếp theo, khác nhánh thiếu học liệu (có dòng "Mời bạn tiếp tục với ý đang ôn"). | Vừa | Lặp lại ở `S3` (*"Giờ mình làm gì tiếp?"*). |
| 3 | Bước tự nhắc lại cuối phiên vẫn hỏi "Ý nào bạn vừa làm rõ?" khi cả hai ý đều **Nên ôn lại**. | Thấp | Chưa gặp đầy đủ ở `S1–S3` (cần tiếp tục theo dõi). |
| 4 | `/xem` hiện đủ ý chuẩn, kể cả điểm người học chưa nói. | Thấp (ảnh hưởng A4 nếu chép lại) | Ghi nhận dấu hiệu ở `S1`; `S2` vẫn tự diễn đạt lại bằng lời mình. |

## Tổng hợp

- **Chủ đề lặp nhiều nhất:** Người thử vướng ở hai điểm phản hồi của ứng dụng (mức **Vừa**): (1) sau khi xem lại kiến thức mà vẫn bị gắn **Nên ôn lại**, ứng dụng không chỉ rõ còn thiếu ý cốt lõi nào (`S1` hỏi lại *"Mình thiếu điểm nào?"*); (2) khi gặp thông báo `[CHƯA ĐỦ CĂN CỨ]`, ứng dụng không gợi ý bước tiếp theo (`S3` gõ lại câu cũ rồi dừng và hỏi *"Giờ mình làm gì tiếp?"*). Ngoài ra, người thử có xu hướng gõ ngay hoặc bấm `/xem` sớm thay vì đọc dòng hướng dẫn lệnh (`S1`, `S2`).
- **Sửa gì sau CP4 (ghi `spec.md` §10):** Đã cập nhật 2 điểm UX trong `codebase/session.py` (dùng chung cho cả CLI `app.py` và giao diện web `web.py`, không thay đổi `codebase/agent.py` hay kết quả `eval/` đã chạy): (a) khi vẫn còn thiếu sau `/xem` và chuyển sang **Nên ôn lại**, hiển thị rõ các ý cốt lõi kèm mã đoạn `[DXX-PYY]` tương ứng cần ôn lại (xử lý vướng mắc của `S1`); (b) bổ sung dòng hướng dẫn bước tiếp theo (*diễn đạt lại, chọn xem lại kiến thức `/xem` hoặc để ôn sau `/sau`*) vào thông báo `_UNVERIFIED` (xử lý vướng mắc của `S3`). Đã ghi nhận vào nhật ký `spec.md` §10 (bảng `Sau CP4`).
- **Giữ gì và vì sao:** Nhánh lệnh `/xem` · `/sau` · `/thoat` và bảng trạng thái cuối phiên kèm mã đoạn `[DXX-PYY]`, vì người thử ít thời gian vẫn xem nhanh và bỏ qua được mà không bị ép (`S2` dùng `/xem` và tự diễn đạt lại đúng; `S3` dùng `/xem`, `/sau`, `/thoat` đúng nhánh như kiểm thử A–C).
- **Để dành sau:** Mở rộng mẫu đo chỉ số A4 với nhiều học viên L3 hơn (hiện mới có `1/2` lượt hoàn thành đạt yêu cầu, `1` ca dừng sớm, mức tiếc nuối `1 / 2 / 0`, chưa đủ cỡ mẫu để kết luận ngưỡng `≥75%` toàn lớp), kiểm soát trường hợp chép sát từ khóa sau `/xem`, và ẩn lời mời *"Ý nào bạn vừa làm rõ?"* khi mọi mục đều ở trạng thái **Nên ôn lại**.
