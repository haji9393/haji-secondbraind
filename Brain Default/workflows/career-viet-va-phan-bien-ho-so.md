---
type: workflow
name: Career - Viết và phản biện hồ sơ
slug: career-viet-va-phan-bien-ho-so
status: active
group: Sự nghiệp
description: "Copywriter viết CV, Người phản biện độc lập chấm góc người tuyển, Trợ lý kiểm sự thật và chỉ giao link Drive khi đạt."
steps:
  - agent: tro-ly-su-nghiep
    task: >-
      Đọc {{input}}, mở hồ sơ cơ hội và kiểm phiên bản brief Haji đã xác nhận. Nếu hồ sơ đã có brief mới hơn phiên bản
      trong {{input}}, hoặc CV đã qua bước giao link sau thời điểm {{input}} được tạo, trả LƯỢT CŨ kèm phiên bản hiện hành và
      dừng, không ghi gì vào hồ sơ hay tiến độ. Nếu thiếu xác nhận, phiên bản không khớp, hoặc phản hồi làm đổi định vị hay cách
      kể vai trò của Haji, trả CHỜ CHỐT BRIEF kèm lý do và việc cần Haji chốt. Nếu đủ, bàn giao ĐÃ CHỐT gồm đường dẫn hồ sơ,
      bằng chứng duyệt, phiên bản, bản nền, mẫu CV theo kênh, luận điểm, case, giới hạn công bố và mục Tiêu chí đạt của brief
      (3 câu người đọc phải kể lại được, 3 lỗi không được mắc, CV mẫu để so). Nếu brief chưa có Tiêu chí đạt, soạn từ luận
      điểm và skills/haji-career/references/haji-cv-review-rubric.md, ghi rõ "Trợ lý soạn, Haji chưa duyệt" và ghi vào hồ sơ.
      Nếu đang chỉnh, xác định đúng bản Drive hiện hành. Bước này KHÔNG sao chép, viết hay sửa CV và không tự nhận CV đã đạt.
  - agent: copywriter
    verify_agent: nd-kiem-chung
    max_retries: 2
    task: >-
      Đọc bàn giao {{prev}}. Nếu LƯỢT CŨ hoặc CHỜ CHỐT BRIEF, chuyển nguyên trạng thái và lý do, không mở bản nháp mới hay sửa Drive.
      Chỉ viết khi ĐÃ CHỐT và hồ sơ hoặc đầu vào {{input}} có xác nhận khớp phiên bản. Đọc haji-cv-builder.md,
      haji-job-targeting.md, haji-cv-evidence-bank.md và haji-cv-review-rubric.md trong skills/haji-career/references.
      Sao chép bản nền đã chốt ngay trong thư mục CV trên Drive nếu cơ hội chưa có bản nháp. Đặt tên
      CV_Phuong Hoang_Apply for [Company]. Ghi ngay mã file, link nội bộ và phiên bản brief vào hồ sơ cơ hội sau khi sao chép.
      Mọi vòng sửa dùng file đó, kể cả lần chạy lại sau lỗi. Nếu đã có bản sao, sửa trên bản đó, không tạo bản khác.
      Khi nhận phản hồi phản biện, sửa đúng các lỗi Chặn và Nên sửa được nêu. Nếu phát hiện lỗi định vị, sai phần đóng góp
      của Haji hoặc thiếu xác nhận cho bằng chứng trọng yếu, trả CHỜ CHỐT BRIEF với vấn đề cụ thể. Trả bàn giao nội bộ gồm
      đường dẫn hồ sơ, phiên bản brief, link và revision CV, phần đã sửa. Không xuất PDF, đổi quyền chia sẻ hay liên hệ nhà tuyển dụng.
      TIÊU CHÍ PHẢN BIỆN VÒNG 1 (người đọc tuyển dụng, theo haji-cv-review-rubric.md mục 1-3): mở đầu bằng 3 dòng Góc nhìn
      (hiring manager của đúng vị trí trong hồ sơ), Quan điểm (luận điểm và Tiêu chí đạt của brief, ghi phiên bản), Cơ sở (dòng JD,
      mục kho dữ kiện, CV mẫu, lỗi Haji đã chê). Mở CV trên Drive và đọc TRƯỚC khi mở brief, viết lại 3 câu Haji làm gì, ở tầm nào,
      mạnh nhất ở đâu, rồi so với Tiêu chí đạt. Không so với lời bàn giao của Copywriter, không chấm quy trình hay dấu chạy.
      Mỗi nhận xét ghi vị trí, câu trích, tiêu chí kèm cơ sở, mức Chặn/Nên sửa/Ghi chú, cách sửa. pass=false CHỈ khi còn lỗi Chặn;
      lỗi Nên sửa ghi vào fixes nhưng vẫn pass=true. Với LƯỢT CŨ hoặc CHỜ CHỐT BRIEF, pass=true chỉ khi điều kiện dừng là đúng.
  - agent: copywriter
    verify_agent: tro-ly-su-nghiep
    max_retries: 2
    task: >-
      Đọc {{prev}}. Nếu LƯỢT CŨ hoặc CHỜ CHỐT BRIEF, chuyển nguyên trạng thái, không sửa Drive. Nếu kết quả vòng 1 còn lỗi
      Nên sửa, sửa trên cùng file Drive. Sau đó tự đối chiếu sự thật theo haji-cv-review-rubric.md mục 2 vòng 2 và trả bàn giao
      gồm link, revision, phần đã sửa và bảng số liệu dùng trong CV kèm mục kho dữ kiện tương ứng.
      TIÊU CHÍ PHẢN BIỆN VÒNG 2 (kiểm sự thật): mở đầu bằng Góc nhìn (người kiểm sự thật), Quan điểm (brief đã chốt, phiên bản),
      Cơ sở (haji-cv-evidence-bank.md mục cụ thể, Red List và Framing bắt buộc mục F, mẫu đã chốt). Mở CV trên Drive và bản hiển
      thị, kiểm từng số (kỳ, mẫu số, chủ thể), Red List, nhất quán chức danh và mốc, headline đã duyệt, tràn chữ và format.
      Không bàn văn ở vòng này. Mỗi lỗi ghi vị trí, câu trích, cơ sở, mức và cách sửa. pass=false CHỈ khi có lỗi Chặn
      (sai sự thật, Red List, hỏng hiển thị, sai mẫu).
  - agent: tro-ly-su-nghiep
    task: >-
      Đọc kết quả đã qua hai vòng phản biện {{prev}} và đầu vào {{input}}. Nếu LƯỢT CŨ, dừng im lặng kèm một dòng lý do.
      Nếu CHỜ CHỐT BRIEF, báo lý do, nội dung Haji cần chốt và dừng. Với bản đạt, mở hồ sơ, đối chiếu lại đúng link Drive và
      revision đã kiểm. Ghi link, phiên bản, kết quả hai vòng (số lỗi Chặn đã sửa, lỗi Nên sửa còn lại), trạng thái chờ Haji duyệt
      và bước tiếp theo vào hồ sơ cơ hội và projects/career/tien-do-ung-tuyen.md. Trình Haji link CV online kèm 2-3 điểm cần duyệt.
      Nếu thiếu bằng chứng phản biện hoặc không mở được đúng file, báo vướng mắc và giữ link nội bộ.
      Chỉ xuất PDF khi Haji yêu cầu. Chỉ ghi đã nộp khi Haji xác nhận.
updated: '2026-11-27'
---
Dùng sau khi Haji chốt phiên bản brief. Trợ lý duyệt điều kiện đầu vào và Tiêu chí đạt. Copywriter viết. Vòng 1, Người phản biện độc lập chấm từ góc hiring manager. Vòng 2, Trợ lý kiểm sự thật. Chỉ lỗi Chặn mới trả bản; mỗi vòng sửa tối đa 2 lần, vẫn chưa đạt thì dừng trước bước giao. Thước đo: [[skills/haji-career/references/haji-cv-review-rubric]].
