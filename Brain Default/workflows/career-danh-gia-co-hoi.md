---
type: workflow
name: Career - Đánh giá cơ hội
slug: career-danh-gia-co-hoi
status: active
group: Sự nghiệp
description: "Gemini nghiên cứu công việc, công ty và lương. Trợ lý sự nghiệp đối chiếu kinh nghiệm và trình hướng CV để Haji duyệt."
steps:
  - agent: agency-research-synthesist
    task: >-
      Nghiên cứu cơ hội trong {{input}}. Tìm JD chính thức, mã tin, địa điểm, ngày, hạn và tình trạng tuyển nếu có.
      Tìm hiểu nhiệm vụ, phạm vi quyết định, đội, công ty, mô hình kinh doanh và tín hiệu về lý do tuyển.
      Kiểm tra lương công bố; nếu thiếu, tìm mốc tham chiếu sát cấp bậc và địa điểm, ghi nguồn, kỳ, tiền tệ,
      gross/net và phần cố định/thưởng nếu biết. Nếu nguồn chưa đủ, ghi chưa xác minh; tách ngân sách của công ty
      khỏi dữ liệu so sánh. Ưu tiên nguồn gốc và ghi URL, ngày kiểm; phân biệt dữ kiện với giả thuyết.
      Bàn giao tóm tắt, nguồn và câu hỏi có thể đổi quyết định. Không chấm Haji, hướng CV hay liên hệ bên ngoài.
    tools: [WebSearch, WebFetch]
  - agent: tro-ly-su-nghiep
    task: >-
      Chạy Nhịp 1 theo skills/haji-career/SKILL.md và skills/haji-career/references/haji-cv-builder.md mục 0-1.
      Đọc đầu vào {{input}} và bàn giao nghiên cứu {{prev}}. Kiểm lại các nguồn có thể đổi kết luận.
      Nếu hồ sơ cơ hội đã có brief Haji chốt mới hơn thời điểm {{input}} được tạo, trả LƯỢT CŨ và dừng, không ghi brief mới hay sửa tiến độ. Mở brief Career, hồ sơ cơ hội nếu có, kho dữ kiện CV và haji-job-targeting.md. Đối chiếu lịch sử theo mã tin;
      thư thiếu mã, vị trí hoặc lý do chỉ dùng trong phạm vi bằng chứng. Lập bảng ngắn:
      chức năng JD -> việc thật Haji đã làm (client, kết quả) -> mức khớp,
      bắt đầu từ chỗ mạnh, không đóng khung theo chức danh hay phía vendor/in-house.
      Trả trong 1 lượt: câu quyết định kèm Capability và Direction, khoảng trống và cách lấp, lane (không khớp lane nào
      thì dựng khung mới từ chuỗi giá trị JD, ghi rõ là khung mới, kèm mẫu 1 khối Insider), 2-3 headline neo theo headline
      đã duyệt, luận điểm, mục Tiêu chí đạt (3 câu người đọc phải kể lại được sau 30 giây, 3 lỗi không được mắc lấy từ skills/haji-career/references/haji-cv-review-rubric.md mục 4, CV mẫu để so) để Haji duyệt cùng brief, 3 client đầu, bản nền CV, register, Consultant/Golf House giữ hay bỏ, tối đa 3-4 câu hỏi.
      Lưu nghiên cứu, đánh giá và brief có phiên bản chờ duyệt vào hồ sơ cơ hội (cập nhật file hiện có
      theo mã tin nếu có) và thêm hoặc sửa dòng trong projects/career/tien-do-ung-tuyen.md.
      Gửi Haji link hồ sơ, phiên bản cần chốt và kết luận về lương theo độ chắc của nguồn. Dừng ở đây.
    tools: [WebSearch, WebFetch]
updated: '2026-11-27'
---
Dùng khi có JD cần theo sâu. Người nghiên cứu bàn giao cho Trợ lý sự nghiệp. Sau khi Haji chốt phiên bản brief, dùng workflow viết CV.
