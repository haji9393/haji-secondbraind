---
type: workflow
name: Career - Viết và phản biện hồ sơ
slug: career-viet-va-phan-bien-ho-so
status: active
group: Sự nghiệp
description: "Viết hồ sơ từ brief Career đã duyệt, kiểm bằng chứng và trình Haji bản nháp."
steps:
  - agent: tro-ly-su-nghiep
    task: >-
      Đọc yêu cầu {{input}} và mở hồ sơ cơ hội. Kiểm đường dẫn hồ sơ, loại đầu ra, phiên bản brief còn hiệu lực
      và xác nhận rõ của Haji cho đúng góc hoặc phiên bản đó trong yêu cầu hoặc hồ sơ. Khi thiếu hoặc vênh, trả CHỜ DUYỆT BRIEF
      kèm điều cần chốt. Nếu đủ, trả ĐÃ CHỐT BRIEF kèm đường dẫn, phiên bản, đầu ra được giao, yêu cầu chính,
      bằng chứng và nguồn gốc. Ghi lại xác nhận của Haji trong hồ sơ nếu được cung cấp trong yêu cầu.
  - agent: copywriter
    task: >-
      Nhận {{prev}} và đối chiếu {{input}}. Nếu chưa ĐÃ CHỐT BRIEF, giữ nguyên trạng thái và dừng phần viết.
      Nếu đã chốt, đọc trực tiếp hồ sơ, JD, skills/haji-career/references/haji-cv-builder.md và
      skills/haji-career/references/haji-cv-evidence-bank.md. Viết đầu ra đã giao theo phần Career của Copywriter.
      Nêu nguồn của claim chính và ghi rõ điểm cần xác nhận. Khi xuất hiện vấn đề làm đổi hướng hoặc mất bằng chứng chính,
      trả CẦN CHỐT LẠI BRIEF kèm lý do và phương án, rồi dừng phần viết. Chuyển bản nháp và phiên bản brief cho Trợ lý sự nghiệp.
  - agent: tro-ly-su-nghiep
    task: >-
      Đọc {{input}} và kết quả {{prev}}. Với trạng thái chờ hoặc cần chốt lại, trình đúng câu hỏi hoặc bằng chứng cần bổ sung.
      Với bản nháp, mở lại brief, JD và kho dữ kiện. Đọc như reviewer tuyển dụng, kiểm phần đầu có chứng minh đúng vai hay chưa,
      phần Haji thực sự sở hữu, nguồn, kỳ đo, mẫu số và Red List. Sửa lỗi trong phạm vi brief rồi kiểm lại một lượt.
      Nếu vẫn có lỗi trọng yếu hoặc phải đổi hướng, trả brief về Haji cùng chứng cứ và phương án xử lý.
      Nếu qua kiểm, lưu đường dẫn hoặc phiên bản bản nháp và kết quả phản biện trong hồ sơ cơ hội.
      Trình bản nháp đầy đủ hoặc link file đã ghi được, phần đã sửa và điểm cần Haji duyệt. Chỉ ghi đã nộp khi có xác nhận nộp thật.
updated: '2026-11-25'
---
Dùng sau khi Haji đã chốt hướng ứng tuyển. Trợ lý sự nghiệp bàn giao bản nháp để Haji duyệt trước khi dùng.
