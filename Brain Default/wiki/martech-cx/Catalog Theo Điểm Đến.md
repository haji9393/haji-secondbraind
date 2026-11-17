---
type: wiki
status: active
tags: [wiki, martech-cx, hang-khong]
created: 2026-11-17
updated: 2026-11-17
source: "[[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]]"
---
# Catalog Theo Điểm Đến

Destination-Based Catalog là cách tổ chức "sản phẩm" cho hệ thống gợi ý trong hàng không, thay cho catalog theo SKU của thương mại điện tử. Nó sinh ra để xử lý hai đặc trưng: hàng dễ hỏng và giá động [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].

## Vì sao catalog theo thời gian thất bại

- **Dữ liệu thưa:** nếu mỗi chuyến bay theo ngày là một SKU (ví dụ "SQ326 đi London ngày 12/12"), lượt truy cập bị chia vụn. Chỉ khoảng 5-10% khách tìm vé trước ngày bay trên 3 tháng [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- **AI không đủ dữ liệu học:** lưu lượng vào một ngày bay cụ thể quá ít để collaborative filtering học được [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- **Vòng đời sản phẩm quá ngắn:** chuyến bay theo ngày hết hạn hoặc hết chỗ ngay khi cất cánh [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].

## Cách dựng

1. **Gom theo điểm đến:** mọi lượt tìm và đặt vé gom dưới một điểm đến chung như "London", "Tokyo", để dồn lưu lượng về một đầu mối cho máy học [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
2. **Ánh xạ mã thành phố:** các sân bay cùng thành phố (Heathrow LHR, Gatwick LGW, Stansted STN) quy về một mã thành phố cha (LON). Nhờ vậy hệ gợi ý quét được mọi chuyến và hiện giá "chỉ từ" thấp nhất [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
3. **Đặt ID theo cú pháp riêng, không dùng SKU, PNR hay số hiệu chuyến bay:**
   `Custom Item ID = Điểm đi-Điểm đến | Hạng khoang | Loại hành trình`, ví dụ `LON-HND | Business | OneWay` [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
   - Tách theo hạng khoang để không gợi ý vé phổ thông cho người đang tìm vé thương gia.
   - Ưu tiên cấu hình một chiều (OneWay) vì luồng này tự nhiên cho giá khởi điểm thấp nhất, làm mồi chuyển đổi.
   Hai ý trên theo [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
4. **Catalog bổ trợ nằm trong catalog chuyến bay,** tách bằng bộ lọc danh mục (hành lý, chỗ ngồi, suất ăn, bảo hiểm) [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]]. Cách xếp hạng và loại trừ xem [[Ancillary Revenue Hàng Không]].

## Thuật toán gợi ý

- **Collaborative filtering** chạy tốt nhất, nhờ lưu lượng lớn của web/app hãng bay (sau khi đã gom theo điểm đến) [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- **Gắn thẻ chủ đề (thematic tagging):** chặng bay không có "thể loại" như phim, nên gắn thuộc tính phong cách sống, ví dụ Geneva là Ski, Paris là Romance, Bali là Beach, để gợi ý theo sở thích [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- **Điểm thiên hướng (propensity score) cho bổ trợ** tính từ cả lượt click xem (như mở sơ đồ ghế) lẫn lượt mua thật [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].

## Giữ chi phí PSS trong tầm

- Giá vé đẩy sang Catalog API hoặc đọc từ bộ đệm giá tĩnh ("Fare Deals" cache) đồng bộ theo chu kỳ, không gọi PSS mỗi lượt xem [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]].
- Với đường bay biến động mạnh, chỉ làm mới giá thật đúng lúc widget gợi ý được tải trên màn hình người dùng [[Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17]]. Nguồn ghi thêm chữ "ngẫu nhiên", chưa rõ là lấy mẫu ngẫu nhiên hay chỉ là cách diễn đạt (cần xác minh).
- Lý do chi phí: [[Dữ Liệu Khách Hàng Hàng Không]].

## Bổ sung của Javis

- **Nguyên lý tổng quát:** khi sản phẩm sống ngắn và dữ liệu thưa, hãy gợi ý ở tầng trừu tượng cao hơn (điểm đến, loại phòng, khung giờ) rồi mới quy về sản phẩm cụ thể lúc khách chọn. Áp được cho khách sạn (gợi ý "phòng hướng biển cuối tuần" thay vì từng phòng từng đêm), sự kiện, tour.
- **Việt Nam:** phần lớn thành phố chỉ có một sân bay, nên ánh xạ mã thành phố ít quan trọng hơn gắn thẻ chủ đề (Phú Quốc là Beach, Đà Lạt là Cool Climate, Sa Pa là Trekking). Đây là gợi ý, chưa kiểm với dữ liệu hãng nội địa.
- **Bẫy khi gom:** gom LHR với LGW thì giá "chỉ từ" có thể là sân bay xa trung tâm hơn khách muốn; cần hiện rõ sân bay ở bước tiếp theo để không mất lòng tin.

Liên quan: [[Bộ Chỉ Số Martech Hàng Không]], [[Hàng Không - Bản Đồ Martech]].
