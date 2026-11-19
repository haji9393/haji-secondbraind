---
type: workflow
name: LinkedIn - Soi đối thủ
slug: li-soi-doi-thu
status: 'off'
group: Marketing
description: Hằng tháng tìm 5-10 người cùng nhắm vai trò CX/Transformation trên LinkedIn VN, chấm điểm, vẽ khoảng trống cho Haji.
steps:
- agent: agency-marketing-social-media-strategist
  task: 'Dùng skill competitive-platform-analysis. Tìm 5-10 người đang xây thương hiệu cá nhân trên LinkedIn ở mảng CX, CRM, transformation, sản phẩm tài chính tại Việt Nam (cùng nhóm vai trò Haji nhắm tới). Chia tier: cạnh tranh trực tiếp, hình mẫu nên học, người kết nối (recruiter, cộng đồng). Mỗi người: link hồ sơ hoặc bài, chủ đề chính, định dạng, nhịp đăng, ví dụ bài nổi. Chỉ dùng thông tin công khai, ghi rõ nguồn. Gợi ý thêm: {{input}}'
  tools: [WebSearch, WebFetch]
- agent: agency-marketing-social-media-strategist
  task: 'Dùng skill benchmark-methodology rồi competitive-report-structure. Chấm điểm từng người theo rubric có bằng chứng, chỉ ra 3-5 khoảng trống mà Haji lấp được bằng trải nghiệm thật (đọc skill haji-career để biết dữ kiện đã khoá). Lưu báo cáo vào marketing/linkedin/research/doi-thu-<YYYY-MM>.md, cập nhật mục "6. Đối thủ và khoảng trống" trong marketing/linkedin/playbook.md, thêm 1 dòng Nhật ký thay đổi. Dữ liệu: {{prev}}'
  verify_agent: nd-kiem-chung
  max_retries: 1
updated: '2026-11-19'
---
Chạy ngày 1 hằng tháng. Kết quả là đầu vào cho "LinkedIn - Chiến lược tháng".
