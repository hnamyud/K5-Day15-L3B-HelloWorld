# Đánh giá lời giảng tự nhiên và phiên dạy lại nhiều lượt

## Bộ thử

[Bộ đánh giá](teachback-variants.json) gồm **66 ca, 78 lượt, phủ 52/52 mục trên 15 ngày**. Trong đó có 58 lời giảng đơn lượt và 8 phiên tương tác. Các lời giảng do nhóm biên soạn để mô phỏng cách học viên nói khi ôn. Học liệu và bộ 38 ca mốc vẫn dùng nguyên phiên bản.

| Chiều muốn đo | Ví dụ hoặc cách kiểm |
|---|---|
| Trả lời thẳng hoặc ngắn | Chấp nhận lời đúng bằng từ của học viên. Câu quá ngắn và thiếu ý nhận câu hỏi làm rõ. |
| Đúng nhưng lan man | Giữ kết luận đủ ý nếu phần kiến thức trong lời giảng đã đủ. Ca về cửa sổ ngữ cảnh và metadata có nhiều cách diễn đạt cùng nội dung để đối chiếu. |
| Liên tưởng và ví dụ lab | Kiểm ánh xạ đúng ý, chẳng hạn cửa sổ ngữ cảnh như cái bàn có chỗ hữu hạn. Kiểm sự khác nhau giữa ví dụ đúng và ví dụ có kết luận sai. |
| Trộn đúng và sai | Dùng ca nêu đúng vòng sinh token nhưng gán thêm tri thức cho Temperature. Chấm cả nhãn và câu hỏi nhắm đúng phần sai. |
| Ngập ngừng, tự sửa trong lời giảng | Kiểm học viên đang nói mình chưa nghĩ xong, hoặc đã đính chính trong cùng câu. |
| Tích lũy và tự sửa qua nhiều lượt | Kiểm AI giữ phần đúng, hỏi đúng ý còn thiếu, sau đó chuyển mục khi đủ. |
| Ranh giới và thao tác | Kiểm lạc đề rồi quay lại, yêu cầu ngoài phạm vi, hai lượt gợi mở, xem lại, để ôn sau và kết thúc sớm. |

## Cách chấm

Ca đạt khi mọi lượt có **đúng nhãn nội bộ và đúng hành vi**. Với ca cần hỏi, phản hồi phải có một câu hỏi và khớp câu hỏi đã gắn với điểm vướng nếu ca chỉ rõ trọng tâm. Khi hiện phần đối chiếu, ứng dụng phải dẫn đúng mã đoạn và đường dẫn của ngày đang ôn. Ca nhiều lượt chỉ đạt khi tất cả các lượt dự kiến đều chạy và đạt tiêu chí. Điểm được tính bằng code theo kỳ vọng đã ghi trước khi chạy.

Kỳ vọng được biên soạn theo 52 mục hiện tại. Phép kiểm nhiều lượt dùng lời giảng được viết sẵn. Kết quả đo cách model phản ứng với những lượt đó. Hiệu quả học của học viên thật cần thu riêng trong [nhật ký dùng thử](../validation/log.md).

## Kết quả với model thật

Chạy dự án ở commit `e935d75` với `gpt-4.1-mini`. **54/66 ca đạt**, gồm **49/58 ca đơn lượt** và **5/8 phiên nhiều lượt**. Có **63/78 lượt dự kiến đạt**, hai lượt không chạy tới vì ứng dụng đã chuyển mục sớm. Không gặp lỗi gọi model. [Kết quả từng ca và lượt](teachback-variants-result.json)

| Kiểu lời giảng đơn lượt | Đạt / tổng |
|---|---:|
| Trả lời thẳng | 6/8 |
| Đúng ý nhưng lan man | 6/7 |
| Liên tưởng | 9/9 |
| Ví dụ lab | 9/11 |
| Trộn ý đúng và sai | 9/13 |
| Ngập ngừng hoặc còn thiếu | 8/8 |
| Tự sửa trong câu | 1/1 |
| Khẳng định sai với giọng tự tin | 1/1 |

- Hai nhóm giữ nguyên nội dung để đổi cách diễn đạt đều đạt **3/3**. Cửa sổ ngữ cảnh có bản nói thẳng, bản kể dài và bản liên tưởng cái bàn. Metadata có bản nói thẳng, bản dùng ví dụ lab và bản kể lại việc mở nhầm tệp. Số ca thấp nên kết quả chỉ xác nhận các ví dụ đã thử.
- **6 lượt xác nhận đủ ý quá sớm**, gồm 5 lượt đáng lẽ hỏi tiếp và 1 lượt đáng lẽ mở phần xem lại. V07, V13, V18 và V24 đều có phần kiến thức đúng đứng cạnh một phát biểu sai. Giám khảo chấp nhận toàn bộ lời giảng. Ở S01, phiên chuyển mục dù học viên chưa tự giải thích đường trả kết quả hàm. Ở S04, giám khảo cho qua ngay cả khi học viên vẫn đang nhầm kiểm kiểu với kiểm nghiệp vụ.
- **Một số nhãn cần người rà lại.** V12 đã có mốc, mục tiêu và cách thu log nhưng bị hỏi lại về hiện trạng. V58 nêu mục tiêu, năng lực, khoảng trống và bước kiểm chứng trong cùng ví dụ nhưng chưa nói thẳng tên track. Cần thống nhất mức chấp nhận ý được hàm ý rồi mới dùng những ca đó để kết luận về model.

Các ca S01 và S04 là ca hồi quy ưu tiên cho luồng nhiều lượt. Với các cặp trực tiếp, lan man và ví dụ, giữ cùng yêu cầu kiến thức để khi sửa prompt có thể kiểm xem hệ thống còn chấp nhận cách diễn đạt khác nhau hay không.

## Cách chạy

```bash
python eval/run_teachback_variants.py --validate-only
MODEL_NAME=gpt-4.1-mini python eval/run_teachback_variants.py --output /tmp/teachback-variants-new.json
```
