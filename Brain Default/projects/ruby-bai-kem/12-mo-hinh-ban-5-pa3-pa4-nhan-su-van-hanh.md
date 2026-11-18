---
type: project-note
project: ruby-bai-kem
created: 2026-11-18
updated: 2026-11-18
source: "Haji chốt trong chat 18/11/2026 20:23: 4 căn R201, R203, R205, R207; bỏ PA1, PA2; tập trung PA3, PA4; chi phí site phải tính tiền thuê khách sạn 85 triệu/căn/tháng. Mô hình Javis mo-hinh-ban-5/model5.py, file Excel ruby-bai-kem-mo-hinh-ban-5.xlsx"
tags: [project, ruby-bai-kem, mo-hinh-tai-chinh, ban-5, nhan-su, van-hanh]
---

# Bản 5: công ty vận hành thuê 4 căn, PA3 so với PA4

## Cách hiểu cấu trúc (cần Haji xác nhận)
- Hai lớp. Lớp chủ nhà: mỗi chủ căn bỏ vốn hoàn thiện (27,04 tỷ / 4 = 6,76 tỷ/căn) và nhận tiền thuê 85 triệu/căn/tháng. Lớp công ty vận hành: thuê nguyên khối 4 căn (340 triệu/tháng), chịu toàn bộ chi phí vận hành, lãi lỗ.
- Lớp chủ nhà hồi vốn đơn giản ~7,4 năm sau thuế cho thuê 10% (6,6 năm trước thuế). Khớp mốc "7 năm thực tế an toàn" Haji nêu, với điều kiện công ty vận hành trả đủ tiền thuê.
- PA3 và PA4 chỉ khác ở lớp công ty vận hành: ai lo back office, ai chịu học phí.

## Bộ máy nhân sự (giá năm 1)
Site, như nhau PA3 và PA4: 12 người, ~205 triệu/tháng (gồm BHXH, tháng 13, hỗ trợ ở + ăn 2 triệu/người).
- GM (Haji) 50 triệu. Trưởng lễ tân kiêm đặt phòng 13. Lễ tân 3 ca x 3 người 8,5 (ca đêm kiêm night audit). Giám sát buồng 10. Buồng 4 x 7,5 (~13 phòng/người/ngày). Kỹ thuật 10 (2 thang máy, hầm, PCCC). Bảo vệ đêm kiêm tạp vụ sảnh 7.
- Mùa cao (12-3) thêm 2 buồng thời vụ. Giặt là thuê ngoài theo đêm phòng.
Back office:
- PA3: nhà vận hành lo trong 12% doanh thu (revenue management, sales đoàn và đại lý, hệ thống đặt phòng, thương hiệu, kế toán trưởng, tuyển dụng, SOP, kiểm tra chất lượng, người thay GM).
- PA4: kế toán nội bộ kiêm thu ngân, nhân sự 13 + đặt phòng, OTA, marketing số 15 (~39 triệu/tháng tổng) + dịch vụ kế toán thuế, kiểm toán 7 + phần mềm 9 + marketing 2% + tuyển dụng, đào tạo 1% doanh thu. Ở năm 3 ~85 triệu/tháng (10,5%) so với PA3 ~97 triệu (12%).
- PA4 rẻ hơn chỉ vì GM kiêm revenue, sales, marketing, nhân sự. Thuê thêm Sales manager 30 triệu thì PA4 thua PA3 ~2,7 tỷ/10 năm.

## Chi phí site 38%
Bảng nhân sự từ dưới lên ra đúng 38% khi doanh thu thuần ~1,04 tỷ/tháng (khớp ví dụ 1 tỷ của Haji). Ở doanh thu cơ sở năm 3 (810 triệu/tháng, TB 59%) chi phí site là 46%, vì ~235 triệu nhân sự là cố định.

## Kết quả cơ sở (100% công ty vận hành, triệu)
| | PA3 | PA4 |
|---|---|---|
| Doanh thu thuần/tháng năm 3 | 810 | 810 |
| Site % / back office % / GOP % năm 3 | 46% / 12% / 42% | 46% / 10,5% / 44% |
| Tiền thuê % doanh thu năm 3 | 42% | 42% |
| Lợi nhuận sau thuế/tháng năm 1 | -141 | -240 |
| Năm 3 | -29 | -10 |
| Năm 10 | -6 | +12 |
| Tháng thấp nhất năm 1 | -378 | -466 |
| Năm 3: tháng cao điểm / thấp điểm (dòng tiền) | +298 / -332 | +350 / -357 |
| Cộng dồn 10 năm, đã trừ chi trước khai trương | -4.745 | -4.715 |
| Quỹ tiền cần chuẩn bị | 4.092 | 5.215 |
| Incentive PA3 / thưởng GM PA4 10 năm | 816 | 124 |

## Độ nhạy (tỷ, cộng dồn 10 năm)
Đầu trên TB 65%: PA3 1,6 / PA4 1,4. Đầu dưới giá -10%: -19,9 / -22,1. Xấu 44%: -29,8 / -33,0. ADR 900k cả năm: 5,9 / 5,6. ADR 600k: -24,7 / -27,2.
Thuê 75 triệu/căn: 0,2 / -0,5. 70 triệu: 2,3 / 1,3. 60 triệu: 6,5 / 4,8. Thuê bậc thang 60/75/85: -3,1 / -3,0.
Điểm hòa 10 năm: thuê ~75 triệu/căn (PA3), ~74 (PA4); hoặc công suất TB ~63%; hoặc ADR TB ~793k (kế hoạch 750k).

## Kết luận
- Ở 85 triệu/căn, tiền thuê (~42% doanh thu) xấp xỉ bằng toàn bộ GOP: công ty vận hành gần như không có lãi ở kịch bản cơ sở, lỗ ~4,7 tỷ/10 năm, cần quỹ 4-5 tỷ.
- PA3 và PA4 gần như hòa về tiền ở cơ sở (chênh 30 triệu/10 năm). PA3 tốt hơn năm 1-2 và cần ít quỹ hơn ~1,1 tỷ; PA4 tốt hơn từ năm 3 (~20-50 triệu/tháng), nhưng phần lợi này là công của GM làm 3-4 việc.
- Thị trường xấu: PA4 lỗ sâu hơn PA3 2-3 tỷ.
- PA3: incentive tính trên GOP trước tiền thuê, nên nhà vận hành vẫn nhận ~0,8 tỷ dù công ty vận hành lỗ. Phải đàm phán incentive tính sau tiền thuê hoặc có ngưỡng.

## Câu hỏi mở
1. Ai sở hữu công ty vận hành, ai góp quỹ 4-5 tỷ? Chủ nhà, người quen R207, Haji theo tỷ lệ nào?
2. 85 triệu/căn là giá cố định hay có thể bậc thang, cố định + chia phần vượt?
3. Mùa vừa 52,5-65% và ADR 750k (Javis đặt).
4. Mức đạt PA3 82% năm 1, PA4 70% / 90% năm 1-2.

## File
- `mo-hinh-ban-5/ruby-bai-kem-mo-hinh-ban-5.xlsx`: 5 tab (Tóm tắt, Đầu vào, Nhân sự, Theo tháng 120 tháng, Theo năm), có công thức. Đã kiểm khớp với Python. Bảng độ nhạy ở tab Tóm tắt là số tĩnh.
- `mo-hinh-ban-5/model5.py`, `scen.py`, `build_xlsx.py`, `verify.py`.
