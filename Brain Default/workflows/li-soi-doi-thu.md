---
type: workflow
name: LinkedIn - Soi đối thủ
slug: li-soi-doi-thu
status: 'off'
group: Marketing
description: "Đối chiếu tác giả cùng chủ đề để tìm luận điểm khác biệt và khoảng trống có bằng chứng."
steps:
- agent: agency-marketing-social-media-strategist
  task: "Dùng skill market-research, file references/competitive-platform-analysis.md. Tìm 5-10 người đang xây thương hiệu cá nhân trên LinkedIn ở mảng CX, CRM, transformation, sản phẩm tài chính tại Việt Nam (cùng phục vụ độc giả CX và vận hành). Chia tier: cạnh tranh trực tiếp, hình mẫu nên học, người kết nối cộng đồng nghề. Mỗi người: link hồ sơ hoặc bài, chủ đề chính, định dạng, nhịp đăng, ví dụ bài nổi. Chỉ dùng thông tin công khai, ghi rõ nguồn. Gợi ý thêm: {{input}} Chọn người viết theo giao điểm chủ đề và độc giả ở marketing/linkedin/playbook.md, gồm tiếng nói chuyên môn, tuyến đầu và người phản biện. Đối chiếu cả bài Substack khi có."
  tools: [WebSearch, WebFetch]
- agent: agency-marketing-social-media-strategist
  task: 'Dùng skill market-research: file references/benchmark-methodology.md rồi references/competitive-report-structure.md. Chấm điểm từng người theo rubric có bằng chứng, chỉ ra 3-5 khoảng trống mà Haji lấp được bằng trải nghiệm thật (đọc skill haji-career để biết dữ kiện đã khoá). Lưu báo cáo vào marketing/linkedin/research/doi-thu-<YYYY-MM>.md, cập nhật mục "6. Đối thủ và khoảng trống" trong marketing/linkedin/playbook.md, thêm 1 dòng Nhật ký thay đổi. Dữ liệu: {{prev}}'
  verify_agent: nd-kiem-chung
  max_retries: 1
updated: '2026-11-19'
---
Chạy ngày 1 hằng tháng. Kết quả là đầu vào cho "LinkedIn - Chiến lược tháng".
