---
type: workflow
name: LinkedIn - Sản xuất tuần
slug: li-san-xuat-tuan
status: 'off'
group: Marketing
description: Mỗi tuần ra 2 bản nháp LinkedIn tiếng Việt đúng giọng Haji, gắn giả thuyết đang test, kiểm Red List và số đã khoá.
steps:
- agent: nd-goc-nhin
  task: 'Đọc marketing/linkedin/playbook.md (trụ nội dung, luật đã chứng minh, thị trường đang quan tâm, giả thuyết đang thử) và radar mới nhất trong marketing/linkedin/research/. Chọn 2 góc bài cho tuần tới, đăng thứ 3 và thứ 5. Mỗi góc: trụ nội dung, insight thị trường nó bám, trải nghiệm thật của Haji làm chất liệu, giả thuyết nó test (mã trong playbook). Không lặp góc của 4 tuần gần nhất trong marketing/linkedin/drafts/. Gợi ý thêm: {{input}}'
- agent: copywriter
  task: 'Dùng skill haji-writing và haji-career. Viết 2 bài LinkedIn tiếng Việt từ 2 góc dưới đây, mục tiêu để recruiter và hiring manager thấy năng lực Head of CX/Transformation/PM tài chính. Tuân thủ luật đã chứng minh trong playbook. Chỉ dùng số đã khoá, không dùng mục Red List. Mỗi bài ghi đầu file: ngày đăng đề xuất, trụ, mã giả thuyết, biến đang test. Góc bài: {{prev}}'
- agent: nd-bien-tap
  task: 'Gọt 2 bài dưới đây hết mùi AI, giữ nguyên ý và số, không dùng em dash. Lưu mỗi bài thành 1 file trong marketing/linkedin/drafts/<YYYY-Www>/ (vd bai-1-thu3.md, bai-2-thu5.md) với frontmatter status: nhap. Bài: {{prev}}'
  verify_agent: nd-kiem-chung
  max_retries: 2
updated: '2026-11-19'
---
Chạy tối chủ nhật. Haji duyệt và tự đăng; Javis không đăng lên LinkedIn.
