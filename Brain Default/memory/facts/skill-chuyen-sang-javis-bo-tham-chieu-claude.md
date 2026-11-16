---
type: preference
provenance: user
origin: javis-learned
created: 2026-11-16
updated: 2026-11-16
---
Khi chuyển skill từ Claude sang Javis, bỏ tham chiếu artifact của claude.ai và bộ nhớ riêng của Claude, thay bằng memory/ của brain. File Sheets đi theo Google Sheet nếu trang Kết nối có Google Sheets, nếu không thì xuất .xlsx vào exports/. Người dùng yêu cầu tự chỉnh các điểm không hợp với Javis. [[javis-builder]] [[conversations/2026-11-16]]

**Vì sao:** Javis không có artifact của claude.ai nên skill sẽ không chạy đúng nếu giữ nguyên.
**Áp dụng:** Khi thêm hoặc sửa skill cho Javis, rà các từ khoá artifact, memory, project của Claude trước khi lưu.
