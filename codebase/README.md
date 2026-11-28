# Giao diện web demo — Ôn trước lab

Giao diện web cho phiên học viên dạy lại, dùng khi demo live (trang 4 trong `slides/outline.md`). Luồng giống hệt `python run.py`: dùng nguyên `TeachbackSession` trong `teachback.py` và `call_model` trong `ai.py`, học liệu từ `data/teachback_lessons.json`. `web.py` chỉ thay lớp nhập/xuất dòng lệnh bằng trang web.

Học viên là người dạy. **AI người học** hỏi lại bằng câu hỏi có sẵn trong học liệu. **Giám khảo** ngầm chấm từng ý chuẩn và chỉ công bố kết quả khi học viên dạy đủ, hết 2 lượt gợi mở, hoặc chọn *Xem lại kiến thức*.

Chỉ dùng thư viện chuẩn của Python, không cần cài thêm gì.

## Chạy

Từ thư mục gốc repo:

```
python codebase/web.py
```

Mở http://localhost:8765 trên trình duyệt. Nhấn `Ctrl+C` trong cửa sổ lệnh để dừng.

- **Lỗi `CERTIFICATE_VERIFY_FAILED` khi gọi Gemini/OpenAI qua HTTPS:** thường do lệnh `python` đang trỏ tới Python của MSYS2, bản này không tin chứng chỉ của Windows. Chạy bằng Python cài từ python.org: `py codebase/web.py`.
- **Model thật:** đọc `.env` ở thư mục gốc, giống `run.py`. Không có `.env` thì tự chạy chế độ giả (`MODEL_PROVIDER=fake`).
- **Đổi cổng:** đặt biến môi trường `PORT`.
- **Thử giao diện không tốn token:** ép chế độ giả bằng `MODEL_PROVIDER=fake`. Biến môi trường được ưu tiên hơn `.env`. Ở chế độ giả, giám khảo không đối chiếu được (cần model thật), nên chỉ thử được *Xem lại kiến thức*, *Để ôn sau* và các màn hình.

```powershell
$env:MODEL_PROVIDER = "fake"; $env:PORT = "8766"; python codebase/web.py
```

## Dùng khi demo

| Thao tác | Cách làm |
|---|---|
| Chọn bài | Bấm một ngày (D01–D15) ở trang đầu. D02–D15 có 3 mục, D01 có 10 mục. |
| Dạy một mục | Trả lời câu hỏi của AI người học trong ô soạn, bấm mũi tên hoặc `Ctrl+Enter`. |
| Xem lại kiến thức | Nút trong ô soạn. Giám khảo công bố ý chuẩn, không gọi model. Sau đó được dạy lại một lần. |
| Để ôn sau | Ghi mục hiện tại là *Nên ôn lại* rồi sang mục tiếp theo. |
| Xem tham chiếu | Bấm mã mục (vd `D01-P52`) để xem mục đề cương và nguồn. Không hiện ý chuẩn. |
| Kết thúc phiên | Nút ở cuối sidebar. Mục chưa đối chiếu giữ trạng thái *Chưa kiểm tra*. |

Sau mục cuối, màn ôn đứng yên để đọc phản hồi. Bấm **Tự nhắc lại và xem tổng hợp** để sang bước cuối.

### Chế độ trình bày

Bật bằng công tắc ở cuối sidebar, phím `T`, hoặc mở `http://localhost:8765/?trinhbay=1`. Khi bật:

- Phía trên ô soạn hiện các câu thử có sẵn của mục đang ôn (`D01-P52`, `D01-P53`, `D03-P51`, `D08-P51`), cộng `B12` (tấn công đổi vai) và `B25` (khái niệm ngoài học liệu). Câu thử lấy nguyên văn từ `eval/benchmark.csv`. Bấm chỉ điền vào ô soạn, chưa gửi.
- Bên phải hiện khung **Bên trong mỗi lượt**: nhãn giám khảo chấm ngầm (kể cả khi chưa công bố cho học viên), công cụ đã gọi, model, độ trễ, token vào/ra và mã mục được dẫn.

Muốn mời người xem lên tự thao tác thì tắt công tắc. Phiên đang ôn vẫn giữ nguyên.

Gợi ý kịch bản demo 2 phút với bài D01 (bấm *Để ôn sau* ở mục 1 để tới *Chatbot và mô hình*):

1. `B17`: giải thích thiếu, AI người học hỏi lại; khung bên phải hiện giám khảo chấm *Thiếu ý*.
2. `B12`: tấn công đổi vai, bị chặn ngay, không gọi model.
3. `B01`: giải thích đủ, giám khảo công bố **Đủ ý** từng ý, tự chuyển sang *Sinh văn bản và Temperature*.
4. `B11`: hiểu sai Temperature, AI người học hỏi lại; giám khảo chấm *Hiểu sai* nhưng chưa công bố.

Độ trễ mỗi lượt gọi model thật (đo ngày 28/11): khoảng 5–6 giây với `cx/gpt-6-luna` qua proxy cục bộ, khoảng 1–1,5 giây với `gemini-3.5-flash-lite` gọi thẳng API.

## Giới hạn

- Server chạy một luồng và giữ **một phiên** trong bộ nhớ. Đủ cho demo trên một máy, không dùng cho nhiều người cùng lúc.
- Tải lại trang vẫn giữ phiên trên server, nhưng lịch sử hội thoại trên trang bị xoá.
- Lời giải thích của học viên không ghi ra file và không in ra cửa sổ lệnh. Bấm *Ôn bài khác* hoặc dừng server là trạng thái phiên bị xoá (`spec.md` §9).
- Font tải từ Google Fonts. Máy demo mất mạng thì trình duyệt dùng font hệ thống.

## File

| File | Vai trò |
|---|---|
| `codebase/web.py` | Server `http.server`: trả trang và API JSON (`/api/bootstrap`, `/api/start`, `/api/send`, `/api/review`, `/api/defer`, `/api/finish`, `/api/recall`, `/api/reset`). |
| `codebase/web/index.html` | Toàn bộ giao diện (HTML, CSS, JS trong một file). |
