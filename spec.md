# AI SPEC — Kiểm tra cách hiểu khái niệm trước lab (A4) · Nhóm HelloWorld · Phòng C401 · Zone L3B

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.

Track: [x] A · [ ] B · [ ] C · [ ] D · [ ] E — bài toán: **A4 · Lớp học kiểu mới** (Phát hiện sớm cách hiểu sai khái niệm pre-class trước khi làm lab bằng phương pháp tự giải thích và hỏi gợi mở bám học liệu chuẩn).
Data BTC cấp đã dùng (không commit nguyên file): `data/preclass/` (`learners.csv`, `events.csv`, `class_events.csv`, `answers.csv`, `chat.csv`, `completed_items.csv`, `rewards.csv`, ngày 05/11–25/11/2026) — tổng hợp tại `evidence/data-mining.md` và script `evidence/count_preclass.py`.

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- **Luồng hiện tại trong khoá (4 bước):**
  1. Học viên lớp L3 mở trang pre-class (`preclass-online.com`) trước buổi học để xem video bài giảng, làm câu hỏi giữa video, mini lab hoặc bài ôn cuối ngày (`pre_post_post`).
  2. Sau khi học xong pre-class và trước khi vào làm lab thực hành, học viên tự ôn nhanh bằng cách đọc lại slide/học liệu (`13/22` phiếu L3), làm bài thử (`8/22`), tự giải thích nhẩm (`7/22`), hỏi công cụ ngoài (`6/22`) hoặc hỏi bạn/trợ giảng (`5/22`) *(nguồn: `evidence/KhaoSat.csv`)*.
  3. Khi bắt đầu viết/chạy bài lab, học viên mới gặp lỗi logic, lỗi kích thước/rò dữ liệu hoặc lệch kết quả test mẫu nên nhận ra mình đã hiểu sai khái niệm cốt lõi ngay từ bước pre-class.
  4. Học viên phải dừng mạch làm lab để quay lại xem học liệu (`7/22`), sửa bài lab (`6/22`), hỏi người khác (`5/22`), hỏi công cụ ngoài (`3/22`) hoặc tạm dừng lab (`1/22`), mất trung vị `20 phút/lần` *(nguồn: `evidence/KhaoSat.csv`)*.
  *(Ảnh chụp luồng `preclass-online.com` đã che thông tin tài khoản: bổ sung trước CP3).*
- **Công cụ / AI đang được dùng cho việc này + nguồn:**
  - Trên `preclass-online.com` đã có **trợ giảng AI** (`teaching_assistant`, khung hỏi dưới video), **lớp học AI** với các bạn học AI tự động xen vào giữa video (`director_decided` xen vào `385/761 = 50.6%` đoạn bài giảng, tạo `13.975` lượt `agent_message_shown`), và **Sổ hiểu bài** *(nguồn: `tracks/track-a-edtech.md`, `data/preclass/README.md`, `evidence/data-mining.md`)*. Tuy nhiên `98.9%` lượt bạn học AI xen vào bị phớt lờ (`151/13.975 = 1.1%` phản hồi) và chưa có bước chủ động tự kiểm tra từng khái niệm ngay sau pre-class, trước giờ làm lab.
  - Ngoài hệ thống khoá, `6/22 (27.3%)` học viên L3 trong khảo sát dùng **công cụ AI bên ngoài** (như ChatGPT) để tự kiểm tra trước lab, và `3/22` hỏi công cụ AI sau khi phát hiện sai trong lab *(nguồn: `evidence/KhaoSat.csv`)*; các công cụ ngoài này không bám trực tiếp học liệu chuẩn của khoá.

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- **Người dùng chính:** Học viên AI20K lớp L3 (`L3A`, `L3B`) vừa hoàn thành bài học pre-class và chuẩn bị bắt đầu làm bài lab áp dụng kiến thức.
- **Việc họ cố làm xong:** Tự kiểm tra lại mức độ hiểu đúng từng khái niệm cốt lõi vừa học trong bài pre-class ngay trước khi bắt đầu làm bài lab thực hành.
- **Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ:**
  - *Giải bằng gì (`evidence/KhaoSat.csv`, n = 22 phiếu L3, chọn nhiều đáp án):* Xem lại học liệu (`13/22 = 59.1%`), làm câu hỏi/bài thử (`8/22 = 36.4%`), tự giải thích (`7/22 = 31.8%`), dùng công cụ ngoài (`6/22 = 27.3%`), hỏi bạn/trợ giảng (`5/22 = 22.7%`).
  - *Hỏng ở đâu:* Xem lại slide chỉ tạo cảm giác "quen mắt" (ảo tưởng hiểu bài) chứ không bộc lộ chỗ hiểu sai bản chất — **`14/22 (63.6%)`** học viên L3 nghĩ mình đã hiểu đủ để áp dụng nhưng vào lab mới phát hiện hiểu sai (vd: áp softmax hai lần trước `CrossEntropyLoss`, dùng `fit_transform` lên tập test gây rò dữ liệu, shuffle dữ liệu chuỗi thời gian, nhầm `axis` hoặc `mean/median`). Còn hỏi bạn/trợ giảng khó thực hiện ngay lúc tự học ngoài giờ, còn công cụ ngoài không gắn học liệu chuẩn và dễ trả lời thay thay vì đặt câu hỏi phản biện.
  - *Vì sao chưa bỏ:* Đọc lại slide nhanh, có sẵn ngay trên hệ thống, không tốn thêm công chuẩn bị và không sợ bị đánh giá điểm số.
- **Pain:** Học viên lớp L3 sau khi hoàn thành bài pre-class và chuẩn bị làm lab thường xem lướt lại học liệu nên tưởng mình đã hiểu đủ, không phát hiện sớm chỗ hiểu sai bản chất cho đến khi chạy bài lab bị lỗi hoặc lệch kết quả; hậu quả là phải dừng giữa chừng để đọc lại kiến thức và sửa bài, mất trung vị 20 phút mỗi lần (dao động 15–60 phút ở nhóm tự tin mình đã hiểu).
- **Bằng chứng — số chính + kết luận** *(đủ 2 nguồn kiểm chéo nhau; chi tiết: `evidence/summary.md`, `evidence/data-mining.md`, `evidence/KhaoSat.csv`)*:
  - **Nguồn 1 — Khảo sát hành vi thật (`evidence/KhaoSat.csv`, `n = 25` phiếu ngoài nhóm, lọc đúng người dùng L3: `22` phiếu — `12 L3B`, `10 L3A`):** `14/22 (63.6%)` nghĩ mình đã hiểu đủ để áp dụng trước lần phát hiện hiểu sai gần nhất trong lab (`5/22` còn phân vân, `3/22` biết chưa hiểu); `17/22 (77.3%)` gặp lại tình trạng này trong 30 ngày qua (`12` chọn dưới 5 lab, `5` chọn trên 5 lab, `5` không nhớ); thời gian tốn thêm để xem lại/sửa lab có trung vị **`20 phút/lần`** (`n = 21` phiếu ghi số phút, `5–60 phút`; riêng nhóm 14 phiếu tự tin có `13` phiếu ghi số phút, `15–60 phút`, trung vị `20 phút`). Có **22 ví dụ cụ thể** về lỗi hiểu sai trước lab (vd: *"đọc slide thấy quen nên chủ quan, lúc code CrossEntropyLoss lỡ cho qua softmax trước nên kết quả lệch hẳn"* — phiếu #21 L3B; *"tưởng fit_transform dùng luôn cho tập test, chạy xong thấy điểm cao bất thường mới biết bị rò dữ liệu"* — phiếu #12 L3B; *"đinh ninh hiểu cách split train/test rồi, làm lab tới bước tiền xử lý bị leak từ tập test sang mới sửa"* — phiếu #10 L3B).
  - **Nguồn 2 — Đào dữ liệu hành vi thật (`data/preclass/`, `evidence/data-mining.md`, `436/721` HV hoạt động, `107.709` events):** Trên `preclass-online.com`, bộ điều phối lớp học AI xen vào `385/761 (50.6%)` đoạn video (`13.975` lượt `agent_message_shown`), nhưng **`98.9%` bị phớt lờ** (`151/13.975 = 1.1%` phản hồi, `0/228` thưởng `phan_hoi_xay_dung`). Đồng thời `69/77 (89.6%)` HV làm kiểm tra sau bài (`pre_post_post`) sai ít nhất 1 câu ngay lần đầu (`399/1.968 = 20.3%` lượt sai), chỉ `18/436 (4.1%)` từng viết tự giải thích (`giai_thich`), và `909/1.223 (74.3%)` lượt nhắn AI chưa có ý riêng (`rubric_y_moi = 0`).
  - **Kết luận đối chiếu:** Hai nguồn bổ sung chặt cho nhau — log pre-class chứng minh xen vào giữa video bị phớt lờ (`98.9%`) và học viên ít tự giải thích (`4.1%`) nên còn sai nhiều (`20.3%` câu `pre_post_post`), còn khảo sát giải thích nguyên nhân cốt lõi là **ảo tưởng hiểu bài (`14/22 = 63.6%`)** khi chỉ đọc lướt slide trước lab, khiến học viên mất trung vị `20 phút/lần` sửa lab. Vì vậy nhóm đổi lát cắt so với CP1: không xen vào lúc đang xem video, mà để học viên chủ động tự giải thích từng ý cốt lõi ngay sau pre-class và trước lab.

## §2. Impact & quyết định chọn *(guide 1.3)*

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| A4 — Phát hiện sớm cách hiểu sai một khái niệm pre-class trước khi làm lab | **14/22 phiếu L3** cho biết họ từng nghĩ mình đã hiểu đủ để áp dụng trước lần phát hiện hiểu sai trong lab (mẫu khảo sát). | **3 lần/người/tháng** *(tự ước tính)*. Trong 14 phiếu, 9 chọn “Dưới 5”, 3 chọn “Trên 5”, 2 chọn “Không nhớ” khi được hỏi số lab phát hiện hiểu sai sau khi bắt đầu trong 30 ngày qua. | Trung vị **20 phút/lần** để xem lại kiến thức hoặc sửa lab (15–60 phút, 13/14 phiếu trên có số phút tự báo cáo trong khảo sát). | **840 phút/tháng (14 giờ/tháng)** trong nhóm 14 phiếu *(tự ước tính)* |  | Có |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

- **Impact / tháng** của hướng chọn = **14 người × 3 lần/người/tháng × 20 phút/lần = 840 phút/tháng (14 giờ/tháng)** trong mẫu khảo sát *(tự ước tính)*.
  - **14 người** là số phiếu L3 chọn “Nghĩ mình hiểu đủ để áp dụng” ở lần phát hiện hiểu sai được hỏi. **20 phút/lần** là trung vị của 13 phiếu trong nhóm có số phút.
  - **3 lần/người/tháng** *(tự ước tính)* lấy từ `(9 × 2 + 3 × 6) / 12 = 3`. Giả định “Dưới 5” là 2 lần (điểm giữa 0–4), “Trên 5” là 6 lần (mức nguyên thấp nhất), và gán 3 lần cho mỗi phiếu “Không nhớ” theo trung bình của 12 phiếu còn lại.
  - Phép tính dùng toàn bộ số lab phát hiện hiểu sai sau khi bắt đầu trong nhóm 14 phiếu để xấp xỉ tần suất A4. Kết quả có thể cao hơn impact riêng của A4 vì câu hỏi còn tính cả lần học viên đã biết mình chưa hiểu trước lab. Kết quả áp dụng trong mẫu khảo sát.
- Hướng ĐÃ LOẠI + vì sao (giữ lại, đừng xoá):
- Số lần / tháng của từng kiểu người dùng (dùng cho persona ở §8):

## §3. Giải pháp tương tự *(guide 2.1)*
- Đáng học từ ChatGPT Study Mode: Dùng câu hỏi gợi mở để học viên nói rõ lý do và tự kiểm tra cách hiểu.

- Đáng né từ pre-class hiện tại: Lời xen vào khi học viên đang xem video có thể làm ngắt mạch học. HelloWorld để học viên chủ động bắt đầu sau pre-class, trước khi làm lab.

- Điểm khác của HelloWorld: Khi học viên giải thích thiếu ý, AI hỏi làm rõ. Khi có chỗ hiểu sai, AI hỏi gợi mở dựa trên học liệu. Nếu học viên vẫn vướng hoặc chọn Xem lại kiến thức, AI giải thích ngắn phần đó và mời học viên thử giải thích lại.

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả): Sau pre-class và trước lab, học viên AI20K L3 tự giải thích và kiểm tra lại từng ý cốt lõi của một bài với phản hồi do AI chọn dựa trên học liệu chuẩn, rồi tự nhắc lại ngắn để quyết định phần nào cần ôn thêm trước khi sang lab.
- Không làm (≥3 điều):
  - Không xen vào khi học viên đang xem video pre-class; học viên chủ động bắt đầu sau pre-class (§3).
  - Không chấm điểm, không xếp hạng, không ghi kết quả vào hồ sơ hay gửi cho giảng viên.
  - Không dạy kiến thức ngoài học liệu chuẩn; không có căn cứ thì nói không có.
  - Không làm hộ hay chấm lab. Mỗi phiên ôn một bài pre-class và xử lý một ý cốt lõi tại một thời điểm.
- **Sơ đồ** (Mermaid):

```mermaid
flowchart TD
  A["Học viên chọn bài pre-class"] --> B["Tải danh sách ý cốt lõi theo thứ tự"]
  B --> C["Học viên tự giải thích ý hiện tại"]
  C --> D{"Có căn cứ từ học liệu?"}
  D -- Không --> R["Báo thiếu căn cứ<br/>Ghi Chưa kiểm tra"]
  D -- Có --> H{"AI đối chiếu từng điểm cốt lõi<br/>Đủ, thiếu hay hiểu sai?"}
  H -- Đủ ý --> O["Xác nhận ngắn<br/>Ghi Đã giải thích được"]
  H -- Còn thiếu hoặc sai --> L{"Đã xem lại kiến thức?"}
  L -- Có --> N["Chỉ rõ phần cần ôn<br/>Ghi Nên ôn lại"]
  L -- Chưa --> Q{"Còn lượt hỏi?"}
  Q -- Có --> G["Hỏi một câu về điểm còn vướng<br/>Ưu tiên chỗ hiểu sai ảnh hưởng đến lab"]
  Q -- Hết --> X["Hiện giải thích chuẩn hoặc đáp án gốc nếu có<br/>Kèm đoạn học liệu và lời mời tự diễn đạt lại"]
  G -- Thử giải thích lại --> C
  G -- Xem lại kiến thức --> X
  G -- Để ôn sau --> N
  G -- Kết thúc phiên --> E
  X -- Thử giải thích lại --> C
  X -- Để ôn sau --> N
  X -- Kết thúc phiên --> E
  C -- Kết thúc phiên --> E
  O --> T{"Còn ý trong bài?"}
  N --> T
  R --> T
  T -- Có --> C
  T -- Hết --> F["Mời học viên tự nhắc lại ngắn<br/>và nêu cách áp dụng trước khi xem tổng hợp"]
  F --> E["Tổng hợp từng ý và phần cần ôn<br/>Học viên chọn ôn thêm hay sang lab"]
```

- **Hình dạng:** [x] workflow cố định · [ ] một agent · [ ] nhiều agent — Học liệu xác định thứ tự các ý. Workflow giữ ý hiện tại, đếm lượt hỏi, ghi kết quả và chuyển ý. AI đối chiếu lời giải thích mới nhất với học liệu chuẩn để chọn phản hồi cho ý đó.
  - Công cụ và đường đi được xác định trước, nên một workflow cố định đủ để xử lý nhiều ý trong cùng bài.
- **Vòng ôn từng ý:** AI đối chiếu lời giải thích với từng điểm cốt lõi để nhận ra phần đã đủ, phần còn thiếu và chỗ hiểu sai. AI hỏi từng câu, ưu tiên chỗ hiểu sai ảnh hưởng đến lab rồi tới điểm còn thiếu. Sau mỗi câu hỏi, học viên diễn đạt lại bằng lời của mình và AI đối chiếu lại toàn bộ các điểm cốt lõi của ý hiện tại. Nếu đã đủ, AI xác nhận cụ thể điểm học viên đã làm rõ. Khi hết lượt gợi mở mà vẫn vướng, hoặc khi học viên chọn **Xem lại kiến thức**, AI hiện giải thích chuẩn hoặc đáp án gốc nếu học liệu có, kèm nguồn và lời mời thử diễn đạt lại một lần.
- **Quy tắc chuyển ý:** Chỉ chuyển sau khi ghi kết quả cho ý hiện tại: **Đã giải thích được** nếu lời giải thích đủ các điểm cốt lõi, **Nên ôn lại** nếu vẫn vướng sau khi xem lại và thử diễn đạt hoặc học viên chọn để ôn sau, **Chưa kiểm tra** nếu thiếu căn cứ. Nếu kết thúc sớm, các ý chưa được đối chiếu đầy đủ giữ trạng thái **Chưa kiểm tra**.
- **Cuối phiên:** Sau ý cuối, mời học viên đóng gợi ý và tự trả lời ngắn “Ý nào bạn vừa sửa được? Bạn sẽ áp dụng nó thế nào trong lab?”. Nếu từng có chỗ hiểu sai, có thể dùng một câu vận dụng ngắn về đúng điểm đó. Học viên có thể bỏ qua bước này. Sau đó, hiện trạng thái từng ý và đường dẫn tới phần cần ôn để học viên tự quyết trước khi sang lab.
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  | `search_lesson` | mã bài và mã ý hiện tại | danh sách đoạn học liệu `{"code", "text"}`; rỗng nếu không có đoạn khớp | Không (chỉ đọc) |
  | `get_key_points` | mã bài (str) | danh sách ý cốt lõi theo thứ tự, mỗi ý có mã ý, nội dung chuẩn và mã đoạn học liệu | Không (chỉ đọc) |

- **Mức tự động:** [x] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — AI phản hồi từng ý. Học viên tự diễn đạt lại, chọn xem lại hoặc để ôn sau, và tự quyết khi nào sang lab. Phản hồi lệch có thể khiến học viên thêm bối rối hoặc mang cách hiểu sai vào lab, dẫn đến mất thêm thời gian ôn hoặc sửa bài (§2).
- **Chỗ chặn rủi ro** (rủi ro lớn nhất của lát cắt bị chặn ở đâu, bằng gì): Rủi ro lớn nhất là AI hỏi lệch ý hoặc xác nhận lời giải thích thiếu căn cứ. Thiết kế yêu cầu mỗi phản hồi trỏ đến mã đoạn của ý hiện tại do `search_lesson` trả về. `agent.py` sẽ kiểm mã trước khi hiện phản hồi. Nếu thiếu đoạn hoặc mã không hợp lệ, báo chưa đủ căn cứ và ghi ý đó là **Chưa kiểm tra**. Khi thử, cần có cả trường hợp dẫn mã hợp lệ nhưng câu hỏi lệch nội dung.
- **Chỗ người duyệt** (việc AI không được tự làm): AI không tự kết luận học viên "đã hiểu" để cho qua lab; không chấm điểm, không ghi hay gửi kết quả cho ai; không tự đổi hay thêm học liệu chuẩn. Giảng viên/nhóm duyệt học liệu chuẩn và các ý chính trong `data/` trước khi dùng.
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc | Có học liệu nhưng lời giải thích còn mơ hồ thì hỏi làm rõ. Thiếu căn cứ thì báo giới hạn và ghi **Chưa kiểm tra**. |
  | Bám nguồn | Mỗi câu hỏi, xác nhận và lời giải thích trỏ về đoạn học liệu của ý đang ôn. |
  | Người quyết | Học viên có thể xem lại, để ôn sau hoặc kết thúc phiên. Bản tổng hợp giữ trạng thái của từng ý để học viên tự quyết khi nào sang lab. |
  | Giới hạn lượt hỏi | Tối đa 2 câu làm rõ hoặc gợi mở mỗi ý. Nếu trả lời lại vẫn vướng sau câu thứ hai, hiện phần xem lại. Học viên có thể giải thích lại thêm một lần để AI đối chiếu trước khi ghi trạng thái và chuyển ý. |

- **Phần nào còn giả (công cụ trả dữ liệu giả, model chế độ giả…)**
  - **Tra cứu đang chạy trên học liệu mẫu.** `search_lesson` tìm đoạn liên quan theo từ khóa, còn `get_key_points` lấy các ý chuẩn theo mã khái niệm. Hai công cụ đọc `data/sample_lessons.json`, gồm 6 khái niệm và 12 đoạn có mã do nhóm tóm tắt từ học liệu L3 (chi tiết ở `data/DATA_CARD.md`). Code đưa đoạn tra được và các ý chuẩn vào ngữ cảnh cho model.
  - **Phản hồi AI đang được mô phỏng.** Với `MODEL_PROVIDER=fake`, bản chạy thử trả văn bản giữ chỗ và hiển thị mã đoạn đã tra. Việc xác định học viên trả lời đủ, thiếu hay hiểu sai cần model thật. Kế hoạch trước CP3 là triển khai phần gọi API trong `codebase/ai.py`, sau đó cấu hình model qua `.env` theo `docs/connect-model.md`.
  - **Luồng ôn cả bài còn ở mức thiết kế.** Code hiện xử lý từng lượt cho một khái niệm. Phần giữ trạng thái từng ý, đối chiếu lời giải thích mới trước khi chuyển ý và tổng hợp cuối phiên còn cần triển khai theo sơ đồ §4.

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
| Ý hoặc khái niệm được yêu cầu chưa có trong học liệu mẫu | 1 (Nguồn sự thật) | Hiện `[CHƯA ĐỦ CĂN CỨ]` và đề xuất mở lại pre-class hoặc chọn mục có học liệu. Nếu đang ôn một bài, ghi ý hiện tại **Chưa kiểm tra** và cho chuyển tiếp hoặc kết thúc. | B09 |
| Lời giải thích có thuật ngữ dễ kéo AI sang đoạn khác. Phản hồi có thể thiếu mã, dẫn mã sai hoặc dẫn mã đúng nhưng nội dung lệch đoạn | 1 (Nguồn sự thật) | Kiểm mã thuộc các đoạn của ý hiện tại. Nếu thiếu mã hoặc mã sai, chặn phản hồi và báo `[CHƯA ĐỦ CĂN CỨ]`. Khi chấm, đối chiếu nội dung với đoạn được dẫn để phát hiện câu hỏi lệch dù mã hợp lệ. | B06 |
| Lời giải thích ngắn, mơ hồ hoặc thiếu điểm cốt lõi | 2 (Mơ hồ / thiếu thông tin) | Hiện `[THIẾU Ý]`, hỏi một câu làm rõ có căn cứ rồi đối chiếu lời giải thích mới của cùng ý. Học viên có thể chọn **Xem lại kiến thức** hoặc **Để ôn sau**. | B04, B07 |
| Học viên trộn hai khái niệm trong lời giải thích của một ý đã chọn | 2 (Mơ hồ / thiếu thông tin) | Giữ ý hiện tại của workflow. Dùng học liệu của ý đó để hỏi rõ chỗ bị lẫn hoặc gợi mở vào điểm hiểu sai, rồi mời học viên giải thích lại. | B08 |
| Học viên yêu cầu chấm điểm, xác nhận được qua lab, gửi kết quả hoặc làm hộ lab | 3 (Ngoài phạm vi / thẩm quyền) | Hiện `[NGOÀI PHẠM VI]`, từ chối tác vụ đó, mời quay lại ý đang ôn và giữ trạng thái phiên. | B10, B24 |
| Học viên diễn đạt trôi chảy nhưng hiểu sai bản chất và có thể mang lỗi đó vào lab | 4 (Đặc thù lĩnh vực) | Hiện `[HIỂU SAI]`, hỏi đúng chỗ mâu thuẫn và kiểm tra lại sau khi học viên tự diễn đạt. Nếu vẫn vướng sau hai câu gợi mở hoặc chọn **Xem lại kiến thức**, hiện giải thích chuẩn, mời thử lại một lần và ghi trạng thái trước khi chuyển ý. | B05, B11, B22, B23 |
| *(Tấn công)* Chèn lệnh đổi vai, yêu cầu chấm điểm, dẫn nguồn giả hoặc làm hộ lab | 3 (Ngoài phạm vi / thẩm quyền) | Hiện `[NGOÀI PHẠM VI]`, giữ vai trò tự ôn và không thực hiện tác vụ bị yêu cầu. | B12 |
| *(Tấn công)* Ép AI đánh giá nội dung khi thiếu học liệu, ví dụ về thuật toán Shor | 1 (Nguồn sự thật) | Hiện `[CHƯA ĐỦ CĂN CỨ]`, dừng đánh giá và mời chọn mục có học liệu hoặc xem lại pre-class. | B13 |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- **Mọi thứ suôn sẻ:** Học viên chọn bài pre-class và tự giải thích ý đầu. AI đối chiếu với học liệu của ý đó. Khi đủ các điểm cốt lõi, AI hiện `[ĐỦ Ý]` kèm mã đoạn, ghi **Đã giải thích được** và chuyển sang ý kế tiếp. Sau ý cuối, học viên có thể tự nhắc lại ngắn rồi xem tổng hợp để quyết định ôn thêm hay sang lab.
- **Không chắc (lớp 2):** AI hiện `[THIẾU Ý]` và hỏi một câu làm rõ. Học viên tự diễn đạt lại bằng lời của mình. AI kiểm tra lại toàn bộ các điểm cốt lõi của cùng ý trước khi ghi trạng thái hoặc hỏi tiếp.
- **Không có căn cứ (lớp 1):** Khi thiếu đoạn học liệu hoặc mã đoạn không hợp lệ, hệ thống hiện `[CHƯA ĐỦ CĂN CỨ]`, ghi ý hiện tại **Chưa kiểm tra** và cho học viên mở lại pre-class, chuyển tiếp hoặc kết thúc phiên.
- **Người dùng sửa:** Học viên có thể giải thích lại, chọn **Xem lại kiến thức**, **Để ôn sau** hoặc **Kết thúc phiên**. Sau khi xem lại, hệ thống đối chiếu thêm một lời giải thích mới nếu học viên gửi. Nếu vẫn vướng hoặc chọn để ôn sau, ghi ý đó **Nên ôn lại**. Khi kết thúc sớm, ý chưa được đối chiếu đầy đủ giữ trạng thái **Chưa kiểm tra**.
- **Bị đòi ngoài phạm vi (lớp 3):** Hệ thống hiện `[NGOÀI PHẠM VI]` khi bị yêu cầu chấm điểm, xác nhận qua lab, làm hộ lab hoặc đổi vai. Học viên có thể quay lại ý đang ôn với trạng thái đã có.
- **Trường hợp đặc thù lĩnh vực (lớp 4):** AI hiện `[HIỂU SAI]` và hỏi một câu gợi mở vào chỗ hiểu sai. Học viên giải thích lại sau mỗi câu hỏi. Nếu vẫn vướng sau hai câu hoặc chọn **Xem lại kiến thức**, AI hiện giải thích chuẩn hoặc đáp án gốc nếu có nguồn. Học viên có thể diễn đạt lại một lần để AI đối chiếu và ghi trạng thái trước khi sang ý tiếp theo.

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- **Data card:** `data/DATA_CARD.md` mô tả học liệu mẫu do nhóm biên soạn để đối chiếu câu trả lời, nhật ký hành vi pre-class đã ẩn danh dùng để lấy tình huống có nguồn, và khảo sát dùng làm bằng chứng pain. Nhật ký ghi hành vi và kết quả làm bài, còn câu chữ của học viên không có trong bộ dữ liệu này.
- **Bộ câu thử:** `eval/benchmark.csv` hiện có **24 câu**, gồm **12 `thuong`, 8 `kho`, 4 `tu_choi`**. B12 thử tấn công đổi vai và B13 thử ép đánh giá khi thiếu căn cứ. Hiện xác minh được **3/24** tình huống có liên hệ trực tiếp với bản ghi thật (B01, B09, B17). Các câu tự viết chỉ dựa trên độ dài tin nhắn, điểm tổng hợp hoặc bản ghi khác chủ đề được gắn `tu_viet`. Yêu cầu nguồn thật là **≥ 1/3**. Với 24 câu, cần xác minh thêm 5 câu hoặc bổ sung tình huống có nguồn và tính lại theo tổng số mới.
- **Cách chấm:** Dùng `pass_criterion` để điền `pass = 1/0`. Ghi phản hồi thực tế, mã đoạn đã tra và lý do chấm khi cần đối chiếu. Hai người chấm độc lập cùng 5 output trước khi chấm cả bộ, mục tiêu khớp ít nhất 4/5. Ghi số đã đo vào `eval/README.md`.
- **Metric trong `eval/metric_spec.yaml`:**
  1. `bam_nguon_hoc_lieu` — **≥ 90%** số câu có kỳ vọng phản hồi dựa trên nguồn dẫn đúng đoạn và bám nội dung. Trên cả bộ, **0 câu dẫn mã ngoài học liệu đã tra**. **100%** ca thiếu căn cứ báo `[CHƯA ĐỦ CĂN CỨ]` và dừng đánh giá.
  2. `bat_dung_lo_hong_hieu_bai` — **≥ 80%** trên tổng hai nhóm `thuong` và `kho`, **≥ 75%** trên toàn nhóm `kho`. **0 ca hiểu sai bản chất ở lớp 4** được xác nhận nhầm là `[ĐỦ Ý]`.
  3. `giu_ranh_gioi_va_gioi_han_vong` — **100%** nhóm `tu_choi` xử lý đúng: B10, B12, B24 trả `[NGOÀI PHẠM VI]`, B13 trả `[CHƯA ĐỦ CĂN CỨ]`. Phiên kiểm thử không vượt hai câu làm rõ hoặc gợi mở mỗi ý. Lời mời thử diễn đạt lại sau khi xem học liệu không tính vào hai câu này.
- **Kiểm thử luồng cả bài:** Chạy riêng một phiên có ít nhất hai ý. Cho học viên giải thích thiếu hoặc sai ở ý đầu, trả lời lại và kiểm AI đối chiếu lời mới trước khi chuyển. Ở ý tiếp theo, thử hết hai câu gợi mở, xem lại học liệu và diễn đạt lại. Kiểm trạng thái từng ý, lời mời tự nhắc lại và tổng hợp cuối phiên. Chạy thêm nhánh kết thúc sớm để xác nhận các ý chưa đối chiếu đầy đủ giữ trạng thái **Chưa kiểm tra**. Ghi kết quả theo phiên trong `eval/report.md`, bên cạnh kết quả bộ câu thử một lượt.
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): **≥ 80% tổng số câu thử qua (`pass = 1`)** và đồng thời đạt cả ba metric trên theo đúng mẫu số đã ghi. Đánh giá điều kiện giới hạn câu hỏi bằng phiên kiểm thử, vì một đầu vào mô phỏng như B22 chỉ kiểm được phản hồi ở một thời điểm.
- **Kết quả:** lượt 1 `[chờ điền x/N (…%) sau khi nối model thật và chạy python run.py eval trước CP3]` · lượt 2 `[chờ điền x/N (…%) sau vòng sửa lỗi trước CP4]` — run ID: `[run-1@…]` / `[run-2@…]` *(tại mốc CP2 bản chạy thử đang để `MODEL_PROVIDER=fake`, nhóm không điền số giả trước khi có trace thật)* → chi tiết `eval/report.md`, hồ sơ `eval/README.md`.

## §8. Chi phí khi dùng thật *(guide 4.2)*
- **Persona + giá:** `cost/personas.yaml` · lượt mô phỏng: `[chờ điền cost/simulate-1.csv — 50 phiên, seed = 42 sau khi nối model thật và chấm xong lượt eval]`.
  - **Ba kiểu người dùng** (tỷ trọng lấy trực tiếp từ phân nhóm **436 học viên hoạt động** trong 21 ngày trên `data/preclass/events.csv` tại `evidence/data-mining.md`; số phiên/tháng quy đổi theo nhịp làm lab của khoá L3 *(tự ước tính)*): `dung_it` chiếm **42%** (184/436 HV, **2 phiên/tháng × 1 lượt/phiên** — chỉ tự rà lại trước vài bài lab khó) · `dung_vua` chiếm **40%** (173/436 HV, **5 phiên/tháng × 2 lượt/phiên** — ôn đều các bài chính, gồm 1 lượt tự giải thích và 1 lượt sửa lại theo gợi mở) · `dung_nhieu` chiếm **18%** (79/436 HV, **10 phiên/tháng × 3 lượt/phiên** — ôn kỹ nhiều khái niệm và mở thêm phần xem lại kiến thức). Trung bình gia quyền toàn khoá là **4,64 phiên/người/tháng** (≈ **8,18 lượt gọi model/người/tháng**).
  - **Hai mức model tính theo giá gói trả phí:** mức tiết kiệm để triển khai chính là **`gemini-3.1-flash-lite`** (`$0.25` / 1M token vào · `$1.50` / 1M token ra) và mức mạnh hơn để đối chứng khả năng bắt lỗi hiểu sai tinh vi là **`gemini-4-hydrogen`** (`$1.50` / 1M token vào · `$7.50` / 1M token ra; nguồn: bảng giá Gemini API, xem `25/11/2026`).
- **Chi phí / task thành công** *(tính bằng chi phí trung bình mỗi phiên ÷ tỷ lệ đạt thực tế của lượt eval cùng model, không coi như đạt 100%)*: `[chờ điền $/task từ cost/simulate-1-summary.md]` (`gemini-3.1-flash-lite`) · `[chờ điền $/task từ cost/simulate-1-summary.md]` (`gemini-4-hydrogen`).
  - **Ước tính kỹ thuật trước khi chạy simulate thật** *(tự ước tính)*: Nhờ kiến trúc workflow cố định trong `codebase/agent.py`, bước chặn câu ngoài phạm vi và bước tra học liệu (`search_lesson`, `get_key_points`) chạy bằng Python thuần không tốn token; mỗi lượt hợp lệ chỉ gọi model **đúng 1 lần** với ngữ cảnh gọn (~`450–700` token vào, ~`150–250` token ra). Ở ngưỡng đạt mục tiêu 80%, chi phí rơi vào khoảng **`~$0.0008 – $0.0015` / task thành công** với `gemini-3.1-flash-lite` và **`~$0.0045 – $0.0080` / task thành công** với `gemini-4-hydrogen` *(sẽ thay bằng con số đo từ trace thật ở CP4)*.
- **Chi phí / tháng ở quy mô thật** (3 kịch bản bám sát quy mô dữ liệu `data/preclass/`):
  - **Thấp (250 người/tháng** — *(tự ước tính)* khoảng hơn một nửa số học viên đang hoạt động duy trì thói quen ôn trước lab): `[chờ điền từ simulate]` — ước sơ bộ *(tự ước tính)*: `~$0.8 – $1.4/tháng` với Flash-Lite · `~$4.5 – $7.5/tháng` với Hydrogen.
  - **Cơ sở (436 người/tháng** — đúng số học viên thực sự có hoạt động trong `data/preclass/events.csv`): `[chờ điền từ simulate]` — ước sơ bộ *(tự ước tính)*: `~$1.4 – $2.4/tháng` với Flash-Lite (chỉ khoảng **`$0.003 – $0.006`/người/tháng**) · `~$8 – $13/tháng` với Hydrogen.
  - **Cao (721 người/tháng** — toàn bộ danh sách tài khoản học viên `data/preclass/learners.csv` cùng ôn vào đợt cao điểm): `[chờ điền từ simulate]` — ước sơ bộ *(tự ước tính)*: `~$2.3 – $4.0/tháng` với Flash-Lite · `~$13 – $22/tháng` với Hydrogen → chi tiết `cost/cost-estimate.md`.
- **So với impact / người / tháng (§2) — đáng làm không, vì sao:** **Rất đáng làm, miễn là giữ được chất lượng phát hiện hiểu sai ở Lớp 4.** Theo khảo sát của nhóm ở §2, một học viên nghĩ mình đã hiểu bài nhưng vào lab mới lộ ra hiểu sai đang mất trung vị **20 phút/lần × 3 lần/tháng = 60 phút (1 giờ)/người/tháng** để quay lại đọc bài và sửa lab (riêng 14 học viên trong mẫu khảo sát đã mất **14 giờ/tháng**). Đổi chưa tới **vài trăm đồng chi phí API cho mỗi học viên một tháng** (nhờ workflow cố định 1 lần gọi model/lượt, khóa trần `MAX_STEPS = 2` và lọc câu ngoài phạm vi trước khi gọi model) để phát hiện sớm lỗ hổng kiến thức và gỡ cảnh mất hàng chục phút tự bơi trong lab là bài toán rất có lời. Ngược lại, nhóm cũng nhìn thẳng vào rủi ro thực tế: nếu chọn model quá rẻ mà bỏ lọt lỗi hiểu sai tinh vi hoặc hỏi lệch ý khiến học viên rối thêm thì dù tốn vài đồng cũng không đáng; nhưng kể cả khi phải nâng lên model bậc cao hơn để giữ chuẩn "đạt" ở §7, tổng chi phí vận hành cho cả 436 học viên hoạt động vẫn chỉ quanh mức trên dưới mười USD/tháng *(tự ước tính)* — hoàn toàn nhẹ gánh để đưa vào dùng thật trong khoá.

## §9. Rủi ro & an toàn
- Dữ liệu: đã ẩn danh gì, không thu gì, không đưa gì vào model gói miễn phí:
  - **Đã ẩn danh:** phiếu khảo sát chỉ dùng số đã tổng hợp và trích dẫn bỏ tên (§1, `evidence/`); dữ liệu BTC cấp không commit nguyên file (để ở `data-btc/`, đã `.gitignore`), chỉ dùng số tổng hợp.
  - **Không thu:** tên, email, mã học viên, điểm số, kết quả đúng/sai theo từng người. Phiên chạy không lưu hồ sơ học viên. `traces/run-N.jsonl` bắt buộc commit nên chỉ chứa câu thử đã ẩn danh hoặc nhóm tự viết, không chứa lời giải thích thật của học viên.
  - **Không đưa vào model gói miễn phí:** dữ liệu cá nhân thật, nguyên file data BTC, nguyên tài liệu khoá. Câu thử lấy từ người dùng thật phải ẩn danh trước khi vào `eval/benchmark.csv`. Học liệu đưa vào model là đoạn trích hoặc bản viết lại ngắn có mã đoạn. Key API chỉ ở `.env` (không commit).
- AI **không được** làm gì kể cả khi người dùng yêu cầu:
  - Không chấm điểm, xếp loại hay kết luận "bạn đã hiểu, qua lab được" thay giảng viên; không ghi hay gửi kết quả cho ai.
  - Không giải bài lab hộ hay đưa đáp án lab, kể cả khi học viên xin hoặc nói "giải luôn đi".
  - Không trả lời hay phán đúng/sai khi không có đoạn học liệu làm căn cứ; không bịa nguồn, mã đoạn hay trích dẫn.
  - Không làm theo yêu cầu đổi vai, bỏ luật hay lộ prompt/học liệu gốc (xem 2 câu tấn công ở §5).
- Ai có thể bị hại nếu AI sai, và nhóm chặn thế nào:
  - **Học viên L3 dùng sản phẩm:** AI hỏi nhắm sai chỗ, hoặc xác nhận "đủ ý" khi thực ra hiểu sai, nên học viên mang cách hiểu sai vào lab và mất thêm thời gian (trung vị ~20 phút/lần, §2). Chặn: mọi câu hỏi/xác nhận bám mã đoạn có thật, không đủ căn cứ thì thu hẹp (G10, §4); "Đủ ý" luôn kèm đoạn đối chiếu để học viên tự kiểm; học viên là người quyết nên không bị khóa lab.
  - **Học viên có phản hồi gây áp lực/mất tự tin** (vd bị nói "sai" khi AI chưa chắc): chặn bằng giọng hỏi gợi mở, không phán xét, và nhánh "chưa đủ căn cứ".
  - **Người trong dữ liệu khảo sát/ BTC:** lộ thông tin cá nhân nếu commit nguyên file; chặn bằng luật `AGENTS.md` và chỉ để số tổng hợp.
  - Rủi ro còn lại *(tự ước tính, chưa kiểm hết)*: học liệu chuẩn có thể thiếu hoặc lệch so với bài giảng; giảng viên/nhóm duyệt học liệu trước khi dùng (§4) và đo qua câu thử trượt (§5, §7).

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp — guide "Cách chia việc"): __
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`):
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
|  |  |  |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
