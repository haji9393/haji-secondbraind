# Wiki Log

Nhật ký thời gian (append-only). Mỗi entry: `## [YYYY-MM-DD] loại | tiêu đề` (loại: init/ingest/update/query/lint/migrate).

## [2026-11-16] ingest | Lô 1 Customer Success từ Google Drive
- Nguồn: folder Drive Customer Success của Haji (khoảng 190 file). Lô này: 8 tài liệu lõi, 1 tài liệu chỉ có phần mở đầu.
- Tạo 9 thẻ nguồn trong `sources/customer-success/`, 9 trang trong `wiki/customer-success/`, 1 trang trong `wiki/insider-addon/`.
- Thiết kế 2 lớp: lõi trung lập với sản phẩm, lớp add-on giữ mọi thứ riêng của Insider.
- Còn lại: phần còn lại của folder CS, Playbook BFSI Part 1, 2, 3, 5, deck khách hàng theo ngành, SLII.

## [2026-11-17] ingest | Hồ sơ bàn giao dự án Ruby Bãi Kem
- Nguồn: sources/ruby-bai-kem/Hồ sơ bàn giao Ruby Bãi Kem 2026-11-17.md (nguyên văn).
- Tạo folder dự án projects/ruby-bai-kem/ (README + 7 trang). Hiệu đính theo Haji: Haji vẫn phụ trách chính; bỏ mọi nội dung về việc Haji rời dự án.
- Đối chiếu với tab Tóm tắt của mô hình bản 2 trên Drive: khớp. Ghi lỗ hổng trong 07-ra-soat-cua-javis.md.

## [2026-11-17] ingest | Tổng hợp martech ngành Hàng không và Du lịch
- Nguồn: sources/martech-cx/Haji - Tổng hợp Hàng không và Du lịch 2026-11-17.md (Haji dán trong chat, lưu nguyên văn).
- Tạo nhóm mới wiki/martech-cx/ với 7 trang. Phần "Bổ sung của Javis" tách riêng, không trích nguồn.
- Thêm 3 câu hỏi mở về năm số liệu và số case.

## [2026-11-17] ingest | Ancillary Revenue ngành Hàng không
- Nguồn: sources/martech-cx/Haji - Ancillary Revenue Hàng không 2026-11-17.md (Haji dán trong chat, lưu nguyên văn).
- Tạo 1 trang mới [[Ancillary Revenue Hàng Không]]; thêm link ở 4 trang martech-cx. Phần trùng với nguồn trước (phí GDS, PSS, mốc T-7/T-48/T-24) không viết lại, chỉ trỏ sang.
- Thêm 1 câu hỏi mở về định nghĩa attach rate.

## [2026-11-17] ingest | Hợp nhất ngành Hàng không (3 nguồn)
- Nguồn: sources/martech-cx/Haji - Hàng không đặc trưng, metrics, catalog, cart recovery 2026-11-17.md, đọc cùng 2 nguồn hàng không trước.
- Tạo 4 trang: [[Bộ Chỉ Số Martech Hàng Không]], [[Catalog Theo Điểm Đến]], [[Cứu Giỏ Bỏ Dở Hàng Không]], [[Nhóm Đối Chứng Toàn Cục]].
- Viết lại [[Dữ Liệu Khách Hàng Hàng Không]] (TTL đầy đủ, định danh, PCI DSS, tách tin vận hành và tiếp thị); cập nhật [[Hành Trình Khách Hàng Hàng Không]], [[Ancillary Revenue Hàng Không]], [[Hàng Không - Bản Đồ Martech]] (mạch tư duy 8 bước).
- Ghi 2 mục Mâu thuẫn (chặn 4 giờ vs geofence; thứ tự định danh) và thêm 3 câu hỏi mở. TTL 30-60 ngày, 12 tháng, 7 ngày được diễn giải là không mâu thuẫn.
