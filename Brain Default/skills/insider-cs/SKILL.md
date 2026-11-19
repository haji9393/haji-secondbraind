---
name: insider-cs
description: "Quản trị khách hàng, xử lý thuê bao và hoàn tiền, trích và đối soát dữ liệu, làm sạch file xuất, lập báo cáo tháng và dựng deck Insider."
group: Marketing
---
# Insider Customer Success

## Tài liệu theo tình huống

- Khi khách gặp vấn đề thuê bao, hóa đơn hoặc hoàn tiền, xác minh đúng giao dịch và trạng thái qua công cụ thanh toán được cấp quyền. Đọc [hướng dẫn](references/customer-billing-ops.md).
- Khi đọc file xuất, biểu mẫu hoặc hóa đơn, chọn cách trích theo định dạng và đối soát từng bản ghi với nguồn trước khi tổng hợp. Đọc [hướng dẫn](references/regex-vs-llm-structured-text.md).


Mở đúng file trong `references/` theo việc.

## Khi nào dùng
| Việc | Mở file |
|---|---|
| Tra KPI, cách framing, vấn đề đã biết của một khách (Viettel, Sacombank, TP Bank, MBS, VETC, GHN...) | `references/insider-client-profiles.md` |
| Làm sạch file .xlsx export thô, thêm cột Conversion, pivot theo event | `references/insider-data-cleanup.md` (kèm `references/rule-sets.md`, `references/master-sheets.md`) |
| Dựng và đánh giá báo cáo hiệu quả tháng | `references/insider-monthly-report.md` (kèm `references/quy-trinh-7-buoc.md`) |
| Dựng file .pptx đúng hệ hình ảnh Insider | `references/insider-deck-style.md` |

## Chuỗi chuẩn cho báo cáo tháng
1. Hồ sơ khách: biết KPI và cách framing trước khi đọc số.
2. Làm sạch dữ liệu export. Trước khi gộp hoặc pivot, đối soát số bản ghi hợp lệ và số chờ kiểm tra với đầu vào.
3. Phân tích theo quy trình 7 bước, làm đủ bước xác nhận bắt buộc.
4. Dựng deck theo style Insider.

Cần khung báo cáo marketing chung (không riêng Insider) thì xem `performance-report` trong skill `marketing-strategy`.
