---
type: workflow
name: Career - Đánh giá cơ hội
slug: career-danh-gia-co-hoi
status: active
group: Sự nghiệp
description: "Nghiên cứu công ty, đánh giá JD và phản biện hướng ứng tuyển trước khi Haji chốt brief."
steps:
  - agent: agency-research-synthesist
    task: >-
      Đọc yêu cầu {{input}} và các nguồn được giao. Xác định công ty, vị trí, JD gốc và giai đoạn ứng tuyển.
      Nếu chưa xác định được cơ hội, trả phần cần bổ sung. Mở JD và trang công ty, báo cáo hoặc nguồn sơ cấp liên quan đến đội.
      Trích nhiệm vụ thật, tiêu chí bắt buộc, kết quả vị trí chịu trách nhiệm và tín hiệu giải thích lý do tuyển.
      Ghi URL gốc, ngày, chi tiết đã đọc, phần chưa kiểm được và câu hỏi cần hỏi nhà tuyển dụng.
      Đối chiếu dữ kiện ngoài nếu chúng có thể làm đổi đánh giá. Giữ giả thuyết riêng và đưa nguồn gốc cho bước sau.
    tools: [WebSearch, WebFetch]
  - agent: tro-ly-su-nghiep
    task: >-
      Đọc projects/career/README.md, projects/career/mau-danh-gia-co-hoi.md, haji-career, JD gốc trong {{input}}
      và gói bằng chứng {{prev}}. Nếu chưa xác định được cơ hội, chỉ trả phần cần bổ sung.
      Tự đối chiếu các nguồn quyết định, lập ba phần đánh giá công việc, nghiên cứu công ty và mức phù hợp.
      Chấm Capability và Direction, nêu điều kiện loại và đánh đổi. Phản biện như người tuyển và theo hướng nghề của Haji.
      Đề xuất theo tiếp, xác minh thêm hoặc bỏ qua, kèm kênh và việc tiếp theo. Nếu theo tiếp, lập brief có phiên bản đang chờ duyệt,
      gồm thông điệp chính, thứ tự yêu cầu và bằng chứng, phạm vi dùng và định dạng.
      Lưu vào hồ sơ cơ hội đã có; nếu chưa có, dùng projects/career/co-hoi/<cong-ty>-<vi-tri>-<ma-tuyen-dung-neu-co>.md.
      Giữ lịch sử của hồ sơ, trình đường dẫn và phần cần Haji chốt. Dừng ở đề xuất.
    tools: [WebSearch, WebFetch]
updated: '2026-11-25'
---
Dùng cho JD cần theo sâu. Trợ lý sự nghiệp bàn giao hồ sơ và đề xuất để Haji quyết định.
