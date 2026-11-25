> Gộp từ skill cũ `insider-data-cleanup` ngày 2026-11-18. Mô tả gốc: Làm sạch file export thô của Insider (.xlsx) thành bảng sẵn sàng phân tích: biến đổi theo loại report, thêm cột Conversion, pivot theo event.


# Insider Data Cleanup Skill

## Khi nào dùng

Use this skill whenever the user uploads a raw Insider export file and wants to clean, transform, or summarize it into analysis-ready tables. Triggers include: "clean up data", "tổng hợp file Insider", "làm bảng từ file export", "tạo file tổng hợp", "bổ sung cột Conversion", "pivot theo event", or any request to process a raw Insider Analytics export (.xlsx) before reporting. Always use this skill BEFORE doing analysis on raw Insider exports - it defines which transformations apply to which report type. Pair with insider-monthly-report skill for full reporting.

## Mục đích

Chuẩn hoá và biến đổi file raw export từ Insider thành các bảng sạch, sẵn sàng
để phân tích và đưa vào report. Skill này xác định **report type → transformation rules**.

---

## BƯỚC 0 - Nhận diện Report Type

Đọc title của sheet đầu tiên (hoặc sheet `Report`) để xác định loại report.

| Title trong file | Report Type | Rule Set |
|---|---|---|
| `App Push Overall Analytics` | App Push | **RULE SET A** |
| `Template Store Analytics` | App Templates | **RULE SET B** |
| `campaign-comparison-report-*` (filename) | Email | **RULE SET C** |
| `Web Push Analytics` | Web Push | 🔲 RULE SET D - Pending |
| `Architect Overall Analytics Report` | Architect | **RULE SET E** |
| Web Templates | Web Templates | 🔲 RULE SET F - Pending |

> **Nếu không nhận ra report type → hỏi user trước khi tiếp tục.**

---

# PHẦN 1 - QUY TẮC CHUNG (Áp dụng cho TẤT CẢ report type)

---

## 1.1 - 5 Metadata Columns (Bắt buộc trên MỌI sheet output)

Mọi sheet consolidate / sheet mới được tạo ra đều phải có đủ 5 cột này ở **cuối bảng**,
sau tất cả các cột dữ liệu khác. Không có ngoại lệ.

| STT | Tên cột | Loại | Nguồn giá trị |
|---|---|---|---|
| 1 | `Time Range` | String - auto-fill | Quy định riêng trong từng Rule Set |
| 2 | `Module` | String - auto-fill | Quy định riêng trong từng Rule Set |
| 3 | `Funnel / Objectives` | Trống - user điền | Dropdown từ `Config!A` |
| 4 | `Products` | Trống - user điền | Dropdown từ `Config!C` |
| 5 | `Agents` | Trống - user điền | Dropdown từ `Config!E` |

```python
# Template áp dụng cho mọi sheet output sau khi xử lý xong
df['Time Range']          = time_range   # lấy từ logic của từng Rule Set
df['Module']              = module       # lấy từ logic của từng Rule Set
df['Funnel / Objectives'] = ''
df['Products']            = ''
df['Agents']              = ''
```

---

## 1.2 - Google Sheets Export & Config Sheet

Mọi output đều export dạng **Google Sheet** với sheet `Config` đi kèm.

> **Trong Javis:** chỉ xuất Google Sheet khi trang Kết nối đã có Google Sheets hoặc máy có sẵn Google credentials cho gspread. Không có thì dùng Fallback `.xlsx` bên dưới và lưu file vào `exports/insider/` trong vault. File raw đầu vào là file user đính kèm trong chat (đường dẫn nằm trong tin nhắn).

### Cấu trúc sheet Config

```
Cột A: Funnel_List (header row 1)
  A2: Acquisition
  A3: Onboarding
  A4: Engagement
  A5: Retention
  A6: Upsell
  A7: Reactivation
  A8+: [để trống - user thêm custom values]

Cột C: Products_List (header row 1)
  C2+: [để trống - user điền]

Cột E: Agents_List (header row 1)
  E2+: [để trống - user điền]
```

### Data Validation (gspread)

```python
import gspread
from gspread_formatting import DataValidationRule, BooleanCondition
from gspread_formatting import set_data_validation_for_cell_range

funnel_rule   = DataValidationRule(BooleanCondition('ONE_OF_RANGE', ["'Config'!$A$2:$A$20"]), showCustomUi=True)
products_rule = DataValidationRule(BooleanCondition('ONE_OF_RANGE', ["'Config'!$C$2:$C$50"]), showCustomUi=True)
agents_rule   = DataValidationRule(BooleanCondition('ONE_OF_RANGE', ["'Config'!$E$2:$E$50"]), showCustomUi=True)

def apply_dropdowns(ws, df, n_rows):
    for col_name, rule in [
        ('Funnel / Objectives', funnel_rule),
        ('Products',            products_rule),
        ('Agents',              agents_rule),
    ]:
        col_letter = col_to_letter(df.columns.get_loc(col_name) + 1)
        set_data_validation_for_cell_range(ws, f"{col_letter}2:{col_letter}{n_rows}", rule)
```

### Fallback (không có Google credentials)

Export `.xlsx` và ghi hướng dẫn:
```
Data > Data validation > Criteria: Dropdown from a range
  Funnel/Objectives : Config!A2:A20
  Products          : Config!C2:C50
  Agents            : Config!E2:E50
```

### Hướng dẫn user sau khi nhận file

```
File da san sang. De dung dropdown:
1. Mo sheet "Config"
2. Dien Products vao cot C (tu C2 tro xuong)
3. Dien Agents vao cot E (tu E2 tro xuong)
4. Quay lai sheet data - dropdown tu dong cap nhat
Funnel/Objectives da co list chuan (A2:A7). Them custom tu A8 tro xuong.
```

---

## 1.3 - Quy trình thực hiện tổng quát

```
BUOC 0: Nhan dien report type
BUOC 1: Doc metadata (Time Range, Module) theo rule cua tung module
BUOC 2: Ap dung Rule Set tuong ung - xu ly tung sheet
BUOC 3: Them 5 metadata columns vao cuoi moi sheet output
BUOC 4: Build PHAN 3 - 2 sheet tong (Campaign Master + Conversion Master)
BUOC 5: Tao sheet Config voi dropdown values
BUOC 6: Preview ket qua - confirm voi user - export Google Sheet
```

---

# PHẦN 2 - RULE SET THEO MODULE

Chi tiết từng Rule Set (cấu trúc file, cột, code pandas) nằm ở [references/rule-sets.md](skills/insider-cs/references/rule-sets.md). BẮT BUỘC đọc file đó trước khi xử lý bất kỳ module nào; không tự suy ra rule.

- RULE SET A - App Push Overall Analytics
- RULE SET B - App Templates (Template Store Analytics)
- RULE SET C - Email (Campaign Comparison Report)
- RULE SET E - Architect (Architect Overall Analytics Report)
- RULE SET D (Web Push), F (Web Templates): pending

---

# PHẦN 3 - 2 SHEET TỔNG (Campaign Master + Conversion Master)

Sau khi xong mọi Rule Set, dựng 2 sheet tổng cross-module theo [references/master-sheets.md](skills/insider-cs/references/master-sheets.md) (BẮT BUỘC đọc trước khi dựng).

---

# CONFIRMATION TEMPLATE (trước khi export)

```
Đã xử lý xong. Tóm tắt kết quả:

METADATA
  Time Range : [value]
  Module     : [value]

PHAN 2 - MODULE OUTPUTS

[RULE SET A - App Push]
  Campaign Metrics  : [N] rows | Conversion tong: [X]
  Conversion Summary: [N] event types | Top: [name] ([N] campaigns)

[RULE SET B - App Templates]
  Campaign Metrics  : [N] rows | Basic variants: [N] | Enhanced: [N]
  Conversion Summary: [N] event types
  ⚠️ Value of Conversion = 0 cho [event X]? → caveat tracking

[RULE SET C - Email]
  Sheet1            : [N] campaigns | Time Range tu filename: [value] OK/⚠️
  (Khong co Conversion Summary)

[RULE SET E - Architect]
  All Journey Metrics : [N] rows | Co goal: [N] | Khong co goal: [N]
  Goal Metrics Summary: [N] conversion types

PHAN 3 - MASTER SHEETS
  Campaign Master   : [N] rows tong (tu [N] modules)
  Conversion Master : [N] rows tong (tu [N] modules, excl. Email)

OUTPUT FORMAT
  □ Google Sheet - co sheet Config + dropdown validation  ← mac dinh
  □ .xlsx - khong co dropdown
  □ Ca hai
```

---

# ROADMAP

| Rule Set | Report Type | Status |
|---|---|---|
| **A** | App Push Overall Analytics | ✅ Defined |
| **B** | App Templates (Template Store Analytics) | ✅ Defined |
| **C** | Email (Campaign Comparison Report) | ✅ Defined |
| D | Web Push | 🔲 Pending - can file mau |
| **E** | Architect (Architect Overall Analytics Report) | ✅ Defined |
| F | Web Templates | 🔲 Pending - can file mau |
