---
name: "Phân tích dữ liệu"
description: "Phân tích và kiểm chứng dữ liệu bằng Python, Excel hoặc Google Sheets. Truy số về công thức và nguồn để giải thích kết quả, phễu và thử nghiệm."
group: Vận hành
---

# Phân tích dữ liệu

## Khi nào dùng

Dùng khi cần giải thích số thay đổi, phân tích hành trình hoặc cohort, đo tác động thay đổi, kiểm dashboard hay viết yêu cầu dữ liệu. Dùng `insider-cs` và [hướng dẫn trích dữ liệu](skills/insider-cs/references/regex-vs-llm-structured-text.md) khi đọc văn bản có mẫu hoặc làm sạch file xuất hỗn hợp.

## Chuẩn bị

Chốt người dùng kết quả, quyết định họ cần đưa ra và mức khác biệt đủ để đổi quyết định. Lập định nghĩa chỉ số gồm mục đích, tử số, mẫu số, cấp bản ghi, sự kiện gốc, thời gian, múi giờ, điều kiện vào/loại trừ, phân khúc, nguồn và người xác nhận. Ví dụ attach rate có thể đo booking có bổ trợ trên số booking đủ điều kiện hoặc hành khách mua bổ trợ trên số hành khách đủ điều kiện. Ghi rõ cách dùng trước khi so.

## Cách chạy

- Dùng Python khi cần xử lý nhiều nguồn, dữ liệu cấp sự kiện, kiểm tra lặp lại hoặc tái lập phân tích. Chạy mã trên đầu vào thực tế và giữ bản mã, điều kiện lọc, các bảng trung gian và kết quả kiểm.
- Dùng Excel hoặc Google Sheets khi người nhận cần xem, thay giả định hoặc điều chỉnh bộ lọc. Giao file có công thức tham chiếu tới dữ liệu và tham số, kèm ô kết quả và điều kiện áp dụng. Kiểm giá trị đã tính bằng công cụ phù hợp và ghi rõ môi trường đã chạy.
- Mở [hướng dẫn thực hành và workbook mẫu](skills/data-analytics/references/tinh-va-kiem-chung.md) để chọn cách thực thi. Dùng một phép kiểm độc lập cho các số chi phối quyết định. Khi chưa có dữ liệu hoặc công cụ để tính lại, ghi phần còn thiếu và trạng thái của kết quả.

## Quy trình

1. Kiểm chất lượng trước khi tính. Ghi bản nguồn và ngày chốt. Nếu phát hiện mất dữ liệu, đổi mẫu số, sai phạm vi hoặc chênh tổng có thể đảo kết luận, báo ngay chỉ số bị ảnh hưởng, phần vẫn dùng được, cách kiểm lại và ai có thể xác nhận trước mốc quyết định. Đếm bản ghi và khóa duy nhất trước/sau join, kiểm khóa trùng, null, múi giờ, trễ dữ liệu và độ phủ. Phân loại mọi bản ghi đầu vào vào nhóm đã xử lý hoặc chờ kiểm tra, giữ định danh hoặc vị trí nguồn. Đối soát tổng quan trọng với nguồn đã chốt.
2. Chọn phương pháp theo câu hỏi. Với phễu, xác định điểm vào, thứ tự bước, cửa sổ và đơn vị đếm. Báo tỷ lệ từng bước và toàn phễu. Với cohort, cố định sự kiện gia nhập và tuổi cohort, so cùng kỳ quan sát, đánh dấu cohort chưa đủ tuổi. Khi tách phân khúc, kiểm thay đổi cơ cấu trước khi kết luận từ số tổng.
3. Với thử nghiệm, chốt giả thuyết, nhóm, đơn vị phân bổ, chỉ số chính, chỉ số cần bảo vệ, ngưỡng tác động thực tế và cửa sổ đo trước khi đọc số. Kiểm lệch tỷ lệ phân nhóm, nhiễm chéo và đủ mẫu. Trình hiệu ứng tuyệt đối, tương đối và khoảng tin cậy khi tính được. Ghi lý do nếu kết quả chưa đủ kết luận. Với dữ liệu quan sát, nêu nhiễu và phần chưa thể quy là tác động nhân quả.
4. Dựng dashboard từ quyết định cần hỗ trợ. Mỗi chỉ số có định nghĩa, kỳ so và hành động khi vượt ngưỡng. Chọn biểu đồ đường cho xu hướng, thanh cho so sánh và bảng cho đối soát. Kiểm bộ lọc, tải dữ liệu, mẫu số và kỳ thời gian trên một ví dụ tính tay hoặc truy vấn độc lập.
5. Tìm nguyên nhân bằng cách phân rã thay đổi từ số tổng về nhóm, bước hành trình hoặc yếu tố tạo ra số. Kiểm trước xem chênh lệch đến từ lỗi dữ liệu, đổi phạm vi hoặc đổi cơ cấu. Với ứng viên nguyên nhân, ghi mức đóng góp, một giải thích cạnh tranh và phép thử có thể phân xử. Khi số chỉ cho thấy mối liên hệ, nêu đó là giả thuyết.
6. Bàn giao kết luận và phần giải thích cho các số chi phối quyết định. Nêu vì sao chọn cách đo, công thức bằng lời và phép tính thay số, tử/mẫu hoặc đầu vào, phạm vi và loại trừ, nguồn gốc đến tab/ô hoặc mã đã chạy, cách kiểm và điểm còn yếu. Nếu công thức tính đúng nhưng định nghĩa có thể dẫn tới cách hiểu khác, nêu cách hiểu và tác động. Đặt phần kỹ thuật dài trong file kiểm chứng có liên kết.

## Kiểm chứng

Kiểm một tập nhỏ từ bản ghi gốc tới biểu đồ. So tổng với tổng phân nhóm theo đúng quy tắc tính. Dùng 0 khi quan sát hợp lệ có giá trị 0, ghi thiếu dữ liệu khi chưa có quan sát, và ghi không xác định khi mẫu số bằng 0. Không dùng trung bình tỷ lệ các nhóm để thay cho tỷ lệ từ tổng tử và tổng mẫu nếu trọng số khác nhau.

Tham khảo [hướng dẫn thử nghiệm của Microsoft](https://learn.microsoft.com/en-us/xbox/playfab/live-service-management/game-configuration/experiments/experimentation-keys).
