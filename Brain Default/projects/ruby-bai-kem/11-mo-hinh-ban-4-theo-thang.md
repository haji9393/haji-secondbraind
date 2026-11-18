---
type: project-note
project: ruby-bai-kem
created: 2026-11-18
updated: 2026-11-18
source: "Haji mô tả cấu trúc từng PA trong chat 18/11/2026 14:41; mô hình Javis mo-hinh/model.py (theo tháng, 132 tháng)"
tags: [project, ruby-bai-kem, mo-hinh-tai-chinh, ban-4]
---

# Mô hình bản 4: mỗi PA một cấu trúc, đo bằng tiền mặt hằng tháng và giá trị cuối năm 10

## Cấu trúc từng PA (Haji chốt 18/11/2026)
- PA1: tiền thuê thô + lãi ngân hàng; trống 12-24 tháng trong kỳ; cuối kỳ trừ phá dỡ 250k/m² + 30% chi phí đảo, xây lại, sửa chữa.
- PA2: vốn xây ban đầu; cho thuê cả tòa ~350 triệu/tháng; trống 12-24 tháng.
- PA3: vốn xây + tư vấn 5.000 USD (mô hình, sản phẩm, yêu cầu vận hành cho thiết kế, kiểm chất lượng chéo); back office 12% doanh thu; chi phí tại site ~38% (nhân sự, điện nước, amenities); incentive tối đa 4% lợi nhuận, tính theo bậc.
- PA4: vốn xây; tự tuyển từ đầu (tối thiểu kế toán, quản lý, 2 lễ tân...), đội đông, tuyển lại thường xuyên; được toàn bộ doanh thu, quy mô, kiểm soát hằng tháng. Chi phí gần như PA3 nhưng có học phí sửa sai, tốn thời gian công sức.
- PA3, PA4: cùng nhân sự site, GĐ lương cơ sở 50 triệu.

## Giả định Javis tự đặt (cần Haji xác nhận)
- Mốc: tháng 1 = 11/2026, năm 0 thi công, khai trương tháng 13 (11/2027), 10 năm vận hành. Túi tiền 30 tỷ (100%), lãi 6,5%/năm tính theo tháng.
- Doanh thu "1 tỷ/tháng" hiểu là doanh thu thuần (sau VAT và phí OTA): ở 65% khoảng 1,04 tỷ/tháng giá năm 1. Mùa vụ theo tab Mùa vụ.
- Site 38% chia: cố định 218 triệu/tháng (tăng 7%/năm) + biến đổi 17% doanh thu. Ở tháng thấp điểm phần cố định làm tỷ lệ chi phí vượt 38%.
- Incentive PA3 theo biên GOP sau back office: >=50%: 4%; 45-50%: 3%; 40-45%: 2%; <40%: 0.
- Back office PA4 tự làm: 95 triệu/tháng cố định (kế toán, sales/OTA, marketing, phần mềm) + 3% doanh thu (quảng cáo, tuyển dụng, đào tạo) = ~12,6% ở 65%. Học phí sửa sai 0,3 tỷ năm 1; cố vấn 180 triệu; mức đạt năm 1 là 70%, năm 2 là 90% (PA3 năm 1 là 82%). GĐ nhận 20% phần lãi vượt tiền thuê PA2.
- Quỹ thay nội thất 3%; TNDN 17%; thuế chia lợi nhuận 5%; khấu trừ VAT vốn ~2,46 tỷ ở tháng 12 vận hành (chỉ đúng nếu công ty là chủ đầu tư).
- PA1: trống 6 tháng đầu + 6 tháng năm 5 (xấu 12 + 12). Cuối kỳ: phá dỡ 325k/m² + sửa chữa, xây lại 2,5 triệu/m² (chưa báo giá), trượt giá 5%/năm = 10,1 tỷ (100%).
- PA2: thuê tăng 4%/năm; trống 6 tháng sau khai trương + 6 tháng khi đổi khách năm 5 (xấu 12 + 12, thuê 280 triệu). Cuối kỳ làm mới 15% vốn.
- Giá trị nhà tăng thêm (PA2-PA4) = (thuê hoàn thiện - thuê thô năm 10) / 8% x 70%.
- Vốn cơ sở 27,04 tỷ; xấu 28 tỷ, giá -10%, trễ 3 tháng.

## Kết quả (phần Chủ nhà 75%, tỷ đồng; tiền/tháng là triệu, gồm lãi ngân hàng)

| | PA1 | PA2 | PA3 | PA4 | PA3 3 năm rồi PA4 |
|---|---|---|---|---|---|
| Tiền/tháng năm 3 (bình quân) | 276 | 305 | 381 | 356 | 381 |
| Tháng thấp nhất năm 3 | 268 | 296 | 217 | 177 | 217 |
| Tiền/tháng năm 10 | 466 | 562 | 661 | 598 | 613 |
| Tiền mặt cuối kỳ (đã trừ chi phí cuối kỳ) | 57,1 | 41,3 | 59,9 | 54,1 | 57,1 |
| Giá trị nhà tăng thêm | 0 | 22,9 | 22,9 | 22,9 | 22,9 |
| Tổng, cơ sở 65% | 57,1 | 64,2 | **82,8** | 77,0 | 80,0 |
| Tổng, xấu 45% | 55,0 | 41,5 | 43,0 | 34,6 | 38,1 |
| Tổng, xấu 40% | 55,0 | 41,5 | 37,4 | 28,1 | 31,8 |
| Thu hồi vốn (cơ sở) | - | năm 8 | năm 6 | năm 6 | năm 6 |

Mốc gửi ngân hàng: 45,0. Năm 1 PA3, PA4 có thêm ~154 triệu/tháng từ khấu trừ VAT (đã loại khỏi so sánh).

Theo công suất (tổng, cơ sở): 55%: PA3 71,0 / PA4 64,6 / PA2 64,2. 60%: 77,0 / 70,9. 70%: 88,7 / 83,0. 75%: 94,6 / 88,8.

## PA3 và PA4: khoảng cách 5,8 tỷ đến từ đâu
- ~3,0 tỷ: 20% chia cho GĐ ở PA4 (~0,42 tỷ/năm ở 65%). Bỏ phần này PA4 = 80,0.
- ~2,4 tỷ: mức đạt chậm (70%, 90%) và học phí sửa sai. Cho PA4 lên nhanh như PA3: 79,4.
- Phần còn lại: back office tự làm 12,6% so với 12% + incentive ~1,6%: gần như hòa.
- Kết luận: về tiền, với Chủ nhà PA3 và PA4 gần như bằng nhau; PA4 chỉ hơn khi đội tự làm lên nhanh và tinh gọn hơn đơn vị quản lý. Phần PA4 "tốn hơn" chủ yếu là thu nhập của GĐ và thời gian học.
- Thị trường xấu: PA4 kém PA3 8-9 tỷ; tháng thấp điểm năm 1 âm 90-110 triệu (phần Chủ nhà), cần quỹ dự phòng.

## Rủi ro chung PA3, PA4 (phải nói thẳng với Chủ nhà)
- Site 38% thấp hơn bảng nhân sự từ dưới lên của bản 2 (riêng nhân sự có GĐ 50 triệu đã ~232 triệu/tháng, cộng định phí 108 triệu). Tính theo bản 2 (~50% doanh thu): PA3 67,8, PA4 61,8, PA2 64,2: PA4 gần hòa PA2.
- Chỉ đếm tiền mặt (bỏ giá trị nhà tăng thêm): PA3 59,9, PA1 57,1, PA4 54,1. PA4 dưới PA1.
- Thị trường xấu: cả PA3, PA4 dưới mốc ngân hàng và dưới PA1.
- Doanh thu khác ~19% chưa kiểm chứng; khấu trừ VAT cần công ty là chủ đầu tư; R207.
- PA2 xấu giả định bên thuê vẫn trả 280 triệu khi khách sạn lỗ: khó đứng.

## Bản 4.1: công suất theo mùa và ADR thực tế (Haji chốt 18/11/2026 14:49)
Haji: thấp điểm 30-45%, cao điểm 75-85%; chi phí ở trên đã khảo sát thực tế; năm hồi vốn bình quân 7 năm (thực tế an toàn); ADR 600-900k đã trừ commission, VAT, OTA.

Giả định Javis: mùa vừa (tháng 4, 7, 8, 11) 52,5-65%; ADR thuần cao 900k / vừa 750k / thấp 600k; doanh thu khác giữ 198k/đêm (chưa kiểm chứng); định phí site 196 triệu/tháng + 17% doanh thu (= 38% ở doanh thu bình quân 937 triệu/tháng). Bảng này thay bảng bản 4 ở trên. Code: mo-hinh/run3.py, run4.py.

| Phần Chủ nhà 75% | PA1 | PA2 | PA3 | PA4 | PA3 rồi PA4 |
|---|---|---|---|---|---|
| Cơ sở (TB 59%): tiền/tháng năm 3 | 276 | 305 | 346 | 312 | 346 |
| Cơ sở: tháng thấp nhất năm 3 | 268 | 296 | 158 | 102 | 158 |
| Cơ sở: tháng thấp nhất năm 1 | 229 | 13 | 69 | -28 | 69 |
| Cơ sở: tiền/tháng năm 10 | 466 | 562 | 597 | 516 | 533 |
| Cơ sở: tổng cuối năm 10 | 57,1 | 64,2 | **77,5** | 70,3 | 73,6 |
| Cơ sở: chỉ tiền mặt | 57,1 | 41,3 | 54,6 | 47,4 | 50,7 |
| Cơ sở: năm hồi vốn | - | 8 | 6 | 7 | 7 |
| Đầu trên (TB 65%) | 57,1 | 64,2 | 84,1 | 77,4 | 80,7 |
| Đầu dưới, giá -10% (TB 52,5%) | 55,0 | 41,5 | 52,3 | 43,7 | 47,3 |
| Xấu (TB 44%) | 55,0 | 41,5 | 43,3 | 34,0 | 37,7 |

Mốc gửi ngân hàng 45,0. Độ nhạy cơ sở: bỏ doanh thu khác (giữ định phí): PA3 62,9, PA4 54,8 (PA3 dưới PA2, PA4 dưới PA1). ADR toàn năm 900k: PA3 85,7, PA4 79,5. ADR toàn năm 600k: PA3 64,5, PA4 57,3.
Tháng thấp điểm: chi phí site của PA3 lên ~60% doanh thu do phần cố định.

## Bản 4.2: bỏ hẳn doanh thu khác (Haji chốt 18/11/2026 14:51)
Chỉ tính doanh thu phòng. Chi phí site giữ 38% trên doanh thu phòng (định phí 156 triệu/tháng + 17%). Bảng này là bộ số hiện hành. Code: mo-hinh/run5.py.

| Phần Chủ nhà 75% | PA1 | PA2 | PA3 | PA4 |
|---|---|---|---|---|
| Cơ sở (TB 59%): tiền/tháng năm 3 | 276 | 305 | 283 | 244 |
| Tháng thấp nhất năm 3 | 268 | 296 | 119 | 56 |
| Tháng thấp nhất năm 1 | 229 | 13 | 48 | -48 |
| Tiền/tháng năm 10 | 466 | 562 | 486 | 392 |
| Tổng cuối năm 10 | 57,1 | 64,2 | **68,1** | 60,2 |
| Chỉ tiền mặt | 57,1 | 41,3 | 45,2 | 37,3 |
| Năm hồi vốn | - | 8 | 8 | 9 |
| Đầu trên (TB 65%) | 57,1 | 64,2 | 73,5 | 66,1 |
| Đầu dưới, giá -10% (TB 52,5%) | 55,0 | 41,5 | 46,2 | 36,9 |
| Xấu (TB 44%) | 55,0 | 41,5 | 39,0 | 28,9 |

Mốc ngân hàng 45,0. Nếu định phí site giữ 196 triệu như khi có pod/cửa hàng: PA3 62,9, PA4 54,8.

Điểm phải xử lý:
- Lãi khách sạn trước thuế năm 3 (100%) ~357 triệu/tháng, tiền thuê PA2 năm 3 ~379 triệu: bên thuê chỉ có doanh thu phòng thì không trả nổi 350 triệu. PA2 thuê 300 triệu: 52,7; 280 triệu: 48,1; 250 triệu: 41,2 (PA3 vẫn đứng đầu, 56,9-62,5).
- Hồi vốn 8-9 năm, dài hơn mốc 7 năm thực tế Haji nêu: cần đối chiếu mốc 7 năm dựa trên doanh thu nào.
- Chỉ đếm tiền mặt, PA1 (57,1) cao hơn mọi phương án xây.

## Bản 4.3 (18/11/2026): PA2 thuê nguyên toà 300tr/tháng, chỉ doanh thu phòng

Thay đổi so với 4.2: PA2 thuê 300tr/tháng (xấu 240tr), +4%/năm. Code: `mo-hinh/run6.py`. Số là phần chủ 75%, tỷ đồng, cuối năm 10. Gửi ngân hàng: 45.

| Kịch bản | PA1 | PA2 | PA3 | PA4 |
|---|---|---|---|---|
| Cơ sở (occ TB 59%, DT thuần 748tr/tháng) | 57.1 | 52.7 | **62.5** | 54.2 |
| Đầu trên (65%) | 57.1 | 52.7 | 67.9 | 60.0 |
| Đầu dưới -10% | 55.0 | 33.0 | 41.7 | 32.2 |
| Xấu 44% | 55.0 | 33.0 | 34.5 | 24.1 |
| ADR 900k đều | 57.1 | 52.7 | 70.9 | 63.9 |
| ADR 600k đều | 57.1 | 52.7 | 49.5 | 40.9 |

Tiền tháng phần chủ, cơ sở (tr): năm 3 PA1 276 / PA2 264 / PA3 283 / PA4 242. Tháng thấp điểm năm 1: PA3 48, PA4 -48.
Hoàn vốn cơ sở: PA3 năm 8, PA4 năm 9, PA2 năm 9 (chuẩn của Haji là 7). PA3 đạt 7 chỉ ở đầu trên, 6 nếu ADR 900k.
Khoảng cách PA3 - PA4 khoảng 8 tỷ: bỏ bonus GM 20% thì PA4 lên 56.3, bỏ thêm chi phí học và ramp như PA3 thì 58.3. Phần còn lại là back office tự dựng.
Chưa xác minh: nguồn chuẩn hoàn vốn 7 năm; giả định mùa trung 52.5-65% ADR 750k; cơ cấu site cost; back office và học phí PA4.

### Được - mất PA3 vs PA4 (bản 4.3)
- Điểm hoà back office: PA4 tự dựng 95tr/tháng + 3% DT rẻ hơn phí 12% của PA3 chỉ khi DT thuần > khoảng 1,06 tỷ/tháng. Mô hình cơ sở 748tr, đầu trên 817tr, nên ở quy mô 1 toà PA4 luôn đắt hơn.
- Chuyển PA3 sang PA4 từ năm vận hành 4 (`PA3>PA4`): 57.6 cơ sở, thấp hơn giữ PA3 (62.5) khoảng 5 tỷ; xấu 28.0 so với 34.5.
- Phần mô hình KHÔNG tính: giá trị năng lực vận hành nếu có toà thứ 2, quyền sở hữu dữ liệu khách và kênh, điều khoản ràng buộc và thoát hợp đồng PA3, rủi ro phụ thuộc 1 GM ở PA4.

### Slide HTML bản 4.3 (18/11/2026)
- `slide/ruby-bai-kem-slide-ban-4.html`: 36 trang, khung điện thoại, có thêm phần E "PA3 hay PA4" (10 trang phân tích sâu). Dựng lại bằng `slide/build_slide.py`, số lấy từ `mo-hinh/run7.py`.
