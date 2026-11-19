---
type: workflow
name: LinkedIn - Thí nghiệm và tối ưu
slug: li-toi-uu-tuan
status: 'off'
group: Marketing
description: Haji dán số liệu bài tuần; đo giả thuyết, biến thắng 2 tuần liền thành luật, biến thua vào danh sách đã thử, cập nhật playbook.
steps:
- agent: agency-project-management-experiment-tracker
  task: 'Số liệu LinkedIn tuần này Haji dán vào: {{input}}. Nếu đầu vào trống hoặc không có số, DỪNG và trả đúng một câu: "Chưa có số liệu tuần này, Haji dán impressions, reactions, comments, lưu, xem hồ sơ, inbound của từng bài để chạy lại." Nếu có: ghi vào mục "8. Nhật ký số liệu" của marketing/linkedin/playbook.md, so với tuần trước và trung bình 4 tuần, đánh giá từng giả thuyết (thắng, thua, chưa đủ dữ liệu) kèm công thức tính (vd tỉ lệ tương tác = (reactions + comments) / impressions).'
- agent: agency-marketing-growth-hacker
  task: 'Từ đánh giá dưới đây, cập nhật marketing/linkedin/playbook.md: biến thắng 2 tuần liên tiếp chuyển vào "3. Luật đã chứng minh" kèm số; biến thua chuyển vào "4. Đã thử, không hiệu quả"; đề xuất 1-2 giả thuyết mới vào "7. Giả thuyết đang thử". Chỉ sửa playbook, không sửa agent hay skill nào. Thay đổi lớn (đổi trụ nội dung, đổi tần suất, đổi mục tiêu) thì KHÔNG tự sửa, ghi vào cuối báo cáo mục "Cần Haji quyết". Thêm 1 dòng Nhật ký thay đổi. Báo cáo ngắn mở đầu bằng "=>", kết thúc bằng "Next:". Đánh giá: {{prev}}'
updated: '2026-11-19'
---
Chạy thứ 6. Cần Haji dán số liệu bài trong tuần (Javis chưa đấu LinkedIn).
