---
type: source
source_kind: own-note
status: processed
created: 2026-11-17
processed_at: 2026-11-17
wiki_links: ["[[Bộ Chỉ Số Martech Hàng Không]]", "[[Catalog Theo Điểm Đến]]", "[[Cứu Giỏ Bỏ Dở Hàng Không]]", "[[Nhóm Đối Chứng Toàn Cục]]", "[[Dữ Liệu Khách Hàng Hàng Không]]", "[[Hành Trình Khách Hàng Hàng Không]]", "[[Ancillary Revenue Hàng Không]]", "[[Hàng Không - Bản Đồ Martech]]"]
url: ""
---
# Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17

Haji dán trong chat Javis ngày 17/11/2026 23:18, nguồn thứ 3 của ngành hàng không, sau [[Haji - Tổng hợp Hàng không và Du lịch 2026-11-17]] và [[Haji - Ancillary Revenue Hàng không 2026-11-17]]. Haji dặn: gom hết thông tin của ngành trước, xử lý một thể sau; đã xử lý cùng 2 nguồn trước ngày 17/11/2026. Gồm 3 phần: (1) đặc trưng ngành, metrics, tactics, lưu ý kỹ thuật; (2) Destination-Based Catalog; (3) Cart Abandonment Recovery. Các dòng "." đứng riêng và các số dính vào chữ (vd "Aviation1", "more_horiz") là dấu trích dẫn của công cụ tổng hợp, giữ nguyên. Tài liệu gốc không đính kèm, số liệu chưa ghi năm.

---

1. Các đặc trưng riêng biệt của Ngành Hàng không ảnh hưởng đến MarTech
Sản phẩm có tính biến mất giá trị ngay lập tức (Perishable Inventory): Một ghế trống trên chuyến bay sẽ rơi về giá trị bằng 0 ngay khi máy bay rời khỏi cửa cất cánh (pushback)
. Do đó, các chiến dịch MarTech phải hyper-aware về mốc thời gian khởi hành
.
Định giá động & Cấu trúc Hạng vé phức tạp (Dynamic Pricing & Fare Classes): Giá vé thay đổi liên tục theo thuật toán của hệ thống Quản trị Doanh thu (RMS như PROS, Amadeus, Sabre)
. Ghế bay được chia thành các "hạng vé/fare buckets" (Y, B, M, H, Q...) quy định quyền lợi đi kèm
.
Tỷ lệ bỏ dở phễu đặt vé siêu cao (Cart Abandonment 80% – 90%): Quy trình đặt vé đòi hỏi cam kết tài chính lớn, nhập thông tin hộ chiếu và nhiều bước phức tạp
.
Đơn hàng chứa nhiều hành khách (PNR - Passenger Name Record): Một giao dịch PNR có thể chứa từ 1 đến 9 hành khách
. Mã PNR thay đổi theo từng lần đặt vé nên không bao giờ được dùng PNR làm ID định danh chính
.
Chi phí API từ hệ thống vận hành PSS bị tính phí (Commercially Metered PSS APIs): Các nhà cung cấp Passenger Service System (Amadeus, Sabre) tính phí trên từng lượt truy vấn API
.
2. Bộ Metrics (Chỉ số) cốt lõi để đo lường hiệu quả MarTech
A. Chỉ số Doanh thu & Tối ưu Chi phí Cấp C-Suite
Direct Channel Shift & GDS Fee Avoidance: Tỷ lệ chuyển dịch đặt vé từ kênh trung gian (OTA/GDS) về kênh trực tiếp (Website/App chính hãng)
. Mỗi booking qua GDS tiêu tốn $8 – $15/chặng, trong khi kênh trực tiếp chỉ tốn $1 – $3/chặng
.
Ancillary Revenue per Pax & Attach Rate: Doanh thu dịch vụ bổ trợ trên mỗi hành khách và tỷ lệ đính kèm dịch vụ phụ (mức chuẩn ngành là 15% – 25%)
.
Tỷ lệ chênh lệch PRASK vs CASK: Tăng trưởng doanh thu trên mỗi ghế-km (PRASK) so với chi phí vận hành trên mỗi ghế-km (CASK)
.
Passenger Load Factor (PLF): Hệ số lấp đầy ghế (mức trung bình kỷ lục hiện tại là 84.6%)
.
B. Chỉ số Hiệu quả Chuyển đổi & Kênh Số (Digital & MarTech KPIs)
Look-to-Book (L2B) Ratio: Tỷ lệ lượt tìm kiếm chuyến bay so với lượt hoàn tất đặt vé thực tế
.
Flight Cart Recovery Rate: Tỷ lệ khôi phục thành công các giao dịch bỏ dở phễu thanh toán
.
Tỷ lệ Tương tác Kênh Native:
Web Push CTR: Đạt 4% – 8% (các thông báo Price Watch cảnh báo giảm giá có tỷ lệ chuyển đổi cao gấp 6 lần App Push)
.
App Opt-In Rate: Đạt 50% – 60% (do hành khách cần nhận thông tin vận hành giờ bay, cổng lên máy bay)
.
WhatsApp Read Rate: Đạt lên tới 68% đối với tin nhắn hội thoại
.
3. Tactics (Chiến thuật) Triển khai MarTech Hiệu quả
Thông điệp Phù hợp Hạng vé (Fare-Class-Aware Personalization): Loại trừ các gợi ý thừa thãi (ví dụ: không bao giờ gửi thông điệp bán "Ưu tiên lên máy bay" cho hành khách mua vé hạng Business vì đặc quyền này đã bao gồm sẵn trong hạng vé)
.
Chuỗi Pre-Flight Upsell Cascade: Phân tầng chiến dịch tự động theo các mốc thời gian:
T-7 ngày: Gợi ý dịch vụ bên thứ ba (khách sạn, thuê xe, tour)
.
T-48 giờ: Mời đấu giá nâng hạng ghế (Upgrade Bidding) hoặc chọn chỗ chân rộng
.
T-24 giờ: Nhắc nhở check-in trực tuyến và bán bổ sung hành lý ký gửi
.
Bám đuổi đa kênh & Bán hàng Hội thoại (WhatsApp Commerce): Tự động kích hoạt luồng bám đuổi khôi phục đặt vé (Web Push → App Push → WhatsApp)
. WhatsApp Commerce cho phép hành khách tái khởi động luồng đặt vé và mua bổ trợ trực tiếp ngay trong giao diện chat
.
Đòn bẩy Bằng chứng Xã hội (Social Proof Overlays): Hiển thị các thông báo thời gian thực ("63 khách hàng đang xem chuyến bay này" hoặc "70% hành khách chọn chỗ chân rộng") để thúc đẩy quyết định tức thì
.
Đo lường Doanh thu Tăng thêm bằng Nhóm Đối chứng (5% Global Holdout): Duy trì một nhóm 5% khách hàng không nhận chiến dịch tiếp thị để chứng minh hiệu quả tăng trưởng doanh thu thực tế (Incremental Revenue Uplift) cho CFO
.
4. Các lưu ý Quan trọng về Quản trị & Kỹ thuật (Key Considerations)
A. Tránh bùng nổ Chi phí API PSS (API Economics)
Không ping trực tiếp PSS: Tuyệt đối không để MarTech Platform gọi API trực tiếp sang Amadeus hay Sabre mỗi khi khách tìm kiếm trên Web/App
.
Giải pháp Caching & Webhooks: Sử dụng bộ đệm trung gian (Fare Cache API), đồng bộ theo lô (Batch sync 2 lần/ngày) đối với giá vé tĩnh
. Chỉ dùng Webhook thời gian thực cho các sự kiện khẩn cấp (hoãn/hủy chuyến)
.
B. Chiến lược Lưu trữ Dữ liệu (Extended TTL Strategy)
Khác với bán lẻ chỉ giữ dữ liệu 90 ngày, hành vi du lịch có vòng đời rất dài
:
Dữ liệu Tìm kiếm (Flight Search): Cần lưu giữ 12 tháng (vì khách hàng tìm kiếm vé trước cả năm)
.
Dữ liệu Đặt vé (Purchases): Cần lưu giữ 36 – 60 tháng (để phân tích thói quen du lịch định kỳ hàng năm)
.
Sự cố Chuyến bay (Disruption Data): Lưu giữ 365 ngày làm cờ chặn (suppression flag), tránh gửi tin nhắn khuyến mãi khi khách hàng vừa trải qua sự cố hoãn/hủy chuyến
.
Lỗi Thanh toán (Payment Failure): Chỉ lưu giữ 7 ngày (vì PNR bị hủy sau 1 tuần, gửi retargeting sau 7 ngày sẽ dẫn khách vào link lỗi)
.
C. Định danh & Bảo mật Dữ liệu (PII & Identity)
Sử dụng Identity Hierarchy chuẩn: Ưu tiên theo thứ tự Loyalty ID (Mã hội viên) > Email > Phone Number
. Tuyệt đối không dùng mã PNR làm định danh chính
.
Bảo mật PCI DSS & PII: Mã hóa SHA-256 cho Loyalty ID và thông tin cá nhân
. Không bao giờ thu thập hoặc lưu trữ số Hộ chiếu chưa mã hóa hay thông tin thẻ tín dụng (PAN/CVV) trên nền tảng MarTech
.
D. Phân tách rành mạch Tin nhắn Marketing & Tin nhắn Vận hành
Tin nhắn vận hành (thẻ lên máy bay, thay đổi cổng, hủy chuyến) có quyền gửi mà không cần Opt-in marketing của khách hàng
. Tuy nhiên, tuyệt đối không được lồng ghép nội dung quảng cáo/upsell vào tin nhắn vận hành để tránh vi phạm pháp luật chống spam quốc tế (GDPR, TCPA)
.
Frequency Capping & Suppress T-4h: Tự động chặn toàn bộ thông điệp tiếp thị trước giờ bay 4 tiếng để dành không gian màn hình cho thông tin làm thủ tục tại sân bay
.
---
Cấu trúc Dữ liệu Catalog theo Điểm đến (Destination-Based Catalog) là một giải pháp kiến trúc được thiết kế riêng cho ngành Hàng không1. Mô hình này giải quyết triệt để các hạn chế của catalog thương mại điện tử truyền thống khi đối mặt với dữ liệu vé máy bay có tính biến mất giá trị ngay lập tức (Perishable Inventory)23 và biến động giá theo thuật toán (Dynamic Pricing)4.1. Tại sao Mô hình Catalog Truyền thống ("Time-Based") Thất bại trong Hàng không?Thách thức Dữ liệu Thưa thớt (Data Sparsity): Khi xây dựng catalog theo mốc thời gian cụ thể (ví dụ: tạo SKU riêng cho "Chuyến bay SQ326 đến London ngày 12/12"), dữ liệu truy cập bị phân tán nghiêm trọng5. Chỉ có khoảng 5% – 10% hành khách tìm kiếm vé máy bay trước thời điểm bay trên 3 tháng5.Không đủ Dữ liệu Huấn luyện AI: Lượng traffic truy cập vào một ngày bay cụ thể trong tương lai là quá ít, khiến các thuật toán Machine Learning (như Collaborative Filtering) không có đủ dữ liệu để học và đề xuất chính xác56.Vấn đề Vòng đời Sản phẩm: Chuyến bay theo ngày cụ thể sẽ nhanh chóng hết hạn hoặc hết chỗ ngay sau khi máy bay cất cánh2more_horiz.2. Giải pháp Cấu trúc Destination-Based CatalogA. Gom nhóm theo Điểm đến (Destination-Level Aggregation)Thay vì tạo catalog theo từng ngày bay riêng biệt, hệ thống tổng hợp tất cả lượt tìm kiếm và đặt vé dưới ô dù của một Điểm đến chung (ví dụ: "London" hoặc "Tokyo")18.Việc gom nhóm này giúp tập trung toàn bộ lưu lượng truy cập (high-volume traffic) về một đầu mối dữ liệu, cung cấp mật độ dữ liệu dày đặc cho máy học để nhận diện xu hướng và đưa ra đề xuất tối ưu1.B. Ánh xạ Mã Thành phố (City-Code Mapping)Hợp nhất nhiều Sân bay: Một thành phố lớn thường sở hữu nhiều sân bay khác nhau (ví dụ: London có Heathrow - LHR, Gatwick - LGW, Stansted - STN)1.Cơ chế Mapping: Hệ thống tự động ánh xạ các mã sân bay IATA riêng lẻ này về một Mã thành phố cha duy nhất (ví dụ: LON)1.Hiển thị Giá "Chỉ từ" (Starting From Price): Nhờ tổng hợp toàn bộ các sân bay trong cùng thành phố, thuật toán đề xuất (Smart Recommender) có thể quét tất cả chuyến bay khả dụng để hiển thị mức giá khởi điểm thấp nhất nhằm thu hút khách hàng1.3. Cấu trúc Định danh Mã Sản phẩm Bắt buộc (Custom Aviation ID Structure)Hàng không không thể sử dụng mã SKU bán lẻ hay mã PNR/Số hiệu chuyến bay để làm ID catalog79. Cấu trúc Custom ID tiêu chuẩn bắt buộc phải tuân theo cú pháp89:$$\text{Custom Item ID} = \mathbf{Origin-Destination} \mid \mathbf{Cabin\ Class} \mid \mathbf{Trip\ Type}$$Ví dụ thực tế: LON-HND | Business | OneWay hoặc SIN-NRT | O | E (Singapore đến Narita | OneWay | Economy)89.Ý nghĩa Chiến lược:Phân tầng chính xác theo hạng khoang để tránh sai sót truyền thông (ví dụ: không gợi ý vé hạng Phổ thông cho hành khách đang tìm kiếm vé hạng Thương gia)9.Ưu tiên cấu hình chuyến bay Một chiều (OneWay) trong catalog vì luồng này tự nhiên hiển thị mức giá khởi điểm thấp nhất, tạo đòn bẩy kích thích chuyển đổi ban đầu9.4. Quản lý Catalog Dịch vụ Bổ trợ (Ancillary Catalog Management)Lưu trữ Hợp nhất & Bộ lọc Phân loại (Category Filters): Các dịch vụ phụ phí (Hành lý ký gửi, Chọn chỗ ngồi, Suất ăn, Bảo hiểm) được lưu trữ ngay bên trong catalog chuyến bay nhưng được phân tách bằng các bộ lọc danh mục riêng10.Mô hình "Top Purchased Ancillaries":Điểm Số Thiên hướng (Propensity Score): Đánh giá xác suất dựa trên cả lượt click xem (ví dụ: xem sơ đồ chỗ ngồi) và lượt mua thực tế11.Trọng số Ưu tiên Kinh doanh (Business-Priority Weighting): Hãng hàng không có thể can thiệp thuật toán bằng cách gán trọng số ưu tiên cho các dịch vụ có biên lợi nhuận cao (như Bảo hiểm du lịch) để đẩy lên vị trí hiển thị đầu tiên11.Cơ chế Loại trừ & Dự phòng (Exclusion & Fallback Logic): Nếu hành khách đã thêm Hành lý vào giỏ hàng, hệ thống tự động loại bỏ gợi ý Hành lý và chuyển sang đề xuất dịch vụ kế tiếp như Vé vào phòng chờ (Lounge Access)6.5. Thuật toán Đề xuất & Tối ưu Chi phí API PSS (API Economics)Lựa chọn Thuật toán:Collaborative Filtering: Hoạt động hiệu quả nhất nhờ tận dụng lưu lượng truy cập lớn của website/app hàng không6.Gắn thẻ Chủ đề (Thematic Tagging): Đối với thuật toán User-Based, do tuyến bay không có "thể loại" tự nhiên như phim ảnh, các chặng bay được gắn thêm thuộc tính phong cách sống (ví dụ: chặng đi Geneva được gắn thẻ Ski, Paris gắn thẻ Romance, Bali gắn thẻ Beach) để AI đề xuất theo sở thích du lịch12.Kiến trúc Tránh bùng nổ Chi phí API PSS:Các hệ thống PSS (Amadeus, Sabre) tính phí trên từng lượt truy vấn API13more_horiz.Dữ liệu giá vé được đẩy trực tiếp sang Catalog API hoặc truy vấn từ bộ đệm giá vé tĩnh ("Fare Deals" cache)Synced theo chu kỳ để hiển thị cho người dùng1617.Real-Time Widget Refresh: Đối với các đường bay biến động mạnh, hệ thống chỉ kích hoạt làm mới giá thực tế ngẫu nhiên tại đúng thời điểm widget đề xuất được tải trên màn hình người dùng
Tỷ lệ bỏ dở phễu đặt vé trong ngành Hàng không thuộc hàng cao nhất (khoảng 80% – 90%) do quy trình thanh toán phức tạp, cam kết tài chính cao và sự biến động liên tục của giá vé theo thuật toán định giá động
.
Chiến lược tối ưu hóa và khôi phục đặt vé bỏ dở (Flight & Cart Abandonment Recovery) được tổng hợp qua 4 trụ cột chiến thuật chính:
1. Tối ưu hóa phễu thanh toán ngay tại điểm chạm (Onsite Personalization)
Exit-Intent Overlays & Trust Badges: Hiển thị popup bắt trúng hành vi chuẩn bị thoát trang khi người dùng có ý định sang trang đối thủ/OTA để so sánh giá
. Đưa ra câu nhắc giải tỏa rào cản tâm lý ("Miễn phí hủy/đổi trong 24h" hoặc "Cam kết giá tốt nhất") ngay tại trang thanh toán
.
Đòn bẩy bằng chứng xã hội (Social Proof Overlays): Hiển thị thông báo thời gian thực như "63 khách hàng đang xem chuyến bay này và 14 khách đã đặt trong 24h qua" hoặc "Chỉ còn 3 ghế giá này" để kích thích hành khách ra quyết định hoàn tất giao dịch ngay lập tức
.
Đồng bộ giá theo thời gian thực (Real-Time Price Handling): Tránh hiển thị giá vé tĩnh đã hết hạn (gây trải nghiệm tiêu cực cho khách hàng); sử dụng bộ đệm Fare Cache API hoặc làm mới giá thực tế ở cấp độ widget để đảm bảo tính chính xác
.
2. Chuỗi bám đuổi khôi phục tự động đa kênh (Omnichannel Recovery Journeys)
Tối ưu hóa giỏ hàng đòi hỏi sự phối hợp nhịp nhàng giữa các kênh tiếp thị theo kịch bản tự động (Architect Journeys)
:
Web Push Notifications: Tiếp cận hành khách ẩn danh hoặc chưa tải app trên trình duyệt Web/Desktop với tỷ lệ click CTR từ **4% – 8%**
. Đặc biệt, tính năng cảnh báo giảm giá vé (Price Watch / Price Drop) mang lại tỷ lệ chuyển đổi vé cao gấp 6 lần so với App Push ở một số triển khai
.
App Push Notifications: Tận dụng tỷ lệ bật nhận thông báo cao của ứng dụng di động (50% – 60%) để gửi thông điệp nhắc nhở hoàn tất giữ chỗ kèm mã ưu đãi dành riêng
.
Conversational Commerce qua WhatsApp: Gửi thông báo bám đuổi chứa đầy đủ chi tiết chặng bay, hình ảnh và nút bấm Call-To-Action
. Tính năng WhatsApp Commerce cho phép hành khách tái khởi động luồng đặt vé và mua bổ sung các dịch vụ phụ phí (hành lý, chỗ ngồi) ngay trong giao diện chat mà không cần thao tác lại từ đầu trên website
.
3. Phân tập dữ liệu theo Bối cảnh & Động lực mua hàng (Contextual Segmentation)
Phân tầng theo vị trí bỏ dở (Funnel Step Drop-off): Phân tách rõ giữa nhóm người dùng bỏ dở ở bước tìm kiếm (Search Abandoner), bước điền thông tin hộ chiếu (Passenger Info Completed) hay bước chọn phương thức thanh toán (Payment Fail / Abandoner)
. Nhóm bỏ dở tại bước thanh toán với giá trị đơn hàng lớn sẽ được xếp vào tệp ưu tiên bám đuổi khẩn cấp (High-Value Cart Abandoners)
.
Phân tập theo Chân dung (Persona-Aware Treatment):
Hành khách nhạy cảm về giá (Budget Vacationer): Đề xuất mã giảm giá % hoặc tặng kèm suất ăn/hành lý ký gửi
.
Hội viên thân thiết (Loyalty Members): Kích hoạt động lực tích điểm dặm thưởng gấp đôi hoặc nâng hạng ghế nếu hoàn tất đặt vé trong cửa sổ thời gian ngắn
.
Tự động hóa bằng Trí tuệ nhân tạo (AI Engine): Ứng dụng Next Best Channel (NBC) để dự đoán kênh có khả năng chuyển đổi cao nhất cho từng cá nhân và Send Time Optimization (STO) để gửi tin nhắn vào đúng thời điểm người dùng dễ mở máy nhất
.
4. Tối ưu kỹ thuật & Tránh ma sát vận hành (Technical Safeguards)
Loại trừ dữ liệu giao dịch offline (Offline-to-Online Suppression): Đồng bộ dữ liệu đặt vé từ quầy/Call Center qua Upsert API để ngay lập tức chặn (suppress) các chiến dịch bám đuổi đối với khách hàng đã thanh toán qua kênh trực tiếp hoặc đại lý, tránh gây phiền hà cho hành khách và lãng phí ngân sách tiếp thị
.
Quản trị hạn định dữ liệu (TTL Strategy): Dữ liệu giỏ hàng bị bỏ dở được lưu trữ và bám đuổi tối ưu trong vòng 30–60 ngày
. Riêng với các trường hợp lỗi thanh toán (Payment Failure), kịch bản cứu giỏ hàng chỉ nên kích hoạt tối đa trong 7 ngày trước khi PNR bị hệ thống PSS tự động hủy
.
