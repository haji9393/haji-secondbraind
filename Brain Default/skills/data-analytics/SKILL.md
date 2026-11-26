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
4. Dựng dashboard từ quyết định cần hỗ trợ. Mỗi chỉ số có định nghĩa, kỳ so và hành động khi vượt ngưỡng. Dùng mục Chọn và kiểm biểu đồ để chọn hình theo câu hỏi và loại biến, rồi kiểm bộ lọc, tải dữ liệu, mẫu số và kỳ đo bằng ví dụ tính tay hoặc truy vấn độc lập.
5. Tìm nguyên nhân bằng cách phân rã thay đổi từ số tổng về nhóm, bước hành trình hoặc yếu tố tạo ra số. Kiểm trước xem chênh lệch đến từ lỗi dữ liệu, đổi phạm vi hoặc đổi cơ cấu. Với ứng viên nguyên nhân, ghi mức đóng góp, một giải thích cạnh tranh và phép thử có thể phân xử. Khi số chỉ cho thấy mối liên hệ, nêu đó là giả thuyết.
6. Bàn giao kết luận và phần giải thích cho các số chi phối quyết định. Nêu vì sao chọn cách đo, công thức bằng lời và phép tính thay số, tử/mẫu hoặc đầu vào, phạm vi và loại trừ, nguồn gốc đến tab/ô hoặc mã đã chạy, cách kiểm và điểm còn yếu. Nếu công thức tính đúng nhưng định nghĩa có thể dẫn tới cách hiểu khác, nêu cách hiểu và tác động. Đặt phần kỹ thuật dài trong file kiểm chứng có liên kết.

### Phép kiểm có thể làm đổi kết luận

- Với phân rã biến động có tương tác giữa các yếu tố, đổi thứ tự phân rã để xem thứ hạng nguyên nhân có đổi không. Phân biệt đóng góp số học với nguyên nhân cần dữ liệu bổ sung.
- Khi rà truy vấn lỗi, lần kết quả từ truy vấn gốc qua bản chỉ sửa từng lỗi có thể che lỗi khác rồi đến bản sửa đầy đủ. Đối chiếu số chính bằng cách đếm độc lập và kiểm dữ liệu bị loại khi nối, chẳng hạn giao dịch thiếu giá.
- Với thử nghiệm, kiểm sự kiện tuyển nhóm có nằm trong kỳ trước hay không. Chỉ dùng thuộc tính có trước gửi để đề xuất nhắm mục tiêu cho lần sau. Khi tỷ lệ phân bổ khác nhau giữa các phân khúc, so kết quả gộp thô với kết quả theo từng phân khúc, rồi tổng hợp theo trọng số phù hợp. Nêu mẫu số theo nhóm được phân bổ.
- Khi đề xuất cỡ nhóm đối chứng, tính theo tỷ lệ nền hoặc độ phân tán, tác động tối thiểu có ý nghĩa, mức sai số và lực kiểm định. Nếu thiếu đầu vào, ghi rõ kết quả chỉ đúng theo giả định. Kiểm định trên tỷ lệ chuyển đổi chỉ hỗ trợ kết luận về chỉ số đó. Muốn đánh giá độ bất định của doanh thu cần dữ liệu phù hợp về biến động doanh thu.

## Chọn và kiểm biểu đồ

Xác định người xem cần đọc giá trị chính xác, so sánh, xem tỷ trọng, theo dõi xu hướng, xem phân bố hay tìm mối liên hệ. Ghi đơn vị quan sát và vai trò của từng biến (nhóm, số đo hoặc thời gian), rồi chọn hình theo câu hỏi.

| Câu hỏi | Cấu trúc dữ liệu | Cách thể hiện |
|---|---|---|
| Nhóm nào cao hơn và chênh bao nhiêu? | Một chỉ số theo nhóm, có thể thêm biến phân nhóm | Thanh hoặc cột. Dùng cột nhóm khi cần so các chuỗi cạnh nhau. |
| Các phần đóng góp bao nhiêu? | Giá trị cộng được theo nhóm và thành phần | Cột chồng để thấy tổng và từng phần. Dùng cột chồng 100% để so tỷ trọng, kèm tổng hoặc cỡ mẫu khi quy mô ảnh hưởng cách hiểu. |
| Chỉ số đổi thế nào qua thời gian? | Một hoặc nhiều chỉ số theo kỳ | Đường với kỳ đo nhất quán. Đánh dấu kỳ chưa đủ hoặc thiếu dữ liệu. |
| Giá trị tập trung và phân tán ra sao? | Một biến số, có thể thêm nhóm | Histogram cho một phân bố, box plot để so phân bố giữa các nhóm. Khi so histogram, dùng cùng ranh giới khoảng chia. |
| Hai biến liên hệ thế nào hoặc điểm nóng nằm ở đâu? | Hai biến số trên cùng đơn vị quan sát, hoặc một chỉ số trên lưới hai chiều | Biểu đồ phân tán cho cặp giá trị số, bản đồ nhiệt cho mẫu hình trên lưới. Khi diễn giải mối liên hệ, nêu rõ giới hạn về nhân quả. |
| Giá trị chính xác là bao nhiêu? | Một hoặc nhiều chỉ số cần tra hoặc đối soát | Bảng có đơn vị, kỳ đo và định nghĩa rõ. |

Trước khi giao, đối chiếu một điểm hoặc một nhóm từ dữ liệu gốc qua phép tổng hợp tới hình. Rà cấp bản ghi, đơn vị, mẫu số, kỳ đo, bộ lọc, nhãn và thang trục. Với biểu đồ thanh, đặt gốc trục giá trị ở 0 để độ dài phản ánh đúng quy mô. Khi hai chuỗi khác đơn vị cần hai trục, ưu tiên hai biểu đồ cùng trục thời gian nếu cách đặt thang có thể tạo ấn tượng sai về mức độ biến động cùng nhau.

Bảng tra dựa trên giáo trình *Nghệ thuật Ra quyết định Dựa trên Dữ liệu*, Trần Hùng Thiện, tháng 10/2025, trang 37-67. Phần đối soát và kiểm cách đọc là hướng dẫn áp dụng.

## Kiểm chứng

Kiểm một tập nhỏ từ bản ghi gốc tới biểu đồ. So tổng với tổng phân nhóm theo đúng quy tắc tính. Dùng 0 khi quan sát hợp lệ có giá trị 0, ghi thiếu dữ liệu khi chưa có quan sát, và ghi không xác định khi mẫu số bằng 0. Không dùng trung bình tỷ lệ các nhóm để thay cho tỷ lệ từ tổng tử và tổng mẫu nếu trọng số khác nhau.

Tham khảo [hướng dẫn thử nghiệm của Microsoft](https://learn.microsoft.com/en-us/xbox/playfab/live-service-management/game-configuration/experiments/experimentation-keys).
