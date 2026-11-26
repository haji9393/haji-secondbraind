---
type: workflow
name: LinkedIn - Thí nghiệm và tối ưu
slug: li-toi-uu-tuan
status: 'off'
group: Marketing
description: "Review tín hiệu định vị sau 7 ngày, ghi quyết định và chuyển câu hỏi về Radar, chiến lược tháng."
steps:
- agent: agency-support-analytics-reporter
  task: "Đọc marketing/linkedin/playbook.md mục Quyết định biên tập, briefs/ và drafts/. Số liệu Haji cung cấp: {{input}}. Ghép đúng URL và giả thuyết, đối chiếu chỉ số đã chọn, mốc so và điều kiện đủ dữ liệu sau 7 ngày. Nếu thiếu, nêu dữ liệu cần, không tăng bộ đếm. Cập nhật đúng dòng của bài, giữ phản hồi thật và mức tiếp cận, so tuần trước và trung bình 4 tuần nếu có. Trả lịch sử từng giả thuyết."
- agent: agency-research-synthesist
  task: "Theo {{prev}} và quy tắc playbook, tách lần trả trước đăng với lần thử dưới mốc. Lần đầu chẩn đoán; sau hai lần hợp lệ dưới mốc, tạm dừng và đọc lại LinkedIn cùng Substack, đề xuất thay đổi cụ thể, dẫn nguồn. Nếu lần làm lại đã duyệt vẫn dưới mốc, ghi dừng trong chu kỳ. Hai bài tốt chỉ cho phép tiếp tục thử. Cập nhật brief và phần đo trong playbook, giữ kết quả thiếu dữ liệu riêng."
  tools: [WebSearch, WebFetch]
- agent: cmo
  task: "Đọc {{prev}}. Với lần làm lại, trình Haji góc/biến đề nghị, lý do và liên kết brief đang chờ duyệt. Nếu luận điểm chính dừng, trình hai hướng thay thế; chỉ áp dụng sau khi Haji chốt. Phản hồi độc giả có giá trị đưa về cuối bản đã đăng cho Radar tuần tới. Ghi quyết định, bằng chứng và câu hỏi nghiên cứu tiếp vào brief. Cập nhật nhật ký từ khóa; chuyển kết quả sang Radar tuần sau và review tháng. Đo phản hồi đúng độc giả theo playbook."
updated: '2026-11-20'
---
Mỗi URL chỉ tính một lần trong cùng giả thuyết.
