---
type: workflow
name: LinkedIn - Radar thị trường
slug: li-radar-thi-truong
status: 'off'
group: Marketing
description: "Quét tín hiệu định vị CX/CRM/AI trên LinkedIn và Substack từ bộ từ khóa và phản hồi độc giả."
steps:
- agent: agency-product-trend-researcher
  task: "Dùng market-research và deep-research. Đọc marketing/linkedin/research/nguon-theo-doi.md, radar trước và phản hồi cuối các bản đã đăng trong drafts/. Quét 7 ngày trên cả LinkedIn và Substack theo sổ nguồn, theo tranh luận của người làm nghề và lãnh đạo vận hành. Từng nguồn ghi URL gốc, tác giả, ngày bài và ngày sự kiện, luận điểm, dẫn chứng, phản biện, cách tác giả triển khai bài. Ghi riêng kết quả mỗi nền tảng kể cả khi paywall, đăng nhập hay không tìm được; chỉ nêu phần đọc được. Ghi chú: {{input}}. Đọc marketing/linkedin/research/chu-de-va-tu-khoa.md và câu hỏi CMO ghi trong briefs/. Áp dụng mục Cách mở rộng từ một câu hỏi: thử cách gọi của khách, tuyến đầu và lãnh đạo; truy tiếp thuật ngữ gặp trong bài gốc và một phản ví dụ. Ghi đường từ truy vấn đến nguồn và góc mới. Tra hai ngôn ngữ, ghi cụm từ, trụ, tín hiệu trái chiều và trả nguồn về brief đã đặt câu hỏi."
  tools: [WebSearch, WebFetch]
- agent: agency-research-synthesist
  task: "Từ {{prev}}, cập nhật sổ nguồn marketing/linkedin/research/nguon-theo-doi.md và radar-<YYYY-MM-DD>.md cùng thư mục. Tách nhận định tác giả với suy luận nhóm; so kỳ trước, truy về nguồn đầu tiên của các bài chia sẻ lại. Chỉ gọi là xu hướng nếu có nguồn độc lập và thay đổi theo thời gian. Giữ cả ý đơn lẻ và ý chưa có case Haji; ghi câu hỏi đáng tranh luận, nguồn đối lập, trụ liên quan và từ khóa cần theo kỳ sau. Cập nhật link mục 5 và nhật ký playbook."
  verify_agent: nd-kiem-chung
  max_retries: 1
updated: '2026-11-20'
---
Đầu ra là bản đọc tuần phục vụ cả chiến lược và phát triển góc.
