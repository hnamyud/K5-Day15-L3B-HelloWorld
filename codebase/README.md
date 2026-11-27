# Giao diện web demo — Ôn trước lab

Giao diện web cho phiên tự ôn, dùng khi demo live (trang 4 trong `slides/outline.md`). Luồng ôn giống hệt `python run.py`: dùng nguyên `StudySession` trong `session.py` và `answer` trong `agent.py`. `web.py` chỉ thay lớp nhập/xuất dòng lệnh bằng trang web.

Chỉ dùng thư viện chuẩn của Python, không cần cài thêm gì.

## Chạy

Từ thư mục gốc repo:

```
python codebase/web.py
```

Mở http://localhost:8765 trên trình duyệt. Nhấn `Ctrl+C` trong cửa sổ lệnh để dừng.

- **Model thật:** đọc `.env` ở thư mục gốc, giống `run.py`. Không có `.env` thì tự chạy chế độ giả (`MODEL_PROVIDER=fake`).
- **Đổi cổng:** đặt biến môi trường `PORT`.
- **Thử giao diện không tốn token:** ép chế độ giả bằng `MODEL_PROVIDER=fake`. Biến môi trường được ưu tiên hơn `.env`.

```powershell
$env:MODEL_PROVIDER = "fake"; $env:PORT = "8766"; python codebase/web.py
```

## Dùng khi demo

| Thao tác | Cách làm |
|---|---|
| Chọn bài | Bấm một bài ở trang đầu. D01 có 2 ý, hợp để demo luồng nhiều ý. |
| Giải thích một ý | Gõ vào ô soạn, bấm mũi tên hoặc `Ctrl+Enter`. |
| Xem lại kiến thức | Nút trong ô soạn. Mỗi ý xem lại được một lần, không gọi model. |
| Để ôn sau | Ghi ý hiện tại là *Nên ôn lại* rồi sang ý tiếp theo. |
| Xem đoạn học liệu | Bấm mã đoạn (vd `D01-P04`) trong phản hồi. |
| Kết thúc phiên | Nút ở cuối sidebar. Ý chưa đối chiếu giữ trạng thái *Chưa kiểm tra*. |

Sau ý cuối, màn ôn đứng yên để đọc phản hồi. Bấm **Tự nhắc lại và xem tổng hợp** để sang bước cuối.

### Chế độ trình bày

Bật bằng công tắc ở cuối sidebar, phím `T`, hoặc mở `http://localhost:8765/?trinhbay=1`. Khi bật:

- Phía trên ô soạn hiện các câu thử có sẵn của ý đang ôn, cộng `B12` (tấn công đổi vai) và `B25` (khái niệm ngoài học liệu). Câu thử lấy nguyên văn từ `eval/benchmark.csv`. Bấm chỉ điền vào ô soạn, chưa gửi.
- Bên phải hiện khung **Bên trong mỗi lượt**: công cụ đã gọi, model, độ trễ, token vào/ra, mã đoạn được dẫn có thuộc ý đang ôn hay không, và ghi chú của agent (vd chặn lớp 3).

Muốn mời người xem lên tự thao tác thì tắt công tắc. Phiên đang ôn vẫn giữ nguyên.

Gợi ý kịch bản demo 2 phút với bài D01:

1. `B17`: giải thích thiếu, AI trả **Thiếu ý** kèm câu hỏi làm rõ.
2. `B12`: tấn công đổi vai, bị chặn **Ngoài phạm vi**, 0 token.
3. `B01`: giải thích đủ, AI trả **Đủ ý**, tự chuyển sang ý Temperature.
4. `B11`: hiểu sai Temperature, AI trả **Hiểu sai** kèm câu hỏi gợi mở.

Mỗi lượt gọi model thật mất khoảng 6 giây (đo với `cx/gpt-6-luna`).

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
