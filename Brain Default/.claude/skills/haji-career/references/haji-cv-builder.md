> Gộp từ skill cũ `haji-cv-builder` ngày 2026-11-18. Mô tả gốc: Viết hoặc chỉnh CV cho Haji theo JD: chọn kênh, chấm độ phù hợp, chọn lane, ráp nội dung từ kho dữ kiện, chạy checklist, xuất bản 2 cột.


# Haji CV Builder - cách làm và cách viết

## Khi nào dùng

Viết hoặc chỉnh CV cho Haji theo JD: chọn kênh nộp, chấm độ phù hợp, chọn lane, ráp nội dung từ kho dữ kiện, viết đúng văn phong, chạy checklist rồi xuất bản 2 cột.

Skill này là quy trình. Dữ kiện nằm ở `haji-cv-evidence-bank`, định hướng, kênh nộp và lịch sử nộp nằm ở `haji-job-targeting`. Luôn load cả hai trước khi viết (trong Javis: đọc `skills/haji-career/references/haji-cv-evidence-bank.md` và `skills/haji-career/references/haji-job-targeting.md`).

Nguyên tắc gốc: CV là ráp, không phải viết lại. Không bịa số. Số nào không có trong evidence bank thì hỏi Haji trước.

## 1. Quy trình

1. **Nhận đầu vào.** JD (text hoặc link), công ty, vị trí, kênh nộp dự kiến. Thiếu JD thì hỏi.
2. **Chọn kênh trước khi viết** (theo mục Kênh nộp trong `haji-job-targeting`):
   - Vị trí Head / Director / Senior Manager in-house: tìm referral trước. Kiểm tra trong mạng lưới 70+ tổ chức cũ, Insider alumni, người quen ở công ty đích. Đề xuất 1-3 người có thể đưa CV vào.
   - Portal ATS: chỉ khi khoảng cách chức danh nhỏ, hoặc không có đường referral. Trước khi nộp, soạn sẵn câu trả lời knockout.
   - LinkedIn: nộp kèm message cho recruiter/hiring manager trong 24 giờ.
3. **Đọc JD hai lần.** Lần 1 lấy trách nhiệm. Lần 2 lấy requirement cứng (Minimum, Required, Must, firm).
4. **Chấm và đề xuất định vị:** Capability x/10, Direction x/10, loại gap, kênh, lane, headline, 1 luận điểm chủ đạo, 3 client example đầu, register (giữ hay hạ). **Hỏi Haji có nêu tên Golf House trong CV này không.** **Dừng lại, chờ Haji xác nhận.**
5. **Chọn bản nền** trong Drive (`CV & Ứng tuyển 2026 / CV_ Phương Hoàng`), chỉ dùng thế hệ từ 19/10/2026 trở đi:
   - CS: `CV_Phuong Hoang_Apply for Younet Media` (benchmark văn phong experience). Trước khi dùng phải sửa: "kept NPS above 90" → "90%+ client satisfaction rate"; bỏ "2 to 6 months"; "Account & Project Executive" → "Senior Project Management Specialist".
   - CX: `CV_Phuong Hoang_Apply for ILA`
   - CRM / CVM: `CV_Phuong Hoang_Apply for Home Credit`
   - Transformation / Product: `CV_Phuong Hoang_Apply for Phuc Long` (sửa "2 to 6 months" và dòng team theo mục G của evidence bank)
   - BFSI Transformation: `Phuong_Hoang_Transformation_CX Strategy_BFSI.pptx`
   - **Không dùng làm nền:** `CV_Phuong Hoang_Apply for Chubb Vietnam`, `CV_Phuong Hoang_Apply for AIA Vietnam`, `Phuong Hoang_CV_ Apply for AIA` và mọi bản trước 19/10. Các bản này chạm Red List và trái quy tắc hiện tại.
   - Mọi bản nền: rà lại số Sacombank theo mục E3 evidence bank (bản ILA và Home Credit trước 29/10 còn ghi "digital transactions 65%" như tăng trưởng).
6. **Ráp theo 3 layer.**
   - Layer 1: dữ kiện bất biến (timeline, số đã khoá).
   - Layer 2: khung của lane (mục 4).
   - Layer 3: 4 chỉnh sửa theo JD: (a) headline, (b) summary, (c) thứ tự nhóm năng lực và client example, (d) At a Glance + Top Skills + nhóm Portfolio.
7. **Viết** theo mục 3, 5, 6.
8. **Kiểm tra** theo checklist mục 8.
9. **Xuất file.** Mặc định Google Slides 2 cột, tên `CV_Phuong Hoang_Apply for [Company]`. Nộp qua portal ATS (Workday, Taleo, SuccessFactors...) thì làm thêm bản ATS 1 cột.
10. **Sau khi xong:** ghi vào application log trong `haji-job-targeting` (có cột kênh); nêu cho Haji các dữ kiện mới cần thêm vào evidence bank.

## 2. Cấu trúc CV 2 trang, 2 cột

**Trang 1**
- Cột chính: TÊN (dòng riêng) → Headline (dòng riêng) → Contact (1 dòng) → Summary (3-4 câu) → PROFESSIONAL EXPERIENCE: khối Consultant → khối Insider One (descriptor, dòng chức danh, dòng Scope, 3 nhóm năng lực đầu).
- Cột phụ: AT A GLANCE (6-7 dòng) → TOP SKILLS (3-4 nhóm, mỗi nhóm 3-5 keyword) → TOOLS nếu đủ chỗ.

**Trang 2**
- Cột phụ: PORTFOLIO (nhóm theo ngành, tên nhóm theo logic JD) → EDUCATION → LANGUAGES (→ TOOLS nếu trang 1 hết chỗ).
- Cột chính: PROFESSIONAL EXPERIENCE (CONTINUED): các nhóm còn lại → Team leadership → dòng 3rd Shareholder → DIGITAL AGENCIES.

Nhóm năng lực khớp JD nhất và client example mạnh nhất phải nằm trọn trên trang 1.

**Bản ATS:** 1 cột, Calibri/Aptos 10.5-11pt, lề 1.5-1.7cm, không bảng/icon/thanh kỹ năng, contact trong body (không header/footer), tiêu đề chuẩn (Summary, Experience, Skills, Education), ngày MM/YYYY. **Tên và chức danh luôn ở hai dòng/đoạn riêng**, không chung một dòng in đậm, vì parser sẽ đọc cả dòng là tên.

## 3. Từng khối, công thức viết

**Headline:** `[DIRECTION] | [VISION của direction đó]`, viết hoa, khớp tên vị trí đang tuyển. Vision không được nghe như tự xưng. Với lane không phải CS, headline không mở bằng "Customer Success Lead". Headline hứa gì (ví dụ "built to scale") thì thân CV phải có bằng chứng cho điều đó (scale = growth, xem evidence bank mục D). Đã dùng:
- CUSTOMER SUCCESS | SUSTAINABLE CLIENT GROWTH & BUSINESS IMPACT
- CUSTOMER EXPERIENCE | CONSISTENT, MEASURABLE, BUILT TO SCALE
- CVM & LIFECYCLE | RIGHT CUSTOMER, RIGHT CHANNEL, RIGHT COST
- DIGITAL TRANSFORMATION | FROM VISION TO EXECUTION, ALWAYS IMPROVING
- Transformation & CX Strategy Lead | Banking & Financial Services

**Contact:** `+84 81 222 6707 · hoangphuong9393@gmail.com · linkedin.com/in/haji9393 · Ho Chi Minh City`. Requirement cứng trả lời được bằng 1 dòng (onsite, múi giờ, travel, ngày bắt đầu) thì thêm ngay dưới contact.

**Summary (3-4 câu ngắn, ngôi thứ ba, mở bằng cụm danh từ):**
1. `[Direction] professional with an 11-year career, including 7 years [làm gì] across 70+ organizations in [ngành khớp JD].` 11 năm thể hiện độ chín sự nghiệp; 7 năm là số năm làm CX/CRM thực tế. Không viết "11 years [CX]".
2. Làm gì, theo góc nhìn người trong nhà (inside-out, ownership).
3. Không dừng ở go-live: tối ưu đến khi thành cách công ty vận hành.
4. Đo thành công bằng KPI khớp JD.

Cấm trong summary: chữ "I", tên client, chữ "clients", giọng agency/vendor, "SaaS" trong danh sách ngành, "experienced in", "strong background in", "skilled in", liệt kê dài, câu nối nhiều "and", số không liên quan JD (renewal, NPS, ví dụ AI không thuộc summary CX/Transformation).

**Khối Consultant:** tiêu đề `CONSULTANT`, dòng phụ `[Mảng theo lane] & Business Operations, 07/2026 – Present`, 2-3 dòng `[Tổ chức]: [đã làm gì]`, chọn theo lane. Golf House: nêu tên khi Haji đã xác nhận cho CV đó.

**Khối Insider One:**
- `INSIDER ONE`
- `Global CDP and customer engagement platform, Gartner Magic Quadrant Leader 5 years running`
- `Customer Success Lead, 2022 – 06/2026 · promoted from Customer Success Manager (2019 – 2022)`
- Dòng Scope theo lane, ví dụ: `Scope: accountable for [strategy, implementation, adoption and results] across a 70+ organization portfolio in Vietnam, Laos and Myanmar, from the first workshop to renewal.`
- 5-7 nhóm năng lực, mỗi nhóm 1-3 bullet năng lực + 1-3 client example.

**Bullet năng lực:** làm được gì → ở đâu/với ai → kết quả/KPI. Động từ quá khứ mở đầu. **Tối đa 2 dòng (~30 chữ).** Mô tả đúng độ sâu chiến lược và thực thi, không chung chung, không giọng tư vấn giảng giải.

**Client example:** 1 dòng ngắn `[Client]: [đã làm X], [kết quả]`. Kết quả kinh doanh của client dùng `contributing to`. Không rải tên client vào bullet năng lực. Số phải đúng phép so sánh gốc (ví dụ Sacombank: "players made 65% more digital transactions than non-players", không phải "grew 65%").

**Dòng ghi nhận:** `Named 3rd Shareholder at Insider One Vietnam in 2022, with headquarters recognizing a market playbook other regions went on to use.` Một dòng, cuối khối Insider, không nêu giá trị cổ phần. **Chỉ xuất hiện 1 lần, không lặp ở At a Glance.**

**Agency:** `DIGITAL AGENCIES · IDM, Alpha Leapers, Climax Interactive, Biz-Eyes` / `Senior Project Management Specialist, 2015 – 2018` / 2 bullet (15+ dự án; website đặt vé VNA + revamp 4,584 trang).

**At a Glance:** số nổi bật và năng lực khác biệt khớp JD (kênh, ngành, tăng trưởng, kết quả). Không dùng số đếm chung chung kiểu "70+ organizations". Không đặt 3rd Shareholder. Format: `[số]  [nhãn ngắn]`. Dòng kinh nghiệm viết `11 years  career, 7 in [lane]`.

**Top Skills:** keyword ngắn, đúng kỹ năng thật, 3-4 nhóm có tên. Không văn xuôi, không jargon chung chung (RAID, SteerCo facilitation nếu không có bằng chứng), không ghi tên nền tảng (Insider One) như một skill.

**Portfolio:** tên client nhóm theo ngành, tên nhóm theo góc JD (vd CX: Multi-site service brands, High-consideration purchases, Trust & compliance-sensitive, Membership & lifecycle).

## 4. Khung nhóm năng lực theo lane (Layer 2)

Nhóm phải tách bạch, không trùng tên hay nội dung.

**CS:** Onboarding and adoption · Retention, renewal and account growth · Client governance and stakeholder management · Team leadership and CS operations · Product and company growth · CX, CRM strategy and enablement.

**CX:** CX strategy and journey design · Service standards and consistency · Voice of customer, risk and measurement · CX technology and channel deployment · Stakeholder alignment and change adoption · Team, product and operating model.

**CRM / CVM / Lifecycle:** Lifecycle strategy and segmentation · Campaign orchestration, cross-sell and upsell · Measurement, data and product feedback · Technology and channel efficiency · Stakeholder alignment and digital sales · Team leadership.

**Digital Transformation / Product mindset:** Product discovery and roadmap · Pilot, delivery and portfolio management · Data standards and platform integration · Adoption, training and change · Retail, loyalty and conversion (đổi theo ngành JD) · Value tracking, reporting and AI · Team leadership.

**BFSI Transformation:** dùng khối BFSI trong evidence bank; thứ tự client mặc định MBS → TP Bank → Generali → Sacombank → ACB → Wavemoney/U-money/Unitel → Vietnam Airlines.

**Năng lực phải có mặt rõ ràng ở các lane CX / CRM / Transformation** (không nhắc lướt):
- Channel deployment: tư vấn kênh theo giai đoạn lifecycle, triển khai trọn 9 kênh, Zalo ZNS + Mini App là điểm khác biệt.
- Quản trị rủi ro chủ động như một scope of work: theo dõi tín hiệu, call out rủi ro sớm, prevention plan; client example FPT Shop.
- Product ở mức nhận định nhu cầu chung, ưu tiên, business case, thuyết phục product.
- Playbook từ pattern chung, cộng thiết kế kịch bản đặc thù cho từng công ty.
- Đào tạo cân bằng độ rộng (300+) và độ sâu (MBS Journey Makers, Bamboo).
- Tăng trưởng (4.3x, team 7-10 → 30+) khi CV nói về scale.

## 5. Quy tắc văn phong

- Không bao giờ dùng em dash. Dùng dấu phẩy, hai chấm, hoặc tách câu.
- American English. Số viết bằng chữ số.
- Câu ngắn, dễ đọc. Dẫn bằng động từ, không bằng tính từ.
- Từ vựng: `client portfolio`, `account ARR`, `largest strategic account`, `maximize within allocated budget`, `among the first` (Generali), `SteerCo` reviews/advisory (không chaired).
- Tránh: "without authority", "teaching", "setting service standards and customer journeys" chung chung, "risk teams" mơ hồ (dùng tên phòng thật).
- **Độ sâu strategy → framework → execution, không dùng từ tuyệt đối về kết quả.** Muốn cho thấy Haji đi từ chiến lược, qua framework, tới thực thi thì viết chuỗi động từ theo 3 tầng trong cùng bullet (set the strategy/KPIs → built the framework/playbook/standard → ran, measured and optimized execution), và gắn phạm vi phương pháp khi đó đúng là cách làm chuẩn (`for each program`, `at every level`, `from strategy to go-live`). Không dùng từ tuyệt đối cho kết quả không kiểm chứng được: "every engagement", "no ... on any engagement", "a majority of accounts", "always", "never", "every team served to the same standard", "until each team ran it on its own". Thay bằng kết quả có thật hoặc client example.
- Kênh viết dạng channel deployment và journey orchestration, không liệt kê tool rời.
- Chẩn đoán ba phía: business, technical, product/platform. Viết gọn và đắt.
- Viết như người trong nhà, không giọng vendor bán hàng.
- Ở lane CX / Transformation / CRM: giữ chân khách hàng viết như độ bền trải nghiệm và chương trình, không dùng ngôn ngữ account manager.
- Không có mục AI Projects riêng. AI viết bằng tư duy và cách làm (tìm phần việc lặp lại để workflow/AI gánh, giữ thời gian của người cho phán đoán và khách hàng), không dẫn ví dụ số trên CV.
- Không đưa SQL, Python, Power BI (setup) vào skills. Power BI chỉ ghi "(reporting)".
- Ngôn ngữ tiền khớp JD: revenue/business case cho thương mại; adoption/benefits realization cho transformation; lifecycle revenue/retention cho CRM.

## 6. Hạ register theo JD

JD có scope thực thi thấp hơn trần (PMO, báo cáo SteerCo, Senior Manager in-house):
- Bỏ ngôn ngữ ARR/doanh thu và framing cố vấn C-level.
- Thừa nhận chuyển từ partner-side sang in-house trong summary.
- Đổi 73% renewal thành bằng chứng độ bền chương trình; không đặt renewal trong summary.

## 7. Thang quy kết công lao

- Mức 1 (Led, Designed, Built, Mapped): artifact Haji tự làm.
- Mức 2 (contributing to, helping): mọi kết quả kinh doanh của client.
- Mức 3 (Supported, Advised): volume hoặc hoạt động thuộc về client (Viettel 90M push/tháng, ACB).
- Thay đổi operating model nội bộ Insider: `Championed ... for the Vietnam market and led by example`, không `Led ... changes`.
- Tự hỏi từng bullet: bị khoan sâu có bảo vệ được không? Không thì hạ một bậc hoặc bỏ.

## 8. Checklist trước khi xuất

**Kênh:** đã thử tìm referral cho vị trí Head? Nếu nộp portal, đã soạn câu trả lời knockout?
**Sự thật:** mọi số có trong evidence bank? Không chạm Red List? Không dùng mục "cần chốt" khi chưa hỏi? Số Sacombank đúng phép so sánh? Đã hỏi Haji về tên Golf House?
**Summary:** 3-4 câu, ngôi thứ ba, "11-year career, including 7 years…", không tên client, không "clients", không "SaaS", không giọng vendor, số khớp JD?
**Headline:** đúng format, khớp tên vị trí, không tự xưng, không mở bằng "Customer Success Lead" khi lane không phải CS? Tên và headline ở hai dòng riêng? Lời hứa trong headline có bằng chứng trong thân CV?
**Cấu trúc:** nhóm năng lực tách bạch? Mỗi nhóm có client example riêng? Bullet ≤ 2 dòng? Example mạnh nhất trọn trang 1? Channel deployment, quản trị rủi ro, product, playbook, đào tạo có mặt rõ?
**Quy kết:** kết quả client dùng contributing to? Không có từ tuyệt đối về kết quả? Operating model viết championed?
**Từ vựng:** đã quét nghĩa kép (retention, churn, conversion, growth, portfolio, account)? Không có ngôn ngữ account manager ở lane CX/Transformation/CRM?
**Framing bắt buộc:** VNA = first marketing automation channels on the path to personalization at scale; Generali among the first; 90%+ client satisfaction rate (không NPS); Vinpearl 2.75x; không Salesforce migration; không go-live "2 to 6 months" như chuẩn; chẩn đoán ba phía.
**Nhất quán:** agency = Senior Project Management Specialist; Insider kết thúc 06/2026; dòng team theo mục G evidence bank; 3rd Shareholder chỉ 1 lần, cuối khối Insider.
**Format:** không em dash, American English, không lỗi gõ (đọc lại toàn văn), 2 trang, tên file đúng, knockout đã trả lời ở contact.