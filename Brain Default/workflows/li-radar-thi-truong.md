---
type: workflow
name: LinkedIn - Radar thị trường
slug: li-radar-thi-truong
status: 'off'
group: Marketing
description: Quét tuần xu hướng CX/CRM/AI, JD Head of CX/Transformation/PM tài chính ở VN, tín hiệu recruiter; cập nhật playbook LinkedIn.
steps:
- agent: agency-product-trend-researcher
  task: 'Dùng skill market-research và deep-research. Quét 7 ngày qua, ưu tiên nguồn Việt Nam và khu vực: (1) chủ đề CX, CRM, AI trong chăm sóc khách hàng, chuyển đổi số đang được bàn nhiều trên LinkedIn và báo ngành; (2) JD mới cho Head of CX, Head of Transformation, PM sản phẩm tài chính cá nhân tại VN: công ty nào, yêu cầu gì lặp lại, từ khoá nào; (3) recruiter, headhunter đang đăng gì. Mỗi ý kèm link nguồn và ngày. Ghi chú thêm: {{input}}. Không bịa link, không bịa số.'
  tools: [WebSearch, WebFetch]
- agent: agency-research-synthesist
  task: 'Chưng cất kết quả quét dưới đây thành 5-8 insight cho LinkedIn tìm việc của Haji. Mỗi insight: điều thị trường quan tâm, bằng chứng (link), gợi ý góc bài mà Haji có trải nghiệm thật để viết. Thêm 1 mục "Từ khoá JD nên xuất hiện trong bài và hồ sơ". Lưu bản đầy đủ vào marketing/linkedin/research/radar-<YYYY-MM-DD>.md, rồi thay mục "5. Thị trường đang quan tâm gì" trong marketing/linkedin/playbook.md bằng tối đa 10 dòng mới nhất, thêm 1 dòng vào Nhật ký thay đổi. Dữ liệu: {{prev}}'
  verify_agent: nd-kiem-chung
  max_retries: 1
updated: '2026-11-19'
---
Chạy mỗi thứ 2 sau 10:00. Đầu vào tuỳ chọn: chủ đề muốn soi thêm tuần này.
