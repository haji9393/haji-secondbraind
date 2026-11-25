---
name: insider-cs
description: "Quản trị khách hàng, xử lý thuê bao và hoàn tiền, trích và đối soát dữ liệu, làm sạch file xuất, lập báo cáo tháng và dựng deck Insider."
group: Marketing
---
# Insider Customer Success

Mở đúng file trong `references/` theo việc.

## Khi nào dùng
| Việc | Mở file |
|---|---|
| Tra KPI, cách framing, vấn đề đã biết của một khách (Viettel, Sacombank, TP Bank, MBS, VETC, GHN...) | [references/insider-client-profiles.md](skills/insider-cs/references/insider-client-profiles.md) |
| Làm sạch file .xlsx export thô, thêm cột Conversion, pivot theo event | [references/insider-data-cleanup.md](skills/insider-cs/references/insider-data-cleanup.md) (kèm [references/rule-sets.md](skills/insider-cs/references/rule-sets.md), [references/master-sheets.md](skills/insider-cs/references/master-sheets.md)) |
| Dựng và đánh giá báo cáo hiệu quả tháng | [references/insider-monthly-report.md](skills/insider-cs/references/insider-monthly-report.md) (kèm [references/quy-trinh-7-buoc.md](skills/insider-cs/references/quy-trinh-7-buoc.md)) |
| Dựng file .pptx đúng hệ hình ảnh Insider | [references/insider-deck-style.md](skills/insider-cs/references/insider-deck-style.md) |
| Khách gặp vấn đề thuê bao, hoá đơn, hoàn tiền: xác minh đúng giao dịch và trạng thái qua công cụ thanh toán được cấp quyền | [references/customer-billing-ops.md](skills/insider-cs/references/customer-billing-ops.md) |
| Trích dữ liệu từ file xuất, biểu mẫu, hoá đơn: chọn regex hay LLM theo định dạng, đối soát từng bản ghi với nguồn | [references/regex-vs-llm-structured-text.md](skills/insider-cs/references/regex-vs-llm-structured-text.md) |

## Chuỗi chuẩn cho báo cáo tháng
1. Hồ sơ khách: biết KPI và cách framing trước khi đọc số.
2. Làm sạch dữ liệu export. Trước khi gộp hoặc pivot, đối soát số bản ghi hợp lệ và số chờ kiểm tra với đầu vào.
3. Phân tích theo quy trình 7 bước, làm đủ bước xác nhận bắt buộc. Nếu có tín hiệu sụt adoption, gián đoạn đo lường hoặc KPI thay đổi, kiểm trước xem do định nghĩa, dữ liệu hay vận hành. Báo sớm ảnh hưởng với khách và đề xuất người xử lý, phép kiểm tiếp theo và mốc cần can thiệp.
4. Dựng deck theo style Insider.

Cần khung báo cáo marketing chung (không riêng Insider) thì xem `performance-report` trong skill `marketing-strategy`.
