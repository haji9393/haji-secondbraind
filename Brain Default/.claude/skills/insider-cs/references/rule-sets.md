# PHẦN 2 - RULE SET THEO MODULE

---

## RULE SET A - App Push Overall Analytics

**Nhận diện**: Title sheet đầu = `"App Push Overall Analytics"`

**Metadata**:
```python
df_overall = pd.read_excel(filepath, sheet_name='Overall Analytics', header=None)
time_range = df_overall.iloc[2, 1]   # Report Time Interval (row 3, col B)
module     = df_overall.iloc[3, 5]   # Product (row 4, col F)
```

**Sheets xử lý**: `Campaign Metrics` (header=3)

```python
import pandas as pd
import numpy as np

df = pd.read_excel(filepath, sheet_name='Campaign Metrics', header=3)
for col in ['PG Conversion', '2G Conversion', '3G Conversion', 'Delivered', 'Opens']:
    df[col] = pd.to_numeric(df[col].replace('-', 0), errors='coerce').fillna(0)
```

### Output 1 - Campaign Metrics + cột Conversion + 5 metadata cols

```python
df['Conversion'] = df['PG Conversion'] + df['2G Conversion'] + df['3G Conversion']
# Cột Conversion chen vao sau '3G Conversion Rate'
# Sau do: + 5 metadata cols (xem Phan 1.1)
```

> Moi row = 1 Variant. Campaign A/B test co nhieu rows cung Campaign ID.

### Output 2 - Conversion Summary Sheet (pivot theo PG/2G/3G Event)

```python
records = []
for _, row in df.iterrows():
    for goal, event_col, conv_col in [
        ('PG', 'PG Event', 'PG Conversion'),
        ('2G', '2G Event', '2G Conversion'),
        ('3G', '3G Event', '3G Conversion'),
    ]:
        event = str(row[event_col]).strip()
        if event not in ['-', 'nan', '', 'None']:   # Giu lai 'Purchase'
            records.append({
                'Campaign ID': row['Campaign ID'],
                'Event':       event,
                'Delivered':   row['Delivered'],
                'Opens':       row['Opens'],
                'Conversion':  row[conv_col],
            })

long_dedup = pd.DataFrame(records).drop_duplicates(subset=['Campaign ID', 'Event'])
conv = long_dedup.groupby('Event').agg(
    No_Campaign = ('Campaign ID', 'nunique'),
    Delivered   = ('Delivered',   'sum'),
    Opens       = ('Opens',       'sum'),
    Conversion  = ('Conversion',  'sum'),
).reset_index()
conv['Open Rate'] = (conv['Opens'] / conv['Delivered']).replace([np.inf, np.nan], 0).round(4)
conv.columns = ['Conversion Name','No. Campaign','Delivered','Opens','Open Rate','Conversion']
conv = conv[['Conversion Name','No. Campaign','Delivered','Opens','Open Rate','Conversion']]
conv = conv.sort_values('No. Campaign', ascending=False).reset_index(drop=True)
# + 5 metadata cols
```

**Schema Conversion Summary - Rule Set A**:

| Cột | Công thức |
|---|---|
| `Conversion Name` | Pivot từ PG/2G/3G Event |
| `No. Campaign` | `nunique(Campaign ID)` |
| `Delivered` | `sum(Delivered)` deduped per (Campaign ID, Event) |
| `Opens` | `sum(Opens)` deduped |
| `Open Rate` | `Opens / Delivered` |
| `Conversion` | `sum(goal_conv)` deduped |
| + 5 metadata cols | Xem Phần 1.1 |

**Lưu ý**:
- `'-'` replace bang 0 truoc khi tinh toan
- `'Purchase'` trong Event: GIU LAI
- Dedup scope: Delivered/Opens - tranh double-count neu cung event o PG+2G

---

## RULE SET B - App Templates (Template Store Analytics)

**Nhận diện**: Title sheet đầu = `"Template Store Analytics"`

**Metadata**:
```python
df_overall = pd.read_excel(filepath, sheet_name='Overall Analytics', header=None)
time_range = df_overall.iloc[2, 1]
module     = df_overall.iloc[3, 5]
```

**Sheets xử lý**: `Campaign Metrics` (header=2), `Click Metrics of Basic Template` (header=3),
`Click Metrics of Enhanced Temp.` (header=2)

### Output 1 - Campaign Metrics + Final Click + Final CTR + 5 metadata cols

**Logic Final Click theo Variant ID**:

| Variant ID thuộc sheet | Công thức |
|---|---|
| `Click Metrics of Basic Template` | Sum tất cả click cols NGOAI TRU tên chứa `"close button click"` hoặc `"overlay"` |
| `Click Metrics of Enhanced Temp.` | Sum `Clicks` WHERE `Action Type = 'Deep Link'` |

Ưu tiên Enhanced > Basic. Mỗi variant chỉ xuất hiện trong 1 sheet.

```python
df_cm    = pd.read_excel(filepath, sheet_name='Campaign Metrics',                header=2)
df_basic = pd.read_excel(filepath, sheet_name='Click Metrics of Basic Template', header=3)
df_enh   = pd.read_excel(filepath, sheet_name='Click Metrics of Enhanced Temp.', header=2)

for col in ['Impressions', 'Users', 'PG Conversion', 'Overall Revenue']:
    df_cm[col] = pd.to_numeric(df_cm[col].replace('-', 0), errors='coerce').fillna(0)

# Basic map
info_cols    = ['Campaign ID','Campaign Name','Variant ID','Variant Name',
                'Segmentation Name','Start Date','Start Time','End Date',
                'End Time','Bypass Frequency Capping','Re-eligibility Duration','Status']
all_click    = [c for c in df_basic.columns if c not in info_cols]
include_cols = [c for c in all_click
                if not any(p in c.lower() for p in ['close button click', 'overlay'])]
for col in all_click:
    df_basic[col] = pd.to_numeric(df_basic[col].replace('-', 0), errors='coerce').fillna(0)
df_basic['Final Click'] = df_basic[include_cols].sum(axis=1)
basic_map = {str(k): v for k,v in df_basic.set_index('Variant ID')['Final Click'].to_dict().items()}

# Enhanced map
df_enh['Clicks'] = pd.to_numeric(df_enh['Clicks'].replace('-', 0), errors='coerce').fillna(0)
enh_map = {
    str(k): v for k,v in
    df_enh[df_enh['Action Type'] == 'Deep Link']
        .groupby('Variant ID')['Clicks'].sum().to_dict().items()
}

# Map vao Campaign Metrics
df_cm['Variant ID']  = df_cm['Variant ID'].astype(str)
df_cm['Final Click'] = df_cm['Variant ID'].map(lambda v: enh_map.get(v, basic_map.get(v, 0)))
df_cm['Final CTR']   = (df_cm['Final Click'] / df_cm['Impressions']).replace([np.inf, np.nan], 0).round(4)
# + 5 metadata cols
```

### Output 2 - Conversion Summary Sheet (pivot theo PG Event)

```python
records = []
for _, row in df_cm.iterrows():
    event = str(row['PG Event']).strip()
    if event not in ['-', 'nan', '', 'None']:
        records.append({
            'Campaign ID':   row['Campaign ID'],
            'Event':         event,
            'Impressions':   row['Impressions'],
            'Users':         row['Users'],
            'Final Click':   row['Final Click'],
            'PG Conversion': row['PG Conversion'],
        })

long_dedup = pd.DataFrame(records).drop_duplicates(subset=['Campaign ID', 'Event'])
conv = long_dedup.groupby('Event').agg(
    No_Campaign      = ('Campaign ID',   'nunique'),
    Impressions      = ('Impressions',   'sum'),
    Users            = ('Users',         'sum'),
    Final_Click      = ('Final Click',   'sum'),
    Value_Conversion = ('PG Conversion', 'sum'),
).reset_index()
conv['Final CTR'] = (conv['Final_Click'] / conv['Impressions']).replace([np.inf, np.nan], 0).round(4)
conv.columns = ['Conversion Name','No. Campaign','Impressions','Users',
                'Final Click','Value of Conversion','Final CTR']
conv = conv[['Conversion Name','No. Campaign','Impressions','Users',
             'Final Click','Final CTR','Value of Conversion']]
conv = conv.sort_values('No. Campaign', ascending=False).reset_index(drop=True)
# + 5 metadata cols
```

**Lưu ý**:
- `header=2` cho Campaign Metrics, `header=3` cho Basic Template (co sub-header row)
- Enhanced Template: group by Variant ID truoc khi map (nhieu rows per variant)
- `Value of Conversion = 0` la binh thuong neu PG tracking chua cau hinh → ghi caveat

---

## RULE SET C - Email (Campaign Comparison Report)

**Nhận diện**: Filename pattern `campaign-comparison-report-YYYY-MM-DD-till-YYYY-MM-DD-*.xlsx`

**Metadata** - parse từ filename:
```python
import re, os
from datetime import datetime

filename   = os.path.basename(filepath)
match      = re.search(r'(\d{4}-\d{2}-\d{2})-till-(\d{4}-\d{2}-\d{2})', filename)
time_range = (f"{datetime.strptime(match.group(1),'%Y-%m-%d').strftime('%d/%m/%Y')} - "
              f"{datetime.strptime(match.group(2),'%Y-%m-%d').strftime('%d/%m/%Y')}") \
             if match else 'Unknown - kiem tra lai ten file'
module = 'Email'   # hardcode
```

> Neu filename khong match pattern → canh bao user, khong tu suy doan tu data.

**Sheets xử lý**: `Sheet1` (header=0)

```python
df = pd.read_excel(filepath, sheet_name='Sheet1', header=0)
df.columns = df.columns.str.strip()   # xu ly trailing spaces trong ten cot
# + 5 metadata cols
```

Khong tao Conversion Summary sheet - Email khong co PG Event column.

**Lưu ý**:
- Sheet ten la `Sheet1`, khong phai `Campaign Metrics`
- `"Total Opens       "` co trailing spaces → `.str.strip()`
- Percentage cols la string `"x.xx%"` → convert neu can tinh toan
- `Campaign Tag` la dimension phan nhom huu ich (FUND, SSG, Bond...)
- Dung cot `Conversion` + `Conversion Rate` san co de phan tich conversion

---

## RULE SET E - Architect (Architect Overall Analytics Report)

**Nhận diện**: Title sheet `Report` = `"Architect Overall Analytics Report"`

**Metadata**:
```python
df_report  = pd.read_excel(filepath, sheet_name='Report', header=None)
time_range = df_report.iloc[3, 1]   # Row 4, col B - Report Time Interval
module     = df_report.iloc[4, 4]   # Row 5, col E - Product value
```

> Metadata nam trong sheet `Report`, KHONG phai `Overall Analytics` nhu Rule Set A/B.

**Sheets xử lý**: `All Journey Metrics` (header=13), `Goal Metrics` (header=1)

### Output 1 - All Journey Metrics + 5 metadata cols

```python
df_aj = pd.read_excel(filepath, sheet_name='All Journey Metrics', header=13)
# header=13: file co 12 rows metadata/header phu phia tren
# Verify: row 13 phai chua 'Journey ID' lam gia tri dau tien

for col in ['Entered','Dropped','Delivered','Sent','Total Clicks','Conversions']:
    df_aj[col] = pd.to_numeric(df_aj[col], errors='coerce').fillna(0)
# + 5 metadata cols
```

### Output 2 - Goal Metrics Summary Sheet

```python
import re

def clean_goal_name(name):
    return re.sub(r'\s*#\d+$', '', str(name)).strip()
    # VD: 'Login Success #28' → 'Login Success'

df_gm = pd.read_excel(filepath, sheet_name='Goal Metrics', header=1)
df_gm['Conversions'] = pd.to_numeric(df_gm['Conversions'], errors='coerce').fillna(0)
gm_map = dict(zip(df_gm['Goal Name'].apply(clean_goal_name), df_gm['Conversions']))

df_aj_conv = df_aj.dropna(subset=['Conversion name']).copy()
df_aj_conv['Conversion name'] = df_aj_conv['Conversion name'].astype(str).str.strip()

agg = df_aj_conv.groupby('Conversion name').agg(
    No_Campaign = ('Journey ID',   'nunique'),
    Entered     = ('Entered',      'sum'),
    Delivered   = ('Delivered',    'sum'),
    Total_Click = ('Total Clicks', 'sum'),
).reset_index()
agg['Total CTR']        = (agg['Total_Click'] / agg['Delivered']).replace([np.inf, np.nan], 0).round(4)
agg['Conversion Value'] = agg['Conversion name'].map(gm_map).fillna(0)
agg['CR']               = (agg['Conversion Value'] / agg['Delivered']).replace([np.inf, np.nan], 0).round(4)
agg.columns = ['Conversion Name','No. Campaign','Entered','Delivered',
               'Total Click','Total CTR','Conversion Value','CR']
# + 5 metadata cols
```

**Schema Goal Metrics Summary**:

| Cột | Công thức |
|---|---|
| `Conversion Name` | Pivot tu `Conversion name` trong All Journey Metrics (cleaned) |
| `No. Campaign` | `nunique(Journey ID)` |
| `Entered` | `sum(Entered)` |
| `Delivered` | `sum(Delivered)` |
| `Total Click` | `sum(Total Clicks)` |
| `Total CTR` | `Total Click / Delivered` |
| `Conversion Value` | Tu `Conversions` trong Goal Metrics (matched by clean name) |
| `CR` | `Conversion Value / Delivered` |
| + 5 metadata cols | Xem Phần 1.1 |

**Lưu ý**:
- Journey khong co `Conversion name` (NaN) → bo qua trong Goal Metrics Summary
- Journey ID duplicate neu co multi-goal → dung `nunique` khi dem
- Goal Name matching strip `#nn` suffix - neu sau merge = 0 → ghi caveat tracking

---

## RULE SET D - Web Push | RULE SET F - Web Templates

Pending - bo sung khi co file mau.
