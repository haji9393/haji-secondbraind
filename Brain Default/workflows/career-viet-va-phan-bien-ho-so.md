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
      kèm điều cần chốt. Nếu đủ, trả ĐÃ CHỐT BRIEF kèm đường dẫn, phiên bản, đầu ra, chân dung nghề nghiệp,
      mạch nghiệp vụ, bằng chứng và nguồn. Với brief cũ, tổng hợp chân dung từ CV gốc, kho dữ kiện và lời Haji
      trong phạm vi hướng đã duyệt. Chỉ hỏi lại khi có quyết định thực sự làm đổi hướng hoặc thiếu bằng chứng trọng yếu.
      Với CV, mở bản gốc Haji chỉ định hoặc bản gần nhất về nghiệp vụ; chốt bản nền nội dung và mẫu có sẵn theo kênh.
      Đưa đường dẫn, đoạn cần giữ hoặc chỉnh và lý do vào bàn giao. Ghi lại xác nhận của Haji trong hồ sơ nếu được cung cấp.
  - agent: copywriter
    task: >-
      Nhận {{prev}} và đối chiếu {{input}}. Nếu chưa ĐÃ CHỐT BRIEF, giữ nguyên trạng thái và dừng phần viết.
      Nếu đã chốt, đọc trực tiếp hồ sơ, JD, skills/haji-career/references/haji-cv-builder.md và
      skills/haji-career/references/haji-cv-evidence-bank.md. Với CV, mở bản nền thực tế; giữ nguyên đoạn đã rõ và
      đúng vai, chuyển thứ tự hoặc chỉnh phạm vi khi cần, viết thêm từ nguồn đã xác nhận khi bản nền còn thiếu.
      Giữ quyết định, cách làm, quyền hạn và kết quả có sẵn trong các ca được chọn. Mỗi thay đổi lớn nêu đoạn gốc,
      thay đổi và lý do; khi rút thì giữ chi tiết làm nên giá trị của ca. Dùng mẫu hai cột hoặc ATS đã có theo kênh.
      Rà giọng với câu chữ trong CV gốc và skills/haji-writing/references/humanizer.md, tránh làm mất nghĩa nghiệp vụ.
      Áp dụng phần Career của Copywriter cho các đầu ra khác.
      Nêu nguồn của claim chính và ghi rõ điểm cần xác nhận. Khi xuất hiện vấn đề làm đổi hướng hoặc mất bằng chứng chính,
      trả CẦN CHỐT LẠI BRIEF kèm lý do và phương án, rồi dừng phần viết. Chuyển bản nháp và phiên bản brief cho Trợ lý sự nghiệp.
  - agent: tro-ly-su-nghiep
    task: >-
      Đọc {{input}} và kết quả {{prev}}. Với trạng thái chờ hoặc cần chốt lại, trình đúng câu hỏi hoặc bằng chứng cần bổ sung.
      Với bản nháp CV, vòng một đọc riêng bản chữ trước khi mở JD. Diễn giải bằng lời thường Haji làm gì, tác động
      quyết định nào và chịu trách nhiệm đến đâu. Nếu chỉ kể được tên khách hàng, sản phẩm hoặc số liệu, sửa mạch kể.
      Vòng hai đặt bản nháp cạnh bản gốc rồi đối chiếu brief, JD và kho dữ kiện. Kiểm từng ca chính còn rõ quyết định,
      cách làm, phạm vi và kết quả như nguồn cho phép; hoàn nguyên hoặc sửa mọi chỗ bị rút thành mô tả chung.
      Kiểm số, kỳ, mẫu số và Red List. Rà cả phần đọc lướt: câu mở và khối Insider phải cho thấy tầm công việc
      và đưa được một ca thật ra trước. Mở bản Google Slides để kiểm thứ tự đọc và chữ; gửi link Drive, chỉ xuất PDF
      khi Haji xác nhận. Với đầu ra khác, dùng brief và nguồn để phản biện theo mục đích của tài liệu.
      Nếu vẫn có lỗi trọng yếu hoặc phải đổi hướng, trả brief về Haji cùng chứng cứ và phương án xử lý.
      Nếu qua kiểm, lưu đường dẫn hoặc phiên bản bản nháp và kết quả phản biện trong hồ sơ cơ hội.
      Trình bản nháp đầy đủ hoặc link file đã ghi được, phần đã sửa và điểm cần Haji duyệt. Chỉ ghi đã nộp khi có xác nhận nộp thật.
updated: '2026-11-26'
---
Dùng sau khi Haji đã chốt hướng ứng tuyển. Trợ lý sự nghiệp bàn giao bản nháp để Haji duyệt trước khi dùng.
