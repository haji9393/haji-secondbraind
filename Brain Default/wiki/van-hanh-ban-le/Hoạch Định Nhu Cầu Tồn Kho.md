---
type: wiki
status: active
tags: [wiki, van-hanh-ban-le]
created: 2026-11-19
updated: 2026-11-19
source: ["[[ECC - Inventory Demand Planning]]"]
---
# Hoạch Định Nhu Cầu Tồn Kho

Thuộc [[Vận Hành Bán Lẻ - Tổng Quan]]. Vai trò: người hoạch định nhu cầu đứng giữa merchandising (bán gì, giá nào), chuỗi cung ứng (kho, vận chuyển) và tài chính (ngân sách tồn kho, GMROI), biến ý định kinh doanh thành đơn đặt hàng sao cho vừa ít hết hàng vừa ít tồn dư [[ECC - Inventory Demand Planning]].

## Quy trình 6 bước
1. Gom tín hiệu cầu (bán qua POS, đơn, xuất kho), làm sạch điểm bất thường.
2. Chọn phương pháp dự báo cho từng mã hàng (SKU) theo phân loại ABC/XYZ.
3. Cộng hệ số khuyến mãi, trừ phần ăn lẹm (cannibalization), thêm yếu tố bên ngoài.
4. Tính tồn an toàn từ độ biến động cầu, độ biến động lead time và mức phục vụ mục tiêu.
5. Sinh đơn đặt hàng đề xuất, làm tròn theo MOQ/thùng/pallet, chuyển người duyệt.
6. Theo dõi độ chính xác (WMAPE, bias), chỉnh mô hình ở chu kỳ sau.

Nguồn: [[ECC - Inventory Demand Planning]].

## Phân loại ABC/XYZ
- ABC theo giá trị: A là 20% mã tạo 80% doanh thu hoặc biên lợi nhuận, B là 30% tạo 15%, C là 50% tạo 5%. Nên xếp theo biên lợi nhuận, không theo doanh thu.
- XYZ theo độ dễ đoán, đo bằng CV = độ lệch chuẩn / trung bình của cầu: X < 0.5, Y 0.5-1.0, Z > 1.0. Tính trên cầu đã bỏ mùa vụ và khuyến mãi.
- Ma trận xử lý: AX tự động bổ sung, tồn an toàn chặt; AZ người xem mỗi chu kỳ; CX tự động, chu kỳ xem thưa; CZ cân nhắc ngừng bán hoặc chỉ làm theo đơn.

Nguồn: [[ECC - Inventory Demand Planning]].

## Chọn phương pháp dự báo theo dạng cầu
| Dạng cầu | Cách chính | Khi nào xem lại |
|---|---|---|
| Ổn định, số lượng lớn | Trung bình trượt có trọng số 4-8 tuần | WMAPE > 25% suốt 4 tuần |
| Có xu hướng | Holt (làm mượt mũ kép) | Tracking signal vượt ±4 |
| Mùa vụ lặp lại | Holt-Winters | Tương quan mùa năm này với năm trước < 0.7 |
| Lắt nhắt, > 30% kỳ bằng 0 | Croston hoặc SBA | Khoảng cách giữa các lần có cầu đổi > 30% |
| Do khuyến mãi | Nền + lớp hệ số khuyến mãi | Thực tế lệch dự báo > 40% |
| Hàng mới (0-12 tuần) | Mượn hồ sơ 3-5 mã tương tự | Dữ liệu riêng cho sai số thấp hơn mã mượn |

Nguồn: [[ECC - Inventory Demand Planning]]. Không dùng trung bình trượt cho hàng mùa vụ vì nó trễ nửa độ dài cửa sổ.

## Đo độ chính xác
- MAPE = trung bình của |thực tế - dự báo| / thực tế. Vỡ ở mã bán ít, chỉ dùng cho mã bán từ 50 đơn vị/tuần.
- WMAPE = tổng |sai số| / tổng thực tế. Phản ánh theo tiền, là chỉ số tài chính quan tâm. Mục tiêu < 25%, báo động > 35%.
- Bias = sai số có dấu trung bình. Dương là dự báo cao (dễ tồn dư), âm là dự báo thấp (dễ hết hàng). Khoẻ trong ±5%, quá ±10% là lỗi cấu trúc.
- Tracking signal = sai số cộng dồn / MAD (độ lệch tuyệt đối trung bình). Vượt ±4 là mô hình đã trôi.

Nguồn: [[ECC - Inventory Demand Planning]].

## Tồn an toàn và điểm đặt hàng
- Tồn an toàn cơ bản: `SS = Z × σ_d × √(LT + RP)`, với Z là hệ số mức phục vụ, σ_d là độ lệch chuẩn cầu mỗi kỳ, LT là lead time, RP là chu kỳ xem xét.
- Khi lead time cũng dao động: `SS = Z × √(LT_tb × σ_d² + d_tb² × σ_LT²)`. NCC có CV lead time > 0.3 cần tồn an toàn cao hơn 40-60%.
- Mức phục vụ: 95% (Z = 1.65) cho hàng A, 99% (Z = 2.33) cho hàng sống còn, 90% (Z = 1.28) cho hàng C. Đi từ 95% lên 99% gần như gấp đôi tồn an toàn, phải tính tiền vốn trước khi quyết.
- Điểm đặt hàng: `ROP = cầu trung bình trong lead time + SS`. Lượng đặt kinh tế: `EOQ = √(2DS/H)`, D là cầu năm, S là chi phí mỗi lần đặt, H là chi phí giữ 1 đơn vị/năm. Thực tế phải làm tròn theo thùng hoặc pallet của NCC.
- Luôn đặt theo vị thế tồn kho (IP), không theo tồn tay, để khỏi đặt trùng khi hàng đang trên đường.

Nguồn: [[ECC - Inventory Demand Planning]].

## Khuyến mãi
- Bóc phần bán do khuyến mãi khỏi lịch sử trước khi dự báo nền, để riêng một lớp hệ số khuyến mãi.
- Mức tăng điển hình: chỉ giảm giá 15-40%; giảm giá + trưng bày + quảng bá 80-200%; doorbuster 300-500%+.
- Ăn lẹm: mã thay thế gần mất 10-30% phần tăng thêm.
- Sau khuyến mãi luôn có sụt cầu 1-3 tuần, mặc định bằng 40% phần tăng thêm, chia 60/30/10 cho 3 tuần sau.

Nguồn: [[ECC - Inventory Demand Planning]].

## Mùa vụ, markdown và loại hàng chậm
- Mua hàng mùa trước 12-20 tuần, chỉ cam kết 60-70% cầu dự kiến, giữ 30-40% để đặt bổ sung theo tốc độ bán đầu mùa.
- Markdown theo tốc độ bán ở giữa mùa so với kế hoạch: từ 80% trở lên thì giữ giá; 60-79% giảm 20-25%; 40-59% giảm 30-40% và huỷ PO đang mở; dưới 40% giảm từ 50% và tìm kênh thanh lý. Mỗi tuần chậm markdown mất 3-5 điểm % biên lợi nhuận.
- Loại hàng chậm khi đủ cả: tồn > 26 tuần bán, tốc độ 13 tuần gần nhất < 50% của 13 tuần đầu, không có khuyến mãi trong 8 tuần tới, không vướng hợp đồng, có mã thay thế. Giảm 30% trong 4 tuần, rồi 50% hoặc thanh lý, hạn thoát 8 tuần.

Nguồn: [[ECC - Inventory Demand Planning]].

## Tình huống khó
- Mã hàng nổi viral (cầu tăng 500-2.000%): không đuổi theo vì lead time 4-8 tuần, chia hạn mức theo điểm bán, chỉ nâng nền khi cầu giữ được hơn 4 tuần.
- NCC tăng gấp đôi lead time: tính lại tồn an toàn ngay, đặt khẩn phần chênh, tìm NCC phụ, báo merchandising mức phục vụ sẽ giảm tạm thời.
- Lễ lệch lịch (như Tết âm lịch, Phục sinh): dự báo theo "tuần so với ngày lễ" thay vì tuần dương lịch.
- MOQ của NCC lớn hơn EOQ: gom nhiều mã cùng NCC cho đủ giá trị tối thiểu, đàm phán MOQ, hoặc chấp nhận tồn dư nếu rẻ hơn đổi NCC.

Nguồn: [[ECC - Inventory Demand Planning]]. Ví dụ Tết âm lịch là suy luận áp dụng cho Việt Nam, bản gốc chỉ nêu Phục sinh.

## Bộ chỉ số theo dõi hằng tuần
| Chỉ số | Mục tiêu | Báo động |
|---|---|---|
| WMAPE | < 25% | > 35% |
| Bias | ±5% | > ±10% suốt 4 tuần |
| In-stock hàng A | > 97% | < 94% |
| Tuần cung ứng toàn bộ | 4-8 tuần | > 12 hoặc < 3 |
| Mã tồn > 26 tuần | < 5% số mã | > 10% |
| Hàng chết (0 bán 13+ tuần) | < 2% số mã | > 5% |
| Tỉ lệ NCC giao đủ PO | > 95% | < 90% |

Nguồn: [[ECC - Inventory Demand Planning]] (benchmark bán lẻ Mỹ, cần xác minh cho Việt Nam).
