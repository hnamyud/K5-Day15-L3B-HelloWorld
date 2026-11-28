# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

Lượt 1 là mốc **CP3 đã nộp từ main**. Lượt 2 trong bảng dưới ghi lần sửa prompt của luồng cũ trên main. **CP4 trên nhánh 15-day** dùng phiên dạy lại hai vai, với báo cáo và phép kiểm riêng. [Đối chiếu CP3 đến CP4](teachback-cp3-cp4.md)

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-230315` | 26/30 | 87% | 11/12 (92%) | 11/14 (79%) | 4/4 (100%) | Qua ngưỡng điểm tổng, chưa đủ dữ liệu để kết luận đạt §7 |
| 2 | `run-2@20261128-001731` | 26/30 | 87% | 11/12 (92%) | 11/14 (79%) | 4/4 (100%) | Qua ngưỡng điểm tổng, chưa đủ dữ liệu để kết luận đạt §7 |

Hai lượt dùng cùng 30 câu, cùng `pass_criterion` và model `cx/gpt-6-luna`. Mỗi lượt đạt **22/26 (85%)** trên nhóm `thuong` và `kho` gộp lại. Đối chiếu trace cho thấy **0 câu dẫn mã ngoài kết quả tra cứu**, 8/8 ca thiếu căn cứ báo đúng nhãn và 0/3 ca hiểu sai bản chất Lớp 4 (`B05`, `B11`, `B23`) bị xác nhận nhầm là `[ĐỦ Ý]`. Mục 5 ghi kết quả kiểm giới hạn câu gợi mở theo phiên. Kết luận §7 còn cần số đo học viên tự giải thích lại đúng.

Kết quả từng câu và trace có trong [Lượt 1](run-1.csv), [trace Lượt 1](../traces/run-1.jsonl), [Lượt 2](run-2.csv) và [trace Lượt 2](../traces/run-2.jsonl).

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Nêu sẵn đáp án trước khi hỏi | 2 | `B06`, `B23` |
| Hỏi lệch chỗ học viên đang nhầm | 1 | `B08` |
| Phản hồi ngắn hơn tiêu chí | 1 | `B03` |

**Các lỗi cụ thể**

| Câu | Đầu vào tóm tắt | Trích phản hồi Lượt 1 | Vì sao trượt |
|---|---|---|---|
| `B03` | Học viên phân biệt đúng workflow cố định và AI Agent. | `[ĐỦ Ý] Bạn đã nêu đúng khác biệt về luồng điều khiển, vai trò của LLM và giới hạn MAX_STEPS; cũng hiểu vì sao nên ưu tiên workflow đơn giản trước [D03-P01] [D03-P02]. Hãy tự quyết định sang làm lab hay ôn thêm.` | Phản hồi có 2 câu, tiêu chí yêu cầu 3–5 câu. |
| `B06` | Học viên cho rằng LLM tự chạy hàm truy vấn, ứng dụng chỉ nhận kết quả cuối. | “ứng dụng mới thực thi rồi đưa kết quả lại cho mô hình [D03-P03]. Ai là bên thực sự chạy hàm trong quy trình này?” | Phản hồi trả lời sẵn bên thực thi, rồi hỏi lại đúng thông tin đó. |
| `B08` | Học viên nhầm RAG với việc model gọi công cụ gửi email và cập nhật cơ sở dữ liệu. | “Trong RAG, bước nào cung cấp tài liệu cho LLM, và RAG có cập nhật trọng số mô hình không? [D07-P01]” | Câu hỏi gộp hai vế và chuyển sang trọng số. Chỗ cần làm rõ là khác biệt giữa truy xuất tài liệu và thao tác gửi tin hoặc sửa dữ liệu. |
| `B23` | Học viên cho rằng workflow và Agent có cùng luồng, còn Agent tự chạy vô hạn. | “Workflow cố định và AI Agent có cùng cách quyết định bước tiếp theo không, nếu trong workflow mã nguồn định sẵn luồng chạy còn Agent để LLM chọn bước và công cụ, lặp có giới hạn `MAX_STEPS`?” | Câu hỏi Có/Không đã nêu sẵn cả bên điều khiển luồng lẫn giới hạn số bước. |

## 3. Một lần cải tiến

Nhóm sửa prompt ở nhánh `[THIẾU Ý]` và `[HIỂU SAI]` để AI bám vào lời giải thích mới nhất, hỏi một câu mở đúng chỗ vướng và dẫn mã đoạn liên quan. Phần giải thích chuẩn dành cho bước **Xem lại kiến thức**. Mục tiêu là để học viên tự chỉ ra và sửa chỗ hiểu sai trước khi vào lab. [Mô tả thay đổi](../docs/de-xuat-cai-tien-goi-mo-luot-2.md)

Trong ba câu được chọn để theo dõi cải tiến (`B06`, `B08`, `B23`), số câu đạt tăng từ **0/3 lên 2/3**. Toàn bộ 30 câu vẫn đạt **26/30 (87%)** vì hai câu cải thiện và hai câu tệ đi.

| Câu | Lượt 1 → Lượt 2 | Điều gì thay đổi |
|---|:---:|---|
| `B06` | 0 → 1 | Lượt 2 hỏi “bên nào thực sự chạy hàm và đưa kết quả trở lại cho mô hình?” `[D03-P03]` và để học viên tự xác định bên thực thi. |
| `B23` | 0 → 1 | Lượt 2 hỏi “điều gì quyết định bước kế tiếp và khi nào quá trình dừng?” `[D03-P01]` `[D03-P02]`, để học viên tự giải thích cả quyền điều khiển luồng lẫn giới hạn bước. |
| `B05` | 1 → 0 | Lượt 1 mời học viên chỉ ra mâu thuẫn về việc cập nhật trọng số. Lượt 2 chỉ hỏi “tài liệu được dùng như thế nào để LLM tạo câu trả lời?” `[D07-P01]`. Câu hỏi chưa gợi trực tiếp vào hiểu nhầm về trọng số. |
| `B11` | 1 → 0 | Lượt 1 để học viên suy ra thay đổi ở đầu ra và rủi ro. Lượt 2 giải thích trước cách lấy mẫu, độ đa dạng và rủi ro sai lệch theo `[D01-P04]`, rồi hỏi lại Temperature làm thay đổi điều gì. |

Lượt 2 được lưu ở commit `287a862`. Commit `c8754f2` khóa ý đang ôn và cập nhật cách chặn yêu cầu ngoài phạm vi sau khi đã có kết quả Lượt 2. Số trong báo cáo phản ánh bản tạo file Lượt 2.

## 4. Còn lại

- **Vẫn trượt ở hai lượt.** `B03` vẫn chỉ có 2 câu. `B08` đã nhận diện thao tác gửi email và cập nhật cơ sở dữ liệu trong lời học viên, nhưng câu hỏi vẫn thêm một vế về trọng số. Học viên vẫn có thể bỏ qua chỗ nhầm giữa đọc tài liệu và tác động ra ngoài.
- **Ưu tiên nếu có thêm một tuần.** Thử các câu gợi mở nhắm đúng một chỗ hiểu sai trong từng lượt. Giữ `B05`, `B06`, `B08`, `B11` và `B23` trong bộ so sánh để phát hiện cả cải thiện lẫn lỗi phát sinh. Kiểm riêng độ dài ở nhánh xác nhận đủ ý để xử lý trường hợp `B03`.

## 5. Kiểm thử phiên ôn nhiều ý D01

Chạy `python run.py` trên commit `c8754f2` với API OpenAI model `gpt-4.1-mini`. D01 có hai ý **Chatbot và LLM** (`[D01-P01]`, `[D01-P02]`) và **Temperature** (`[D01-P03]`, `[D01-P04]`). Model và phiên bản code của ca kiểm thử này khác với Lượt 2 của bộ 30 câu. Người kiểm thử nhập câu theo kịch bản để quan sát luồng.

| Ca kiểm thử | Cách chạy | Kết quả quan sát |
|---|---|---|
| Chatbot và LLM | Nhập ba lời giải thích liên tiếp cho rằng LLM tự lưu lịch sử hoặc gọi công cụ. Sau phần xem lại, tự diễn đạt lại vai trò của LLM và ứng dụng chatbot. | Hai phản hồi đầu mỗi phản hồi có một câu gợi mở, dẫn `[D01-P01]` và `[D01-P02]`. Khi lời giải thích lần thứ ba vẫn sai, chương trình hiện **Xem lại kiến thức**. Lời diễn đạt mới được đối chiếu và nhận `[ĐỦ Ý]` trước khi chuyển sang Temperature. |
| Temperature | Nhập ba lời giải thích liên tiếp cho rằng tăng Temperature làm mô hình biết thêm hoặc trả lời chính xác hơn. Sau phần xem lại, tự diễn đạt lại tác động lên cách lấy mẫu. | Ý mới có lại hai lượt gợi mở, mỗi lượt hiện một câu hỏi dẫn `[D01-P04]`. Lượt kế tiếp hiện **Xem lại kiến thức**. Sau khi nhận `[ĐỦ Ý]` cho lời diễn đạt mới, chương trình hiện lời mời tự nhắc lại và tổng hợp hai ý đều **Đã giải thích được**. |
| Kết thúc sớm | Mở phiên D01 mới, nhập một lời giải thích sai về Chatbot và LLM, đợi AI phản hồi, chọn `/sau` rồi `/thoat` ở ý thứ hai. | Phiên in tổng hợp ngay. Chatbot và LLM là **Nên ôn lại**, Temperature là **Chưa kiểm tra**. |

**Số đo từ API:** Phiên hai ý có 8 lần gọi model, 10.005 token vào và 774 token ra. Phiên kết thúc sớm có 1 lần gọi model, 1.236 token vào và 125 token ra. Lời mời tự diễn đạt sau phần xem lại nằm ngoài số câu gợi mở.

**Quan sát về chất lượng:** AI đã nêu trước một số ý mà câu hỏi yêu cầu người học tự giải thích. Ví dụ, ở ý Temperature, AI nói tăng Temperature không cải thiện độ chính xác rồi hỏi lại vì sao. Phiên này xác nhận giới hạn số câu hiển thị, đồng thời ghi nhận lỗi nêu sẵn ý cần gợi mở.

**Trạng thái §7:** Ca thử với AI thật đã xác nhận tối đa hai câu gợi mở cho mỗi ý và trạng thái đúng khi kết thúc sớm. Tỷ lệ học viên tự giải thích lại đúng cần đo từ các phiên có người dùng thật. [Nhật ký dùng thử](../validation/log.md)

## 6. Mô phỏng phiên D01 mở rộng

Học liệu mẫu `1.1-d01` dùng [đề cương Day 1 công khai](https://e-learning-production.vercel.app/ngay/ngay-01) để bổ sung 8 mục cho phiên tự ôn. Các mục ưu tiên kiến thức nền và chuẩn bị gọi API. Phạm vi bắt buộc trước lab cần được nhóm đối chiếu với slide hoặc transcript pre-class K5. [Data card](../data/DATA_CARD.md)

| Phần ôn | Mã đoạn | Ví dụ để học viên tự giải thích |
|---|---|---|
| Bản đồ AI | `[D01-P05]` | Vì sao hệ thống tạo ảnh có thể thuộc GenAI mà không cần là LLM? |
| Chatbot và LLM | `[D01-P01]` `[D01-P02]` | Khi mở lại cuộc trò chuyện, phần nào quản lý lịch sử? |
| Sinh token và Temperature | `[D01-P03]` `[D01-P04]` | Sau khi chọn một token, model làm gì? Tăng Temperature thay đổi điều gì? |
| Token và tokenizer | `[D01-P06]` | Hai đoạn cùng số từ có nhất thiết dùng cùng số token không? |
| Transformer và attention | `[D01-P07]` | Với cùng một đại từ, vì sao đổi phần còn lại của câu có thể đổi đối tượng được nhắc đến? |
| Cửa sổ ngữ cảnh | `[D01-P08]` | Nếu lịch sử quá dài, bạn sẽ gửi lại phần nào và vì sao? |
| Huấn luyện và giới hạn | `[D01-P09]` `[D01-P10]` | Phân biệt ba bước huấn luyện và giải thích vì sao model vẫn có thể trả lời sai. |
| Tham số sinh và giới hạn đầu ra | `[D01-P11]` | Phân biệt top-p với giới hạn độ dài khi câu trả lời bị ngắt. |
| Đọc một lần gọi API | `[D01-P12]` | Trường nào do ứng dụng gửi đi? Tìm số token đã dùng ở đâu? |
| Chọn model và ước tính chi phí | `[D01-P13]` `[D01-P14]` | Với 1.000 token vào và 250 token ra, tính tiền theo hai mức giá giả định trong học liệu. |

**Kết quả kiểm thử.** Chạy `MODEL_PROVIDER=fake python run.py`, chọn bài 1 rồi dùng `/xem` và `/sau` ở từng mục. Chương trình hiện đủ 10 mục, phần xem lại, lời mời tự nhắc lại và bảng tổng hợp. Với phản hồi theo kịch bản, đã kiểm luồng hai lượt gợi mở rồi xem lại, đối chiếu khi diễn đạt lại, chặn phản hồi dẫn sai mã và giữ nguyên mục đang ôn. Cả 30 đầu vào của benchmark cho cùng phản hồi ở chế độ giả khi đối chiếu trước và sau cập nhật. Các kết quả này đo luồng và mã nguồn trên dữ liệu mô phỏng. Chất lượng model thật và kết quả học A4 của bản mở rộng chưa được đo.

## 7. Kiểm tra phiên dạy lại hai vai

Phiên mới dùng [52 mục học liệu mô phỏng](../data/teachback_lessons.json) trên 15 ngày theo đề cương công khai. Kiểm tra bằng chế độ giả cho thấy cả 15 ngày đều chọn được, mở đầu bằng câu hỏi và hiện nội dung kèm nguồn khi chọn `/xem`. Các bài kiểm thử theo kịch bản kiểm thêm việc giới hạn hai câu gợi mở, chuyển sang giám khảo và giữ đáp án ngoài đầu vào của vai người học.

Chạy `MODEL_NAME=gpt-4.1-mini python run.py` và nhập `ôn lại ngày 1`. Khi lời giảng giả lập nhầm công cụ tạo ảnh với LLM, AI hỏi “Bạn xếp một công cụ chỉ tạo ảnh vào đâu trong bản đồ này?”. Sau khi lời giảng mới phân biệt đủ AI, ML, Deep Learning, GenAI và LLM, giám khảo xác nhận hai ý đúng, giải thích theo `[D01-P51]`, dẫn mục 1.1–1.2 của đề cương và phiên chuyển sang Chatbot và mô hình. Số đo API của ca này là 3 lời gọi, 957 token vào và 34 token ra. Đây là một ca chạy luồng với lời giảng giả lập. Kết quả học của người dùng thật và tỷ lệ giám khảo gắn đúng nhãn trên toàn bộ học liệu còn cần đo.
