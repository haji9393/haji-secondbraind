---
name: "Báo cáo tháng Insider"
description: "Dựng và đánh giá báo cáo hiệu quả hàng tháng cho khách hàng Insider: bước xác nhận bắt buộc và quy trình phân tích 7 bước."
group: Marketing
---

# Insider Monthly Performance Report Skill

## Khi nào dùng

Use this skill whenever building, evaluating, or presenting a monthly performance report for clients using the Insider platform. Triggers include: "báo cáo tháng", "monthly report", "đánh giá hiệu quả Insider", "performance Insider", "review tháng", "report cho [client]", or any request to analyze/summarize Insider campaign/module results across any vertical (Telecom, Banking, Super App, Logistics, E-commerce). Always use this skill even for brief prompts like "làm report VTT tháng này" or "review Sacombank tháng 3". Do NOT attempt to build or evaluate an Insider report without reading this skill first - the confirmation step and 7-step analysis process are mandatory.

## Verticals được hỗ trợ

| Vertical | Client tiêu biểu | Đặc thù chính |
|---|---|---|
| **Telecom** | Viettel (VTT) | Large base, ARPU, churn critical, nhiều Khối/đơn vị |
| **Banking / Securities** | Sacombank, TP Bank, MB Bank, MBS | Compliance, long conversion cycle, AUM focus |
| **Super App / Logistics** | VETC, GHN | Multi-sided platform, volume & feature adoption |
| **E-commerce / Other** | Printerval, Ahamove | Cart recovery, GMV, activation, sender/driver segments |

---

## BƯỚC 0 - MANDATORY CONFIRMATION

> **Quy tắc bắt buộc**: Trước khi build hoặc đánh giá bất kỳ report nào, phải confirm đủ 3 input dưới đây. Không tự suy đoán nếu thông tin chưa rõ.

### [INPUT 1] Business Objectives & Funnel

Xác nhận hoặc hỏi:

```
1. Client đang theo đuổi Objective(s) nào tháng này?
   □ Tăng Conversion Rate (CR)
   □ Tăng MAU / DAU
   □ Giảm Churn / Tăng Retention
   □ Upsell / Cross-sell
   □ Onboarding / Activation
   □ Reactivation / Win-back
   □ Feature Adoption
   □ Khác: ___

2. Funnel stage nào là focus chính tháng này?
   Acquisition → Onboarding → Engagement → Retention → Upsell → Reactivation

3. Có target cụ thể không? (VD: CR +5%, MAU đạt 2M, Churn < 3%)

4. Có thay đổi chiến lược nào so với tháng trước không?
```

### [INPUT 2] Scope & Data

Xác nhận hoặc hỏi:

```
1. Modules Insider đang active tháng này?
   □ App Push  □ InApp (100% rollout)  □ InApp (A/B Testing)
   □ Web Push  □ Web InApp / InStory  □ Email  □ SMS
   □ Architect (Journey)  □ WhatsApp  □ Khác: ___

2. Kỳ báo cáo: Tháng mấy? So sánh với tháng nào?

3. Có data không?
   → Nếu có file/export → yêu cầu đính kèm trước khi phân tích
   → Nếu không → báo cáo dừng ở framework, không có số liệu thực

4. Data dimensions nào có sẵn?
   (Campaign name, Keyword, Business Unit/Khối, Personnel, Product, Region, Segment...)
```

### [INPUT 3] Hướng phân tích (Smart of Report)

Xác nhận hoặc hỏi:

```
1. Audience của report là ai?
   □ Internal team (technical, detailed)
   □ Client marketing team (balanced)
   □ Client C-level / CMO (executive summary)

2. Có hypothesis hoặc góc nhìn muốn tập trung không?
   VD: "Nghi campaign push kém hiệu quả"
       "Muốn thấy ROI của Architect"
       "So sánh Email vs Push"
       "Chứng minh Insider đang tạo giá trị"

3. Output format mong muốn?
   □ HTML Dashboard  □ PowerPoint (.pptx)  □ Markdown  □ Excel (.xlsx)
```

> Sau khi nhận đủ 3 input → tiến hành phân tích theo quy trình 7 bước bên dưới.

---

## PHẦN 1 - QUY TRÌNH 7 BƯỚC PHÂN TÍCH (Core Analysis Engine)

> Mindset: Bạn là **Senior Analytics Consultant**. Không phải chỉ "đọc data rồi báo cáo" - mà là **dùng data để trả lời câu hỏi kinh doanh**. Mỗi con số phải serve một business question cụ thể.

Chi tiết từng bước (câu hỏi phải hỏi user, code kiểm tra, template output) nằm ở `references/quy-trinh-7-buoc.md`. BẮT BUỘC đọc file đó sau BƯỚC 0 và trước khi phân tích; làm đủ 7 bước, đúng thứ tự, không bỏ bước.

1. Understand Data Field Availability & Meaning
2. Validate Data - 5-Row Sample Reconfirmation
3. Confirm Conversion Definition Per Module
4. Understand Business Issues & Formalize Analytic Objectives
5. Offer Hypotheses & Confirm Before Testing
6. Analyze - Test Hypotheses & Extract Insights
7. Synthesize - Present Insights & Recommend Actions

---

## PHẦN 2 - Platform Health Check

Luôn kiểm tra trước khi đánh giá hiệu quả (có thể chạy song song với Step 1-2):

| Hạng mục | Mục đích | Cờ đỏ |
|---|---|---|
| CDP Profile coverage | % user được track | < 60% → data gap |
| Event tracking status | PG Event, AddToCart, Purchase | Missing → revenue attribution sai |
| Segment size vs. addressable base | Reach thực tế | Quá nhỏ → misconfiguration |
| Channel opt-in rates | Deliverability | < 30% push opt-in → cần Permission dialog |

> ⚠️ **Tracking caveat rule**: Nếu phát hiện tracking lỗi (VD: PG Event "Purchase" missing), ghi rõ caveat, đề xuất fix, và đặt asterisk (*) trên MỌI conversion metric trong report. Ước lượng impact nếu có thể (VD: "~2,000+ missed conversions/tháng").

---

## PHẦN 3 - Report Output Structure

### Cấu trúc chuẩn cho mọi report:

```
1. EXECUTIVE SUMMARY (1 slide / 1 section)
   - Headline metric: 1 con số nổi bật nhất
   - 3-line summary: volume, engagement, conversion
   - Tracking status: ⚠️ caveat nếu có

2. PLATFORM HEALTH (nếu có issues)
   - CDP coverage, tracking status, channel health

3. HYPOTHESIS SUMMARY TABLE
   - Bảng tóm tắt H1-H5 + verdicts (from Step 7)

4. PHÂN TÍCH 3 LENSES (from Step 6)
   - Lens 1: Module Performance (tab/slide per module)
   - Lens 2: Objective Performance (mapping table)
   - Lens 3: Funnel Coverage (gap analysis)

5. ✅ WHAT'S GOOD  ← MANDATORY
   ≥3 điểm cụ thể, có số liệu

6. 🎯 WHAT'S NEXT  ← MANDATORY
   3 loại: Fix / Optimize / Explore

7. APPENDIX (optional)
   - Data quality notes
   - Conversion definitions used
   - Detailed tables
```

### Color coding chuẩn

| Status | Hex | Ý nghĩa |
|---|---|---|
| 🟢 Green | `#22c55e` | On track / Healthy / Confirmed |
| 🟡 Yellow | `#f59e0b` | Needs attention / Partially confirmed |
| 🔴 Red | `#ef4444` | Critical issue / Off track / Rejected |
| 🔵 Blue | `#3b82f6` | Opportunity / Explore |

### Audience-specific framing

| Audience | Tone | Detail level | Focus | Hypothesis depth |
|---|---|---|---|---|
| Internal team | Technical | Full metrics, raw data | Module-level deep dive | Full H1-H5 with data |
| Client marketing | Balanced | Key metrics + insights | Objective alignment | Summary table + top 3 |
| Client C-level/CMO | Executive | Headlines + actions | Business impact, ROI | Answer first, then evidence |

---

## PHẦN 4 - Client & Vertical References

Xem chi tiết per-vertical và per-client tại:
- Skill `insider-client-profiles` (`skills/insider-client-profiles/SKILL.md`) - Industry profiles, đặc thù KPI, cách frame kết quả
- KPI templates per objective, benchmarks, red flags: file `references/objectives.md` của bản gốc KHÔNG có trong Javis. Thiếu benchmark thì hỏi user, không tự đặt số.

---

## PHẦN 5 - Output Format Guide

| Format | Dùng khi | Cách làm trong Javis |
|---|---|---|
| HTML Dashboard | Internal review, interactive, có charts + tabs | Ghi file .html vào `exports/insider/` trong vault |
| PowerPoint (.pptx) | Client presentation, C-level | Dựng bằng script (python-pptx hoặc pptxgenjs), theo skill `insider-deck-style` |
| Markdown/Text | Draft nhanh, discussion | - |
| Excel (.xlsx) | Raw data log, performance tracking | Dựng bằng script (openpyxl), lưu vào `exports/insider/` |

### HTML Dashboard specifics:
- Tab switching cho từng module
- Chart.js cho visualizations
- Responsive, có thể mở trên mobile
- Color-coded metrics (green/yellow/red)
- Include data tables dưới mỗi chart

### PowerPoint specifics:
- Embed matplotlib charts as images
- 1 key takeaway per slide
- Max 5 bullet points per slide
- Speaker notes cho presenter
- Consistent color palette throughout

---

## PHẦN 6 - Quality Checklist

Trước khi deliver report, verify:

**Process integrity:**
- [ ] Đã confirm đủ 3 inputs (Objective, Scope, Smart)?
- [ ] Đã show 5-row sample và user confirm data meaning?
- [ ] Đã confirm conversion definition per module?
- [ ] Đã formalize hypotheses và user confirm trước khi test?

**Analysis completeness:**
- [ ] Đã cover cả 3 Lenses (Module, Objective, Funnel)?
- [ ] Mỗi hypothesis có verdict rõ ràng (Confirmed/Partial/Rejected)?
- [ ] Có Hypothesis Summary Table?

**Output quality:**
- [ ] Có section "What's Good" với ≥3 điểm cụ thể?
- [ ] Có section "What's Next" với 3 loại action (Fix/Optimize/Explore)?
- [ ] Tracking caveat đã ghi rõ nếu có lỗi?
- [ ] Control Group đã loại trừ khỏi calculations?
- [ ] Charts có title, legend, và label rõ ràng?
- [ ] Tone phù hợp với audience?
- [ ] MoM comparison nếu có data tháng trước?
- [ ] Insight viết theo Pyramid: answer first → evidence → so what?
