---
type: project-note
project: ruby-bai-kem
created: 2026-11-17
updated: 2026-11-17
source: "[[sources/ruby-bai-kem/Hồ sơ bàn giao Ruby Bãi Kem 2026-11-17]]"
---

# Phương án và mô hình tài chính bản 2

Hai lớp lựa chọn độc lập: làm sản phẩm gì (3 phương án sản phẩm) và ai khai thác (PA1 đến PA4). Mọi tài liệu từ 12/11/2026 so theo PA1 đến PA4.

## 3 phương án sản phẩm

1. Khách sạn + shophouse + nhà hàng, cà phê, bar.
2. Khách sạn + dorm/pod nghỉ ngắn giờ + studio dài hạn + shophouse.
3. Như phương án 2, thêm giặt ủi theo giờ và coworking.

Mô hình hiện chạy gần phương án 2. Doanh thu khác (cửa hàng, pod) khoảng 19% doanh thu, chưa kiểm chứng.

## 4 phương án vận hành

| | PA1 | PA2 | PA3 | PA4 |
|---|---|---|---|---|
| Cách làm | Không xây, cho thuê nhà thô | Xây hoàn thiện rồi cho thuê làm khách sạn | Xây hoàn thiện, thuê đơn vị vận hành, sau đó nhận bàn giao | Xây hoàn thiện, lập công ty tự vận hành |
| Kỳ hợp đồng | Tối thiểu 10 năm | 3 đến 5 năm | Tối thiểu 3 năm | Không áp dụng |
| Thu nhập | 35 triệu/căn/tháng + lãi gửi vốn không dùng | 85 đến 100 triệu/căn/tháng | Lợi nhuận trừ phí quản lý | 100% lợi nhuận |
| Đối tác đã tiếp xúc | Chưa | Chưa | DD Hospitality (có kinh nghiệm Bãi Kem), chưa báo giá | Không áp dụng |
| Pháp nhân | Thu nhập cho thuê cá nhân | Thu nhập cho thuê cá nhân | Công ty riêng của Chủ nhà | Công ty riêng của Chủ nhà |

- PA3: phí thường gặp là phí nền cộng thưởng khi doanh thu vượt ngưỡng; cần hỏi thêm nhiều đơn vị như DD Hospitality.
- **PA4 (đã hiệu đính): Haji trực tiếp điều hành**, nhận lương cơ sở, hưởng 20% phần lợi nhuận vượt mức tiền thuê PA2, xây hệ thống để sau này bàn giao. Giả định này vẫn hiệu lực; bỏ qua ghi chú "cần người thay thế" trong bản gốc.

## Mô hình tài chính bản 2

File: "Ruby Bãi Kem - Mô hình tài chính và so sánh 4 phương án (bản 2)", Google Sheet lập 17/11/2026. Tab: Tóm tắt, Nguồn dữ liệu, Đầu vào, Mùa vụ, Nhân sự, Cơ sở, Xấu, Độ nhạy, Cần xác minh. Mọi giả định ở tab Đầu vào (chữ xanh nền vàng); mô hình V4 là nguồn của nhiều số vốn.

### Cách so sánh
- Chu kỳ 10 năm cho mọi phương án, tính trên cả 4 căn, kèm phần 75% của Chủ nhà.
- Cùng xuất phát từ túi tiền 36 tỷ (vốn phương án tốn nhất ở kịch bản xấu, làm tròn). Tiền chưa dùng và tiền thu về gửi ngân hàng 6,5%/năm.
- Tổng tài sản cuối năm 10 = tiền mặt - chi phí cuối kỳ (tái thiết PA1, làm mới PA2) + giá trị nhà tăng thêm (giả định).
- Suất chiết khấu chốt 9% khi cần quy về giá trị hiện tại.

### Kết quả (tỷ đồng, cả 4 căn)

| Chỉ tiêu | PA1 | PA2 | PA3 | PA4 |
|---|---|---|---|---|
| Cơ sở: vốn bỏ thêm | 0 | 23,1 | 23,9 | 24,0 |
| Cơ sở: tiền về năm ổn định sau thuế (/năm) | 1,50 | 3,91 | 3,26 | 4,00 |
| Cơ sở: tổng tài sản cuối năm 10 | 82,2 | 110,3 | 104,3 | 112,2 |
| Cơ sở: không tính giá trị nhà tăng thêm | 82,2 | 75,9 | 69,9 | 77,8 |
| Cơ sở: quy ra lãi mỗi năm trên túi tiền | 8,6% | 11,8% | 11,2% | 12,0% |
| Cơ sở: năm lấy lại đủ vốn | không bỏ vốn | 6 | 7 | 7 |
| Cơ sở: phần 75% của Chủ nhà | 61,7 | 82,7 | 78,2 | 84,1 |
| Xấu: vốn bỏ thêm | 0 | 32,8 | 33,6 | 33,8 |
| Xấu: tiền về năm ổn định (/năm) | 1,20 | 2,64 | 1,85 | 2,49 |
| Xấu: tổng tài sản cuối năm 10 | 61,5 | 58,7 | 54,8 | 61,9 |
| Xấu: hơn/kém gửi ngân hàng | -6,0 | -8,9 | -12,8 | -5,6 |
| Xấu: năm lấy lại đủ vốn | không bỏ vốn | sau năm 10 | sau năm 10 | sau năm 10 |

Kịch bản xấu: công suất -15%, giá -10%, đơn giá xây 12 triệu/m², thuê PA2 còn 70 triệu/căn, khai trương trễ 3 tháng, trống 24 tháng (PA1, PA2).

Mốc dễ nhớ: công suất tối thiểu để PA4 hơn PA2 là 64,2%; để PA3 hơn PA2 (phí kiểu 1) là 71,6%. Giá phòng bình quân năm 1 là 1.039.300 đ/đêm gồm VAT. Nhân sự 11 người, khoảng 199 triệu/tháng.

### Giả định chính (cơ sở)

| Nhóm | Giả định | Nguồn, độ tin cậy |
|---|---|---|
| Khoản 1: thiết kế, giấy phép, PCCC | 0,84 tỷ | V4; thiết kế 350.000 đ/m² |
| Khoản 2: xây dựng, kỹ thuật | 7,88 triệu/m² x 2.100 m² = 16,54 tỷ (gồm dự phòng 10%, VAT, hầm, bể phốt, 2 thang máy) | V4; chưa có báo giá |
| Khoản 3: nội thất, thiết bị | 108,6 triệu/phòng x 53 = 5,76 tỷ | V4 |
| Khoản 4: trước khai trương, dự trữ | 0,72 tỷ + dự trữ 6 tháng định phí; PA4 thêm cố vấn 180 triệu | V4; cố vấn ước tính |
| Công suất năm ổn định | 65% (trần 95%/tháng); PA3 năm 1 đạt 82%; PA4 năm 1 70%, năm 2 90% | Chủ nhà chốt mức an toàn; chưa đối chiếu |
| Giá phòng 3 mùa (gồm VAT) | Cao (12-3) 1,25 triệu; vừa (4, 7, 8, 11) 1,0 triệu; thấp (5, 6, 9, 10) 0,8 triệu | Ước từ giá công khai |
| Phí kênh bán | 15,5% giá trước VAT | V4, bình quân 5 kênh |
| Biến phí; định phí ngoài lương | 30,3% doanh thu thuần; 108 triệu/tháng | V4; phí khu Sun chưa có |
| Bảo trì; quỹ thay nội thất | 1,5%; 3% doanh thu thuần | Ước tính; V4 |
| Tăng giá và chi phí; lương; trượt giá xây | 4%; 7%; 5%/năm | Theo lương tối thiểu vùng |
| Thuế công ty | TNDN 17%; chia lợi nhuận về cá nhân 5% | Nghị định 320/2025, cần kế toán xác nhận |
| Thuế cho thuê cá nhân | GTGT 5% + TNCN 5% trên phần vượt 500 triệu/năm | Có nguồn nêu ngưỡng 1 tỷ (NĐ 141/2026), cần xác nhận |
| Giá thuê | Thô 35 triệu; đã làm phòng 92,5 triệu/căn/tháng | Khảo sát Bãi Kem + tin rao |
| Nhận lại nhà PA1 năm 10 | 8,27 tỷ (xấu 24,55 tỷ) | Chưa báo giá tại đảo |
| Phí quản lý PA3 | Kiểu 1: 20 triệu/tháng + 5% doanh thu; 3 kiểu khác chọn trong ô | Bảng giá Kans Hospitality; JLL 2024 |
| Giá trị nhà tăng thêm | Tỷ suất quy đổi 8%; hệ số tình trạng sau 10 năm 70% | Giả định; chiếm khoảng 30% tổng tài sản |
| Tỷ lệ hưởng của Chủ nhà | 75% (3/4 căn) | Chưa có thỏa thuận R207 |

### Điểm lệch cần thống nhất ngay
- **Đơn giá 12 triệu/m²:** Chủ nhà hiểu đã gồm cơ điện, PCCC, nội thất lớn. Mô hình dùng 12 triệu chỉ cho phần xây ở kịch bản xấu rồi cộng nội thất. Theo cách hiểu của Chủ nhà: 2.100 x 12 triệu = 25,2 tỷ, trong trần 28 tỷ.
- **Trần 28 tỷ:** vốn kịch bản xấu 32,8 đến 33,8 tỷ, vượt trần.
- **Bản đồ quyết định còn số bản 1 (13/11):** PA1 66,8; PA2 94,9; PA3 94,8; PA4 115,8 tỷ. Phải đồng bộ một bộ số trước khi đưa Chủ nhà.

## Được, mất và cách xử lý

Cây quyết định 3 ngã rẽ: có xây không (PA1 vs xây) -> xây xong chỉ thu tiền thuê hay giữ kinh doanh (PA2 vs giữ) -> ai điều hành (PA3 vs PA4). Bản đầy đủ: "Bốn căn Ruby: 10 năm tới làm gì".

| | Được | Mất | Xử lý đã đề xuất |
|---|---|---|---|
| PA1 | Không bỏ vốn; tiền sinh lãi + tiền thuê; rủi ro thi công sang khách thuê; công sức thấp nhất | Không kiểm soát chất lượng, bố cục; cuối kỳ phải tái thiết hoặc cho thuê rẻ; khóa tài sản 10 năm; khách thuê có thể bỏ dở | Điều khoản thanh lý rõ; duyệt thiết kế khách thuê; cọc 6-12 tháng; quỹ tái thiết hằng năm; rà soát năm 5 có quyền lấy lại. Chia doanh thu với khách thuê thô không thực tế |
| PA2 | Thuê cao hơn PA1; tài sản hoàn chỉnh theo chuẩn Chủ nhà; rủi ro kinh doanh thuộc bên thuê; hợp đồng ngắn giữ quyền chuyển PA3, PA4; Chủ nhà đã có kinh nghiệm cho thuê | Phần thuê tăng thêm chủ yếu để hoàn vốn; bên thuê đòi giảm giá; hao mòn nhanh; trống giữa hợp đồng; thương hiệu thuộc bên thuê | Giá thuê 2 mức theo mùa; kỳ đầu 3 năm; trả trước theo quý; biên bản bàn giao có hình; tên khách sạn và tài khoản đặt phòng thuộc Chủ nhà |
| PA3 | Đội chuyên nghiệp; hệ sinh thái của đơn vị; giữ lợi nhuận sau phí; nhận lại khách sạn đang chạy sau 3 năm | Phí quản lý; thất thoát do không nắm sổ; phải mua hoặc xây hệ thống sau bàn giao; lợi ích có thể lệch | Một người của Chủ nhà giám sát sổ hằng tháng; tài khoản đứng tên công ty Chủ nhà; phí nền thấp, thưởng theo lợi nhuận; thỏa thuận trước giá chuyển giao hệ thống; quyền chấm dứt nếu dưới chỉ tiêu 2 quý |
| PA4 | 100% lợi nhuận (và 100% rủi ro); tiết kiệm phí; toàn quyền xây mô hình để nhân rộng; công ty tách bạch cho người kế nhiệm | Rủi ro giai đoạn xây; Chủ nhà không quản trị được chi tiết; xuất phát thấp về kênh bán; tuyển, giữ người tại đảo; phụ thuộc người điều hành chủ chốt (Haji) | Báo cáo 1 trang hằng tháng; kế toán độc lập; Chủ nhà xem trực tiếp tài khoản, phần mềm; cố vấn vận hành rà thiết kế và 6 tháng đầu; sổ tay vận hành; đào tạo người phó; thuê ngoài giặt là, bảo trì |

Chung cho PA2, PA3, PA4:
- Giải ngân theo cổng: chỉ mở khoản xây khi có đủ (1) chấp thuận cải tạo, ghép căn của ban quản lý khu, (2) thẩm duyệt PCCC phương án ghép, (3) khảo sát kết cấu và hầm.
- Tổng thầu trọn gói giá cố định, chi phí ăn ở thợ trong giá, thanh toán theo mốc nghiệm thu, phạt chậm, giữ tiền bảo hành; giám sát độc lập về phía Chủ nhà; dự phòng 10-15%.
- Nội thất mid-century đơn giản, 3-4 mẫu phòng chuẩn, làm phòng mẫu trước, đặt xưởng đất liền theo lô.
- Lịch ngược từ APEC; trễ thì mở cửa từng phần.
- Thỏa thuận góp vốn R207 ký trước khi đập tường.
- Mốc kiểm tháng 12 và 24 sau khai trương: lợi nhuận thấp hơn tiền thuê PA2 thì chuyển sang cho thuê.
