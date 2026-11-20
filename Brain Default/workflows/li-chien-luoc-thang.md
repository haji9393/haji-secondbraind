---
type: workflow
name: LinkedIn - Chiến lược tháng
slug: li-chien-luoc-thang
status: 'off'
group: Marketing
description: "Trình định vị, mạch tám bài và quyết định tối ưu tháng tới từ tín hiệu nhận diện chuyên môn."
steps:
- agent: cmo
  task: "Đọc marketing/linkedin/playbook.md, strategy/_mau-thang.md, bản chiến lược 90 ngày trong strategy/, báo cáo đối thủ và tối đa 4 radar gần nhất trong research/ cùng kết quả trước. Các đường dẫn ngắn tính từ marketing/linkedin/. Lập một trang theo mẫu: độc giả, năng lực, tranh luận, luận điểm có thể bác bỏ, trụ, trình tự 8 bài tiếng Việt (2/tuần), đề dự phòng, giả thuyết và chỉ số. Bám định vị và thước đo trong playbook. Nếu thiếu nghiên cứu thì nêu rõ phần tạm và yêu cầu bổ sung trước khi chốt. Yêu cầu: {{input}}. Tổng kết vòng tháng trước: người đọc gắn Haji với vấn đề gì, bằng chứng nào còn yếu. Trình Haji câu định vị, trụ, cụm từ và phương án giữ/đổi cùng điều kiện xem lại."
- agent: tl-phan-bien
  task: "Dùng council rà {{prev}}: nguồn gốc và giới hạn, bằng chứng ngược, mạch hiểu biết qua các tuần, mục tiêu định vị, khả năng đo và Red List. Nêu điểm phải sửa và phương án thay thế."
- agent: tro-ly-ceo
  task: "Chốt bản đề xuất từ {{prev}} vào marketing/linkedin/strategy/<YYYY-MM>.md, trình Haji quyết giữa phương án ưu tiên và hướng thay thế. Ghi trạng thái chờ duyệt. Giữ các phiên bản và quyết định cũ trong cùng file. Chỉ ghi đã duyệt nếu tin nhắn thật của Haji xác nhận đúng tháng và phiên bản. Khi nhận duyệt, cập nhật link bản duyệt ở mục 2 playbook."
updated: '2026-11-20'
---
Hồ sơ tháng là đầu vào của buổi chọn góc.
