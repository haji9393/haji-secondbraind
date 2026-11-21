# Đề xuất LinkedIn 24 và 26/11 | Cá nhân hoá, app push và chatbot trong CX

**Trạng thái** CHỜ THÁNG • CHỜ DUYỆT GÓC. Hai giả thuyết mới, bản 1. Đề xuất thay CRM A và AI A trong [[ban-giao-cmo-linkedin-2026-11-23|bàn giao trước]]. Kế hoạch tháng 11 chưa có bản duyệt trong thư mục strategy. Duyệt tháng có hai vị trí sửa, rồi duyệt từng góc trước khi sản xuất. [[marketing/linkedin/playbook|Playbook]] [[2026-11-19-dinh-vi-tru-lich-chi-so|Lịch tham khảo]]

**Định vị đang thử** Haji giúp đội CX và vận hành chọn bước tiếp theo theo trạng thái thật của khách và đo xem khách có hoàn tất việc. Độc giả chính là trưởng CX, lifecycle/CRM và CSKH tại doanh nghiệp Việt có app hoặc chatbot. Cả hai bài dùng tình huống đổi trả bán lẻ minh hoạ.

## 24/11 | Push theo trạng thái đơn

- **Trụ** CRM và vòng đời, với CX sau triển khai.
- **Góc chính** “Khách đã đặt lịch lấy hàng đổi trả. Vì sao app vẫn nhắc đặt lịch?” Cá nhân hoá bằng trạng thái yêu cầu. Chỉ xét gửi lời nhắc tùy chọn khi khách còn một bước làm được và bước đó còn hạn. Kiểm trạng thái sát lúc gửi, loại yêu cầu đã hoàn tất, đặt thời hạn lưu gửi (TTL) theo hạn thao tác, và mở thẳng màn hình đổi trả có trạng thái hiện tại. TTL giới hạn thời gian lưu tin chờ phát. Trạng thái vẫn có thể thay đổi sau lúc gửi, nên màn hình đích cần xử lý cả trường hợp khách đã đặt lịch. [[Hyper-Personalization]] [Firebase về TTL](https://firebase.google.com/docs/cloud-messaging/customize-messages/setting-message-lifespan)
- **Phương án hai** “Sau khi mở push, có thêm ai đặt lịch?” Chia ngẫu nhiên theo khách đủ điều kiện giữa nhóm gửi và nhóm giữ lại lời nhắc tùy chọn, giữ các thông báo vận hành cần thiết ở cả hai nhóm. Đo chênh lệch tỷ lệ đặt lịch đúng hạn trên toàn bộ khách được phân vào mỗi nhóm. Theo dõi tắt thông báo và liên hệ hỗ trợ cùng việc nếu có dữ liệu. Chốt cửa sổ đo và cỡ mẫu trước thử. Phản biện chính là khách có thể tự hoàn thành, và tỷ lệ mở chỉ cho thấy tương tác với tin. Chọn góc chính vì đội có thể rà một hành trình trước khi đủ lưu lượng thử nghiệm. [[Nhóm Đối Chứng Toàn Cục]] [Braze về nhóm đối chứng](https://www.braze.com/docs/user_guide/audience/global_control_group)
- **Nguồn và giới hạn** Một thử nghiệm trên app bán lẻ ghi nhận tăng tần suất push đại trà đi cùng tỷ lệ gỡ app cao hơn và tỷ lệ mở trực tiếp thấp hơn. Kết quả giới hạn ở thiết kế và bối cảnh nghiên cứu, chưa xác định tần suất cho lời nhắc đổi trả. Case nhà cung cấp tại Việt Nam mô tả dùng app push trong hành trình đa kênh, chưa tách tác động của push. Dùng case Việt Nam nội bộ để đối chiếu, giữ tên khách ngoài bản công khai khi chưa rõ quyền. [Nghiên cứu Wohllebe và cộng sự](https://real.mtak.hu/138580/1/IM_2021_02_Wohllebe.pdf) [Case đa kênh do nhà cung cấp công bố](https://insiderone.com/case-studies/seabank/)

## 26/11 | AI chatbot và quyền thực hiện

- **Trụ** AI trong dịch vụ, với CX sau triển khai.
- **Góc chính** “Chatbot nói đã đổi lịch lấy hàng. Hệ thống có ghi nhận chưa?” Chọn một yêu cầu rồi quyết định bot được tra cứu, hướng dẫn hay thực hiện. Tra cứu dựa trên trạng thái mới nhất từ hệ thống đơn. Đổi lịch chỉ báo thành công sau khi hệ thống nghiệp vụ xác nhận. Nếu quyền, trạng thái hoặc kết quả chưa rõ, nêu trạng thái thật và hướng khách sang bước hoặc người có thể xử lý. Kiểm đủ cảnh đặt được, hết khung giờ và chưa rõ kết quả. Đây là đề xuất vận hành.
- **Phương án hai** “Bot nên dừng ở bước nào khi lịch khách muốn đã hết?” Dùng nếu chưa có quyền ghi. Cho bot hướng dẫn lựa chọn còn khả dụng, hoặc chuyển người với mã yêu cầu và lý do, rồi xem tải phát sinh ở đội xử lý. Phản biện chính là giới hạn quyền có thể đẩy thêm việc sang nhân viên. Quyết định thử theo từng loại yêu cầu, dựa trên tỷ lệ hoàn thành được xác minh, tỷ lệ xác nhận sai và liên hệ lại cùng việc nếu nối được dữ liệu. Tỷ lệ hoàn thành tính trên toàn bộ yêu cầu đủ điều kiện được đưa vào luồng, gồm cả ca cần người hỗ trợ. Nếu chưa nối được kết quả nghiệp vụ, kiểm mẫu thủ công và ghi phần chưa xác minh.
- **Nguồn và giới hạn** Thử nghiệm thực địa Taobao ghi nhận chat ngắn hơn và điểm đánh giá giảm trong nhóm chat đủ điều kiện AI, chưa thấy thay đổi có ý nghĩa thống kê về liên hệ lại cùng việc trong 7 ngày. Đây là bản thảo nghiên cứu trên một nền tảng, có giới hạn về độ phủ chấm điểm. Case chatbot tiếng Việt xác nhận có triển khai thực tế, song do nhà cung cấp công bố và chưa kiểm chứng tiêu chí hoàn tất đổi lịch. [Nghiên cứu Taobao](https://arxiv.org/abs/2605.14830) [Case chatbot tiếng Việt](https://fpt.ai/case-studies/sendo-uses-fpt-ai-conversation-to-elevate-its-customer-service/)

## Biên tập và đo

Mở cả hai bài bằng một cảnh đổi trả có nhãn minh hoạ. Bài đầu cho thấy khách nhận tin gì và trạng thái yêu cầu lúc đó. Bài sau cho thấy lời bot nói và kết quả trong hệ thống. Dùng kinh nghiệm thiết kế hành trình và triển khai App Push của Haji ở mức đã xác minh. Phần chatbot dùng nghiên cứu gốc và phép kiểm đề xuất. Không gán số thị trường hay kết quả chatbot cho Haji. [[haji-cv-evidence-bank]] mục D, E3 và F.

**Giả định biên tập, tự tin vừa** Người phụ trách lifecycle phản hồi bằng quy tắc gửi/dừng cụ thể. Người phụ trách CSKH phản hồi bằng loại thao tác họ có thể hoặc chưa thể giao bot. Đếm phản hồi chuyên môn của đúng nhóm độc giả sau 7 ngày kể từ ngày đăng thực tế, dự kiến 01/12 và 03/12 nếu đăng đúng lịch. Bốn tuần đầu tạo mốc nền. Trường hợp thiếu bằng chứng tiếp cận đúng người ghi chưa đủ dữ liệu.

**Quyết định cần chốt** Lấy đổi trả bán lẻ làm ví dụ chung. Chọn trạng thái và thời hạn của lời nhắc làm góc 24/11. Chọn quyền thực hiện và kết quả được hệ thống xác nhận làm góc 26/11. Câu hỏi cho Radar là team Việt Nam nào đo hoàn tất tác vụ qua log nghiệp vụ, có tách được tác động của push hoặc chatbot trên cùng hành trình.

## Đối chiếu nguồn mở ngày 21/11/2026

Rà nhanh tài liệu công khai tiếng Việt và tiếng Anh, ưu tiên 2025–21/11/2026, giữ nghiên cứu bán lẻ 2021 vì có phân nhóm ngẫu nhiên. Tìm web theo miền LinkedIn và Substack, đối chiếu PDF gốc, tài liệu Firebase và case triển khai. Các nhánh tìm gồm `lifecycle push purchase already completed suppression holdout`, `nhắc khách đã mua app push`, `push notification abandon checkout opt out`, `chatbot order confirmation refund tool success`, `chatbot đổi lịch hoàn tiền xác nhận`. Chọn bài gốc có cơ chế, quan sát hoặc phép đo trực tiếp. Loại hồ sơ bán hàng chung và bài chỉ lặp số. Đây là lượt rà nhanh, không lập lưu đồ đếm kết quả.

- LinkedIn công khai, đọc được bài của [Zendesk về verified outcomes](https://www.linkedin.com/pulse/verified-outcomes-new-standard-service-heres-why-zendesk-l2vte?tl=en), Paulette Chafe, đăng 28/09/2026. Nhà cung cấp minh hoạ tra CRM, thử lại hoàn tiền và gửi mã xác nhận. Đây là ví dụ sản phẩm có lợi ích thương mại, trọng lượng thấp cho hiệu quả thực địa. Bài John Stuckey về dừng nhắc sau hoàn tất có bản lập chỉ mục, hai lượt mở URL gốc trả 404. Bài gốc của [Yournotify](https://vn.linkedin.com/pulse/omnichannel-customer-engagement-guide-using-whatsapp-sms-emailtogether-swsfe?tl=vi) mở được ngày 21/11, đề xuất dừng SMS và email sau khi mua. Ví dụ minh hoạ của nhà cung cấp, trọng lượng thấp cho hiệu quả app push. Phạm vi là web công khai, không bao phủ feed đăng nhập hay bình luận bị ẩn.
- Substack công khai, mở được bài của [Arslan Aziz, 13/07/2026](https://staffdatascientist.substack.com/p/the-complete-metric-design-framework). Tác giả kể một marketplace thấy lượt mở tăng nhưng đơn không tăng và có holdout hai tháng. Tự thuật không công bố dữ liệu hay cỡ nhóm, trọng lượng thấp cho hiệu quả, hữu ích để chọn chỉ số. [Karen Spinner, 28/09/2026](https://wonderingaboutai.substack.com/p/do-ai-chatbots-deny-more-refunds) tự chạy mô phỏng với tám mô hình và 36 tình huống, cho thấy chỉ dẫn tiết kiệm làm thay đổi quyết định chi trả. Bằng chứng gốc mô phỏng, trọng lượng vừa trong bộ tình huống, thấp với đổi lịch thực địa. Không bao phủ Notes, bài trả phí hay thảo luận trong tài khoản.

**Hai cách giải thích cần kiểm.** Push sai có thể do trạng thái đã đặt chưa đến hệ thống gửi, hoặc do tin hợp lệ lúc gửi nhưng đến sau khi khách đã đặt. Ghép dấu thời gian đặt, quyết định gửi và phát tin để phân biệt. Với bot, có thể hệ thống đã đổi lịch nhưng phản hồi xác nhận bị mất, hoặc thao tác chưa ghi nhận mà bot đã báo xong. Đối chiếu mã yêu cầu, trạng thái lịch và dấu thời gian trước khi thử lại.

**Còn thiếu.** Chưa thấy đội bán lẻ Việt Nam công bố log đổi trả nối trạng thái đơn với thời điểm gửi và nhận push, hoặc kết quả đặt lịch đúng hạn của nhóm giữ lại lời nhắc. Chưa thấy số liệu Việt Nam đối chiếu lời bot với lịch đã ghi, theo dõi riêng hết khung giờ và kết quả chưa rõ. Đủ cơ sở để trình hai góc minh hoạ. Hiệu quả tại Việt Nam vẫn là câu hỏi từ brief.

## Bàn giao Copywriter cho CMO | Phương án 24 và 26/11/2026

Đề xuất **24/11 A + 26/11 A**. Cùng dùng tình huống minh họa về lịch lấy hàng đổi trả. Bài 24/11 giúp đội Lifecycle quyết định điều kiện gửi. Bài 26/11 giúp đội CSKH quyết định khi nào bot được báo đã đổi lịch. Kế hoạch tháng và hai góc chờ Haji duyệt.

### 24/11 | CRM và vòng đời

| Luận điểm | Ai đọc và đang tin gì | Nguồn đổi cách nghĩ | Phản biện mạnh nhất | Quyết định hữu ích |
|---|---|---|---|---|
| **A. Khách đã đặt lịch. Vì sao app vẫn nhắc đặt?** | Lead Lifecycle/CX tin rằng lọc đúng đối tượng khi vào hành trình là đủ. | Yournotify minh họa việc dừng tin chờ sau giao dịch ở kênh khác. Firebase cho thấy tin được nhận để phát có thể vẫn đang chờ thiết bị. | Khách có thể đặt sau lần kiểm cuối nhưng trước lúc nhận tin. TTL chỉ giới hạn thời gian lưu tin chờ phát. | Đối chiếu giờ đặt, giờ quyết định gửi và giờ tới thiết bị nếu đo được. Nếu trạng thái cập nhật chậm, kiểm lại ở nguồn đơn sát lúc gửi. Nếu tin tới muộn, đặt TTL theo thời gian còn hữu ích. Chỉ nhắc khi khách còn bước làm được và còn hạn. Mở thẳng màn hình đổi trả hiển thị trạng thái hiện tại. |
| **B. Lời nhắc giúp thêm bao nhiêu khách đặt lịch đúng hạn?** | Lead CRM xem tỷ lệ mở và số lịch đặt sau khi khách bấm là bằng chứng lời nhắc có tác dụng. | Aziz kể lượt mở tăng trong khi số đơn đi ngang. Đây là tự thuật thiếu dữ liệu công khai. Tài liệu Braze giải thích cách dùng nhóm giữ lại để đo phần tăng thêm. | Khách có thể tự đặt lịch. Hành trình đổi trả có thể thiếu mẫu để phân biệt tác động nhỏ với nhiễu. | Khi đủ mẫu, phân ngẫu nhiên theo khách đủ điều kiện, giữ thông báo vận hành ở cả hai nhóm và chỉ giữ lại lời nhắc tùy chọn ở nhóm đối chứng. So tỷ lệ đặt đúng hạn trên toàn bộ khách được phân nhóm và theo dõi tắt thông báo. Chốt cỡ mẫu và cửa sổ đo trước thử. |
| **C. Có nên gửi thêm lần nhắc thứ hai?** | Quản lý CRM thấy còn yêu cầu chưa đặt lịch và muốn tăng tần suất. | Wohllebe và cộng sự quan sát nhiều lượt gỡ app hơn và tỷ lệ mở trực tiếp giảm khi tăng tần suất push đại trà trong thử nghiệm bán lẻ Đức. | Lời nhắc đổi trả gắn với hạn và có thể được khách mong đợi. Nghiên cứu không xác định tần suất phù hợp cho bước này. | Nếu đang cân nhắc lần nhắc thứ hai, chỉ thử với khách vẫn còn bước phải làm và còn hạn. Giữ lần nhắc đầu giống nhau, giữ lại riêng lần hai ở nhóm đối chứng. Đọc số lịch đặt đúng hạn cùng tỷ lệ tắt thông báo. |

### 26/11 | AI trong dịch vụ

| Luận điểm | Ai đọc và đang tin gì | Nguồn đổi cách nghĩ | Phản biện mạnh nhất | Quyết định hữu ích |
|---|---|---|---|---|
| **A. Bot nói đã đổi lịch. Hệ thống ghi lịch mới chưa?** | Trưởng CSKH hoặc QA bot xem câu báo thành công hoặc chat đã đóng là dấu hiệu đủ. | Paulette Chafe minh họa bằng giao dịch hoàn tiền đã xác minh và mã xác nhận. Taobao cho thấy thời lượng chat, điểm đánh giá và liên hệ lại có thể kể các câu chuyện khác nhau. | Phản hồi xác nhận có thể bị mất sau khi lịch đã đổi. Thử lại ngay có thể lặp thao tác. | Kiểm ba cảnh đổi được lịch, hết khung giờ và chưa rõ kết quả. Khi chưa rõ, tra theo mã yêu cầu trước khi thử lại. Chỉ báo đã đổi sau khi hệ thống đơn xác nhận lịch mới. Tính tỷ lệ hoàn tất có xác nhận trên mọi yêu cầu đủ điều kiện vào luồng, kể cả chuyển người. Trong các ca bot báo xong, đo tỷ lệ báo xong sai và giữ riêng ca chưa đối chiếu được. |
| **B. Bot được tra cứu, hướng dẫn hay đổi lịch?** | Chủ sản phẩm bot hoặc trưởng CSKH tin rằng bot hiểu yêu cầu và tra được đơn thì có thể tự đổi. | Case Sendo mô tả trả lời và tra thông tin đơn. Mô phỏng của Spinner gợi ý rằng chỉ dẫn tiết kiệm có thể đổi quyết định chi trả trong các tình huống được thử. | Giới hạn quyền ghi có thể tăng tải nhân viên và buộc khách chờ. Kết quả mô phỏng hoàn tiền chưa nói được gì về hiệu quả đổi lịch. | Chọn một loại yêu cầu và chốt quyền theo năng lực hệ thống. Cho tra lịch nếu có dữ liệu, hướng dẫn khi chưa có quyền ghi, cho đổi khi có quyền và xác minh được kết quả. Khi chuyển, kèm mã yêu cầu và lý do. Theo dõi tải chuyển cùng tỷ lệ hoàn tất có xác nhận. |
| **C. Hết khung giờ khách muốn. Khi nào nên chuyển người?** | Quản lý phân tuyến muốn để bot thử hết các bước trước khi chuyển. | Phân tích ghép cặp trong preprint Taobao thấy kết quả khác nhau giữa các ca chuyển vì giới hạn kỹ thuật và các ca chuyển khi khách đã bức xúc. | Ca khách bức xúc có thể vốn khó hơn. Dữ liệu chưa xác định ngưỡng chuyển, và chuyển sớm có thể kéo dài hàng chờ. | Với một loại yêu cầu, cho khách chọn giờ còn phù hợp nếu có. Khi bot không thể đưa ra bước tiếp theo, thử chuyển kèm mã yêu cầu và lý do. So thời gian chờ, tải hàng đợi và tỷ lệ hoàn tất có xác nhận. |

### Thủ pháp viết và chất liệu

Học **Paulette Chafe** cách theo một yêu cầu qua lời khách nghe và bằng chứng khách có thể kiểm. Mở bằng một câu nhắc đặt lịch hoặc lời bot báo đã đổi. Đặt ngay sau đó trạng thái trên màn hình đổi trả hoặc bản ghi lịch mới. Kết bằng câu hỏi mà đội vận hành có thể trả lời bằng một lần kiểm log. [Bài gốc của Chafe](https://www.linkedin.com/pulse/verified-outcomes-new-standard-service-heres-why-zendesk-l2vte?tl=en)

- **Minh họa.** Toàn bộ cảnh bán lẻ, lời khách và lời bot đều giả định. Bài của Chafe là ví dụ sản phẩm. SeABank và Sendo là triển khai do nhà cung cấp công bố, chưa có số đo riêng cho hai quyết định.
- **Trải nghiệm thật của Haji.** Có thể kể ở ngôi thứ nhất về công việc thiết kế hành trình và triển khai App Push ở phạm vi đã xác minh. Giữ cảnh đổi trả có nhãn minh họa. Bài chatbot dựa trên nguồn công khai và đề xuất phép kiểm. [[haji-cv-evidence-bank]] mục D, E3 và F.

### Ghi chú cho Designer

- **24/11 A.** Đặt câu nhắc cạnh trạng thái “đã đặt lịch”. Nếu có hình, dùng hai dòng thời gian để người đọc thấy giờ đặt nằm trước lúc quyết định gửi hay giữa lúc gửi và lúc nhận. Gắn nhãn “Tình huống minh họa”.
- **26/11 A.** Đặt lời bot cạnh trạng thái lịch trong hệ thống đơn. Dùng ba hàng cho xác nhận thành công, hết khung giờ và chưa rõ kết quả. Bản text có thể dùng ngay sau khi duyệt góc.

### Haji kiểm lại

1. Chốt kế hoạch tháng và cặp 24/11 A, 26/11 A.
2. Xác nhận câu nào về trải nghiệm App Push của Haji có thể kể công khai.
3. Cân nhắc 24/11 B nếu đủ mẫu cho nhóm đối chứng, hoặc 26/11 B nếu hệ thống chưa cho bot ghi và xác nhận lịch mới.

### URL gốc cho CMO

- **24/11.** [Firebase, thời hạn lưu tin](https://firebase.google.com/docs/cloud-messaging/customize-messages/setting-message-lifespan) · [Braze, nhóm đối chứng](https://www.braze.com/docs/user_guide/audience/global_control_group) · [Arslan Aziz, Substack](https://staffdatascientist.substack.com/p/the-complete-metric-design-framework) · [Wohllebe và cộng sự, thử nghiệm tần suất push](https://real.mtak.hu/138580/1/IM_2021_02_Wohllebe.pdf) · [Yournotify, LinkedIn](https://vn.linkedin.com/pulse/omnichannel-customer-engagement-guide-using-whatsapp-sms-emailtogether-swsfe?tl=vi) · [Insider One, case SeABank](https://insiderone.com/case-studies/seabank/).
- **26/11.** [Paulette Chafe, LinkedIn](https://www.linkedin.com/pulse/verified-outcomes-new-standard-service-heres-why-zendesk-l2vte?tl=en) · [Wang và cộng sự, preprint](https://arxiv.org/abs/2605.14830) · [PDF, mục 3.5, 4 và 5](https://arxiv.org/pdf/2605.14830) · [Karen Spinner, Substack](https://wonderingaboutai.substack.com/p/do-ai-chatbots-deny-more-refunds) · [FPT.AI, case Sendo](https://fpt.ai/case-studies/sendo-uses-fpt-ai-conversation-to-elevate-its-customer-service/).
