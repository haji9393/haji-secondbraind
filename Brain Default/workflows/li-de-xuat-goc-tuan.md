---
type: workflow
name: LinkedIn - Đề xuất góc tuần
slug: li-de-xuat-goc-tuan
status: 'off'
group: Marketing
description: "Đề xuất góc chuyên môn và trình Haji chọn theo định vị và câu hỏi thật của độc giả."
steps:
- agent: nd-goc-nhin
  task: "Đọc marketing/linkedin/playbook.md, strategy/<YYYY-MM>.md đã duyệt, briefs/ và research/radar gần nhất. Nếu chưa duyệt tháng, trả CHỜ THÁNG. Với hai vị trí tuần, đề xuất 2-3 luận điểm khác nhau cho mỗi vị trí, nêu người đọc, niềm tin, bằng chứng, phản biện và quyết định. So với 4 tuần drafts/ để tránh lặp. Đọc bài gốc. Ghi chú {{input}}. Mỗi góc nêu trụ, tranh luận, độc giả và điều muốn họ nhớ về tư duy Haji."
  tools: [WebSearch, WebFetch]
- agent: copywriter
  task: "Nếu {{prev}} là CHỜ THÁNG thì chuyển trạng thái đó. Với các góc còn lại, đọc lại nguồn gốc, chỉ ra cách tác giả dựng lập luận, đề nghị sửa hoặc đảo góc khi bằng chứng yêu cầu. Chuyển bảng góc và URL cho CMO."
  tools: [WebSearch, WebFetch]
- agent: cmo
  task: "Nếu {{prev}} báo chờ tháng thì trả trạng thái đó. Với từng vị trí đã đủ nguồn, điền marketing/linkedin/briefs/_mau-de-bai.md thành briefs/<chu-de>.md, tái dùng đúng hồ sơ theo mã giả thuyết. So hai góc tốt nhất, chọn một, giải thích vai trò trong tháng. Chốt chỉ số, mốc so, điều kiện đủ dữ liệu và phản biện. Tra playbook khi đề bị trả hai lần hoặc giả thuyết đã tạm dừng."
- agent: tro-ly-ceo
  task: "Trình Haji hai lựa chọn cho từng vị trí, đường dẫn brief, phiên bản và đề nghị của CMO từ {{prev}}. Nếu thiếu duyệt tháng thì chỉ trình phần còn thiếu. Ghi quyết định theo playbook khi nhận phản hồi thật, dừng ở đề xuất cho tới khi Haji chọn."
updated: '2026-11-20'
---
Tách lần trình đề khỏi lần viết để Haji có thể trả lại hoặc chọn một góc khác.
