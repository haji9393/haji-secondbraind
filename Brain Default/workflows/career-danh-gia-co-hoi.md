---
type: workflow
name: Career - Đánh giá cơ hội
slug: career-danh-gia-co-hoi
status: active
group: Sự nghiệp
description: "Nhịp 1: đối chiếu JD với việc thật của Haji, chấm điểm và đưa kế hoạch CV để Haji chốt."
steps:
  - agent: tro-ly-su-nghiep
    task: >-
      Chạy Nhịp 1 theo skills/haji-career/SKILL.md và skills/haji-career/references/haji-cv-builder.md mục 0-1.
      Đọc JD trong {{input}}. Nếu chỉ có tin đăng lại hoặc chưa rõ công ty, tìm nhanh JD gốc và trang công ty
      (WebSearch/WebFetch), ghi URL; không lập bảng trích nguồn dài. Mở skills/haji-career/references/haji-cv-evidence-bank.md
      và haji-job-targeting.md. Lập bảng ngắn: chức năng JD -> việc thật Haji đã làm (client, kết quả) -> mức khớp,
      bắt đầu từ chỗ mạnh, không đóng khung theo chức danh hay phía vendor/in-house.
      Trả trong 1 lượt: câu quyết định kèm Capability và Direction, khoảng trống và cách lấp, lane (không khớp lane nào
      thì dựng khung mới từ chuỗi giá trị JD, ghi rõ là khung mới, kèm mẫu 1 khối Insider), 2-3 headline neo theo headline
      đã duyệt, luận điểm, 3 client đầu, bản nền CV, register, Consultant/Golf House giữ hay bỏ, tối đa 3-4 câu hỏi.
      Lưu vào projects/career/co-hoi/<cong-ty-vi-tri>.md (cập nhật nếu đã có) và thêm hoặc sửa dòng trong
      projects/career/tien-do-ung-tuyen.md. Dừng, chờ Haji chốt rồi mới viết.
    tools: [WebSearch, WebFetch]
updated: '2026-11-27'
---
Dùng khi có JD mới. Một bước, làm thẳng; viết CV chạy ở workflow career-viet-va-phan-bien-ho-so sau khi Haji chốt.
