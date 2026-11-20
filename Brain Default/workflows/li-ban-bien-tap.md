---
type: workflow
name: LinkedIn - Họp biên tập nhóm Marketing
slug: li-ban-bien-tap
status: active
group: Marketing Linkedin
description: Nhóm Marketing Linkedin nhận một đề mở, nghiên cứu LinkedIn và Substack, phát triển luận điểm và trình Haji chọn góc.
steps:
- agent: cmo
  task: "Nhận đề của Haji: {{input}}. Đọc marketing/linkedin/playbook.md và chiến lược tháng nếu có. Chốt câu hỏi độc giả cần giải, trụ định vị đang thử và quyết định buổi biên tập cần đưa ra. Nếu chưa có tháng duyệt, vẫn nghiên cứu và trình hướng thử; ghi rõ cần duyệt tháng trước khi sản xuất."
- agent: agency-research-synthesist
  task: "Đọc marketing/linkedin/research/chu-de-va-tu-khoa.md, sổ nguồn, Radar gần nhất và câu hỏi từ briefs/. Với đề của CMO: {{prev}}, tận dụng nguồn còn phù hợp và tự mở nguồn gốc trên LinkedIn lẫn Substack. Mở rộng từ khóa theo vai người nói, phễu, cơ chế và phản ví dụ. Ghi phạm vi truy cập từng nền tảng, URL/ngày, luận điểm tác giả, bằng chứng và giới hạn. Trả cả câu hỏi gốc, đường tìm và hai cách giải thích khác nhau. Nếu chưa đủ nguồn, ghi cụ thể phần còn thiếu."
  tools: [WebSearch, WebFetch]
- agent: copywriter
  task: "Đọc phần bàn giao {{prev}} và mở lại các nguồn quyết định. Cho mỗi vị trí trong tuần đề xuất 2-3 luận điểm khác nhau: ai đọc, họ đang tin gì, nguồn nào làm thay đổi cách nghĩ, phản biện mạnh nhất và quyết định nào hữu ích. Chỉ ra một thủ pháp viết có thể học từ tác giả; phân biệt ví dụ minh họa với trải nghiệm thật. Chuyển cả URL cho CMO."
  tools: [WebSearch, WebFetch]
- agent: cmo
  task: "So các phương án {{prev}} với kế hoạch tháng và quyết định trong marketing/linkedin/briefs/. Dùng cùng mẫu và hồ sơ của li-de-xuat-goc-tuan, cùng mã giả thuyết cho cùng chủ đề; nếu đã có đề xuất thì cập nhật đúng hồ sơ thay vì tạo bản trùng. Ghi lựa chọn, phương án thứ hai, chỉ số chính, mốc so, điều kiện đủ dữ liệu và thay đổi so lần trước. Chuyển việc thiếu nguồn về Radar với truy vấn cụ thể. Góc chưa duyệt, giả thuyết tạm dừng hoặc thiếu tháng duyệt phải ghi rõ trạng thái."
- agent: tro-ly-ceo
  task: "Trình Haji từ {{prev}}: chọn gì cho từng bài, vì sao, bằng chứng có thể đảo kết luận, link brief và phiên bản. Kết thúc ở điểm cần Haji duyệt. Khi có lời duyệt thật, lưu theo playbook và dùng li-san-xuat-tuan cho vị trí đủ điều kiện. Sau đăng, li-toi-uu-tuan đọc số sau 7 ngày và đưa câu hỏi về Radar. Không tự giao việc nền hoặc đăng bài."
updated: '2026-11-20'
---
Dùng khi giao nhóm Marketing Linkedin một đề mở cần nghiên cứu ngay. Khi đã có Radar và chỉ cần chốt góc định kỳ, dùng li-de-xuat-goc-tuan. Cả hai dùng chung brief và vòng duyệt.
