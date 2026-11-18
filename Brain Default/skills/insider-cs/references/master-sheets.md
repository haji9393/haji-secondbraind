# PHẦN 3 - 2 SHEET TỔNG (Campaign Master + Conversion Master)

Sau khi hoan thanh tat ca Rule Sets, tao 2 sheet tong hop cross-module.
Moi sheet consolidate toan bo campaigns tu moi module da xu ly trong cung file/session.

---

## 3.1 - Sheet "Campaign Master"

Moi row = 1 campaign/variant. Mapping field theo module:

| Cột output | App Push (A) | App Templates (B) | Email (C) | Architect (E) |
|---|---|---|---|---|
| `Campaign Name` | Campaign Name | Campaign Name | Campaign Name | Journey Name |
| `ID` | Variant ID | Variant ID | Campaign ID | Journey ID |
| `Impression` | Delivered | Impressions | Delivered | Delivered |
| `Click` | Opens | Final Click | Total Opens | Total Clicks |
| `CTR` | Click / Impression | Click / Impression | Click / Impression | Click / Impression |
| `Conversion` | Conversion (PG+2G+3G) | PG Conversion | Conversion | Conversions |
| `CR` | Conversion / Impression | Conversion / Impression | Conversion / Impression | Conversion / Impression |
| `Module` | metadata | metadata | "Email" | metadata |
| `Time Range` | metadata | metadata | parse filename | metadata |

```python
def build_campaign_master(processed_modules):
    """
    processed_modules: dict { module_name: df_processed }
    Moi df da co du cac cot goc + cac cot bo sung tu Rule Set tuong ung
    """
    frames = []

    for module_name, df in processed_modules.items():

        if module_name == 'App Push':
            tmp = df[['Campaign Name','Variant ID','Delivered','Opens',
                       'Conversion','Time Range','Module']].copy()
            tmp.columns = ['Campaign Name','ID','Impression','Click',
                           'Conversion','Time Range','Module']

        elif module_name == 'App Templates':
            tmp = df[['Campaign Name','Variant ID','Impressions','Final Click',
                       'PG Conversion','Time Range','Module']].copy()
            tmp.columns = ['Campaign Name','ID','Impression','Click',
                           'Conversion','Time Range','Module']

        elif module_name == 'Email':
            tmp = df[['Campaign Name','Campaign ID','Delivered','Total Opens',
                       'Conversion','Time Range','Module']].copy()
            tmp.columns = ['Campaign Name','ID','Impression','Click',
                           'Conversion','Time Range','Module']

        elif module_name == 'Architect':
            tmp = df[['Journey Name','Journey ID','Delivered','Total Clicks',
                       'Conversions','Time Range','Module']].copy()
            tmp.columns = ['Campaign Name','ID','Impression','Click',
                           'Conversion','Time Range','Module']

        tmp['CTR'] = (tmp['Click'] / tmp['Impression']).replace([np.inf, np.nan], 0).round(4)
        tmp['CR']  = (tmp['Conversion'] / tmp['Impression']).replace([np.inf, np.nan], 0).round(4)
        frames.append(tmp)

    master = pd.concat(frames, ignore_index=True)
    master = master[['Campaign Name','ID','Module','Time Range',
                      'Impression','Click','CTR','Conversion','CR']]
    # 3 cot phan tich - de trong voi dropdown
    master['Funnel / Objectives'] = ''
    master['Products']            = ''
    master['Agents']              = ''
    return master
```

---

## 3.2 - Sheet "Conversion Master"

Moi row = 1 conversion event type. Consolidate tu Conversion Summary Sheet cua tung module.

> Email (Rule Set C) khong co Conversion Summary → khong contribute vao sheet nay.

| Cột output | App Push (A) | App Templates (B) | Architect (E) |
|---|---|---|---|
| `Conversion Name` | Conversion Name | Conversion Name | Conversion Name |
| `No. Campaign` | No. Campaign | No. Campaign | No. Campaign |
| `Impression` | Delivered | Impressions | Delivered |
| `Click` | Opens | Final Click | Total Click |
| `CTR` | Click / Impression | Click / Impression | Click / Impression |
| `Conversion` | Conversion | Value of Conversion | Conversion Value |
| `CR` | Conversion / Impression | Conversion / Impression | CR |

```python
def build_conversion_master(conv_summaries):
    """
    conv_summaries: list of dfs - Conversion Summary tu moi module (A, B, E)
    Email (C) khong co → khong pass vao
    Moi df da co 5 metadata cols
    """
    frames = []

    for df in conv_summaries:
        module = df['Module'].iloc[0]

        if module in ['App Push', 'app_push']:
            tmp = df[['Conversion Name','No. Campaign','Delivered','Opens',
                       'Conversion','Module','Time Range']].copy()
            tmp.columns = ['Conversion Name','No. Campaign','Impression','Click',
                           'Conversion','Module','Time Range']

        elif module in ['Inapp', 'inapp', 'InApp']:
            tmp = df[['Conversion Name','No. Campaign','Impressions','Final Click',
                       'Value of Conversion','Module','Time Range']].copy()
            tmp.columns = ['Conversion Name','No. Campaign','Impression','Click',
                           'Conversion','Module','Time Range']

        elif module in ['Architect', 'architect']:
            tmp = df[['Conversion Name','No. Campaign','Delivered','Total Click',
                       'Conversion Value','Module','Time Range']].copy()
            tmp.columns = ['Conversion Name','No. Campaign','Impression','Click',
                           'Conversion','Module','Time Range']

        tmp['CTR'] = (tmp['Click'] / tmp['Impression']).replace([np.inf, np.nan], 0).round(4)
        tmp['CR']  = (tmp['Conversion'] / tmp['Impression']).replace([np.inf, np.nan], 0).round(4)
        frames.append(tmp)

    master = pd.concat(frames, ignore_index=True)
    master = master[['Conversion Name','Module','Time Range','No. Campaign',
                      'Impression','Click','CTR','Conversion','CR']]
    master['Funnel / Objectives'] = ''
    master['Products']            = ''
    master['Agents']              = ''
    return master
```
