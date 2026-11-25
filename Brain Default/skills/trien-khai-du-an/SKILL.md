---
name: "Chiến lược triển khai và quản trị dự án"
description: "Chốt brief, mục tiêu, ưu tiên và mốc dự án. Chọn mô hình quản trị, kiểm tính khả thi của kế hoạch và cảnh báo sớm rủi ro."
group: Vận hành
---

# Chiến lược triển khai và quản trị dự án

## Khi nào dùng

Dùng khi cần chọn cách quản trị, khởi động hoặc tiếp quản dự án, rà kế hoạch, xử lý dự án chệch hướng, triển khai thử, mở rộng hoặc bàn giao vận hành. Dùng `business-strategy-presentation` để phát triển phương án chiến lược và `haji-work-standards` để phản biện, trình Haji chốt.

## Chuẩn bị

Mở yêu cầu mới, brief gần nhất, nhật ký quyết định, kế hoạch, bằng chứng hiện trạng và ràng buộc. Đối chiếu phần thay đổi với nguồn và ngày xác nhận. Khi hai nguồn vênh và lựa chọn ảnh hưởng tới phạm vi, kết quả hoặc cam kết, ghi từng cách hiểu và đưa đúng câu cần người có quyền chốt.

### Viết bản recap và đóng khung brief

Viết một bản recap ngắn trước khi lập hoặc đổi kế hoạch. Dùng hồ sơ đang có làm nơi lưu bản làm việc khi được giao cập nhật dự án. Nếu chỉ được nhờ rà soát, có thể trình recap trong kết quả. Brief mới ghi ngày, phiên bản, nguồn và trạng thái của từng điểm quan trọng: đã chốt, giả định làm việc hoặc cần quyết.

| Phần | Ghi gì và tự rà gì |
|---|---|
| Bối cảnh và câu hỏi cần quyết | Điều gì kích hoạt công việc, ai yêu cầu, ai chịu tác động và ai có quyền chốt? Ghi phần mới so với brief trước. |
| Mục tiêu và kết quả cần đạt | Viết lý do, thay đổi cụ thể cần thấy, đối tượng, mốc nền nếu có, đích, hạn, nguồn đo hoặc bằng chứng đạt và người xác nhận. Có bản vẽ là đầu ra. Chủ nhà có đủ căn cứ chọn phương án là kết quả cần kiểm. |
| Phạm vi, bàn giao và nghiệm thu | Ghi phần trong và ngoài phạm vi, đầu ra phải giao, người nhận, tiêu chí chấp nhận và các ràng buộc về tiền, người hoặc điều kiện phê duyệt. Tách yêu cầu bắt buộc khỏi phần linh hoạt. |
| Mốc và thời gian | Đi ngược từ ngày cần kết quả. Mỗi mốc có điều kiện hoàn tất, người phụ trách và người duyệt, hạn cam kết, ngày dự báo và phụ thuộc. Tính cả thời gian duyệt, bàn giao và dự phòng. Ngày chưa xác nhận được ghi là dự kiến. |
| Ưu tiên và đánh đổi | Xếp trước việc chặn mốc, bảo vệ kết quả hoặc có hạn khó dời. Sau đó xét tác động, công sức và khả năng đảo ngược. Ghi việc làm ngay, tiếp theo và để sau, kèm lý do. Khi đưa việc mới lên đầu, chỉ ra việc nào phải lùi và ai có quyền đổi cam kết. |
| Điểm mở và cảnh báo đầu tiên | Ghi giả định, xung đột, rủi ro hoặc phụ thuộc chưa có người phụ trách. Gắn mỗi điểm quan trọng với cách kiểm, người xử lý và hạn cần trả lời. |

Đọc lại recap như người mới tiếp quản và thử trả lời một câu: kế hoạch này có thể giao đủ mọi đầu ra mà vẫn lỡ mục tiêu nào? Đưa ra cách xử lý sớm nếu có căn cứ. Trình Haji phần cần quyết trước khi cam kết. Dùng giả định có ghi rõ để tiếp tục phần có thể đảo ngược.

Trước khi chọn cách quản trị, nhìn toàn dự án: yêu cầu nào đã ổn định, giả định nào còn mở, phần nào có thể thử và đảo ngược, phần nào lệ thuộc phê duyệt hoặc có chi phí sửa cao. Kiểm nhịp phản hồi thật của người dùng hoặc người duyệt, luồng việc có bị chen ngang thường xuyên không, đội có đủ thời gian và kỹ năng để hoàn tất một phần việc trong mỗi vòng không. Ghi căn cứ từ hồ sơ. Khi thiếu dữ liệu, đưa lựa chọn tạm và điều kiện xác nhận lại.

## Cách chọn mô hình

Chọn cách **đo kết quả** và cách **tổ chức thực thi** theo hai câu hỏi riêng. OKR diễn đạt mục tiêu và kết quả đo được. Agile là nhóm nguyên tắc thích ứng thông qua phản hồi. Scrum là một khung thực thi có thể dùng cho công việc phức tạp. Waterfall, Kanban và mô hình kết hợp phù hợp với các điều kiện thực thi khác nhau.

| Cách làm | Chọn khi | Cách áp dụng và điều kiện xem lại |
|---|---|---|
| OKR | Cần nhiều người cùng hướng tới một thay đổi có thể đo trong một kỳ. | Chốt mốc nền, đích, thời hạn, nguồn đo và người chịu trách nhiệm cho kết quả. Ghi các sáng kiến hỗ trợ ở kế hoạch thực thi tương ứng. |
| Waterfall hoặc lập kế hoạch theo giai đoạn | Yêu cầu đủ ổn định, các bước có thứ tự, phê duyệt bắt buộc hoặc làm lại tốn kém. | Chốt mốc, phụ thuộc, dự phòng và tiêu chí qua từng cổng duyệt. Nếu giả định chính chưa được kiểm, thêm bước khám phá trước khi cam kết phần khó đảo ngược. |
| Agile theo vòng ngắn | Nhu cầu hoặc giải pháp còn chưa rõ, có thể giao từng phần dùng được và có người phản hồi đủ sớm. | Mỗi vòng định nghĩa điều cần học, phần việc sẽ thử, tiêu chí và thời điểm phản hồi. Xem lại cách chạy khi vòng nào cũng kết thúc mà chưa có dữ liệu hay phản hồi. |
| Scrum | Công việc phức tạp, có đội đủ kỹ năng làm ra phần tăng thêm sử dụng được mỗi Sprint và có người sắp thứ tự ưu tiên sản phẩm. | Dùng mục tiêu Sprint, các trách nhiệm và nhịp kiểm tra theo Scrum Guide. Nếu đội thường xuyên bị kéo sang việc khẩn hoặc khó hoàn tất một phần dùng được, xem lại độ phù hợp của Scrum. |
| Kanban | Việc đến liên tục, độ lớn khác nhau hoặc ưu tiên thay đổi theo ngày. | Hiển thị dòng việc, giới hạn việc đang làm, theo dõi tuổi đầu việc, tốc độ hoàn tất và điểm chờ. Xem công việc nào cần được gỡ trước khi kéo thêm việc vào. |
| Kết hợp | Một phần có thể học qua vòng ngắn, phần khác có cam kết cứng, phụ thuộc hoặc cổng duyệt. | Chỉ rõ phần nào dùng cách nào, dữ liệu nào phải bàn giao qua mỗi cổng và ai quyết. Đặt cổng theo lúc phải cam kết tiền, thời gian hoặc phạm vi. |
| Kế hoạch theo mốc đơn giản | Việc ngắn, ít người, phụ thuộc rõ và điều phối nhẹ. | Dùng danh sách mốc, người phụ trách, thời hạn và tiêu chí nghiệm thu. Bổ sung cơ chế khi có điểm nghẽn lặp lại. |

Trong hồ sơ dự án, ghi lựa chọn theo giai đoạn hoặc luồng việc, 2-3 căn cứ cụ thể, đánh đổi, phương án thay thế gần nhất và tín hiệu khiến nhóm đổi cách làm. Thiết kế bộ hồ sơ và nhịp họp vừa đủ với dự án. Tham khảo [PMI về điều chỉnh cách quản trị](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmi-tailoring.pdf), [nguyên tắc Agile](https://agilemanifesto.org/principles.html), [Scrum Guide](https://scrumguides.org/scrum-guide), [Kanban Guide](https://kanbanguides.org/the-kanban-guide/) và [hướng dẫn OKR](https://www.whatmatters.com/faqs/okrs-objectives-key-results-explanation-examples).

## Quy trình quản trị chủ động

1. Đi ngược từ kết quả cần đạt đến mốc nghiệm thu. Mỗi mốc có đầu ra, người chịu trách nhiệm, người duyệt, hạn, dự trù nguồn lực và phụ thuộc. Xác định chuỗi công việc hoặc bước phê duyệt mà nếu chậm sẽ đẩy lùi mốc cuối. Khi chưa rõ phạm vi, chia nhỏ để khảo sát hoặc thử trước khi cam kết.
2. Trước mỗi đợt triển khai, hình dung dự án có thể trượt vì đâu. Kiểm phụ thuộc bên ngoài, người đang kiêm nhiều vai, dữ liệu thiếu, thay đổi chưa duyệt, ngân sách đã cam kết, thời gian chờ và mức sẵn sàng vận hành. Tách rủi ro có thể phát sinh, vấn đề đã xảy ra và dữ kiện chưa đủ để đánh giá. Ưu tiên theo tác động và thời gian còn lại để xử lý.
3. Tại mỗi lần rà, mở bằng chứng mới nhất và kiểm cả phần Haji chưa hỏi nếu nó có thể làm đổi kết quả. So hạn dự báo với hạn cam kết, giờ cần với giờ thực có, khối lượng mở với tốc độ xử lý, và điều kiện nghiệm thu với phần đã chứng minh. Rà khi có tín hiệu mới có thể làm đổi quyết định, nhất là trước mốc khó đảo ngược. Dùng `data-analytics` để kiểm số và `tai-chinh-ke-toan` khi dự báo ảnh hưởng nguồn lực hoặc dòng tiền.
4. Trong phạm vi được giao, chủ động làm rõ dữ kiện, cập nhật rủi ro, tính kịch bản hoặc đề xuất gỡ vướng. Nếu phát hiện đề bài đụng mục tiêu đã chốt, mốc không khả thi hoặc có rủi ro chưa ai giữ, nêu ngay bằng chứng và cách xử lý. Trình người có quyền quyết khi cần đổi phạm vi, ngân sách, hạn cam kết hoặc chấp nhận rủi ro vượt thẩm quyền.
5. Duy trì brief và kế hoạch gốc có phiên bản. Mỗi khi mục tiêu, mốc hoặc ưu tiên thay đổi, recap ngắn điều đã đổi, lý do, tác động, ai chốt và phần nào phải làm lại. Giữ hạn cam kết để so với tiến độ thực tế và hạn dự báo. Sau khi thay đổi được duyệt, cập nhật brief, các mốc, phụ thuộc và phân công liên quan. Với phép thử, định trước tiêu chí để tiếp tục, làm lại, thu hẹp hoặc dừng. Với bàn giao, kiểm người tiếp quản, tài liệu, hỗ trợ và ngày đo kết quả sau khi vận hành. Ghi bài học cùng điều kiện áp dụng.

## Cảnh báo sớm và xử lý

Mỗi rủi ro quan trọng có tín hiệu dẫn trước, nguồn hoặc cách tính, ngưỡng kích hoạt, người theo dõi, biện pháp xử lý và thời điểm muộn nhất còn có thể can thiệp. Chọn ngưỡng từ hạn cam kết, năng lực, khoảng dự phòng và tác động. Các dấu hiệu đáng kiểm gồm đầu việc bị chặn lâu, dữ liệu bắt buộc chưa có người xác nhận, dự phòng bị tiêu nhanh hoặc thời điểm phê duyệt dự báo đã lấn vào thời gian của bước sau.

Khi chạm ngưỡng, báo cho người phụ trách trong lượt rà hiện tại. Nêu **điều vừa thay đổi, bằng chứng, mốc hoặc kết quả bị ảnh hưởng, hướng xử lý ưu tiên, phương án dự phòng và ai cần quyết trước lúc nào**. Nếu rủi ro đã xảy ra, ghi thành vấn đề đang xử lý và cập nhật dự báo. Nếu thiếu dữ liệu để phân loại, ghi phần chưa biết, ai có thể kiểm và hạn có câu trả lời. Tham khảo [PMI về dấu hiệu kích hoạt và người phụ trách rủi ro](https://www.pmi.org/learning/library/risk-analysis-project-management-7070).

Ví dụ minh họa cho dự án cải tạo. Khi công năng còn vài phương án, dùng vòng ngắn để thử mặt bằng với người vận hành và so tác động vào mô hình. Khi bước sau cần hồ sơ đã duyệt để báo giá, quản trị bằng mốc và kiểm điều kiện bàn giao giữa hai phần. Giả sử cần 5 ngày làm việc từ khi chốt bản vẽ tới khi có hồ sơ báo giá, mà chỉ còn 3 ngày theo dự báo, khoảng dự phòng là `3 - 5 = -2 ngày`. Báo sớm nguy cơ trượt ít nhất 2 ngày theo giả định hiện tại. Trình phương án đẩy sớm phiên duyệt hoặc đổi mốc báo giá, kèm điều kiện để từng hướng khả thi.

## Hồ sơ dự án

Dùng `projects/<slug>/` và tôn trọng cấu trúc hiện có. README hoặc kế hoạch chính dẫn tới brief hiện hành, mục tiêu, mô hình đã chọn, mốc, thứ tự ưu tiên, quyết định, rủi ro và tiến độ. Giữ nguồn, ngày và phiên bản ở nơi dùng số. Một dự án nhỏ có thể dùng chung một file.

## Kiểm chứng

Trước khi giao, kiểm người đọc có thể nhắc lại đúng mục tiêu, cách biết đã đạt, ưu tiên hiện tại, mốc cam kết so với dự báo và ai cần quyết phần còn mở. Kiểm vì sao mô hình phù hợp, dấu hiệu nào khiến phải đổi cách làm, mốc nào dễ trượt trước và còn bao lâu để can thiệp. Kiểm tiêu chí nghiệm thu và thời điểm đo kết quả sau bàn giao. Tham khảo [hướng dẫn quản lý lợi ích của PMI](https://www.pmi.org/standards/benefits-realization).
