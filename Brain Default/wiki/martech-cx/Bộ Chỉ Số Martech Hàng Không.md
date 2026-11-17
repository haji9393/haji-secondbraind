---
type: wiki
status: active
tags: [wiki, martech-cx, hang-khong]
created: 2026-11-17
updated: 2026-11-17
source: "[[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]]"
---
# Bộ Chỉ Số Martech Hàng Không

Trang này trả lời hai câu: vì sao martech hàng không khác bán lẻ, và đo hiệu quả bằng chỉ số nào cho từng tầng người nghe.

## 5 đặc trưng ngành chi phối martech

| Đặc trưng | Hệ quả cho martech |
|---|---|
| Hàng dễ hỏng: ghế trống về giá trị 0 ngay khi máy bay rời cửa (pushback) | Mọi chiến dịch phải bám sát mốc giờ khởi hành |
| Giá động và hạng vé phức tạp: RMS (PROS, Amadeus, Sabre) đổi giá liên tục, ghế chia theo fare bucket Y, B, M, H, Q, mỗi hạng một bộ quyền lợi | Thông điệp phải biết khách đang ở hạng vé nào |
| Bỏ dở phễu 80-90%: cam kết tài chính lớn, nhập hộ chiếu, nhiều bước | Cứu giỏ là use case lớn nhất, xem [[Cứu Giỏ Bỏ Dở Hàng Không]] |
| Một PNR chứa 1-9 hành khách, và PNR đổi theo mỗi lần đặt | Không dùng PNR làm ID khách, xem [[Dữ Liệu Khách Hàng Hàng Không]] |
| API của PSS (Amadeus, Sabre) tính phí từng lượt gọi | Kiến trúc phải dùng bộ đệm, xem [[Catalog Theo Điểm Đến]] |

Toàn bộ bảng theo [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].

## Chỉ số cho C-suite (doanh thu và chi phí)

- **Direct Channel Shift và phí GDS tránh được:** tỷ lệ booking chuyển từ OTA/GDS về web/app chính hãng; GDS tốn 8-15 USD/chặng, kênh trực tiếp 1-3 USD/chặng [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- **Ancillary Revenue per Pax và Attach Rate:** doanh thu bổ trợ trên mỗi khách và tỷ lệ đính kèm dịch vụ phụ; chuẩn ngành 15-25% [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]]. Định nghĩa attach rate chưa rõ, xem [[Ancillary Revenue Hàng Không]].
- **Chênh lệch PRASK và CASK:** tăng trưởng doanh thu trên ghế-km so với chi phí trên ghế-km [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]]. Công thức ở [[Kinh Tế Doanh Thu Hàng Không]].
- **Passenger Load Factor:** hệ số lấp đầy, mức trung bình kỷ lục hiện tại 84,6% [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]] (chưa có năm, cần xác minh).
- **Doanh thu tăng thêm đo bằng nhóm đối chứng 5%:** để chứng minh cho CFO, xem [[Nhóm Đối Chứng Toàn Cục]].

## Chỉ số kênh số

| Chỉ số | Ý nghĩa | Mức tham chiếu theo nguồn |
|---|---|---|
| Look-to-Book (L2B) | Lượt tìm chuyến bay so với lượt đặt xong | Chưa có |
| Flight Cart Recovery Rate | Tỷ lệ giao dịch bỏ dở được cứu thành công | Chưa có |
| Web Push CTR | Tỷ lệ click | 4-8%; Price Watch chuyển đổi gấp 6 lần App Push |
| App Opt-In Rate | Tỷ lệ bật nhận thông báo app | 50-60%, vì khách cần thông tin giờ bay, cổng |
| WhatsApp Read Rate | Tỷ lệ đọc tin hội thoại | Tới 68% |

Toàn bộ bảng theo [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].

## Bổ sung của Javis

- **Công thức nên chốt với khách theo [[Metric Handshake]]:**
  - L2B = số lượt tìm / số booking hoàn tất. Số càng cao càng nhiều người xem mà không mua; ngành thường đo theo từng kênh vì bot và OTA tìm kiếm làm phình mẫu số.
  - Cart Recovery Rate = số giỏ bỏ dở được hoàn tất trong cửa sổ bám đuổi / số giỏ bỏ dở đủ điều kiện bám đuổi. Phải chốt cửa sổ (ví dụ 7 ngày) và có loại khách đã mua ở quầy hay chưa.
  - Doanh thu tăng thêm = (doanh thu/khách nhóm nhận) trừ (doanh thu/khách nhóm đối chứng), nhân số khách nhóm nhận.
- **Chọn chỉ số theo người nghe:** CEO và CFO nghe tiền (phí GDS tránh được, doanh thu tăng thêm, ancillary/pax); CCO và giám đốc kênh số nghe L2B, recovery rate, CTR. Mở deck C-level bằng chỉ số tầng trên, chỉ số kênh để ở phụ lục. Nối với [[Tiếp Cận C-level]].
- **CTR, opt-in, read rate là chỉ số trung gian,** không phải kết quả. Báo cáo cho C-level nên dẫn từ chúng tới doanh thu hoặc chi phí, nếu không sẽ bị hỏi "thì sao".

Liên quan: [[Hàng Không - Bản Đồ Martech]].
