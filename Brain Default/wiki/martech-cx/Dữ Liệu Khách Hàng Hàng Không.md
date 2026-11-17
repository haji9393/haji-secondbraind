---
type: wiki
status: active
tags: [wiki, martech-cx, hang-khong]
created: 2026-11-17
updated: 2026-11-17
source: "[[Haji - Tổng hợp Hàng không và Du lịch 2026-11-17]], [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]]"
---
# Dữ Liệu Khách Hàng Hàng Không

Tầng dữ liệu là chỗ đề xuất martech hàng không hay chết nhất: gọi PSS tốn tiền, định danh sai, giữ dữ liệu sai hạn, hoặc trộn tin tiếp thị vào tin vận hành.

## Chi phí gọi PSS

- Hệ thống đặt chỗ (PSS: Amadeus, Sabre, Navitaire) tính phí trên từng lượt gọi API [[Haji - Tổng hợp Hàng không và Du lịch 2026-11-17]] [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- Luật: tuyệt đối không gọi thẳng PSS để hiển thị cá nhân hoá trên web/app [[Haji - Tổng hợp Hàng không và Du lịch 2026-11-17]].
- Cách làm: dựng bộ đệm trung gian (Fare Cache API), đồng bộ theo lô 2 lần/ngày, chỉ dùng webhook thời gian thực cho sự kiện khẩn như chậm hoặc huỷ chuyến [[Haji - Tổng hợp Hàng không và Du lịch 2026-11-17]].
- Với hệ gợi ý, cách tổ chức catalog để giảm số lượt gọi xem [[Catalog Theo Điểm Đến]].

## Thời gian giữ dữ liệu (TTL)

Bán lẻ thường giữ khoảng 90 ngày, còn chu kỳ tìm và đặt vé máy bay kéo dài cả năm [[Haji - Tổng hợp Hàng không và Du lịch 2026-11-17]].

| Loại dữ liệu | Thời gian giữ | Nguồn |
|---|---|---|
| Lịch sử tìm chuyến bay | 12 tháng | [[Haji - Tổng hợp Hàng không và Du lịch 2026-11-17]] |
| Lịch sử mua | 36-60 tháng, để thấy thói quen du lịch hằng năm | [[Haji - Tổng hợp Hàng không và Du lịch 2026-11-17]] |
| Hạng hội viên | Giữ cố định | [[Haji - Tổng hợp Hàng không và Du lịch 2026-11-17]] |
| Dữ liệu sự cố (chậm, huỷ chuyến) | 365 ngày, dùng làm cờ chặn quảng cáo cho khách vừa gặp sự cố | [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]] |
| Giỏ hàng bỏ dở | 30-60 ngày | [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]] |
| Lỗi thanh toán | Tối đa 7 ngày, trước khi PSS tự huỷ PNR | [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]] |

Cách đọc bảng: TTL không phải "giữ càng lâu càng tốt" mà khớp với vòng đời của tín hiệu. Tìm kiếm 12 tháng dùng cho gợi ý điểm đến; giỏ 30-60 ngày dùng cho bám đuổi; lỗi thanh toán 7 ngày vì sau đó PNR không còn để cứu. Ba con số không mâu thuẫn nhau. (Diễn giải của Javis.)

## Định danh khách hàng

- Không bao giờ dùng mã đặt chỗ (PNR) làm ID chính: PNR đổi theo mỗi lần đặt [[Haji - Tổng hợp Hàng không và Du lịch 2026-11-17]], và một PNR có thể chứa 1-9 hành khách [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- Thứ bậc định danh: Loyalty ID trước, rồi Email, rồi Số điện thoại, băm SHA-256 [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- Nguồn 1 liệt kê các khoá ưu tiên gồm mã hội viên (Frequent Flyer ID), CRM ID, email/số điện thoại băm SHA-256, nhưng không xếp thứ tự [[Haji - Tổng hợp Hàng không và Du lịch 2026-11-17]]. Xem mục Mâu thuẫn.

## Bảo mật thanh toán (PCI DSS)

- Không lưu số hộ chiếu dạng thô, số thẻ (PAN) hay CVV trên nền tảng martech [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].

## Tách tin vận hành và tin tiếp thị

- Tin vận hành (thẻ lên máy bay, đổi cổng, chậm chuyến) và tin tiếp thị phải tách luồng; không chèn bán thêm vào tin vận hành, để tuân thủ GDPR, TCPA [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- Chặn mọi tin tiếp thị trong 4 giờ trước giờ khởi hành [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]]. Điểm này vênh với kịch bản geofence sân bay, xem [[Hành Trình Khách Hàng Hàng Không]].

## Hợp nhất dữ liệu nhiều thương hiệu trong tập đoàn

- Nối dữ liệu giữa hãng mẹ, hãng giá rẻ con và app tiện ích (ví dụ Singapore Airlines, Scoot, Kris+) mà không vi phạm quy định bảo mật dữ liệu cá nhân (PII) giữa các công ty thành viên [[Haji - Tổng hợp Hàng không và Du lịch 2026-11-17]].
- Nguồn gọi giải pháp này là Group Level Unification (GLU). Tên gọi có thể là thuật ngữ của nhà cung cấp, ghi ở [[Insider - Lớp Add-on]] (cần xác minh).

## Mâu thuẫn

- **Thứ tự khoá định danh:** nguồn 3 xếp Loyalty ID > Email > Phone [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]]; nguồn 1 có thêm CRM ID mà không xếp hạng [[Haji - Tổng hợp Hàng không và Du lịch 2026-11-17]]. Chưa rõ CRM ID đứng ở đâu. Gợi ý của Javis để Haji chốt: Loyalty ID > CRM ID > Email > Phone, vì CRM ID cũng là khoá nội bộ ổn định nhưng phủ cả khách chưa là hội viên.

## Bổ sung của Javis

- **Băm SHA-256 không đồng nghĩa với ẩn danh:** email và số điện thoại có thể bị dò ngược bằng cách băm sẵn danh sách. Cần chuẩn hoá trước khi băm (chữ thường, bỏ khoảng trắng, số điện thoại theo E.164) để hai hệ thống ra cùng một mã.
- **Ở Việt Nam** cần đối chiếu với Nghị định 13/2023 về bảo vệ dữ liệu cá nhân trước khi chia sẻ dữ liệu giữa các công ty thành viên, và với quy định gửi tin quảng cáo khi tách tin vận hành, tin tiếp thị (GDPR, TCPA không áp trực tiếp). (Cần xác minh quy định hiện hành.)
- **Cờ chặn sự cố 365 ngày** là một dạng "lắng nghe trước khi bán": khách vừa bị huỷ chuyến mà nhận quảng cáo vui vẻ sẽ thấy bị coi thường. Nguyên lý này dùng được cho ngân hàng (khách vừa khiếu nại) và viễn thông (khách vừa mất sóng).

Liên quan: [[4 Mô Hình Hãng Bay]], [[Hành Trình Khách Hàng Hàng Không]], [[Cứu Giỏ Bỏ Dở Hàng Không]], [[Hàng Không - Bản Đồ Martech]].
