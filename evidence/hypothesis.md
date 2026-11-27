# Giả thuyết — viết TRƯỚC khi tìm bằng chứng (5 phút, commit ngay)

> Điền ở guide bước 1.1. Ôn lại: ngày 2 · lab ngày 2.
> Viết **trước** khi đọc dòng data đầu tiên hay hỏi người đầu tiên, để không sửa cho khớp kết quả. Kết quả ngược giả thuyết vẫn đủ điểm nếu số là thật.

- Ngày giờ viết: 27/11/2026 17:33
- Người dùng chính (một vai cụ thể): Học viên lớp L3 đang tự học video và làm câu hỏi kiểm tra trên trang pre-class trước giờ lên lớp.
- **Mình nghĩ:** Học viên lớp L3 gặp khó khi tự học bài pre-class vì các câu hỏi giữa video và lời xen vào tự động của bạn học AI hiện tại chưa kéo họ vào việc tự giải thích lại ý kiến thức, khiến họ thường bỏ qua câu hỏi giữa video, trả lời sai lần đầu rồi chỉ xem đáp án lướt qua hoặc phớt lờ lời bạn học AI xen vào; hậu quả là học thụ động, không sửa được hiểu nhầm trước khi lên lớp chính.
- **Có thể còn cách giải thích khác:** (1) Học viên bận nên chủ đích xem nhanh video cho kịp tiến độ, không muốn bị ngắt quãng bởi quiz hay bạn học AI; (2) Câu hỏi hoặc lời bạn học AI xen vào xuất hiện chưa đúng lúc / dài dòng nên gây phiền; (3) Học viên đã hiểu bài sẵn nên bỏ qua câu hỏi chứ không phải vì không hiểu.
- **Mình đúng nếu thấy:** (1) Trên `data/preclass/`: ≥30% lượt mở câu hỏi giữa video bị đóng bỏ qua (`skipped_stop = true`) hoặc ≥30% câu trả lời lần đầu (`lan_thu = 1`) bị sai, VÀ <5% lượt bạn học AI xen vào (`agent_message_shown`) nhận được phản hồi thực sự từ học viên; (2) Trên khảo sát ≥20 học viên L3: ≥50% báo từng bỏ qua quiz hoặc chỉ xem đáp án lướt qua khi làm sai trong 1 tháng qua.
- **Nguồn sẽ dùng** (≥1 nguồn đạt ngưỡng, guide 1.2): [x] đào data · [ ] phỏng vấn ≥3 · [x] khảo sát ≥20 — nguồn chính: đào dữ liệu hành vi thật `data/preclass/` (BTC cấp) · nguồn để kiểm lại: khảo sát Google Form ≥20 học viên lớp L3 ngoài nhóm (do Mạnh & Bách triển khai).
