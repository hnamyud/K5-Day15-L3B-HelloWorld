# Bản đồ 15 ngày và đánh giá phiên học sinh dạy lại cho AI

## Kết quả phiên CP4 trên nhánh 15-day

Cả 38 ca đã được gắn mã mục theo bộ 52 mục mới và chạy trong phiên hai vai. Model dự án là `gpt-4.1-mini`. `gpt-4.1` chấm phản hồi bổ sung, đối chiếu toàn bộ lời đáp với các ý chuẩn.

| Phép kiểm | Kết quả |
|---|---:|
| Ca có mục tương ứng trong học liệu mô phỏng | 38/38, trên 15 ngày |
| Đúng nhãn nội bộ của giám khảo | 37/38 |
| Đúng nhãn theo nhóm | 14/14 đủ ý, 8/8 thiếu ý, 15/16 hiểu sai |
| Ca thiếu hoặc sai nhận đúng một câu gợi mở và đạt các tiêu chí chấm câu hỏi | 23/24 |
| Ca thiếu hoặc sai bị chuyển mục sớm | 1/24 |
| Lỗi kỹ thuật khiến ca không có kết quả | 0/38 |

**Ca trượt M34.** Học viên nói có thể chuyển yêu cầu sang tiến trình khác mà vẫn đọc trạng thái trong bộ nhớ riêng. Giám khảo gắn nhầm **Đủ ý**, công bố phần chuẩn và chuyển mục trước khi học viên tự sửa. 23 ca còn lại chỉ hiện câu hỏi ở lượt đầu. Lượt này ghi 47 lần gọi model cho dự án, 16.227 token vào và 605 token ra. Số token của lượt chấm bổ sung nằm ngoài phép đếm này.

Phép thử này kiểm lượt đầu với lời giảng giả lập. Kết quả học A4 ở người dùng thật còn cần đo. CP3 đã nộp từ main dùng bộ 30 câu CP2. Bản thử trung gian trước khi tách vai chỉ có 28 ca trong mục có học liệu. Các phép đo có mẫu số và phạm vi khác nhau. [Đối chiếu CP3 đến CP4](teachback-cp3-cp4.md) · [Phản hồi luồng hai vai](teachback-15days-result.json) · [Chấm bổ sung](teachback-15days-result-judge.json)

Chạy lại bằng `MODEL_NAME=gpt-4.1-mini python eval/run_study_15days.py --judge-model gpt-4.1 --output /tmp/teachback-15days-new.json`. Dùng tên tệp mới cho mỗi lượt.

## Bản đồ kiến thức

Bản đồ tóm tắt các mục tiêu trong đề cương công khai. Cột **Trước khi thay học liệu** ghi phạm vi phiên cũ để giải thích mốc so sánh phía dưới. Phiên mới có 52 mục mẫu trên 15 ngày. Phạm vi chính thức của pre-class 5 cần đối chiếu với học liệu K5.

| Ngày theo đề cương | Các ý kiến thức và kỹ năng | Trước khi thay học liệu | Ca giả lập |
|---|---|---|---:|
| [01 · AI & LLM Foundation](https://e-learning-production.vercel.app/ngay/ngay-01) | AI/ML/DL/GenAI; Transformer và attention; sinh token; huấn luyện, context và lấy mẫu; từ LLM đến agent; chọn model, API và chi phí | D01 · 10 mục nền tảng | 20 |
| [02 · Xác định bài toán cho AI](https://e-learning-production.vercel.app/ngay/ngay-02.html) | Double Diamond; người dùng và pain; hiện trạng, mục tiêu, cách đo; automate/augment; Rule–Workflow–Agent và quyết định Go/No-Go | Chưa có mục cho tình huống thử | 1 |
| [03 · Từ chatbot đến agentic agent](https://e-learning-production.vercel.app/ngay/ngay-03.html) | Bốn mức hệ thống; Agentic Fit; quyền điều khiển luồng; ReAct và quan sát; công cụ, trace và điều kiện dừng | D03 · workflow và agent | 2 |
| [04 · Prompt Engineering & Tool Calling](https://e-learning-production.vercel.app/ngay/ngay-04.html) | Role–Task–Context–Format; few-shot; system prompt; khai báo tham số công cụ; vòng gọi công cụ và kiểm tra chỉ thị trong dữ liệu | D03 · Tool Calling | 2 |
| [05 · Thiết kế sản phẩm AI](https://e-learning-production.vercel.app/ngay/ngay-05.html) | Giả thuyết, thử nghiệm fidelity thấp và MVP; PRD; kỳ vọng, giải thích và quyền kiểm soát; tự chủ, phục hồi và hai loại lỗi | Chưa có mục cho tình huống thử | 1 |
| [06 · AI Product Hackathon](https://e-learning-production.vercel.app/ngay/ngay-06.html) | Pain có bằng chứng; thu hẹp lát cắt; prototype; golden set; kiểm chứng người dùng, demo và phản biện | Chưa có mục cho tình huống thử | 1 |
| [07 · Data Foundations — Embedding & Vector Store](https://e-learning-production.vercel.app/ngay/ngay-07.html) | Nguồn dữ liệu; chunking; embedding và cosine; chỉ mục vector; metadata và bộ lọc | Chưa có mục cho tình huống thử | 1 |
| [08 · RAG Pipeline](https://e-learning-production.vercel.app/ngay/ngay-08.html) | Nạp và lập chỉ mục; xử lý truy vấn; dense/sparse/hybrid; re-ranking; đóng gói ngữ cảnh, trích dẫn và đánh giá RAG | D07 · RAG và bám nguồn | 2 |
| [09 · Multi-agent và kết nối hệ thống](https://e-learning-production.vercel.app/ngay/ngay-09.html) | Khi cần tách agent; các mẫu điều phối, supervisor–worker; giao việc và trạng thái; MCP, A2A và trace | Chưa có mục cho tình huống thử | 1 |
| [10 · Data Pipeline & Data Observability](https://e-learning-production.vercel.app/ngay/ngay-10.html) | Ingest theo nguồn; hợp lệ và đúng thực tế; luật chất lượng; quan sát dữ liệu; dừng, cách ly hoặc tiếp tục | Chưa có mục cho tình huống thử | 1 |
| [11 · Guardrails, HITL và Responsible AI](https://e-learning-production.vercel.app/ngay/ngay-11.html) | Rủi ro theo tầng; kiểm đầu vào và đầu ra; quyền hạn và duyệt người; kiểm thử phòng thủ và quản trị | Chưa có mục cho tình huống thử | 1 |
| [12 · Hạ tầng Cloud & Deployment](https://e-learning-production.vercel.app/ngay/ngay-12.html) | Từ chạy cục bộ đến dịch vụ; container, cấu hình, health check; xác thực, giới hạn tần suất/ngân sách; stateless và triển khai | Chưa có mục cho tình huống thử | 1 |
| [13 · Monitoring, Logging, Observability & LLMOps](https://e-learning-production.vercel.app/ngay/ngay-13.html) | Metrics, logs, traces và chất lượng; latency theo percentile và token; correlation ID; bảo vệ dữ liệu và cảnh báo theo SLO | Chưa có mục cho tình huống thử | 1 |
| [14 · AI Evaluation & Benchmarking](https://e-learning-production.vercel.app/ngay/ngay-14.html) | Golden set; metric truy xuất và sinh trả lời; LLM-as-judge và thiên lệch; nhiễu thống kê, phân loại lỗi và cổng phát hành | D09 · Eval và bộ câu thử | 2 |
| [15 · Retrospective & Track Decision](https://e-learning-production.vercel.app/ngay/ngay-15.html) | Nhìn lại dựa trên bằng chứng; tổng hợp bài học lớp; đối chiếu năng lực với yêu cầu vai trò; chọn track và cam kết tiếp theo | Chưa có mục cho tình huống thử | 1 |

## Thiết kế kiểm thử ở mốc trước khi thay học liệu

- **38 lời tự giải thích giả lập trên 15 ngày.** Có 28 ca trên 14 mục hiện có, gồm 14 đúng đủ, 6 thiếu ý và 8 hiểu sai. Mỗi mục hiện có một lời giảng đủ và một lời giảng có vấn đề. Thêm 10 tình huống chưa có học liệu trực tiếp, mỗi ngày còn lại một ca. Mẫu tập trung vào D01 với 20 ca.
- **Đo theo đường học viên sử dụng.** Với 28 ca có mục, gọi phiên ôn trên mục tương ứng. Với 10 ca chưa có mục, kiểm việc chọn bài theo danh sách thực tế và thử thêm đường nhập một lượt độc lập. Phần thử độc lập giúp phát hiện tra nhầm chủ đề khi chưa có căn cứ.
- **Chấm riêng vai người học.** Nhãn và chuyển mục được đối chiếu với kỳ vọng đặt trước. Model chấm đọc đoạn nguồn và phản hồi để đánh giá bám nguồn, giọng người mới học, một câu hỏi mở có trọng tâm, và việc nêu sẵn lời giải. Ở ca đủ ý, xác nhận ngắn là phù hợp. Ở ca thiếu hoặc sai, học sinh cần còn cơ hội tự nói ra phần cần sửa.
- **Giới hạn.** Đây là thử nghiệm tổng hợp, mỗi lời giảng là lượt đầu trong một mục. Kết quả dùng để xem độ phủ và hành vi ban đầu của bản hiện tại. Tỷ lệ học sinh tự sửa, tiến bộ sau hai lượt và độ tin cậy trên người học thật cần đánh giá theo phiên riêng.

[Dữ liệu và kỳ vọng](study-15days.json). Trường `lesson_code` được bổ sung khi chuyển sang học liệu 15 ngày.

## Kết quả trên luồng trước khi tách vai

Chạy bản hiện có với `gpt-4.1-mini` và dùng `gpt-4.1` chấm riêng. Dịch vụ từ chối tên model cấu hình ban đầu `cx/gpt-6-luna`. Phiên thử ghi 30 lần gọi model cho dự án, dùng 36.366 token vào và 3.010 token ra theo API. Số này gồm hai ca nhập tự do tra sang chủ đề khác và không gồm chi phí model chấm. [Phản hồi dự án](study-15days-result.json) · [Điểm của LLM chấm](study-15days-result-judge.json)

| Phép kiểm | Kết quả | Ý nghĩa |
|---|---:|---|
| Độ phủ theo đề cương | 5/15 ngày có ý được kiểm | Ứng dụng hiện có bốn mã bài. Tool Calling của ngày 4 theo đề cương đang dùng học liệu dưới mã D03, RAG ngày 8 dùng D07, Eval ngày 14 dùng D09. |
| Gắn đúng nhãn trong mục có học liệu | 23/28 | 11/14 đủ ý, 4/6 thiếu ý và 8/8 hiểu sai. D01 đạt 19/20. |
| Xác nhận đủ ý quá sớm | 2/6 ca thiếu ý | M23 và M30 chuyển mục trước khi học sinh bổ sung giới hạn vòng agent hoặc nguyên tắc trích nguồn. |
| Câu gợi mở đạt theo LLM chấm | 7/14 ca thiếu hoặc sai | Đúng nhãn, có căn cứ, giữ vai người học, hỏi mở đúng một trọng tâm và giữ lại phần học sinh cần tự diễn đạt. |
| Câu gợi mở đạt khi đối chiếu nguyên văn | 0/14 ca thiếu hoặc sai | 10 ca nói sẵn ít nhất một phần cốt lõi, hai ca hỏi nhiều câu hoặc nhiều ý, hai ca xác nhận đủ ý quá sớm. |
| Nhập tự do khi thiếu mục tương ứng | 8/10 báo thiếu căn cứ | M27 chuyển từ kiểm chứng với người dùng sang kỷ luật bộ câu thử. M33 tra được học liệu liên quan về người duyệt, nhưng đây là mục của bài Tool Calling và câu hỏi bị dàn trải. |

M19 tính đúng **0,004 USD** và dự án vẫn trả `[THIẾU Ý]`, rồi lặp lại chính cách tính của học sinh. M29 và M36 bị hậu kiểm chặn do phản hồi thiếu mã hợp lệ hoặc có mã ngoài kết quả tra, theo thông báo hiển thị. Vì vậy, khả năng xác nhận đủ ý cũng cần kiểm thêm bên cạnh việc sửa cách hỏi.

### Đối chiếu 14 phản hồi cần gợi mở

| Ca | Quan sát khi đọc nguyên văn |
|---|---|
| M02 | Nêu sẵn ranh giới GenAI và LLM rồi yêu cầu giải thích lại. |
| M04 | Có hai câu hỏi, một câu gộp lịch sử và công cụ. |
| M06 | Nói sẵn Temperature chỉ thay đổi cách lấy mẫu và hỏi hai câu. |
| M08 | Nêu token có thể là một phần từ hoặc dấu câu trước khi hỏi về khác biệt giữa từ và token. |
| M10 | Giải thích sẵn vai trò của các token khác trong ngữ cảnh trước khi hỏi về đại từ. |
| M12 | Nêu cách chọn lọc và tóm tắt ngữ cảnh trước khi hỏi lại lý do. |
| M14 | Nói sẵn người đánh giá cung cấp tín hiệu lúc huấn luyện rồi hỏi vai trò của họ. |
| M16 | Hỏi hai ý độc lập về Temperature và giới hạn token đầu ra. |
| M18 | Nói sẵn `usage` là trường trả về rồi hỏi lại chiều gửi nhận. |
| M20 | Nói sẵn chi phí gồm token vào và ra rồi hỏi vai trò của token vào. |
| M23 | Cho chuyển mục khi học sinh còn thiếu giới hạn vòng lặp. |
| M25 | Nói sẵn ứng dụng là bên thực thi hàm rồi hỏi lại cách phân vai. |
| M30 | Cho chuyển mục trước khi học sinh giải thích trích nguồn hoặc xử lý thiếu căn cứ. |
| M37 | Nói trước cần giữ chuẩn và bộ câu thử, rồi yêu cầu học sinh giải thích. |

LLM chấm có lúc chỉ xét câu hỏi cuối. Chẳng hạn, ở M14 và M25 nó đánh dấu không nói sẵn đáp án dù câu trước đã nêu đáp án. Khi dùng LLM để theo dõi chỉ số gợi mở, cần đối chiếu **toàn phản hồi** và chấm người trên mẫu hiệu chuẩn. Mốc 0/14 là kết quả áp tiêu chí nghiêm “đúng một trọng tâm và để học sinh tự nói phần cốt lõi”, trên mẫu giả lập hiện tại.

## Đề xuất kiến trúc

**Tách hai vai trong một workflow cố định.** Vai đối chiếu làm việc ngầm với học liệu, xác định nhãn và chọn đúng một điểm còn thiếu hoặc sai. Vai người mới học dùng kết quả đó để hỏi một câu tò mò trong phạm vi ý hiện tại. Học sinh chỉ nghe giọng của người mới học. Sau khi học sinh tự diễn đạt lại, workflow gọi đối chiếu lần nữa và quyết định hỏi tiếp, chuyển mục hoặc hiện phần xem lại theo giới hạn của phiên.

Với M25, AI người mới học có thể hỏi “Sau khi model đưa ra tên hàm và tham số, điều gì xảy ra để kết quả quay lại cuộc trò chuyện?” Câu hỏi giữ trọng tâm ở bên thực thi nhưng để học sinh tự nêu câu trả lời. Phần giải thích chuẩn thuộc bước **Xem lại kiến thức**.

Bước đầu có thể dùng một lần gọi LLM để tạo trường quyết định nội bộ và một câu hỏi hiển thị, rồi kiểm nhãn, mã nguồn và số câu hỏi bằng code. Chỉ thử gọi model thứ hai để viết câu hỏi nếu thử lại trên cùng bộ cho thấy bước đối chiếu đã ổn mà vẫn thường xuyên lộ đáp án hoặc hỏi ghép. So sánh thêm thời gian phản hồi và token trước khi chọn phương án. Kết quả hiện tại đủ chỉ ra chỗ cần sửa trong cách gợi mở, chưa chứng minh dùng hai model sẽ giải quyết lỗi.
