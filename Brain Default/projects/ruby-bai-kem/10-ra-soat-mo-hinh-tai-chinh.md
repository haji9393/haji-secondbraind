---
type: project-note
project: ruby-bai-kem
created: 2026-11-17
updated: 2026-11-17
source: "Sheet bản 2 (tab Đầu vào, Nhân sự, Cơ sở) đọc 17/11/2026 23:30; Haji chốt trong chat: tiền thuê PA2 không tính kiểu giá thuê từng căn, PA3 và PA4 đều trả lương GĐ 50 triệu (lương cơ sở), nhân sự như nhau"
tags: [project, ruby-bai-kem, mo-hinh-tai-chinh, ra-soat]
---

# Rà soát mô hình tài chính: các lỗ hổng

Mọi số dưới đây là phần Chủ nhà 75%, cuối năm 10, kịch bản cơ sở 65%, vốn 27,04 tỷ (12 triệu/m² all-in), túi tiền 32 tỷ, mốc gửi ngân hàng 45,1 tỷ. Nhân sự PA3 = PA4 = 232,5 triệu/tháng (GĐ 50 triệu).

## Lỗ hổng 1 (nặng nhất): tiền thuê PA2 không neo vào kinh tế của chính khách sạn
- Công thức: 92,5 triệu/căn x 4 căn x 12 = 4,44 tỷ/năm (giá năm 1). Mức 85-100 triệu là giá thuê shophouse 12-15 phòng đứng riêng, không phải giá thuê một khách sạn 53 phòng ghép từ 4 căn.
- Kiểm tra khả năng trả: năm 3, công suất 65%, toàn bộ lãi tiền mặt của khách sạn (doanh thu thuần 13,55 tỷ, trừ biến phí, nhân sự có GĐ 50 triệu, định phí, bảo trì, quỹ nội thất) = 4,24 tỷ. Tiền thuê PA2 năm 3 = 4,80 tỷ. Bên thuê trả nhiều hơn toàn bộ số khách sạn làm ra, chưa tính lãi của họ.
- Kịch bản xấu còn lệch hơn: ở 45% khách sạn chỉ làm ra 0,91 tỷ/năm, ở 40% còn 0,30 tỷ, nhưng mô hình vẫn giả định bên thuê trả 70 triệu/căn (~3,4 tỷ/năm).
- Hệ quả dây chuyền: cùng ô tiền thuê này quyết định (a) dòng tiền PA2, (b) giá trị nhà tăng thêm của cả PA2, PA3, PA4 (= chênh tiền thuê hoàn thiện so với thô / 8% x 70%), (c) ngưỡng chia 20% cho GĐ ở PA4, (d) "ngưỡng công suất PA4 hơn PA2". Ô này sai thì 4 kết luận lớn của deck sai theo.
- Cách sửa đề xuất: tiền thuê PA2 = phần bên thuê trả được từ lãi khách sạn. Trần lý thuyết ở 65% ~3,9 tỷ/năm giá năm 1 (~6,2 triệu/phòng/tháng). Bên thuê cần giữ biên lợi nhuận, nên mức thực tế khoảng 2,6-2,9 tỷ/năm (55-60 triệu quy theo căn, ~4,2-4,5 triệu/phòng/tháng). Cần Haji chốt con số hoặc nguồn.

## Lỗ hổng 2: lương GĐ chỉ tính cho PA4 (đã sửa theo Haji)
- Bản 2 để "Quản lý 25 triệu" cho cả PA3, PA4. Bản 3 (Javis) chỉ nâng PA4 lên 50 triệu, PA3 giữ 25 triệu: sai. PA3 thuê đơn vị quản lý vẫn phải trả lương GĐ khách sạn, cộng phí quản lý (20 triệu/tháng + 5% doanh thu).
- Sửa: nhân sự PA3 = PA4 = 232,5 triệu/tháng. PA3 giảm từ 68,1 xuống 63,8 tỷ; tiền về/tháng năm 3 từ 207 xuống 184 triệu; thu hồi năm 9.

## Kết quả sau khi sửa 2 lỗ hổng (cơ sở 65%)

| Tiền thuê PA2 (quy theo căn) | PA1 | PA2 | PA3 | PA4 |
|---|---|---|---|---|
| 92,5 triệu (như bản 2, không khả thi) | 56,0 | 70,9 | 63,8 | 69,7 |
| 60 triệu | 56,0 | 41,3 | 49,2 | 54,0 |
| 55 triệu | 56,0 | 36,7 | 47,0 | 51,3 |

- Giá trị nhà tăng thêm ở mức 55 triệu chỉ còn 9,0 tỷ (trước 25,8).
- PA4 hơn PA2 từ công suất ~51-53% (không còn 67%). Phần chia 20% cho GĐ có từ 65%: ~0,23-0,28 tỷ/năm.
- **PA1 (để thô) lại đứng đầu ở 65%.** PA4 chỉ hơn PA1 khi công suất từ ~67% (tiền thuê 60 triệu) hoặc ~70% (55 triệu). PA3 cần 71-74%.
- Kịch bản xấu 40-45%: PA3, PA4 còn 6-30 tỷ, dưới mốc ngân hàng 45 tỷ; PA2 phụ thuộc bên thuê có trụ được không.

## Lỗ hổng khác
3. **PA1 giả định hợp đồng 10 năm, 35 triệu/căn.** Báo cáo thị trường nói thực tế chỉ ký 3-5 năm. PA1 đang thắng nên giả định này cần kiểm kỹ nhất.
4. **Khấu trừ VAT vốn (~2,1-2,5 tỷ) và khấu hao của PA3, PA4** giả định công ty là chủ đầu tư. Nhà đứng tên cá nhân Chủ nhà: công ty phải thuê lại nhà (phát sinh thuế cho thuê cá nhân) hoặc góp tài sản. Chưa mô hình hóa.
5. **Giá trị nhà tăng thêm của PA3, PA4 neo theo tiền thuê PA2**, không theo lãi khách sạn. Bảo thủ, nhưng phải nói rõ trên slide.
6. **PA2 không có chi phí của chủ nhà** (bảo hiểm tòa nhà, sửa kết cấu, phí khu nếu chủ chịu). Nhỏ, nên thêm 1-2% tiền thuê.
7. **Khấu hao nội thất 15 năm** gộp chung với xây dựng; thực tế 5-8 năm. Chỉ ảnh hưởng thuế.
8. **Doanh thu khác 2,49 tỷ (~19%) chưa kiểm chứng**, báo cáo thị trường khuyên bỏ pod/dorm. Cắt phần này thì PA3, PA4 giảm mạnh.
9. **Kịch bản xấu bản 2 = công suất x 0,85 (55,3%)**, không phải 40-45%. Tab Xấu phải đổi ô công suất.

## Việc cần Haji chốt
- Tiền thuê PA2 đúng là bao nhiêu, hoặc nguồn (báo giá bên thuê, tỷ lệ % lãi khách sạn).
- PA1: kỳ hợp đồng thực tế và giá thuê thô.
- Cấu trúc pháp lý công ty vận hành và nhà đứng tên cá nhân.
