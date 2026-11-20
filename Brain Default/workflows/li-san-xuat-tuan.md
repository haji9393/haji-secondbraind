---
type: workflow
name: LinkedIn - Sản xuất tuần
slug: li-san-xuat-tuan
status: 'off'
group: Marketing
description: "Viết bài giúp độc giả hiểu cách Haji nhìn một quyết định CX, CRM hoặc AI theo góc đã duyệt."
steps:
- agent: copywriter
  task: "Đọc marketing/linkedin/playbook.md, kế hoạch tháng trong strategy/ và hồ sơ trong briefs/ cho đúng tuần. Đầu vào {{input}} có thể chứa lời duyệt thật của Haji; ghi lại đúng góc và phiên bản nếu rõ. Kiểm cả duyệt tháng, duyệt góc, quyết định dừng và duyệt lần thử lại. Với từng vị trí chưa đủ điều kiện, trả CHỜ DUYỆT hoặc DỪNG kèm lý do. Chỉ viết vị trí đủ điều kiện. Mở lại nguồn gốc, ghi công ý vay mượn, phân biệt ý tác giả và Haji. Dùng haji-writing, haji-career cho dữ kiện cá nhân, giữ Red List. Kèm link brief, nguồn và giả thuyết. Bài phải giúp người đọc tự ra một quyết định; bỏ lời mời tuyển dụng và các đoạn liệt kê thành tích chỉ để giới thiệu bản thân."
  tools: [WebSearch, WebFetch]
- agent: nd-bien-tap
  task: "Với {{prev}}, giữ nguyên trạng thái các vị trí chờ/dừng, chỉ biên tập bài đủ điều kiện. Kiểm chứng luận điểm quan trọng nhất từ bản gốc, trả về đúng bước nếu thiếu bằng chứng. Lưu bản nháp tiếng Việt trong marketing/linkedin/drafts/<YYYY-Www>/ theo ngày đăng T3/T5, status nhap, đường dẫn brief và phiên bản, ngày, mã giả thuyết, biến thử. Gửi Haji duyệt bản cuối. Khi có URL đã đăng, ghi URL và phản hồi thực vào cuối bản và brief."
  tools: [WebSearch, WebFetch]
  verify_agent: nd-kiem-chung
  max_retries: 2
updated: '2026-11-20'
---
Mỗi vị trí được xét riêng; Haji duyệt và tự đăng.
