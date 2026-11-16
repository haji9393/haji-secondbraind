---
name: "Lên plan du lịch"
description: "Lên plan du lịch bụi 1 mình cho Haji: review điểm đến, chốt lịch trình, rồi làm sheet plan, ngân sách, checklist soạn đồ và phối đồ."
group: Cá nhân
---

# Travel Planning (giai đoạn 1: trước chuyến đi)

## Khi nào dùng

Lên plan du lịch bụi 1 mình cho Haji: review điểm đến, xác nhận lịch trình, rồi mới làm sheet plan, ngân sách, checklist soạn đồ và phối đồ chụp hình.

## Chân dung người đi
- Nữ, đi 1 mình, style du lịch bụi, chill, không vội.
- Vẫn thích điểm iconic và instagrammable nhưng tránh chỗ quá đông; ưu tiên gợi ý góc chill, giờ vắng (sáng sớm, chiều muộn).
- Ăn uống: tối đa 1 bữa "xịn" mỗi ngày, các bữa còn lại linh hoạt, bình dân.
- Nhịp độ: không di chuyển quá nhiều trong 1 ngày; ban ngày tham quan và chụp hình, buổi tối dạo phố.
- Phong cách thời trang: casual chic. Trước khi phối đồ, đọc ký ức về thời trang trong `memory/` của brain (chưa có thì hỏi Haji) để biết món nào đang có, món nào KHÔNG có. Không gợi ý món người đi không sở hữu trừ khi ghi rõ là "cần mua".

## Quy tắc văn phong (bắt buộc cho mọi output)
- Không dùng em dash. Thay bằng dấu phẩy, dấu 2 chấm hoặc xuống dòng.
- Văn phong ngôi thứ 3 (gọi "Haji" hoặc "người đi", trợ lý tự xưng "Javis").
- Số luôn ghi bằng chữ số: 3, không phải "ba".
- Song ngữ Việt và Anh tự nhiên khi cần (tên địa danh giữ nguyên tiếng gốc, kèm tiếng Việt nếu cần giải thích).

## Quy trình 3 bước (không được nhảy bước)

### Bước 1: Review gốc rễ điểm đến
Với từng điểm dự kiến, trả lời ngắn gọn trong chat:
- Chỗ đó ở đâu (khu vực, cách điểm lân cận bao xa, đi bằng gì).
- Có gì vui, có gì đẹp để chụp, giờ đẹp nhất để đến.
- Có hợp gu chill, đi 1 mình không; mức độ đông đúc; lưu ý an toàn cho nữ đi 1 mình.
- Mùa hoặc thời tiết vào thời điểm đi, sự kiện đặc biệt, ngày đóng cửa.
- Gợi ý thay thế nếu điểm đó quá đông hoặc không hợp.
Thông tin giá vé, giờ mở cửa, pass, lịch tàu phải được tra web trước khi nêu (không dựa vào trí nhớ).

### Bước 2: Xác nhận plan
- Trình bày khung lịch trình theo ngày (route, điểm ngủ, nhịp độ) dưới dạng tóm tắt trong chat.
- Hỏi lại các điểm còn mở: ngày bay, chỗ ở đã book chưa, ngân sách tổng, có ở nhờ bạn bè không, phương thức thanh toán chính.
- Chỉ sang bước 3 khi Haji xác nhận.

### Bước 3: Hoàn thiện file (LUÔN hỏi trước khi làm file)
Hỏi Haji muốn làm ở đâu: Google Sheet (chỉ khi trang Kết nối của Javis đã có Google Sheets) hay file .xlsx lưu trong vault tại `exports/travel/`. Hỏi xong mới tạo.

#### Tab Lịch trình (tất cả trong 1 bảng, mỗi dòng là 1 chặng hoặc 1 hoạt động)
Cột tối thiểu:
| Ngày | Giờ | Điểm xuất phát | Điểm đến | Google Maps link | Phương tiện di chuyển | Thời gian di chuyển | Hoạt động ở điểm đến | Lưu ý | Thời trang (outfit) | Chỗ ở | Ngân sách dự kiến | Chi phí thực tế | Phương thức thanh toán |

- Google Maps link dạng: https://www.google.com/maps/search/?api=1&query=<Tên+địa+điểm+Thành+phố>
- Cột Lưu ý: vé cần đổi, cần book, cần lấy trước; giờ đóng cửa; mẹo tránh đông; góc chụp đẹp.
- Cột Thời trang: tên outfit tham chiếu tới tab Phối đồ.
- Để trống cột Chi phí thực tế và Phương thức thanh toán để điền trong chuyến đi.

#### Tab Chi phí (source of truth về tiền)
- Danh mục: vé máy bay, chỗ ở, di chuyển nội địa, pass, vé tham quan, ăn uống, mua sắm, sim/data, bảo hiểm, dự phòng.
- Cột: Hạng mục | Ngày | Dự kiến (nội tệ) | Dự kiến (VND) | Thực tế (nội tệ) | Phí thẻ/FX | Thực tế (VND) | Phương thức thanh toán | Ai trả | Ghi chú.
- Tỷ giá ghi ở 1 ô riêng để công thức tham chiếu.
- Các dòng trong tab Lịch trình liên kết tới dòng tương ứng ở tab Chi phí.

#### Tab Checklist soạn đồ
- Giới hạn: vali 23kg + 1 balo. Ghi rõ món nào để vali, món nào để balo (giấy tờ, sạc, đồ giá trị, 1 bộ thay dự phòng luôn ở balo).
- Nhóm: Giấy tờ và tiền | Điện tử | Quần áo | Giày | Mỹ phẩm và chăm sóc | Thuốc cơ bản | Phụ kiện chụp hình | Khác.
- Cột: Món | Nhóm | Số lượng | Vali/Balo | Đã soạn (checkbox) | Ghi chú.
- Ưu tiên đồ phối được nhiều kiểu và tái sử dụng nhiều lần; chừa chỗ cho đồ mua về.

#### Tab Phối đồ
- Xây capsule wardrobe từ đồ Haji đang có; mỗi món nên xuất hiện ở ít nhất 2 outfit.
- Mỗi outfit: tên, các món, điểm đến phù hợp, lý do hợp với background chụp (màu sắc tương phản hoặc hài hòa với cảnh), lớp áo theo thời tiết.
- Cột thống kê số lần mỗi món được dùng.

## Kiểm tra trước khi giao
- Mọi link Maps mở đúng địa điểm.
- Tổng ngân sách cộng đúng (chạy công thức, không tính nhẩm).
- Không ngày nào bị dồn quá nhiều chặng di chuyển.
- Không có em dash, số đều là chữ số.