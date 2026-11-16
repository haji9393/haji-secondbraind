---
name: "Hồ sơ khách hàng Insider"
description: "Hồ sơ từng khách hàng Insider (Viettel, Sacombank, TP Bank, MBS, VETC, GHN...): KPI, cách framing, vấn đề đã biết, ghi chú riêng."
group: Marketing
---

# Insider Client Profiles

## Khi nào dùng

Use this skill for ANY task involving a named Insider client - including business reviews, monthly reports, analysis/deep-dives, decks, pitch decks, and presentations. Triggers include client names (Viettel, VTT, Sacombank, TP Bank, MBS, MB Securities, VETC, GHN, Ahamove, Printerval, Vinpearl) or vertical references ("Banking client", "Telecom client", "Logistics client"). ALWAYS use this skill before starting any client-facing deliverable - it loads the correct KPIs, framing approach, known issues, and per-client notes so output is contextually accurate. Do NOT skip this skill even for quick tasks like "tóm tắt kết quả cho VTT" or "chuẩn bị slide cho Sacombank".

## Step 1 - Confirm Client & Task

Before loading any profile, ask:

> "Bạn đang làm việc với client nào, và deliverable là gì?"
> *(Ví dụ: "Sacombank - Business Review tháng 5" hoặc "VTT - Deck pitch CDP")*

If client name is already in the prompt, confirm:
> "Tôi sẽ dùng profile **[Client Name]** cho task **[Task Type]**. Đúng không?"

**Supported task types:** Business Review / Monthly Report · Analysis / Deep-dive · Deck / Pitch / Presentation

Once confirmed, load the relevant vertical profile below, plus any per-client notes.

---

## Step 2 - Load Vertical Profile

Read the matching section and apply KPIs, framing, and known issues throughout the deliverable.

---

### 🔵 Telecom - Viettel (VTT)

**Đặc thù:**
- User base cực lớn (tens of millions), push volume cao (90M+/tháng)
- Nhiều đơn vị kinh doanh (Khối): TTDH, TTDVM, TTTH, TTDD, VTpost
- Nhiều nhân sự cùng chạy campaign → Personnel dimension quan trọng
- Product-driven: gói cước, data, VAS, TV360, 5G
- Conversion cycle ngắn: đăng ký gói cước = minutes

**Modules active:** App Push · InApp (100% + A/B) · Architect

**KPIs ưu tiên:**
- Push: Delivered volume, Open Rate, CTR, 2G/3G Conversion
- InApp: Impression, CTR, CR (Conv/Clicks)
- A/B: Uplift %, statistical confidence
- Architect: Entry → Completion Rate, end-of-journey conversion

**Dimensions phân tích:**
- By Khối (Business Unit) → ai đang perform tốt/kém
- By Product / Split 2 → sản phẩm nào convert tốt
- By Personnel / Split 3 → nhân sự nào cần hỗ trợ
- By timeline → trend theo tháng / theo tuần

**Known issues:**
- ⚠️ PG Event "Purchase" tracking thường misconfigured → 0 conversion trên nhiều campaign. Luôn dựa trên Event goal (custom events), không dùng PG Purchase mặc định
- Control Group rows cần loại trừ khỏi tính toán
- Volume lớn nhưng CTR thấp → cần segment tốt hơn

**Cách frame kết quả:**
- C-level: conversion volume + tracking gap impact
- Marketing team: per-Khối performance + top/bottom campaigns
- Technical: tracking fixes + A/B test methodology

---

### 🟢 Banking / Securities - Vertical Profile

**Đặc thù:**
- Compliance requirements cao, content cần review kỹ
- Conversion cycle dài: account opening → first trade → AUM build
- User segments rõ ràng: New → Active → VIP → Dormant
- Product complexity: stocks, bonds, derivatives, savings

**Modules active:** App Push · Email · Journey/Architect · InApp

**KPIs ưu tiên:**
- Activation: eKYC completion, first trade
- Engagement: DAU/MAU, session depth
- Upsell: AUM growth, product diversification
- Retention: Dormant rate, win-back success

**Dimensions phân tích:**
- By user segment (New / Active / VIP / Dormant)
- By product type (equity / bond / derivative)
- By journey stage
- By channel (app / web / email)

**Cách frame kết quả:**
- Dùng ROAD framework cho strategic conversations
- Focus vào "barrier analysis" per segment
- AUM và trading volume = ultimate success metric

#### Per-Client Notes (Banking)

| Client | Đặc thù riêng | Known issues | Status |
|--------|--------------|--------------|--------|
| **Sacombank** | Gamification layer ("Game Xây Nhà Xanh"), C-level dashboard active, multi-vendor | Game + Automation layers cần tách riêng khi report | Active |
| **TP Bank** | CDP positioning pitch đang active, CEO-level audience | Deck cần business-outcome-first, tránh technical detail | Active |
| **MBS (MB Securities)** | Securities-specific: first trade, margin lending. GGAM/ROAD framework đang train | Competitor: WOAY mạnh hơn cho complex game mechanics | Active |
| **MB Bank** | *(Placeholder - điền sau)* | - | TBD |

---

### 🟠 Super App / Logistics - VETC, GHN

**Đặc thù:**
- Multi-sided platform (sender/receiver, merchant/driver)
- Transaction volume là core metric
- Feature adoption quan trọng: auto-toll, loyalty, nạp tiền, đăng ký eWallet
- Operational KPIs: delivery time, completion rate

**Modules active:** App Push · InApp · Journey · Web Push

**KPIs ưu tiên:**
- Transaction volume & frequency
- Feature adoption rate
- User activation (first transaction, cross-sell)
- Retention by user type

**Dimensions phân tích:**
- By user type (sender/driver, merchant/individual)
- By feature (payment, tracking, rating)
- By region/city
- By transaction type

**Known issues:**
- VETC: Executive comms cần metric-led momentum framing (CEO audience)
- GHN: OKR-aligned reporting - link campaigns → company OKRs

**Cách frame kết quả:**
- Volume impact > rate improvement
- OKR-aligned (link campaigns → company OKRs)
- Operational efficiency angle

---

### 🔴 E-commerce - Printerval, Ahamove

**Đặc thù:**
- GMV-driven, cart recovery critical
- Short conversion cycle nhưng repeat purchase matters
- Seasonal peaks (holidays, sales events)
- Multi-channel attribution phức tạp

**Modules active:** Email (Klaviyo + Insider) · Web Push · App Push · Journey

**KPIs ưu tiên:**
- GMV contribution
- Cart abandonment recovery rate
- Repeat purchase rate
- Email/Push → Revenue attribution

**Dimensions phân tích:**
- By campaign type (promotional / lifecycle / transactional)
- By product category
- By customer lifecycle stage
- By channel (Klaviyo vs Insider vs GA4)

**Known issues:**
- Printerval: UTM normalization challenges, SUMIFS/IMPORTRANGE formula complexity trong Google Sheets attribution
- Ahamove: Web push metrics declining (Chrome policy changes) → frame carefully

**Cách frame kết quả:**
- Revenue attribution là core story
- Compare channels (email vs push vs in-app)
- UTM tracking accuracy matters

---

## Step 3 - New Client Discovery

Khi gặp client chưa có profile, chạy discovery questions sau:

1. **Business model**: B2C? B2B? Marketplace? SaaS?
2. **Primary metric**: Revenue? MAU? Transactions? AUM?
3. **Current Insider modules**: Đang dùng gì? Planned?
4. **User base size**: Thousands? Millions?
5. **Conversion definition**: Mua hàng? Đăng ký? First action?
6. **Existing tracking**: GA4? Internal? Insider events?
7. **Team structure**: Ai chạy campaign? Bao nhiêu người?
8. **Pain points**: Đang gặp vấn đề gì với Insider?

Sau đó tạo profile mới theo template:

```
## [Vertical] - [Client Name]

**Đặc thù**: ...
**Modules active**: ...
**KPIs ưu tiên**: ...
**Dimensions phân tích**: ...
**Known issues**: ...
**Cách frame kết quả**: ...
```

Và thông báo cho user: *"Profile mới cho [Client] đã được tạo. Bạn muốn lưu vào `skills/insider-client-profiles/SKILL.md` không?"*

---

## Quick Reference - Client → Vertical Mapping

| Client | Vertical | Key metric |
|--------|----------|------------|
| Viettel (VTT) | Telecom | Conversion volume, CTR |
| Sacombank | Banking | AUM, game engagement |
| TP Bank | Banking | CDP adoption, activation |
| MBS | Securities | First trade, AUM |
| MB Bank | Banking | *(TBD)* |
| VETC | Super App | Transaction volume |
| GHN | Logistics | Delivery completion, feature adoption |
| Ahamove | E-commerce / Logistics | GMV, web push reach |
| Printerval | E-commerce | GMV, email revenue |
| Vinpearl | Hospitality | *(extend as needed)* |
