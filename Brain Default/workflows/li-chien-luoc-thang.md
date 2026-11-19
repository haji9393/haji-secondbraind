---
type: workflow
name: LinkedIn - Chiến lược tháng
slug: li-chien-luoc-thang
status: 'off'
group: Marketing
description: CMO đề xuất trụ nội dung, KPI, giả thuyết tháng cho LinkedIn tìm việc; phản biện qua council; Trợ lý CEO trình Haji duyệt.
steps:
- agent: cmo
  task: 'Đọc marketing/linkedin/playbook.md, báo cáo đối thủ mới nhất và 4 file radar gần nhất trong marketing/linkedin/research/. Đề xuất chiến lược LinkedIn tháng tới cho mục tiêu tìm việc: 3-4 trụ nội dung, tỉ lệ bài từng trụ trên 8 bài/tháng, 2-3 giả thuyết cần test (mỗi giả thuyết chỉ đổi 1 biến: hook, định dạng, độ dài, giờ đăng, CTA), KPI mục tiêu kèm công thức. Dùng dữ kiện đã khoá từ skill haji-career. Ghi chú của Haji: {{input}}'
- agent: tl-phan-bien
  task: 'Dùng skill council để phản biện đề xuất dưới đây với 4 giọng (chính, Skeptic, Pragmatist, Critic). Soi: có phục vụ tìm việc không, có rủi ro Red List hay số chưa khoá không, giả thuyết có đo được không, có nặng hơn 2 bài/tuần không. Trả bản đề xuất đã sửa kèm danh sách điểm đã đổi. Đề xuất: {{prev}}'
- agent: tro-ly-ceo
  task: 'Soạn bản trình Haji duyệt từ chiến lược đã phản biện dưới đây: kết luận 3 dòng mở đầu bằng "=>", bảng trụ nội dung và tỉ lệ, giả thuyết tháng, KPI kèm công thức, "Next:" là việc Haji cần quyết. Lưu vào marketing/linkedin/research/chien-luoc-<YYYY-MM>.md với status: cho-duyet. CHƯA sửa playbook; chỉ khi Haji duyệt mới chép trụ nội dung và giả thuyết vào playbook. Dữ liệu: {{prev}}'
updated: '2026-11-19'
---
Chạy ngay sau "LinkedIn - Soi đối thủ". Kết quả luôn chờ Haji duyệt.
