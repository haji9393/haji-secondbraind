---
type: workflow
name: Từ ý tưởng ra bài đăng
slug: y-tuong-thanh-bai-dang
status: active
description: Tìm góc tiếp cận, viết bài, biên tập, rồi kiểm chứng trước khi đăng.
steps:
- agent: cmo
  task: 'Tìm góc tiếp cận cho ý tưởng sau: {{input}}'
- agent: copywriter
  task: 'Viết bài đăng hoàn chỉnh theo góc tiếp cận đã chốt dưới đây:


    {{prev}}'
- agent: nd-kiem-chung
  task: 'Biên tập bài dưới đây cho gọn và chắc hơn:


    {{prev}}'
  verify_agent: nd-kiem-chung
  max_retries: 2
updated: '2026-09-05'
---

Tìm góc tiếp cận, viết bài, biên tập, rồi kiểm chứng trước khi đăng.
