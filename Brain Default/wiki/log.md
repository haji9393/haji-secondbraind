# Wiki Log

Nhật ký thời gian (append-only). Mỗi entry: `## [YYYY-MM-DD] loại | tiêu đề` (loại: init/ingest/update/query/lint/migrate).

## [2026-11-16] ingest | Lô 1 Customer Success từ Google Drive
- Nguồn: folder Drive Customer Success của Haji (khoảng 190 file). Lô này: 8 tài liệu lõi, 1 tài liệu chỉ có phần mở đầu.
- Tạo 9 thẻ nguồn trong `sources/customer-success/`, 9 trang trong `wiki/customer-success/`, 1 trang trong `wiki/insider-addon/`.
- Thiết kế 2 lớp: lõi trung lập với sản phẩm, lớp add-on giữ mọi thứ riêng của Insider.
- Còn lại: phần còn lại của folder CS, Playbook BFSI Part 1, 2, 3, 5, deck khách hàng theo ngành, SLII.
