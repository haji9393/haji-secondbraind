---
type: wiki
status: active
tags: [wiki, martech-cx, hang-khong]
created: 2026-11-17
updated: 2026-11-17
source: "[[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]]"
---
# Cứu Giỏ Bỏ Dở Hàng Không

Tỷ lệ bỏ dở phễu đặt vé hàng không thuộc hàng cao nhất, khoảng 80-90%, do thanh toán phức tạp, cam kết tài chính cao và giá động liên tục [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]]. Chiến lược cứu giỏ gồm 4 trụ [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].

## Trụ 1: Giữ khách ngay tại trang (onsite)

- **Popup khi khách sắp thoát (exit-intent) và huy hiệu tin cậy:** bắt đúng lúc khách định sang OTA hay đối thủ so giá; đặt câu gỡ rào cản như "Miễn phí huỷ/đổi trong 24h", "Cam kết giá tốt nhất" ngay trang thanh toán [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- **Bằng chứng xã hội:** "63 khách đang xem chuyến bay này và 14 khách đã đặt trong 24h qua", "Chỉ còn 3 ghế giá này" [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- **Giá phải đúng thời gian thực:** không hiện giá tĩnh đã hết hạn; dùng Fare Cache API hoặc làm mới giá ở cấp widget [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].

## Trụ 2: Chuỗi bám đuổi đa kênh

| Kênh | Vai trò | Số theo nguồn |
|---|---|---|
| Web Push | Với khách ẩn danh hoặc chưa cài app, trên web/desktop | CTR 4-8%; Price Watch/Price Drop chuyển đổi gấp 6 lần App Push ở một số triển khai |
| App Push | Nhắc hoàn tất giữ chỗ kèm mã ưu đãi riêng | Opt-in 50-60% |
| WhatsApp | Tin bám đuổi đủ chi tiết chặng bay, ảnh, nút CTA; khách đặt tiếp và mua bổ trợ ngay trong chat | Read rate tới 68% |

Bảng theo [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]]. Thứ tự Web Push, App Push, WhatsApp cũng có trong [[Haji - Ancillary Revenue Hàng không 2026-11-17]].

## Trụ 3: Phân tập theo bối cảnh và động lực

- **Theo bước bỏ dở:** tách người bỏ ở bước tìm kiếm, bước đã điền thông tin hộ chiếu, và bước thanh toán (lỗi thanh toán hoặc bỏ). Nhóm bỏ ở bước thanh toán với giá trị đơn lớn vào tệp ưu tiên khẩn (High-Value Cart Abandoners) [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- **Theo chân dung:** khách nhạy giá nhận mã giảm % hoặc tặng suất ăn, hành lý; hội viên nhận dặm gấp đôi hoặc nâng hạng ghế nếu đặt xong trong khung giờ ngắn [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- **AI:** Next Best Channel đoán kênh dễ chuyển đổi nhất cho từng người; Send Time Optimization gửi đúng lúc người đó hay mở máy [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].

## Trụ 4: Chặn ma sát kỹ thuật

- **Chặn khách đã mua offline:** đồng bộ booking ở quầy, tổng đài, đại lý qua Upsert API để dừng ngay chuỗi bám đuổi, tránh làm phiền và phí ngân sách [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- **Hạn dữ liệu:** giỏ bỏ dở giữ và bám đuổi trong 30-60 ngày; riêng lỗi thanh toán chỉ bám tối đa 7 ngày, trước khi PSS tự huỷ PNR [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]]. Bảng hạn dữ liệu đầy đủ ở [[Dữ Liệu Khách Hàng Hàng Không]].

## Bổ sung của Javis

- **Thứ tự triển khai đề xuất:** trụ 4 trước (chặn khách đã mua, hạn 7 ngày), vì làm sai ở đây gây phàn nàn ngay; rồi trụ 3 (chia theo bước bỏ dở), rồi mới tới trụ 2 và trụ 1. Kinh nghiệm chung khi triển khai cho enterprise, chưa có số kiểm chứng.
- **Giảm giá phải đứng sau giá động:** mã giảm % cho khách nhạy giá chỉ nên bật khi giá hiện tại không thấp hơn giá lúc khách bỏ dở, nếu không là tặng tiền vô ích. Cần phối hợp với đội quản trị doanh thu.
- **"Chỉ còn 3 ghế giá này"** phải lấy từ số ghế thật của fare bucket trong RMS. Số giả có rủi ro pháp lý về quảng cáo gây nhầm lẫn (cần xác minh quy định Việt Nam).
- **Việt Nam:** chặng cuối nên là Zalo thay WhatsApp; xem [[Hành Trình Khách Hàng Hàng Không]].
- Đo hiệu quả bằng Cart Recovery Rate và doanh thu tăng thêm so với [[Nhóm Đối Chứng Toàn Cục]], không chỉ đếm số giỏ "được cứu", vì một phần khách vẫn tự quay lại mua.

Liên quan: [[Bộ Chỉ Số Martech Hàng Không]], [[Ancillary Revenue Hàng Không]], [[Hàng Không - Bản Đồ Martech]].
