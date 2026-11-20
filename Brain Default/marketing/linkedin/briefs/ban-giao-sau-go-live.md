# Bàn giao yêu cầu khách hàng sau go-live

- Giả thuyết LI-HANDOFF, phiên bản 2, kỳ kế hoạch tháng 11/2026, tuần 23-29/11/2026. Hai vị trí dự kiến là thứ Ba 24/11 và thứ Năm 26/11.
- **CHỜ THÁNG • CHỜ DUYỆT GÓC** cho cả hai vị trí. Chưa có lời duyệt của Haji cho phiên bản 2. Hồ sơ chưa ghi quyết định tạm dừng LI-HANDOFF.
- Độc giả chính là trưởng CSKH và vận hành dịch vụ tại doanh nghiệp Việt Nam đã dùng CRM, có yêu cầu đi qua nhiều đội. Người đọc nên xác định được ai giữ lời hẹn và hồ sơ nào cần kiểm trong ca tiếp theo.
- Trụ thử là CX sau triển khai. CRM là bối cảnh chính, AI là phép thử mở rộng. Giả thuyết biên tập là câu hỏi về quyền tiếp quản giúp người đọc liên hệ Haji với việc sửa cách vận hành sau triển khai.

| Vị trí dự kiến | Góc ưu tiên | Phương án thứ hai và điều kiện đổi |
|---|---|---|
| Thứ Ba 24/11 | Ai gọi lại cho khách khi CRM đã chuyển phiếu hoàn tiền mà kế toán chưa xác nhận nhận? Thử giữ trách nhiệm cập nhật ở người chuyển đến khi người nhận xác nhận. Dùng cảnh minh họa sẵn trong [[bai-linkedin-ban-giao-crm]]. | Khi nào trưởng ca cần can thiệp vào phiếu sắp quá hẹn? Chọn góc này nếu đội đã có người tiếp quản rõ nhưng chưa có cách xử lý lời hẹn có nguy cơ trễ. |
| Thứ Năm 26/11 | Nhân viên nhận được gì để làm tiếp ngay? Chọn một loại yêu cầu và đối chiếu dữ kiện khách đã cung cấp, màn hình nhân viên, quyền xử lý và kết quả nghiệp vụ. Ghi riêng xác minh bắt buộc và việc khách phải lặp dữ kiện đã có. | Chat đã đóng, khách có quay lại qua kênh khác? Chỉ đổi khi nối được bot, CRM và tổng đài theo mã yêu cầu, theo dõi đủ 7 ngày từ lần chuyển đầu và đối chiếu được kết quả nghiệp vụ. |

## Nguồn và chất liệu

- [Manasa Nadaduru, LinkedIn](https://www.linkedin.com/posts/manasanadaduru_dynamics365-crm-businessanalysis-activity-7457469284907175936-67Kn). Đọc bài gốc và bình luận công khai ngày 20/11. Case tác giả tự thuật về đội quay lại Excel/email rồi chỉnh quy trình theo việc thực tế. Bình luận bổ sung góc nhìn đội bận và tiêu chí thành công của nghiệp vụ. Dùng để tránh mở bài bằng kết luận chung về go-live. Chưa xác minh độc lập.
- [Kim Secia, LinkedIn](https://www.linkedin.com/posts/ksecia_ai-doesnt-need-to-resolve-every-support-activity-7500650880900276224-yLQy). Đọc bài và bình luận công khai của Avi Dixit ngày 20/11. Kim phân biệt lúc chuyển người và ngữ cảnh cần chuyển. Avi bổ sung quyền xử lý và thời gian nằm giữa hai bên. Đây là đề xuất nghề nghiệp. Với dữ liệu nhạy cảm, người nhận chỉ cần ngữ cảnh cần thiết và có thể vẫn phải xác minh danh tính.
- [Fernando Duarte, Substack, 25/05/2026](https://1fernandoduarte.substack.com/p/ai-support-economics-part-1). Đọc bài công khai. Tác giả đề xuất đo cả lần liên hệ lại, công sửa của người và đường xử lý cuối. Học cách mở bằng chênh lệch giữa dashboard và hàng chờ. Khung đo tham khảo, tự tin vừa về tính hữu ích biên tập, thấp về khả năng suy rộng tới doanh nghiệp Việt Nam.
- [Intercom, LinkedIn](https://www.linkedin.com/pulse/transformation-action-what-takes-automate-81-your-customer-service-e9d3f?tl=en). Tự thuật của nhà cung cấp cho thấy AI có thể tạo giá trị khi đội sửa cả cách vận hành. Dùng làm phản biện, giữ số liệu ở phạm vi riêng của nguồn.
- [[haji-cv-evidence-bank]] E4 và F, [[doi-chieu-case-ban-giao]]. Có thể dùng ẩn danh kinh nghiệm dựng bảng theo dõi hành trình, hỗ trợ lãnh đạo chỉnh mục tiêu và đào tạo đội nội bộ tự vận hành. Cảnh hoàn tiền là minh họa. Chưa có case Haji đo hiệu quả cuộc gọi lặp hoặc bàn giao bot sang người.

## Quyết định buổi biên tập

Đề xuất giữ **24/11 CRM A + 26/11 AI A** để thử trụ CX sau triển khai. Bản lịch 19/11 cũng đặt CRM sau go-live vào 24/11, với góc rộng về dấu hiệu suy yếu. CRM A thu về một quyết định của trưởng ca. Bản lịch đặt góc đào tạo và mức độ sử dụng công cụ vào 26/11. AI A dùng vị trí này để thử cùng vấn đề bàn giao trong bối cảnh bot sang người, đưa góc AI lên sớm hơn bản lịch nháp. [[2026-11-19-dinh-vi-tru-lich-chi-so]] · [[marketing/linkedin/playbook]]

- **CRM A trước CRM B.** Trưởng CSKH có thể kiểm ngay ai đang giữ lời hẹn. Hàng đợi có người trực có thể đã thực hiện việc này. Kiểm dấu thời gian trên một loại phiếu trước khi đề xuất thêm thao tác xác nhận. Nếu người giữ lời hẹn đã rõ mà phiếu vẫn trễ, CRM B giúp xác định bước còn treo và lúc trưởng ca cần can thiệp. [Manasa Nadaduru](https://www.linkedin.com/posts/manasanadaduru_dynamics365-crm-businessanalysis-activity-7457469284907175936-67Kn) · [Kim Secia và Avi Dixit](https://www.linkedin.com/posts/ksecia_ai-doesnt-need-to-resolve-every-support-activity-7500650880900276224-yLQy)
- **AI A trước AI B.** Quản lý CSKH có thể kiểm một ca bàn giao qua transcript, màn hình và quyền xử lý. AI B cần dữ liệu nối kênh để đếm mỗi yêu cầu một lần và cần kết quả nghiệp vụ để nhận diện khách bỏ cuộc. Xếp AI C sau hai góc này vì loại ca chuyển có thể khác độ khó và chuyển sớm có thể tăng tải. Nghiên cứu Taobao gợi câu hỏi cần kiểm, với mức tự tin thấp khi suy rộng về Việt Nam. [Kim Secia và Avi Dixit](https://www.linkedin.com/posts/ksecia_ai-doesnt-need-to-resolve-every-support-activity-7500650880900276224-yLQy) · [Wang và cộng sự](https://arxiv.org/abs/2605.14830)
- **Cách kể.** Theo một yêu cầu qua màn hình khách và màn hình nhân viên, rồi kết bằng một việc người đọc có thể kiểm trong ca. Gắn nhãn minh họa cho cảnh hoàn tiền. Nếu dùng trải nghiệm Haji, kể ẩn danh trong phạm vi E4 và F đã đối chiếu. [Hans van Dam](https://hansvandam.substack.com/p/false-containment-how-your-best-dashboard) · [[doi-chieu-case-ban-giao]]

## Đo sau đăng

| Chỉ số chính | Mốc so | Điều kiện đủ dữ liệu | Biến thử và ngày đọc |
|---|---|---|---|
| Số người đúng nhóm có phản hồi cụ thể trong 7 ngày mỗi bài. Tính mỗi người một lần mỗi bài theo bình luận hoặc tin nhắn quy được về bài. Tín hiệu đủ chuẩn gồm kể một ca tương tự, nêu cách áp dụng hoặc phản biện bằng tình huống cụ thể. | Bốn tuần đầu đủ dữ liệu làm mốc nền. Chưa có ngưỡng số. So các bài có mức tiếp cận đúng nhóm tương đương khi có mốc. | Có URL, đủ 7 ngày và có căn cứ xác nhận mức tiếp cận đủ trong nhóm trưởng CSKH/vận hành. Ghi lượt hiển thị riêng, cùng bằng chứng tiếp cận đúng nhóm. Khi thiếu số, thiếu căn cứ về tiếp cận hoặc chưa đủ ngày, ghi chưa đủ dữ liệu và giữ nguyên bộ đếm. Ghi 0 khi đủ điều kiện và đã kiểm các kênh phản hồi mà không thấy phản hồi đạt chuẩn. | Bối cảnh bàn giao giữa hai đội so với bot sang người. Đọc 01/12 cho CRM và 03/12 cho AI nếu đăng đúng lịch. Hai bài dùng để thăm dò, chưa đủ để quy khác biệt cho bối cảnh. |

Nguồn cho quy tắc đo là [[marketing/linkedin/playbook]]. Các ngày đọc là kế hoạch, dịch theo ngày đăng thực tế.

## Lịch sử quyết định

| Phiên bản | Haji duyệt hoặc trả lại | Lý do và bước tiếp |
|---|---|---|
| 1 | Chờ duyệt | Đề xuất CRM rồi AI. CRM dự phòng góc trưởng ca. AI dự phòng chi phí trên mỗi yêu cầu hoàn tất và gộp việc liên hệ lại vào góc chính. |
| 2 | Chờ tháng và chờ duyệt cả hai góc | Giữ cặp CRM trước, AI sau. CRM A làm rõ việc nhận cả phiếu lẫn lời hẹn, nêu rủi ro xác nhận tay. AI A thu về khả năng xử lý của nhân viên. Đưa liên hệ lại qua kênh khác thành AI B có điều kiện dữ liệu và để góc chi phí ngoài tuần này. Trình Haji duyệt tháng rồi duyệt từng góc. [[ban-giao-cmo-linkedin-2026-11-23]] |

Số lần Haji trả trước đăng ghi nhận là **0**. Số lần thử đủ dữ liệu sau đăng ghi nhận là **0**.

| Bài đã đăng / URL | Ngày đăng và ngày đo | Chỉ số, mốc so và mức tiếp cận đúng độc giả | Phản hồi thật | Kết luận và bước tiếp |
|---|---|---|---|---|

## Câu hỏi chuyển Radar

Đã ghi các truy vấn và bằng chứng cần tìm cho kỳ sau trong [[marketing/linkedin/research/radar-2026-11-20#Câu hỏi từ LI-HANDOFF phiên bản 2]]. Mức tự tin vừa để chọn góc thăm dò, thấp về độ phổ biến tại Việt Nam và hiệu quả của quy tắc bàn giao.

## Bổ sung nghiên cứu 20/11

[[marketing/linkedin/research/radar-2026-11-20|Radar bàn giao sau go-live]] ghi đường tìm, phạm vi truy cập và trọng lượng từng nguồn. Hai giả thuyết cần phân biệt là phiếu thiếu người giữ lời hẹn và phiếu đã có người nhận nhưng thiếu ngữ cảnh hoặc điều kiện xử lý. Nghiên cứu Taobao cho thấy chat có thể ngắn hơn mà chưa thấy thay đổi có ý nghĩa thống kê ở lần liên hệ lại trong 7 ngày. Nguồn tiếng Việt tìm được là tiếng nói tư vấn và nhà cung cấp. Còn thiếu hồ sơ của trưởng ca hoặc CSKH tại Việt Nam. [Wang và cộng sự](https://arxiv.org/abs/2605.14830) · [Nguyễn Thiện Tâm](https://vn.linkedin.com/posts/tamsaigon72_enterpriseai-aicustomercare-digitaltransformation-activity-7508741133011746816-wuXm)
