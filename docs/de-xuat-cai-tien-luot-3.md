# Cải tiến thứ hai: phản hồi đối chiếu dạng JSON có kiểm tra (lượt 3)

> **Trạng thái:** PR #2 đã thay luồng đối chiếu trên `main` bằng phiên dạy lại (`codebase/teachback.py`). Ở luồng đó, model chỉ chấm từng ý bằng JSON, còn câu hỏi lấy sẵn từ học liệu. Vì vậy thay đổi 1 và 2 dưới đây (trong `codebase/agent.py`) **không được gộp vào `main`**. Khi gỡ xung đột, nhóm giữ `agent.py` của `main`. Trên `main` chỉ còn thay đổi 3 (`temperature` trong `codebase/ai.py`), kết quả `run-3` và tài liệu này. `run-3` đo trên luồng cũ (commit `ed0ee3e`), trước khi chuyển sang teachback, nên chỉ dùng để so với `run-1` và `run-2`, không đại diện cho luồng hiện tại.

Lượt 2 vẫn đạt 26/30 như lượt 1. Prompt mới sửa được `B06`, `B23` nhưng làm trượt `B05`, `B11`, còn `B03`, `B08` trượt ở cả hai lượt. [Kết quả lượt 2](../eval/run-2.csv) · [Cải tiến thứ nhất](de-xuat-cai-tien-goi-mo-luot-2.md)

## Vì sao lần sửa prompt trước chưa tăng điểm

Ở lượt 2, model vừa chẩn đoán chỗ sai vừa tự viết cả phản hồi bằng văn bản tự do. Mỗi lần chạy, nó lệch theo một kiểu khác nhau:

| Câu | Kiểu lệch ở lượt 2 |
|---|---|
| `B03` | Đủ ý nhưng chỉ có 2 câu, tiêu chí yêu cầu 3–5 câu |
| `B05` | Câu hỏi chung chung, không chạm vào chỗ hiểu nhầm "cập nhật trọng số" |
| `B08` | Hỏi gộp hai vế (truy xuất và trọng số), không hỏi vào chỗ lẫn với gửi email / sửa dữ liệu |
| `B11` | Giải thích sẵn cách lấy mẫu và độ đa dạng rồi mới hỏi lại |

Thêm quy tắc vào prompt chỉ đẩy lỗi từ câu này sang câu khác. Ngoài ra, `call_openai` trong `codebase/ai.py` không gửi `temperature` (trong khi `call_gemini` và `call_claude` đặt 0.2), nên output của `cx/gpt-6-luna` dao động giữa các lần chạy. Đây có thể là một phần lý do `B05` và `B11` đang đạt lại trượt.

## Ba thay đổi

### 1. Model trả JSON, code kiểm và tự ghép phản hồi (`codebase/agent.py`)

Ở chế độ đối chiếu (gồm cả phiên ôn trên `python run.py` và UI web), model chỉ trả một đối tượng JSON:

```json
{
  "label": "ĐỦ Ý | THIẾU Ý | HIỂU SAI | NGOÀI PHẠM VI | CHƯA ĐỦ CĂN CỨ",
  "codes": ["mã đoạn hỗ trợ"],
  "learner_claim": "cụm trích nguyên văn trong lời học viên cần xem lại",
  "question": "đúng một câu hỏi mở",
  "confirm": "1–2 câu xác nhận (chỉ khi ĐỦ Ý)"
}
```

Code kiểm từng trường trước khi hiện cho học viên:

| Kiểm tra | Chặn kiểu lỗi |
|---|---|
| `codes` không rỗng và chỉ gồm mã đã tra được (chấp nhận cả dạng `[D03-P03]` hay `D03-P01, D03-P02`) | Bịa mã, dẫn mã ngoài ý đang ôn |
| `learner_claim` phải là cụm có thật trong lời học viên (so sau khi bỏ dấu, dấu câu) | Hỏi chung chung, không bám chỗ sai (`B05`) |
| `question` có đúng một dấu `?` và kết thúc bằng `?` | Hỏi nhiều câu một lúc (`B08`) |
| `question` không chứa "thực chất", "thực ra", "chứ không", "nghĩa là" | Nêu sẵn đáp án trong câu hỏi |
| `question` không kết thúc bằng "hay không", "đúng không", "phải không" | Câu hỏi có/không, không gợi mở |
| Nhánh `THIẾU Ý` / `HIỂU SAI` không có trường nào cho lời giải thích | Giải thích sẵn rồi mới hỏi (`B11`) |

Nếu JSON vi phạm, code gọi lại model **một lần** kèm danh sách lỗi. Vẫn sai thì chặn bằng `[CHƯA ĐỦ CĂN CỨ]`, giống cách nhóm đang chặn mã đoạn không hợp lệ (§4 chỗ chặn rủi ro). Lời giải thích chuẩn vẫn chỉ có ở nhánh **Xem lại kiến thức** và vòng cuối, hai nhánh này giữ dạng văn bản như cũ.

Phản hồi hiển thị do code ghép:

- `[HIỂU SAI] Hãy xem lại phát biểu: “<learner_claim>” [mã]. <question> Hãy diễn đạt lại bằng lời của bạn, hoặc chọn “Xem lại kiến thức”.`
- `[THIẾU Ý] Bạn đã nêu: “<learner_claim>” [mã]. <question> …` (cùng lời mời)

### 2. Nhánh `[ĐỦ Ý]` luôn đủ 3 câu (`codebase/agent.py`)

Code ghép: `<confirm của model>` + `Đoạn học liệu đối chiếu: [mã].` + `Bạn tự quyết định sang làm lab hay ôn thêm.` Nếu model tự thêm lời mời sang lab trong `confirm`, code bỏ câu đó để không lặp. Nhắm `B03`.

### 3. Đặt `temperature` thấp cho provider OpenAI-compatible (`codebase/ai.py`)

`call_openai` gửi `temperature: 0.2`, cùng mức với Gemini và Claude, để giảm dao động giữa các lần chạy. Model nào không nhận tham số này thì đặt `MODEL_TEMPERATURE=` (để trống) trong `.env`. Proxy `cx/gpt-6-luna` đã nhận tham số khi chạy lượt 3.

## Không làm (và vì sao)

- **Không thêm danh sách "hiểu sai thường gặp" vào `data/sample_lessons.json`.** Danh sách đó sẽ gần như trùng bộ câu thử, và học liệu phải được giảng viên duyệt (§4).
- **Không đưa câu của bộ thử vào prompt làm ví dụ** (luật "không giấu câu thử vào code" trong `AGENTS.md`).
- **Không gọi thêm một lần model để tự chấm câu hỏi.** Cách này tốn gấp đôi token và độ trễ. Để dành nếu kiểm bằng code chưa đủ.
- **Không sửa `eval/benchmark.csv`, `eval/metric_spec.yaml`, chuẩn "đạt" §7, hay `run-1` / `run-2`.**

## Đo thế nào

Chạy `python run.py eval` (trên Windows nên dùng `py`) với cùng model `cx/gpt-6-luna`, đủ 30 câu, cùng `pass_criterion`. Kết quả: `run-3@20261128-114412`, 30/30 câu, 0 lỗi kỹ thuật, ghi ở [`eval/run-3.csv`](../eval/run-3.csv) và [`traces/run-3.jsonl`](../traces/run-3.jsonl), commit `ed0ee3e` cùng code đã sinh ra nó.

Lần chạy thử với Gemini lúc gỡ lỗi chỉ dùng để sửa bộ kiểm, không tính vào kết quả.

## Kết quả sơ bộ (chờ chấm chính thức)

Cột `pass` của `run-3.csv` chưa điền. Bảng dưới là đối chiếu sơ bộ theo `pass_criterion`, người chấm chính thức có thể khác.

| Câu | Lượt 2 | Lượt 3 (sơ bộ) | Quan sát |
|---|:---:|:---:|---|
| `B03` | 0 | 1 | Đủ 3 câu, dẫn đúng mã |
| `B05` | 0 | 1 | Trích đúng "cập nhật trực tiếp trọng số", hỏi điều gì xảy ra với trọng số |
| `B08` | 0 | 1 | Hỏi RAG đang làm gì khi model gửi email và cập nhật database, không còn vế trọng số |
| `B11` | 0 | chưa rõ | Hết đoạn giải thích dài, nhưng câu hỏi vẫn mở đầu bằng "Nếu tăng temperature chỉ làm thay đổi cách lấy mẫu token…" |
| `B23` | 1 | chưa rõ | Hỏi về giới hạn dừng vòng lặp, chưa hỏi về bên điều khiển luồng |
| `B18` | 1 | 1 | Lượt 2 trả `[ĐỦ Ý]`, lượt 3 trả đúng `[THIẾU Ý]` và hỏi về bước người duyệt |

Nếu chấm như trên, lượt 3 đạt khoảng 28–29/30. Trace không có lần gọi lại nào vì JSON vi phạm, nên điểm tăng đến từ việc tách trường và prompt mới chứ không phải từ bước gọi lại.

## Đánh đổi

- **Độ trễ:** mỗi câu gọi model mất khoảng 4–10 giây, trước khoảng 5 giây.
- **Token:** token vào tăng khoảng 20% (prompt có thêm phần định dạng JSON). `cost/cost-estimate.md` cần tính lại nếu dùng bản này.
- **Câu trả lời đều khuôn hơn:** phản hồi gợi mở luôn có dạng "Hãy xem lại phát biểu: “…”". Dễ kiểm hơn nhưng kém tự nhiên hơn văn bản tự do.

## Còn lại

- Câu hỏi hai vế dạng "…như thế nào, và cần làm gì…?" vẫn lọt qua vì bộ kiểm chỉ đếm dấu `?` (`B04`, `B05`, `B06`). Các câu này vẫn trong ngưỡng đạt nhưng nên siết thêm.
- Lộ ý qua mệnh đề giả định "Nếu … chỉ …" (`B11`) chưa bị chặn. Có thể thêm "nếu … chỉ" vào danh sách cụm cần chặn, hoặc yêu cầu `question` không lặp lại nội dung của học liệu.
- Thay đổi ở `codebase/agent.py` và `codebase/ai.py` cần Nguyễn Duy Mạnh (người phụ trách phần này) xem trước khi gộp vào `main`. Kết quả chính thức cần chấm `run-3.csv`, chạy `python run.py score eval/run-3.csv`, rồi cập nhật `eval/report.md` và changelog §10 trong `spec.md`.
