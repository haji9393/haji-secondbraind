---
type: wiki
status: active
tags: [wiki, van-hanh-ban-le]
created: 2026-11-19
updated: 2026-11-19
source: ["[[ECC - Inventory Demand Planning]]", "[[ECC - Returns Reverse Logistics]]"]
---
# Vận Hành Bán Lẻ - Tổng Quan

Trang trung tâm cho 2 mảng vận hành của nhà bán lẻ nhiều điểm bán: dòng hàng đi xuôi (dự báo, đặt hàng, tồn kho) và dòng hàng đi ngược (đổi trả). Chưng cất từ 2 skill ECC đã gỡ ngày 2026-11-19; bản gốc nằm trong `sources/van-hanh-ban-le/`.

## Hai dòng chảy hàng hoá
| | Dòng xuôi: [[Hoạch Định Nhu Cầu Tồn Kho]] | Dòng ngược: [[Quản Trị Đổi Trả Hàng]] |
|---|---|---|
| Câu hỏi chính | Bán bao nhiêu, đặt bao nhiêu, khi nào | Nhận lại không, hàng về đâu, hoàn bao nhiêu |
| Đánh đổi | Hết hàng vs tồn dư | Trải nghiệm khách vs bảo vệ biên lợi nhuận |
| Đầu vào | POS, đơn hàng, lead time NCC, lịch khuyến mãi | Chính sách đổi trả, tình trạng hàng, lịch sử khách |
| Đầu ra | Đơn đặt hàng (PO), tồn an toàn, lịch markdown | RMA, phân hạng A-D, kênh xử lý, hoàn tiền, đòi NCC |
| Ngưỡng sức khoẻ | WMAPE < 25%, in-stock hàng A > 97% | Xử lý < 48 giờ, tỉ lệ restock > 45% |

Nguồn số ngưỡng: [[ECC - Inventory Demand Planning]], [[ECC - Returns Reverse Logistics]]. Đây là benchmark của bản gốc (bối cảnh bán lẻ Mỹ, 40-200 cửa hàng), chưa kiểm cho thị trường Việt Nam (cần xác minh).

## Hai dòng chảy nối nhau ở đâu
- Hàng trả hạng A quay lại tồn kho, nên tồn khả dụng thật phải tính cả hàng đang về từ đổi trả. Vị thế tồn kho: `IP = Tồn tay + Đang về - Nợ giao - Đã giữ cho đơn` [[ECC - Inventory Demand Planning]].
- Khuyến mãi sâu kéo cầu ảo, sau đó là đợt sụt cầu và thường là đợt trả hàng tăng (mua thử, mua theo size). Kế hoạch khuyến mãi nên tính cả hai [[ECC - Inventory Demand Planning]] [[ECC - Returns Reverse Logistics]].
- Lỗi do NCC (hàng lỗi vượt ngưỡng 2-5%) đi theo đường đòi NCC, đồng thời là tín hiệu để xem lại NCC đó trong kế hoạch đặt hàng [[ECC - Returns Reverse Logistics]].
- Phantom inventory (hệ thống ghi 200, đếm thực tế 40) thường lộ ra khi hàng trả không được nhập kho đúng [[ECC - Inventory Demand Planning]].

## Liên hệ với CX
- Đổi trả là một điểm chạm CX: chính sách ngoại lệ ưu tiên khách giá trị cao, xem logic ở [[Quản Trị Đổi Trả Hàng]] và nối với [[Quy Trình Cứu Churn]].
- Đo theo giá trị ròng của khách (LTV sau trả hàng) thay vì chỉ tỉ lệ trả, giống tư duy [[Metric Handshake]]: thống nhất "giá trị" là gì trước khi đo.
- Phân tầng khách như ABC theo đóng góp biên lợi nhuận, tương tự cách chia hàng trong [[Hoạch Định Nhu Cầu Tồn Kho]].
