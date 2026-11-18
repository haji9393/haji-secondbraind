# Dung slide HTML Ruby Bai Kem ban 4.3 (Javis, 18/11/2026). Chay: python3 build_slide.py
# So lieu lay tu mo-hinh/run6.py + run7.py (phan Chu nha 75%, ty dong).
import os, html
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ruby-bai-kem-slide-ban-4.html')

C = dict(PA1='#B5A994', PA2='#8FA37E', PA3='#3E5A47', PA4='#C0673E', ink='#2B2A27', mute='#7A7368',
         line='#D9D0C1', bg='#F3EDE3', card='#FBF8F2', gold='#C79A3A', red='#B4452F')
PLANS = ['PA1', 'PA2', 'PA3', 'PA4']

def vn(x, d=1):
    s = f"{x:,.{d}f}" if d else f"{x:,.0f}"
    return s.replace(',', 'X').replace('.', ',').replace('X', '.')

# ---------- so lieu (ban 4.3, PA2 thue 300 tr) ----------
TOT = dict(PA1=57.1, PA2=52.7, PA3=62.5, PA4=54.2)
CASH = dict(PA1=57.1, PA2=35.4, PA3=45.2, PA4=36.9)   # tien mat cuoi ky da tru chi phi cuoi ky
UP = dict(PA1=0, PA2=17.3, PA3=17.3, PA4=17.3)
XAU = dict(PA1=55.0, PA2=33.0, PA3=34.5, PA4=24.1)
BANK = 45.0
YRS = dict(PA1=[236, 255, 276, 299, 262, 344, 372, 401, 432, 466],
           PA2=[117, 239, 264, 290, 193, 340, 373, 407, 445, 485],
           PA3=[177, 260, 283, 306, 332, 359, 388, 419, 451, 486],
           PA4=[92, 192, 242, 260, 279, 299, 319, 341, 364, 387])
MONTHS = ['T11', 'T12', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10']
Y1 = dict(PA3=[166, 311, 313, 278, 316, 173, 53, 48, 181, 182, 51, 56],
          PA4=[87, 232, 233, 205, 236, 92, -43, -48, 101, 102, -47, -43])
SCEN = [('Cơ sở · 59%', [57.1, 52.7, 62.5, 54.2]), ('Đầu trên · 65%', [57.1, 52.7, 67.9, 60.0]),
        ('ADR 900k', [57.1, 52.7, 70.9, 63.9]), ('ADR 600k', [57.1, 52.7, 49.5, 40.9]),
        ('Đầu dưới · 52%', [55.0, 33.0, 41.7, 32.2]), ('Xấu · 44%', [55.0, 33.0, 34.5, 24.1])]

# ---------- SVG helpers ----------
W = 357
def svg(h, body, w=W):
    return f'<svg viewBox="0 0 {w} {h}" width="100%" role="img" xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif">{body}</svg>'
def t(x, y, s, size=11, fill=None, anchor='start', weight=400):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill or C["ink"]}" text-anchor="{anchor}" font-weight="{weight}">{html.escape(str(s))}</text>'

def hbars(groups, vmax=75, bank=None, hi='PA3'):
    """groups: list of (label, values[4])"""
    rows = sum(len(PLANS) for _ in groups); rh = 19; gap = 26
    h = len(groups) * (gap + len(PLANS) * rh) + 14
    x0 = 40; x1 = W - 34; sc = (x1 - x0) / vmax; b = ''; y = 0
    for lab, vals in groups:
        b += t(0, y + 14, lab.upper(), 9.5, C['mute'], weight=700); y += gap - 4
        for p, v in zip(PLANS, vals):
            col = C[p] if p in (hi, 'PA4') or hi == 'all' else C[p]
            b += t(0, y + 13, p, 11, weight=700)
            b += f'<rect x="{x0}" y="{y+3}" width="{max(1,v*sc):.1f}" height="13" rx="3" fill="{col}"/>'
            b += t(x0 + v * sc + 5, y + 14, vn(v), 11, weight=700)
            y += rh
    if bank:
        bx = x0 + bank * sc
        b += f'<line x1="{bx:.1f}" y1="18" x2="{bx:.1f}" y2="{y}" stroke="{C["ink"]}" stroke-dasharray="3 3" stroke-width="1.2"/>'
        b += t(bx, y + 11, f'Gửi ngân hàng {vn(bank,0)}', 9.5, C['ink'], 'middle', 700)
        y += 14
    return svg(y + 2, b)

def stack_value():
    data = [('PA1', CASH['PA1'], 0), ('PA3', CASH['PA3'], UP['PA3']), ('PA4', CASH['PA4'], UP['PA4'])]
    h = 200; base = 170; x = 30; bw = 70; sc = 140 / 65; b = ''
    b += f'<line x1="0" y1="{base}" x2="{W}" y2="{base}" stroke="{C["line"]}"/>'
    by = base - BANK * sc
    b += f'<line x1="0" y1="{by:.1f}" x2="{W}" y2="{by:.1f}" stroke="{C["ink"]}" stroke-dasharray="3 3"/>' + t(W, by - 4, 'ngân hàng 45', 9.5, C['ink'], 'end', 700)
    b += '<defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="#EBD9C8"/><line x1="0" y1="0" x2="0" y2="6" stroke="#C0673E" stroke-width="2"/></pattern></defs>'
    for i, (p, cash, up) in enumerate(data):
        xx = x + i * 110; hc = cash * sc; hu = up * sc
        b += f'<rect x="{xx}" y="{base-hc:.1f}" width="{bw}" height="{hc:.1f}" fill="{C[p]}" rx="2"/>'
        if up:
            b += f'<rect x="{xx}" y="{base-hc-hu:.1f}" width="{bw}" height="{hu:.1f}" fill="url(#hatch)" rx="2"/>'
            b += t(xx + bw / 2, base - hc - hu / 2 + 4, '+' + vn(up), 10.5, C['PA4'], 'middle', 700)
        b += t(xx + bw / 2, base - hc + 16, vn(cash), 11, '#fff', 'middle', 700)
        b += t(xx + bw / 2, base - hc - hu - 6, vn(cash + up), 13, C['ink'], 'middle', 800)
        b += t(xx + bw / 2, base + 15, p, 11, C['ink'], 'middle', 700)
    return svg(h + 8, b)

def lines(series, labels, ymin=-100, ymax=500, h=210, keys=PLANS, zero=True, step=100):
    x0, x1, y0, y1 = 34, W - 30, 10, h - 26
    n = len(labels); sx = lambda i: x0 + (x1 - x0) * i / (n - 1); sy = lambda v: y1 - (v - ymin) / (ymax - ymin) * (y1 - y0)
    b = ''
    v = ymin
    while v <= ymax:
        b += f'<line x1="{x0}" y1="{sy(v):.1f}" x2="{x1}" y2="{sy(v):.1f}" stroke="{C["line"] if v else C["ink"]}" stroke-width="{0.6 if v else 1}"/>' + t(x0 - 5, sy(v) + 3.5, vn(v, 0), 9, C['mute'], 'end')
        v += step
    for i, l in enumerate(labels):
        if n <= 12: b += t(sx(i), h - 10, l, 9, C['mute'], 'middle')
    used = []
    for k in keys:
        ly = sy(series[k][-1]) + 4
        while any(abs(ly - u) < 11 for u in used): ly += 11
        used.append(ly)
        pts = ' '.join(f'{sx(i):.1f},{sy(v):.1f}' for i, v in enumerate(series[k]))
        wdt = 2.6 if k in ('PA3', 'PA4') else 1.6
        b += f'<polyline points="{pts}" fill="none" stroke="{C[k]}" stroke-width="{wdt}" stroke-linejoin="round"/>'
        b += t(sx(n - 1) + 4, ly, k, 9.5, C[k], 'start', 800)
    return svg(h, b)

def month_bars(a, bser, h=200, ymin=-100, ymax=350):
    x0, x1, y0, y1 = 32, W - 4, 8, h - 24
    n = 12; cw = (x1 - x0) / n; sy = lambda v: y1 - (v - ymin) / (ymax - ymin) * (y1 - y0)
    b = ''
    for v in range(ymin, ymax + 1, 100):
        b += f'<line x1="{x0}" y1="{sy(v):.1f}" x2="{x1}" y2="{sy(v):.1f}" stroke="{C["ink"] if v==0 else C["line"]}" stroke-width="{1 if v==0 else .6}"/>' + t(x0 - 5, sy(v) + 3.5, vn(v, 0), 9, C['mute'], 'end')
    for i in range(n):
        for j, (k, s) in enumerate((('PA3', a), ('PA4', bser))):
            v = s[i]; x = x0 + i * cw + 3 + j * (cw - 6) / 2; w = (cw - 6) / 2 - 1
            top, bot = (sy(v), sy(0)) if v >= 0 else (sy(0), sy(v))
            b += f'<rect x="{x:.1f}" y="{top:.1f}" width="{w:.1f}" height="{bot-top:.1f}" fill="{C[k] if v>=0 else C["red"]}"/>'
        b += t(x0 + i * cw + cw / 2, h - 9, MONTHS[i], 8.5, C['mute'], 'middle')
    return svg(h, b)

def waterfall():
    steps = [('PA3', 62.5, 'tot'), ('Back office tự dựng', -4.2, 'd'), ('Năm đầu chậm, học việc', -2.0, 'd'),
             ('Thưởng GĐ 20%', -2.1, 'd'), ('PA4', 54.2, 'tot')]
    h = 230; y1 = 190; vmin = 45; vmax = 65; sy = lambda v: y1 - (v - vmin) / (vmax - vmin) * 165
    n = len(steps); cw = W / n; b = ''; run = 0
    b += f'<line x1="0" y1="{y1}" x2="{W}" y2="{y1}" stroke="{C["line"]}"/>' + t(2, y1 - 4, 'trục bắt đầu từ 45', 8.5, C['mute'])
    for i, (lab, v, kind) in enumerate(steps):
        x = i * cw + 10; w = cw - 20
        if kind == 'tot':
            top = sy(v); b += f'<rect x="{x:.1f}" y="{top:.1f}" width="{w:.1f}" height="{y1-top:.1f}" fill="{C[lab]}" rx="2"/>'
            b += t(x + w / 2, top - 6, vn(v), 13, C['ink'], 'middle', 800); run = v
        else:
            a, c = sy(run), sy(run + v); b += f'<rect x="{x:.1f}" y="{a:.1f}" width="{w:.1f}" height="{c-a:.1f}" fill="{C["red"]}" opacity=".85" rx="2"/>'
            b += t(x + w / 2, c + 14, vn(v), 11.5, C['red'], 'middle', 800)
            b += f'<line x1="{x-20+w:.1f}" y1="{a:.1f}" x2="{x:.1f}" y2="{a:.1f}" stroke="{C["mute"]}" stroke-dasharray="2 2"/>'
            run += v
        for k, part in enumerate(wrap(lab, 11)):
            b += t(x + w / 2, y1 + 14 + k * 11, part, 9, C['ink'], 'middle', 600)
    return svg(h + 10, b)

def wrap(s, n):
    out, cur = [], ''
    for w in s.split():
        if len(cur) + len(w) + 1 > n and cur: out.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    return out + [cur]

def pl_stack():
    # 100% khoi, trieu/thang, nam van hanh 3
    rows = [('PA3', [('Chi phí tại khách sạn', 318, '#B5A994'), ('Back office', 97, C['gold']), ('Thưởng vận hành', 13, C['PA4']), ('Quỹ thay mới 3%', 24, C['line']), ('Lãi trước thuế', 357, C['PA3'])]),
            ('PA4', [('Chi phí tại khách sạn', 318, '#B5A994'), ('Back office', 133, C['gold']), ('Thưởng vận hành', 23, C['PA4']), ('Quỹ thay mới 3%', 24, C['line']), ('Lãi trước thuế', 311, C['PA3'])])]
    x0 = 36; sc = (W - x0 - 4) / 810; b = ''; y = 6
    for p, parts in rows:
        b += t(0, y + 22, p, 12, weight=800); x = x0
        for lab, v, col in parts:
            b += f'<rect x="{x:.1f}" y="{y+8}" width="{v*sc:.1f}" height="22" fill="{col}"/>'
            if v * sc > 22: b += t(x + v * sc / 2, y + 23, vn(v, 0), 10, '#fff' if col in (C['PA3'], C['PA4'], C['gold']) else C['ink'], 'middle', 700)
            x += v * sc
        y += 40
    lx = 0; ly = y + 6
    for lab, v, col in rows[0][1]:
        wdt = 12 + len(lab) * 5.2
        if lx + wdt > W: lx = 0; ly += 15
        b += f'<rect x="{lx}" y="{ly-8}" width="9" height="9" fill="{col}"/>' + t(lx + 12, ly, lab, 9.5, C['ink']); lx += wdt + 8
    return svg(ly + 6, b)

def breakeven():
    h = 210; x0, x1, y0, y1 = 36, W - 8, 10, h - 30
    rmin, rmax, cmin, cmax = 400, 1300, 0, 170
    sx = lambda r: x0 + (r - rmin) / (rmax - rmin) * (x1 - x0); sy = lambda c: y1 - (c - cmin) / (cmax - cmin) * (y1 - y0)
    b = ''
    for c in range(0, 171, 50):
        b += f'<line x1="{x0}" y1="{sy(c):.1f}" x2="{x1}" y2="{sy(c):.1f}" stroke="{C["line"]}" stroke-width=".6"/>' + t(x0 - 5, sy(c) + 3.5, c, 9, C['mute'], 'end')
    for r in range(400, 1301, 300):
        b += t(sx(r), h - 14, vn(r, 0), 9, C['mute'], 'middle')
    b += t((x0 + x1) / 2, h - 2, 'Doanh thu thuần, triệu/tháng', 9, C['mute'], 'middle')
    b += f'<rect x="{sx(748):.1f}" y="{y0}" width="{sx(817)-sx(748):.1f}" height="{y1-y0}" fill="{C["PA2"]}" opacity=".18"/>'
    b += t(sx(782), y0 + 10, 'Ruby', 9.5, C['PA3'], 'middle', 800)
    b += f'<line x1="{sx(rmin):.1f}" y1="{sy(.12*rmin):.1f}" x2="{sx(rmax):.1f}" y2="{sy(.12*rmax):.1f}" stroke="{C["PA3"]}" stroke-width="2.6"/>'
    b += f'<line x1="{sx(rmin):.1f}" y1="{sy(95+.03*rmin):.1f}" x2="{sx(rmax):.1f}" y2="{sy(95+.03*rmax):.1f}" stroke="{C["PA4"]}" stroke-width="2.6"/>'
    b += t(sx(rmax) - 2, sy(.12 * rmax) - 6, 'PA3: 12%', 10, C['PA3'], 'end', 800)
    b += t(sx(rmin) + 2, sy(95 + .03 * rmin) - 6, 'PA4: 95 tr + 3%', 10, C['PA4'], 'start', 800)
    bx = sx(1056)
    b += f'<circle cx="{bx:.1f}" cy="{sy(126.7):.1f}" r="4" fill="{C["ink"]}"/>' + t(bx + 6, sy(126.7) + 14, 'hoà ở ~1,06 tỷ', 9.5, C['ink'], 'start', 700)
    return svg(h, b)

def thresholds():
    rows = [('PA3', 41.1, 49.0, 53.6), ('PA4', 50.2, 57.7, 62.0)]
    h = 150; x0, x1 = 40, W - 10; vmin, vmax = 35, 70; sx = lambda v: x0 + (v - vmin) / (vmax - vmin) * (x1 - x0); b = ''
    for v in range(35, 71, 5):
        b += f'<line x1="{sx(v):.1f}" y1="14" x2="{sx(v):.1f}" y2="96" stroke="{C["line"]}" stroke-width=".6"/>' + t(sx(v), 110, f'{v}%', 9, C['mute'], 'middle')
    b += f'<line x1="{sx(59.2):.1f}" y1="8" x2="{sx(59.2):.1f}" y2="100" stroke="{C["ink"]}" stroke-width="1.4" stroke-dasharray="4 3"/>' + t(sx(59.2), 8, 'kế hoạch 59%', 9.5, C['ink'], 'middle', 800)
    marks = [('NH', '#7A7368'), ('PA2', C['PA2']), ('PA1', C['PA1'])]
    for i, (p, a, bb, c) in enumerate(rows):
        y = 40 + i * 38
        b += t(0, y + 4, p, 12, C[p], weight=800)
        b += f'<line x1="{sx(a):.1f}" y1="{y}" x2="{sx(c):.1f}" y2="{y}" stroke="{C[p]}" stroke-width="3"/>'
        for (lab, col), v in zip(marks, (a, bb, c)):
            b += f'<circle cx="{sx(v):.1f}" cy="{y}" r="6" fill="{col}" stroke="#fff" stroke-width="1.5"/>' + t(sx(v), y - 10, vn(v, 0), 9.5, C['ink'], 'middle', 700)
    lx = 0
    for lab, col in [('hoà gửi ngân hàng', '#7A7368'), ('hoà PA2', C['PA2']), ('hoà PA1', C['PA1'])]:
        b += f'<circle cx="{lx+5}" cy="{132}" r="5" fill="{col}"/>' + t(lx + 14, 136, lab, 9.5); lx += 14 + len(lab) * 5.4 + 14
    return svg(h, b)

def tornado():
    rows = [('Không tính giá trị nhà', -17.3, 0), ('Công suất ±10%', -5.8, 5.8), ('Giá phòng (ADR) ±10%', -5.8, 5.8),
            ('Chi phí tại khách sạn +10%', -3.5, 0), ('Khai trương trễ 3 tháng', -1.8, 0), ('Vốn xây 28 tỷ', -1.3, 0)]
    h = len(rows) * 30 + 20; xm = 210; sc = 6.8; b = ''
    b += f'<line x1="{xm}" y1="0" x2="{xm}" y2="{h-14}" stroke="{C["ink"]}"/>'
    for i, (lab, lo, hi) in enumerate(rows):
        y = i * 30 + 6
        b += t(0, y + 14, lab, 10, C['ink'], weight=600)
        lw = min(-lo * sc, xm - 150)
        b += f'<rect x="{xm-lw:.1f}" y="{y+4}" width="{lw:.1f}" height="16" fill="{C["red"]}" opacity=".85"/>'
        b += t(xm - lw - 3 if lw < 55 else xm - lw + 3, y + 16, vn(lo), 9.5, C['red'] if lw < 55 else '#fff', 'end' if lw < 55 else 'start', 800)
        if hi:
            b += f'<rect x="{xm}" y="{y+4}" width="{hi*sc:.1f}" height="16" fill="{C["PA3"]}"/>' + t(xm + hi * sc + 3, y + 16, '+' + vn(hi), 9.5, C['PA3'], 'start', 800)
    b += t(xm, h - 2, 'tỷ đồng, so với cơ sở (giống nhau ở PA3 và PA4)', 9, C['mute'], 'middle')
    return svg(h, b)

def cover_art():
    b = '<path d="M40 330 V150 A138 138 0 0 1 316 150 V330 Z" fill="#FBF8F2" stroke="#E2D8C8"/>'
    b += '<line x1="178" y1="20" x2="178" y2="70" stroke="#2B2A27" stroke-width="1.5"/><circle cx="178" cy="80" r="12" fill="#C79A3A"/>'
    for i in range(3):
        x = 70 + i * 60
        b += f'<rect x="{x}" y="120" width="60" height="185" fill="#EADFCB" stroke="#B88D5C"/>'
        for r in range(3):
            for c in range(2):
                b += f'<rect x="{x+12+c*22}" y="{135+r*38}" width="13" height="24" rx="6.5" fill="#3E5A47"/>'
        b += f'<rect x="{x}" y="250" width="60" height="7" fill="#B4452F"/><rect x="{x+22}" y="272" width="16" height="33" rx="8" fill="#2B2A27"/>'
    b += '<rect x="250" y="120" width="58" height="185" fill="none" stroke="#2B2A27" stroke-dasharray="4 4"/>'
    b += t(279, 200, 'R207', 13, weight=800, anchor='middle') + t(279, 216, 'cơ hội', 9.5, C['mute'], 'middle')
    b += '<line x1="20" y1="305" x2="336" y2="305" stroke="#2B2A27" stroke-width="1.5"/><path d="M52 305 v-14 h14 v14z" fill="#B88D5C"/><ellipse cx="59" cy="280" rx="6" ry="14" fill="#8FA37E"/>'
    return svg(335, b)

# ---------- slide helpers ----------
SLIDES = []
SEC = dict(TT='NHẬN ĐỊNH THỊ TRƯỜNG', A='A · ĐẦU TƯ', B='B · VẬN HÀNH', E='E · PA3 HAY PA4', C='C · THI CÔNG', D='D · KIỂM SOÁT')
def slide(sec, title, body, nxt=None, dots=True):
    SLIDES.append((sec, title, body, nxt, dots))
def p(s): return f'<p>{s}</p>'
def lead(s): return f'<p class="lead">{s}</p>'
def concl(s): return f'<div class="concl"><b>=&gt;</b> {s}</div>'
def note(s): return f'<p class="note">{s}</p>'
def big(n, s, col='PA4'): return f'<div class="big"><span style="color:{C[col]}">{n}</span><p>{s}</p></div>'
def pm(plus, minus, fix=None):
    o = '<div class="pm"><div class="plus"><h4>+ ĐƯỢC</h4>' + ''.join(f'<p>{x}</p>' for x in plus) + '</div>'
    o += '<div class="minus"><h4>− MẤT</h4>' + ''.join(f'<p>{x}</p>' for x in minus) + '</div></div>'
    if fix: o += f'<div class="fix"><h4>› {fix[0]}</h4><p>{fix[1]}</p></div>'
    return o
def cards(items):
    return '<div class="cards">' + ''.join(f'<div class="cardi"><span class="tag">{a}</span><h4>{b}</h4><p>{c}</p></div>' for a, b, c in items) + '</div>'
def table(head, rows, hl=None):
    o = '<table><thead><tr>' + ''.join(f'<th>{h}</th>' for h in head) + '</tr></thead><tbody>'
    for r in rows:
        o += '<tr>' + ''.join(f'<td class="{"hl" if hl is not None and i==hl else ""}">{c}</td>' for i, c in enumerate(r)) + '</tr>'
    return o + '</tbody></table>'
def legend(keys=PLANS):
    return '<div class="legend">' + ''.join(f'<span><i style="background:{C[k]}"></i>{k}</span>' for k in keys) + '</div>'
def H(s): return s  # tieu de co the chua <em>

# ================= NOI DUNG =================
slide(None, '03 căn nhà ở Bãi Kem nên làm gì trong <em>10 năm tới</em>?',
      cover_art() + lead('Tài liệu tư vấn gửi Chủ nhà về R201, R203, R205 và cơ hội ghép thêm căn R207. Bản 4: mô hình tính theo từng tháng, mỗi phương án một cấu trúc riêng.')
      + '<p class="meta">Ruby Bãi Kem Boutique · Phú Quốc · 18/11/2026</p>', dots=False)

slide('TÓM TẮT MỘT TRANG', 'Đề xuất: xây khối 53 phòng <em>có điều kiện</em>, rồi chọn giữa thuê quản lý và tự vận hành bằng số thật',
      p('Các trang sau giải thích lần lượt từng ý, theo thứ tự một dự án sẽ trải qua.')
      + cards([('TT', 'Thị trường', 'Dài hạn thuận lợi nhờ hạ tầng mới. 2027-2029 cạnh tranh mạnh vì nhiều phòng mới ra cùng lúc.'),
               ('A', 'Có nên xây?', 'Chỉ khi giá trị căn nhà sau hoàn thiện được thẩm định. Nếu chỉ đếm tiền mặt, để thô cho thuê vẫn nhỉnh hơn.'),
               ('B', 'Ai vận hành?', 'Thuê đơn vị quản lý (PA3) thu về nhiều nhất, 62,5 tỷ. Tự vận hành (PA4) ít hơn khoảng 8 tỷ, đổi lại gia đình sở hữu doanh nghiệp.'),
               ('E', 'PA3 hay PA4?', 'Khoảng cách 8 tỷ đến từ cấu trúc chi phí, không phải may rủi. PA4 đáng chọn khi có toà thứ 2 hoặc giá phòng bám 900 nghìn.'),
               ('C', 'Xây thế nào?', 'Vốn cơ sở 27 tỷ, trần 28 tỷ. Chỉ khởi công khi đủ 04 điều kiện. R207 là tùy chọn.'),
               ('D', 'Giữ quyền ra sao?', 'Tiền, kênh bán, quyền quyết định và đường lui do Chủ nhà nắm, dù chọn PA3 hay PA4.')])
      + concl('Hôm nay chỉ cần duyệt tối đa 0,84 tỷ chi phí hồ sơ. Đầu tháng 3/2027 quyết định xây hay dừng, và PA3 hay PA4, khi đã có báo giá thật.'),
      'Nhận định thị trường Nam Phú Quốc.', dots=False)

slide('TT', 'Nam Phú Quốc có nền tảng dài hạn tốt, nhưng <em>2027-2029</em> sẽ là giai đoạn cạnh tranh mạnh',
      p('Tóm tắt từ báo cáo thị trường Nam Phú Quốc 2027-2042, có đối chiếu với số liệu đã công bố.')
      + cards([('DÀI HẠN', 'Từ khoảng 2030', 'Nhà ga sân bay mới, tàu điện và trung tâm hội nghị cùng đi vào hoạt động. Báo cáo ước công suất toàn thị trường có thể đạt 70-75% vào năm 2030.'),
               ('NGẮN HẠN', '2027-2029', 'Nhiều khách sạn lớn khai trương quanh APEC. Giá phòng và công suất của cơ sở nhỏ nhiều khả năng bị ép trong 2-3 năm.')])
      + p('Hai nhận định này không mâu thuẫn, chỉ khác khung thời gian. Câu hỏi chính là giữ được tài sản và dòng tiền qua 2027-2029 hay không.')
      + concl('Giá trị lớn nhất của chu kỳ đến từ tài sản tăng giá nhờ hạ tầng. Lợi nhuận vận hành rõ nét hơn từ khoảng 2030.')
      + note('Nguồn: Báo cáo thị trường Nam Phú Quốc 2027-2042 (11/2026); số khách 10 tháng đối chiếu với Bộ VHTTDL.'),
      'Cầu và cung hiện nay.')

slide('TT', 'Khách đến tăng đều, nhưng phòng mới tăng nhanh hơn nên <em>công suất bình quân còn thấp</em>',
      '<div class="stats">'
      + ''.join(f'<div><b>{a}</b><span>{b}</span><i>{c}</i></div>' for a, b, c in [
          ('9,25 tr', 'lượt khách 10 tháng đầu 2026, tăng 30%. Khách quốc tế tăng gần 60%.', 'số công bố'),
          ('+71%', 'lượt tìm kiếm Phú Quốc từ Hàn Quốc. Sân bay đã vượt công suất thiết kế 4 triệu khách/năm.', 'báo cáo'),
          ('~30%', 'công suất phòng bình quân toàn đảo 8 tháng đầu 2026. Cao điểm đầu năm báo chí ghi trên 90%.', 'báo cáo, chưa đối chiếu'),
          ('10.000', 'phòng mới hoàn thành năm 2027, trong đó hơn 10 khách sạn 5-6 sao mở trước APEC.', 'báo cáo, báo chí'),
          ('64%', 'là phần chủ nhà thực nhận trên giá bán OTA, sau hoa hồng, thuế và khuyến mãi.', 'báo cáo')]) + '</div>'
      + concl('Đối thủ chính của khách sạn nhỏ là resort lớn khi họ giảm giá. Lợi thế cần có là chi phí vận hành thấp.'),
      'Hạ tầng và chính sách sắp tới.')

slide('TT', 'Hạ tầng là phần chắc chắn nhất, cơ chế đặc thù nên xem là <em>cơ hội cộng thêm</em>',
      '<div class="timeline">' + ''.join(f'<div><b>{a}</b><p>{b}</p></div>' for a, b in [
          ('03/2027', 'Trung tâm hội nghị APEC hoàn thiện, hội trường 4.030 chỗ.'),
          ('04/2027', 'Nhà ga sân bay mới (T2) khai thác giai đoạn 1, hướng tới 20-24 triệu khách/năm vào 2030.'),
          ('11/2027', 'Tàu điện 17 km khai thác thương mại.'),
          ('2030', 'Báo cáo dự phóng 16-18 triệu lượt khách hàng không, nguồn cung 40-45 nghìn phòng, công suất lý thuyết 70-75%.')]) + '</div>'
      + p('Cơ chế đặc thù (miễn thị thực 180 ngày, thẻ tạm trú dài hạn) hiện còn là đề án. Nếu được thông qua, phòng ở dài ngày có bếp có lợi nhất.')
      + p('Khách hội nghị hợp với khách sạn nhỏ ở vài nhóm: phòng tràn khi resort kín, đoàn 20-50 người, nhân sự sự kiện ở dài ngày. Báo cáo khuyên không kỳ vọng quá 20-30% doanh thu.')
      + concl('Mốc tham chiếu: cung và cầu cân bằng vào khoảng 2029-2030.')
      + note('Mốc hạ tầng theo báo cáo, chưa đối chiếu văn bản chính thức.'),
      'Nhịp chu kỳ sau một kỳ APEC.')

slide('TT', 'Tiền lệ Đà Nẵng cho thấy nhịp sau APEC: <em>tăng nóng, thanh lọc, rồi hồi phục</em>',
      p('Đà Nẵng sau APEC 2017: khách tăng mạnh khoảng 18 tháng. Giữa 2019 có thêm gần 6.000 phòng, công suất về khoảng 50%, mất vài năm để hồi phục.')
      + '<div class="timeline">' + ''.join(f'<div><b>{a}</b><p>{b}</p></div>' for a, b in [
          ('2027-2029 · Thanh lọc', 'Báo cáo dự báo cơ sở nhỏ đạt 25-40% công suất, giá thực nhận thấp nhất khoảng 820 nghìn/đêm (2028).'),
          ('2029-2030 · Cân bằng', 'Cung cầu gặp nhau khi hạ tầng mới chạy đủ.'),
          ('2030-2035 · Hấp thụ', 'Giá thực nhận lên khoảng 1 triệu (2030), 1,48 triệu (2035).'),
          ('Từ 2036 · Tái đầu tư', 'Tài sản cần làm mới để giữ phân khúc.')]) + '</div>'
      + concl('Đối chiếu với bản tính: năm đầu bản tính đặt công suất bình quân 49% (PA3) và 41% (PA4), cao hơn mức 25-40% báo cáo dự báo. Năm ổn định 59%. Đây là rủi ro lớn nhất của mọi phương án có xây.'),
      '04 phương án đang được cân nhắc.')

slide('TRƯỚC KHI BẮT ĐẦU', '04 phương án, <em>mỗi phương án một cấu trúc tiền riêng</em>',
      p('R201, R203, R205 đã thanh toán đủ. Bản tính giả định ghép thêm R207 thành khối 04 căn, 53 phòng. Mua R207 là tùy chọn, chưa chốt.')
      + cards([('PA1', 'Để thô cho thuê', 'Cho thuê nguyên trạng 140 triệu/tháng cả khối, tăng 4%/năm. Không bỏ vốn. Hết hạn phải phá dỡ và sửa lại.'),
               ('PA2', 'Xây xong rồi cho thuê', 'Chủ nhà xây, cho một bên thuê nguyên toà 300 triệu/tháng, tăng 4%/năm.'),
               ('PA3', 'Xây xong, thuê đơn vị quản lý', 'Đơn vị quản lý nhận 12% doanh thu cho back office, cộng thưởng 2-4% theo biên lợi nhuận. Tư vấn ban đầu 5.000 USD.'),
               ('PA4', 'Xây xong, tự vận hành', 'Gia đình lập công ty, tự dựng back office. Giám đốc lương 50 triệu cộng 20% phần lời vượt tiền thuê PA2.')])
      + '<div class="fix"><h4>CÁCH ĐỌC SỐ</h4><p>Số tiền là phần của Chủ nhà (75%), tính đến cuối năm thứ 10 (10/2037), tỷ đồng. Mốc so sánh: 30 tỷ tiền nhàn rỗi gửi ngân hàng 6,5%/năm thành <b>45 tỷ</b> phần Chủ nhà.</p></div>',
      'Các giả định chung cho cả 04 phương án.')

slide('TRƯỚC KHI BẮT ĐẦU', 'Giả định chung: <em>chỉ tính tiền phòng</em>, công suất và giá theo 3 mùa',
      table(['Mùa', 'Tháng', 'Công suất', 'Giá thuần/đêm'],
            [['Cao điểm', '12, 1, 2, 3', '75-85% (cơ sở 80%)', '900 nghìn'],
             ['Trung bình', '4, 7, 8, 11', '52,5-65% (60%)*', '750 nghìn*'],
             ['Thấp điểm', '5, 6, 9, 10', '30-45% (37,5%)', '600 nghìn']])
      + p('Bình quân năm 59%. 53 phòng cho doanh thu thuần khoảng <b>748 triệu/tháng</b> (giá 2028), tăng 4%/năm. Giá thuần đã trừ hoa hồng, VAT và phí OTA.')
      + '<ul class="ul">' + ''.join(f'<li>{x}</li>' for x in [
          'Bỏ hẳn doanh thu cửa hàng và pod.',
          'Chi phí tại khách sạn 38% doanh thu (đã khảo sát thực tế), lương tăng 7%/năm.',
          'Khai trương 11/2027. Năm đầu đạt 82% công suất ổn định (PA3) hoặc 70% rồi 90% (PA4).',
          'Thuế thu nhập doanh nghiệp 17%, thuế cổ tức 5%, quỹ thay mới đồ 3% doanh thu.',
          'Giá trị nhà tăng thêm: chênh lệch tiền thuê hoàn thiện và thô năm 10, vốn hoá 8%, chỉ lấy 70%.']) + '</ul>'
      + note('* Mùa trung bình là giả định của người lập, cần xác minh với số thực tế.'),
      'Câu hỏi đầu tiên: có nên xây?')

slide('A', 'Để thô cho thuê là cách nhẹ nhàng nhất, nhưng <em>tài sản bị khóa 10 năm</em>',
      pm(['Không bỏ thêm vốn. 30 tỷ nhàn rỗi vẫn gửi ngân hàng.', 'Tiền về đều ngay từ năm đầu: khoảng 236 triệu/tháng phần Chủ nhà, gồm cả lãi tiền gửi.'],
         ['Trống 6 tháng đầu và 6 tháng khi đổi khách ở năm thứ 5.', 'Hết hạn phải phá dỡ và sửa lại: khoảng 7,6 tỷ phần Chủ nhà (đã tính trượt giá).', 'Bên thuê tự sửa nhà theo ý họ. Suốt 10 năm, gia đình không xây được gì của riêng mình.'],
         ('NẾU VẪN CHỌN PA1', 'Duyệt thiết kế của bên thuê trước khi thi công, giữ cọc đủ để sửa lại nhà, có điều khoản thanh lý nếu họ bỏ dở.'))
      + big('57,1 tỷ', 'Phần Chủ nhà cuối năm 10, đã trừ chi phí sửa nhà. Thị trường xấu vẫn còn 55 tỷ.', 'PA1'),
      'So với xây, để thô thu về bao nhiêu?')

slide('A', 'Xây chỉ hơn để thô nhờ <em>giá trị căn nhà tăng thêm</em>, và phần này chưa được thẩm định',
      p('Phần Chủ nhà cuối năm 10, tỷ đồng. Khối đặc là tiền mặt, phần sọc là giá trị nhà tăng thêm (ước tính).')
      + stack_value()
      + p('Chỉ đếm tiền mặt, để thô (57,1) hơn PA3 (45,2) khoảng 12 tỷ. Cộng 17,3 tỷ giá trị nhà thì PA3 vượt lên 62,5. Nếu vốn hoá 10% thay vì 8%, phần này còn 13,8 tỷ.')
      + concl('Nên xây chỉ khi đơn vị độc lập thẩm định giá trị nhà sau hoàn thiện đạt mức này. Không đạt thì PA1 là lựa chọn an toàn.'),
      'Nếu xây, có 03 cách vận hành.')

slide('B', 'PA2 · Xây xong cho thuê: tiền đều, nhưng <em>giá thuê 300 triệu đã sát lợi nhuận</em> của khách sạn',
      pm(['Không phải vận hành. Tiền về đều từ năm 2: khoảng 264 triệu/tháng năm 3.', 'Hợp đồng 3-5 năm, hết hạn vẫn đổi hướng được.'],
         ['Trống 6 tháng sau khai trương và 6 tháng đổi khách ở năm 5.', 'Lãi trước thuế của chính khách sạn này năm 3 khoảng 357 triệu/tháng. Thuê 300 triệu, bên thuê chỉ còn lời mỏng, dễ xin giảm giá.', 'Cuối kỳ làm mới khoảng 15% vốn xây.', 'Hoàn vốn năm 9.'],
         ('CÁCH GIẢM RỦI RO', 'Giá thuê tách mùa cao và mùa thấp, có mức sàn. Giữ cọc đủ để làm mới.'))
      + big('52,7 tỷ', 'Phần Chủ nhà sau 10 năm. Thị trường xấu (thuê 240 triệu, trống lâu hơn) còn 33 tỷ.', 'PA2'),
      'Cách thứ 2: thuê đơn vị quản lý.')

slide('B', 'PA3 · Thuê đơn vị quản lý: <em>thu về nhiều nhất</em>, đổi lại là phí 12% doanh thu trả mãi',
      pm(['Có ngay kênh bán, quy trình và đội chuyên nghiệp. Năm đầu đạt 82% công suất ổn định.', 'Thưởng 2-4% tính theo biên lợi nhuận: đơn vị quản lý chỉ ăn thêm khi Chủ nhà có lời.', 'Năm đầu không có tháng âm tiền.'],
         ['Phí back office khoảng 90-100 triệu/tháng, tăng theo doanh thu.', 'Dữ liệu khách, tài khoản OTA dễ nằm phía đơn vị quản lý nếu hợp đồng không ghi rõ.', 'Năng lực vận hành tích lũy ở họ, không ở gia đình.'],
         ('CÁCH GIẢM RỦI RO', 'Tài khoản kênh bán và dữ liệu đứng tên công ty Chủ nhà, quyền chấm dứt theo KPI, bàn giao đầy đủ khi kết thúc.'))
      + big('62,5 tỷ', 'Phần Chủ nhà sau 10 năm. Hoà PA2 khi công suất bình quân từ 49%, hoàn vốn năm 8.', 'PA3'),
      'Cách thứ 3: gia đình tự vận hành.')

slide('B', 'PA4 · Tự vận hành: doanh nghiệp thuộc về gia đình, nhưng <em>thu về ít hơn PA3 khoảng 8 tỷ</em>',
      pm(['Toàn quyền giá, kênh bán, dữ liệu khách và đội ngũ.', 'Các con có chỗ học quản trị ngay trên tài sản nhà mình.', 'Hệ thống dựng xong có thể dùng lại cho toà thứ 2.'],
         ['Back office tự dựng khoảng 120-135 triệu/tháng, đắt hơn phí 12% ở quy mô 1 toà.', 'Năm đầu khách đến chậm (70% công suất ổn định), có 4 tháng thấp điểm âm khoảng 45 triệu.', 'Phụ thuộc vào 1 Giám đốc.'],
         ('CÁCH GIẢM RỦI RO', 'Quỹ dự phòng cho năm đầu, lương cơ sở cộng 20% phần lời vượt tiền thuê PA2, thoả thuận chấm dứt viết sẵn từ đầu.'))
      + big('54,2 tỷ', 'Phần Chủ nhà sau 10 năm. Hoà PA2 khi công suất bình quân từ 58%, hoàn vốn năm 9.', 'PA4'),
      'Đặt cả 04 phương án cạnh nhau.')

slide('B', 'Thị trường bình thường, cả 04 cách đều hơn gửi ngân hàng. <em>Thị trường xấu, chỉ để thô còn hơn.</em>',
      p('Phần Chủ nhà cuối năm thứ 10, tỷ đồng. Đường nét đứt là 45 tỷ nếu gửi ngân hàng.')
      + hbars([('Thị trường bình thường', [TOT[k] for k in PLANS]), ('Thị trường xấu', [XAU[k] for k in PLANS])], bank=BANK, hi='all')
      + note('Thị trường xấu: công suất bình quân 44%, giá phòng thấp hơn 10%, vốn 28 tỷ, khai trương trễ 3 tháng, PA2 thuê 240 triệu và trống lâu hơn.')
      + concl('PA3 dẫn đầu khi thị trường bình thường. Khi thị trường xấu, mọi phương án có xây đều dưới ngân hàng, PA3 giảm ít nhất trong 3 cách xây.'),
      'Tiền về hằng tháng của từng phương án.')

slide('B', 'Tiền về mỗi tháng: PA1 và PA3 cao nhất những năm đầu, <em>PA4 thấp nhất suốt 10 năm</em>',
      p('Triệu đồng mỗi tháng, phần Chủ nhà, sau thuế, gồm lãi tiền gửi. Năm 1 không tính khoản hoàn VAT vốn xây.')
      + lines(YRS, [f'N{i}' for i in range(1, 11)], ymin=0, ymax=500) + legend()
      + table(['Phần Chủ nhà', 'PA1', 'PA2', 'PA3', 'PA4'],
              [['Vốn bỏ ra', '0', '20,3 tỷ', '20,9 tỷ', '21,0 tỷ'],
               ['Mỗi tháng, năm 3', '276 tr', '264 tr', '283 tr', '242 tr'],
               ['Mỗi tháng, năm 10', '466 tr', '485 tr', '486 tr', '387 tr'],
               ['Tiền mặt cuối năm 10', '57,1', '35,4', '45,2', '36,9'],
               ['Giá trị nhà tăng thêm', '0', '17,3', '17,3', '17,3'],
               ['<b>Tổng cuối năm 10</b>', '<b>57,1</b>', '<b>52,7</b>', '<b>62,5</b>', '<b>54,2</b>'],
               ['Hoàn vốn', 'không cần', 'năm 9', 'năm 8', 'năm 9']])
      + note('Năm 5 PA1 và PA2 giảm vì 6 tháng trống khi đổi khách thuê. Tiền mặt cuối kỳ đã trừ chi phí sửa nhà (PA1) và làm mới (PA2).'),
      'Ngoài tiền, còn tiêu chí nào?')

slide('B', 'Ngoài tiền, mỗi góc nhìn nghiêng về <em>một phương án khác nhau</em>',
      table(['Góc nhìn', 'Câu hỏi', 'Nghiêng về'],
            [['Nhà đầu tư', 'Sau 10 năm còn bao nhiêu, thị trường xấu có trụ được không', 'PA3 (nhiều nhất), PA1 (an toàn nhất)'],
             ['Người mẹ', 'Tài sản và doanh nghiệp còn trong tay gia đình không, các con nhận lại gì', 'PA4'],
             ['Kế toán, pháp lý', 'Thuế và hợp đồng có đơn giản, an toàn không', 'PA1, PA2']])
      + p('Bảng điểm cũ (PA4 4,2 điểm) được chấm trên số của bản 2, khi PA4 còn dẫn về tiền. Số bản 4 đã đổi thứ tự đó.')
      + concl('Câu hỏi cho Chủ nhà: quyền sở hữu doanh nghiệp và việc để lại cho con có đáng khoảng 8 tỷ trong 10 năm không? Hàng điểm nên do Chủ nhà tự chấm lại.'),
      'Phân tích sâu: PA3 hay PA4.')

# ---- E: PA3 vs PA4 ----
slide('E', 'PA3 hơn PA4 ở <em>cả 6 kịch bản</em>, khoảng cách 7-10 tỷ',
      p('Phần Chủ nhà cuối năm 10, tỷ đồng.')
      + table(['Kịch bản', 'PA3', 'PA4', 'Chênh'], [[s, vn(v[2]), vn(v[3]), vn(v[2] - v[3])] for s, v in SCEN], hl=3)
      + p('Khoảng cách gần như không đổi khi thị trường tốt hay xấu. Nghĩa là nó đến từ <b>cấu trúc chi phí</b>, không phải từ may rủi thị trường.')
      + p('Chạy PA3 vài năm đầu rồi chuyển sang tự vận hành từ năm 4 cũng không cứu được: 57,6 tỷ, thấp hơn giữ PA3 khoảng 5 tỷ.')
      + concl('Câu hỏi đúng không phải "PA4 có tốt không", mà là "8 tỷ đổi lấy quyền tự vận hành có đáng không".'),
      '8 tỷ đó đến từ đâu?')

slide('E', 'Khoảng cách 8 tỷ có <em>3 nguồn</em>, lớn nhất là back office tự dựng',
      p('Đi từ PA3 sang PA4, phần Chủ nhà cuối năm 10, tỷ đồng.')
      + waterfall()
      + '<ul class="ul">' + ''.join(f'<li>{x}</li>' for x in [
          '<b>Back office tự dựng, 4,2 tỷ:</b> 95 triệu/tháng cố định cộng 3% doanh thu, đắt hơn 12% của PA3 ở quy mô 53 phòng.',
          '<b>Năm đầu chậm và học việc, 2,0 tỷ:</b> PA4 đạt 70% công suất năm đầu (PA3 82%), cộng 0,3 tỷ chi phí học và 180 triệu cố vấn.',
          '<b>Thưởng Giám đốc 20%, 2,1 tỷ:</b> khoảng 0,28 tỷ/năm từ năm 3. PA3 cũng có thưởng 2-4% nhưng nhỏ hơn.']) + '</ul>'
      + concl('Hai nguồn đầu là chi phí học việc và quy mô. Nguồn thứ ba là cái giá của việc giữ người giỏi, có thể đàm phán.'),
      'Một tháng điển hình năm 3 của hai phương án.')

slide('E', 'Một tháng năm 3: cùng doanh thu 810 triệu, <em>PA4 còn lại ít hơn 46 triệu</em>',
      p('Cả khối, triệu đồng/tháng, năm vận hành thứ 3 (2030).')
      + pl_stack()
      + table(['Khoản', 'PA3', 'PA4'],
              [['Doanh thu thuần', '810', '810'], ['Chi phí tại khách sạn (38%)', '318', '318'],
               ['Back office', '97 (12%)', '133 (95 tr + 3%)'], ['Thưởng vận hành', '13', '23'],
               ['Quỹ thay mới 3%', '24', '24'], ['<b>Lãi trước thuế</b>', '<b>357</b>', '<b>311</b>']])
      + note('Chi phí tại khách sạn giống nhau: cùng Giám đốc 50 triệu, cùng đội nhân sự.'),
      'Khi nào back office tự dựng rẻ hơn?')

slide('E', 'Back office tự dựng chỉ rẻ hơn khi doanh thu vượt <em>khoảng 1,06 tỷ/tháng</em>',
      p('Chi phí back office theo doanh thu thuần, triệu đồng/tháng.')
      + breakeven()
      + p('Ruby ở vùng 748-817 triệu, còn cách điểm hoà khoảng 30%. Muốn tới đó cần một trong ba điều:')
      + '<ul class="ul"><li>Giá phòng thuần bình quân trên 1 triệu/đêm.</li><li>Thêm khoảng 20 phòng (R207 hoặc tầng tum).</li><li>Một toà thứ 2 dùng chung back office.</li></ul>'
      + note('Kể cả khi toà thứ 2 gánh một nửa phần cố định, PA4 lên 60,4 tỷ, vẫn dưới PA3. Toà 2 làm PA4 đáng cân nhắc, chưa làm PA4 hơn PA3.'),
      'Dòng tiền theo mùa của năm đầu.')

slide('E', 'Năm đầu, PA4 có <em>4 tháng thấp điểm âm tiền</em>, PA3 thì không',
      p('Tiền về phần Chủ nhà mỗi tháng, năm vận hành đầu (11/2027 - 10/2028), triệu đồng, chưa tính hoàn VAT.')
      + month_bars(Y1['PA3'], Y1['PA4']) + legend(['PA3', 'PA4'])
      + p('Tháng 5, 6, 9, 10 năm 2028, PA4 âm khoảng 45 triệu/tháng. Gộp cả năm vẫn dương, nhưng nếu khai trương trễ hoặc thị trường xấu, mức âm sâu tới 100-115 triệu/tháng.')
      + concl('Nếu chọn PA4, để riêng quỹ dự phòng khoảng 0,5 tỷ cho 12 tháng đầu. Khoản hoàn VAT vốn xây (khoảng 1,8 tỷ phần Chủ nhà, tháng 10/2028) không nên tính vào quỹ này.'),
      'Ngưỡng công suất của từng phương án.')

slide('E', 'PA3 chịu được <em>công suất thấp hơn PA4 khoảng 9 điểm</em> trước khi thua các lựa chọn khác',
      p('Công suất bình quân năm (đã ổn định) để mỗi phương án hoà với gửi ngân hàng, PA2 và PA1.')
      + thresholds()
      + table(['Mốc hoà', 'PA3', 'PA4'], [['Gửi ngân hàng', '41%', '50%'], ['PA2 (thuê 300 tr)', '49%', '58%'], ['PA1 (để thô)', '54%', '62%'], ['Giá thuần bình quân để hoà PA1', '680 nghìn', '786 nghìn']])
      + concl('Kế hoạch 59% chỉ cao hơn ngưỡng hoà PA2 của PA4 khoảng 1 điểm. PA3 có biên an toàn khoảng 10 điểm.'),
      'Yếu tố nào làm số thay đổi nhiều nhất?')

slide('E', 'Rủi ro lớn nhất chung cho cả hai là <em>giá trị nhà và công suất</em>, không phải vốn xây',
      p('Thay đổi phần Chủ nhà cuối năm 10 khi một giả định đổi, các giả định khác giữ nguyên.')
      + tornado()
      + p('Hai phương án nhạy gần như nhau với từng yếu tố. Chọn PA3 hay PA4 không làm dự án an toàn hơn trước thị trường. Nó chỉ quyết định ai giữ phần chênh 8 tỷ.')
      + concl('Ưu tiên kiểm tra theo thứ tự: thẩm định giá trị nhà, rồi công suất và giá thực tế của 3-5 khách sạn trên phố Ruby, sau cùng mới tới báo giá xây.'),
      'Những gì bảng tính không đo được.')

slide('E', 'Những gì bảng tính <em>không đo được</em> lại là lý do chính để chọn PA4',
      table(['Yếu tố', 'PA3', 'PA4'],
            [['Dữ liệu khách, tài khoản OTA', 'Phụ thuộc hợp đồng', 'Của gia đình'],
             ['Năng lực vận hành', 'Tích lũy ở đơn vị quản lý', 'Tích lũy ở công ty gia đình'],
             ['Mở rộng toà thứ 2', 'Trả phí 12% lần nữa', 'Dùng lại back office'],
             ['Để lại cho các con', 'Một tài sản cho thuê quản lý', 'Một doanh nghiệp đang chạy'],
             ['Rủi ro con người', 'Đổi đơn vị quản lý theo hợp đồng', 'Phụ thuộc 1 Giám đốc'],
             ['Ràng buộc', 'Hợp đồng tối thiểu 3 năm', 'Thoả thuận chấm dứt viết sẵn']])
      + concl('Nếu Chủ nhà chỉ cần tài sản sinh lời, PA3 hợp lý hơn. Nếu Chủ nhà muốn để lại một doanh nghiệp, PA4 là cái giá khoảng 8 tỷ cho mục tiêu đó.'),
      'Hoàn vốn so với mốc 7 năm.')

slide('E', 'Mốc hoàn vốn an toàn 7 năm <em>chỉ đạt khi giá hoặc công suất cao hơn cơ sở</em>',
      table(['Kịch bản', 'PA3', 'PA4'],
            [['Cơ sở (59%, giá 600-900 nghìn)', 'năm 8', 'năm 9'], ['Đầu trên (65%)', 'năm 7', 'năm 8'],
             ['Giá thuần 900 nghìn cả năm', 'năm 6', 'năm 7'], ['Đầu dưới (52%)', 'quá 10 năm', 'quá 10 năm']])
      + p('Hoàn vốn ở đây là năm tiền mặt cộng dồn từ khách sạn bù đủ vốn bỏ ra. Không tính giá trị nhà tăng thêm.')
      + concl('Để PA3 về đúng 7 năm cần công suất bình quân khoảng 65%, hoặc giá thuần bình quân khoảng 820 nghìn. Đây là con số cần đối chiếu với các khách sạn đang chạy trên phố Ruby.'),
      'Khi nào chọn PA3, khi nào chọn PA4.')

slide('E', 'Quy tắc chọn: <em>mặc định PA3</em>, chuyển sang PA4 khi có ít nhất 1 trong 3 điều kiện',
      '<div class="rule"><h4>Chọn PA4 nếu</h4><ol><li>Có kế hoạch toà thứ 2 trong 3-5 năm để dùng chung back office.</li><li>Giá thuần thực tế các khách sạn cùng phố bám mức 900 nghìn trở lên.</li><li>Chủ nhà xác định để lại doanh nghiệp cho các con là mục tiêu chính, chấp nhận thu ít hơn khoảng 8 tỷ.</li></ol></div>'
      + '<div class="rule g"><h4>Nếu chọn PA3, hợp đồng phải có</h4><ol><li>Tài khoản OTA, website, Google Maps, phần mềm và dữ liệu khách đứng tên công ty Chủ nhà.</li><li>Phí tính trên tiền đã về tài khoản; thưởng theo biên lợi nhuận, không theo doanh thu.</li><li>Quyền chấm dứt khi trượt KPI 2 quý liền, 90 ngày bàn giao đầy đủ.</li><li>Báo giá chính thức 12% và thang thưởng trước 28/02/2027.</li></ol></div>'
      + concl('Cả hai đều cần Haji phụ trách chính: ở PA4 là Giám đốc, ở PA3 là người đại diện Chủ nhà đọc báo cáo và giữ 04 quyền.'),
      'Phần thi công: xây thế nào để không vượt vốn.')

# ---- C ----
slide('C', '04 căn ghép thành một khối <em>53 phòng</em>, dùng chung một lõi thang',
      '<img src="img/khoi-53-phong.jpg" alt="Mặt cắt khối 53 phòng">'
      + p('<b>Tầng 2 đến 5:</b> 53 phòng, mỗi phòng 20-22 m².') + p('<b>Tầng trệt:</b> sảnh, quầy kiêm lễ tân, giặt sấy. Khách tự nhận phòng ngoài giờ. Bản tính không tính doanh thu cửa hàng hay pod.')
      + p('<b>Hầm và bể phốt</b> làm mới hoàn toàn. Tầng tum để trống, làm sau khi có sổ.')
      + concl('R207 là phần mở rộng tùy chọn. Các số trong bản tính cho 04 căn; nếu chỉ làm 03 căn, cần chạy lại trước khi quyết.'),
      'Phong cách phòng quyết định phần lớn chi phí nội thất.')

slide('C', 'Một mẫu phòng sáng, ấm, <em>dùng chung cho cả 53 phòng</em>',
      '<img src="img/mau-phong.jpg" alt="Mẫu phòng tham khảo">'
      + p('<b>Nội thất lớn đóng sẵn:</b> giường gỗ, tủ quần áo, WC. Phần này đã nằm trong đơn giá 12 triệu/m².')
      + p('<b>Đồ rời:</b> đèn vải dạng lồng đèn, cây xanh chậu gốm, thảm cói, tranh khung gỗ.')
      + concl('Một mẫu duy nhất, mua một lần ở đất liền, chở ra một chuyến. Đó là cách giữ chi phí nội thất.'),
      '03 hướng phối màu để Chủ nhà chọn.')

slide('C', '03 hướng phối màu, cùng một nền <em>trắng ấm và gỗ tự nhiên</em>',
      '<img src="img/huong-mau.jpg" alt="03 hướng phối màu">'
      + note('Ảnh tham khảo sưu tầm, bản quyền thuộc tác giả gốc. Chỉ dùng để thống nhất phong cách.'),
      'Vốn hoàn thiện cho cả khối.')

slide('C', 'Vốn hoàn thiện 100% cho 04 căn: <em>cơ sở 27 tỷ, trần 28 tỷ</em>',
      big('27,04 tỷ', 'Vốn xây cơ sở cả khối, phần Chủ nhà khoảng 20,3 tỷ. Trần 28 tỷ dùng cho kịch bản xấu.', 'PA4')
      + p('Đơn giá 12 triệu/m² đã gồm điện nước, PCCC và nội thất lớn. 2.100 m² nhân 12 triệu là 25,2 tỷ; phần còn lại cho thiết kế, giấy phép và đồ rời. Chuẩn bị khai trương thêm 0,72 tỷ.')
      + table(['Điểm dễ đội giá', 'Cách xử lý'],
              [['Phú Quốc thiếu thợ', 'Tổng thầu trọn gói có đội sẵn trên đảo, giá cố định, lo chỗ ở cho thợ.'],
               ['Nội thất đội giá', 'Một mẫu phòng duy nhất, mua ở Bình Dương và TP.HCM, chở ra một lần.'],
               ['02 căn lệch cao độ 1 m', 'Chốt bản vẽ ghép trước khi đấu thầu, giám sát độc lập kiểm tra kết cấu.'],
               ['Chưa có báo giá thật', 'Ít nhất 03 báo giá trọn gói đúng phạm vi 12 triệu/m², giá tốt nhất dưới trần.']])
      + note('Vốn tăng từ 27 lên 28 tỷ chỉ làm phần Chủ nhà giảm khoảng 1,3 tỷ: ít hơn nhiều so với rủi ro công suất.'),
      'Trước khi chi tiền xây, cần đủ 04 điều kiện.')

slide('C', 'Chỉ khởi công khi <em>đủ 04 điều kiện</em>',
      p('Nếu một điều kiện không đạt, dự án dừng và chỉ mất chi phí hồ sơ, tối đa khoảng 0,84 tỷ cho cả khối. Các mốc ngày là đề xuất.')
      + '<div class="timeline">' + ''.join(f'<div><b>{a}</b><p>{b}</p></div>' for a, b in [
          ('15/01/2027 · Điều kiện 1', 'Ban quản lý khu Sun chấp thuận bằng văn bản việc ghép căn và làm lại hầm.'),
          ('31/01/2027 · Điều kiện 2', 'Giá trị căn nhà sau hoàn thiện được đơn vị độc lập thẩm định, đủ để xây có lợi hơn để thô (tăng thêm từ khoảng 23 tỷ cả khối).'),
          ('15/02/2027 · Điều kiện 3', 'Hồ sơ PCCC cho phương án ghép 04 căn được thẩm duyệt.'),
          ('28/02/2027 · Điều kiện 4', 'Có 03 báo giá tổng thầu, giá tốt nhất dưới trần 28 tỷ.'),
          ('03/2027 · Khởi công', 'Khởi công sau tháng 4/2027 nhiều khả năng không kịp APEC.'),
          ('11/2027 · Khai trương', 'Trước APEC. Tầng tum làm sau khi có sổ.')]) + '</div>'
      + note('R207 không nằm trong 04 điều kiện. Mua nếu giá hợp lý, quyết định riêng.'),
      'Khi khách sạn mở cửa, Chủ nhà giữ quyền bằng cách nào?')

# ---- D ----
slide('D', 'Dù PA3 hay PA4, Chủ nhà giữ <em>04 quyền then chốt</em>',
      p('04 quyền này áp dụng cho cả PA3 và PA4, kể cả khi người vận hành là người lập đề xuất này.')
      + cards([('1', 'Quyền giữ tiền', 'Mọi khoản thu về thẳng tài khoản công ty. Người vận hành chỉ có quỹ tạm ứng có giới hạn, khoản chi lớn cần 02 chữ ký.'),
               ('2', 'Quyền giữ kênh bán', 'Tài khoản Agoda, Booking, website, Google Maps và phần mềm quản lý đều đứng tên công ty.'),
               ('3', 'Quyền quyết định', 'Vay vốn, đổi mô hình, bán dưới giá sàn, tuyển quản lý: chỉ Chủ nhà quyết.'),
               ('4', 'Quyền thay người', 'Được tiếp quản bất cứ lúc nào, 90 ngày bàn giao, người vận hành không được kéo nhân sự đi theo.')]),
      'Và một chỉ số để theo dõi hằng tháng.')

slide('D', 'Mỗi tháng, Chủ nhà chỉ cần xem <em>một chỉ số: công suất phòng</em>',
      table(['Đèn', 'Điều kiện (12 tháng gần nhất)', 'Việc cần làm'],
            [['<span class="dot" style="background:#3E5A47"></span> Xanh', 'Từ 59% trở lên (kế hoạch)', 'Vận hành bình thường.'],
             ['<span class="dot" style="background:#C79A3A"></span> Vàng', 'Dưới 59%, hoặc 1 tháng thấp hơn kế hoạch tháng đó quá 10 điểm', 'Xem lại giá phòng, kênh bán, chi phí.'],
             ['<span class="dot" style="background:#B4452F"></span> Đỏ', 'Dưới ngưỡng hoà PA2 kéo dài 02 quý: PA3 49%, PA4 58%', 'Cân nhắc chuyển sang cho thuê lại.']])
      + p('Năm đầu so với kế hoạch từng tháng (bình quân 49% với PA3, 41% với PA4), vì khách sạn mới luôn cần thời gian. Các tháng thấp điểm 5, 6, 9, 10 so với mức 30-45%.')
      + '<div class="fix"><h4>03 CÁCH TỰ ĐỐI CHIẾU SỔ SÁCH</h4><p>1. Số đêm phòng trên phần mềm, tiền các kênh trả về và sao kê ngân hàng phải khớp nhau.</p><p>2. Số bộ ga gối đem giặt khớp với định mức theo số đêm phòng bán.</p><p>3. Mỗi quý có một khách bí mật ở thử, và so giá với 3-5 khách sạn trên phố Ruby.</p></div>',
      'Hôm nay cần quyết định gì?')

slide('QUYẾT ĐỊNH HÔM NAY', 'Hôm nay chưa cần quyết định xây, <em>chỉ cần duyệt bước kiểm tra 04 điều kiện</em>',
      '<div class="timeline">' + ''.join(f'<div><b>{a}</b><p>{b}</p></div>' for a, b in [
          ('1 · Thống nhất hướng đi', 'Xây có điều kiện. PA3 làm phương án mặc định, PA4 nếu có 1 trong 3 điều kiện ở trang quy tắc chọn.'),
          ('2 · Duyệt chi phí hồ sơ', 'Tối đa khoảng 0,84 tỷ cho cả khối, giải ngân theo từng điều kiện.'),
          ('3 · Chưa làm ngay', 'Chưa ký thuê quản lý, chưa đặt cọc nhà thầu, chưa mua nội thất, chưa làm tầng tum.')]) + '</div>'
      + table(['Việc', 'Phụ trách', 'Hạn'],
              [['Văn bản chấp thuận của Sun', 'Haji', '15/01'], ['Thẩm định giá trị căn nhà', 'Haji', '31/01'],
               ['Hình thức công ty, thuế', 'Kế toán thuế', '31/01'], ['Thẩm duyệt PCCC', 'Haji, tư vấn PCCC', '15/02'],
               ['Khảo sát công suất, giá 3-5 khách sạn phố Ruby', 'Haji', '15/02'],
               ['03 báo giá tổng thầu', 'Haji', '28/02'], ['Báo giá chính thức đơn vị quản lý', 'Haji', '28/02'],
               ['Quyết định mua R207 (tùy chọn)', 'Chủ nhà', '28/02'], ['Quyết định xây hay dừng, PA3 hay PA4', 'Chủ nhà', 'Đầu 03/2027']])
      + concl('Mục tiêu sau cùng: giữ tài sản, giữ quyền, và chọn cách vận hành theo số thật chứ không theo cảm giác.'),
      None, dots=False)

slide('NGƯỜI THỰC THI', 'Haji <em>phụ trách chính</em> dù Chủ nhà chọn PA3 hay PA4',
      p('Kinh nghiệm: quản lý khách hàng doanh nghiệp tại Insider One (nền tảng dữ liệu khách hàng) và điều hành Golf House Vietnam.')
      + cards([('01', 'Xây hệ thống từ đầu', 'Kênh đặt phòng, marketing, nhân sự, kế toán dựng ngay từ ngày đầu và thuộc về công ty của Chủ nhà.'),
               ('02', 'Đội ngũ và cách quản trị', 'Có sẵn đội ngũ và cách điều hành. Hướng dẫn thế hệ kế thừa để các con tiếp quản khi sẵn sàng.'),
               ('03', 'Công nghệ, dữ liệu khách', 'Quản lý phần mềm, kênh bán và dữ liệu khách hàng, để khách quay lại và giảm phụ thuộc phí kênh.')])
      + big('~8 tỷ', 'Phần Chủ nhà thu ít hơn trong 10 năm nếu tự vận hành thay vì thuê quản lý. Đây là con số cần cân với giá trị của một doanh nghiệp gia đình.', 'PA4')
      + note('Ràng buộc ở PA4: lương cơ sở 50 triệu cộng 20% phần lời vượt tiền thuê PA2, không vượt thì không thưởng. Chủ nhà giữ 04 quyền, thoả thuận chấm dứt viết sẵn từ đầu.'),
      'Phụ lục: giả định cần xác minh.', dots=False)

slide('PHỤ LỤC', 'Giả định <em>cần xác minh</em> trước khi quyết',
      table(['Giả định', 'Đang dùng', 'Ảnh hưởng'],
            [['Công suất, giá mùa trung bình', '60%, 750 nghìn', '±10% công suất = ±6 tỷ'],
             ['Giá trị nhà tăng thêm', '17,3 tỷ phần Chủ nhà', 'Bỏ đi thì PA1 dẫn đầu'],
             ['Mốc hoàn vốn 7 năm', 'Nguồn chưa rõ', 'Bản tính ra 8-9 năm'],
             ['Back office PA4', '95 tr/tháng + 3%', 'Nguồn chính của chênh 8 tỷ'],
             ['Chi phí học việc PA4', '0,3 tỷ + cố vấn 180 tr', 'Khoảng 2 tỷ cùng năm đầu chậm'],
             ['Phí PA3', '12% + thưởng 2-4%', '15% thì PA3 còn 60,0; 10% thì 64,1'],
             ['Tiền thuê PA2', '300 tr/tháng', 'Sát lợi nhuận khách sạn']])
      + note('Mô hình: 132 tháng từ 11/2026, lãi gửi 6,5%/năm cộng dồn tháng, phần Chủ nhà 75%. Code: mo-hinh/model.py, run6.py, run7.py. Nguồn thị trường: Báo cáo Nam Phú Quốc 2027-2042 (11/2026).'),
      None, dots=False)

# ================= RENDER =================
CSS = '''
:root{--bg:#F3EDE3;--ink:#2B2A27;--mute:#7A7368;--line:#D9D0C1;--accent:#C0673E;--green:#3E5A47;--card:#FBF8F2}
*{box-sizing:border-box}html{scroll-snap-type:y proximity;background:#E7DFD2}
body{margin:0;font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased}
.deck{max-width:460px;margin:0 auto}
.slide{background:var(--bg);min-height:100svh;padding:26px 24px 18px;display:flex;flex-direction:column;scroll-snap-align:start;border-bottom:1px solid var(--line)}
@media(min-width:600px){.slide{min-height:auto;margin:24px 0;border-radius:18px;box-shadow:0 6px 24px rgba(0,0,0,.08);border:none}}
.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}
.sec{font-size:11px;letter-spacing:.14em;font-weight:800}
.dots{display:flex;gap:4px}.dots span{width:20px;height:20px;border-radius:50%;border:1px solid #BFB4A3;font-size:10px;display:grid;place-items:center;color:var(--mute)}
.dots span.on{background:var(--green);color:#fff;border-color:var(--green)}
h1{font-family:Lora,Georgia,"Times New Roman",serif;font-size:25px;line-height:1.22;margin:0 0 12px;font-weight:700}
h1 em{font-style:normal;color:var(--accent)}
p{font-size:14.5px;line-height:1.5;margin:0 0 10px}
.lead{font-size:15px;color:#4A463F}.meta{font-size:12px;color:var(--mute);margin-top:16px}
.note{font-size:12px;color:var(--mute);line-height:1.45}
.concl{background:var(--green);color:#F3EDE3;border-radius:14px;padding:13px 15px;font-size:14.5px;line-height:1.45;margin:10px 0 6px;font-weight:600}
.concl b{color:#E3B663;margin-right:4px}
.cards{display:grid;gap:8px;margin:6px 0 10px}
.cardi{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 12px}
.cardi .tag{font-size:10px;font-weight:800;letter-spacing:.1em;color:var(--accent)}
.cardi h4{margin:2px 0 3px;font-size:14.5px}.cardi p{font-size:13.5px;margin:0;color:#4A463F}
.pm{display:grid;gap:8px;margin-bottom:8px}
.pm>div,.fix{border-radius:12px;padding:10px 12px}
.plus{background:#E4EADB}.minus{background:#F2DED3}.fix{background:var(--card);border:1px solid var(--line);margin-bottom:8px}
.pm h4,.fix h4{margin:0 0 5px;font-size:11px;letter-spacing:.12em}.pm p,.fix p{font-size:13.5px;margin:0 0 5px}
.big{display:flex;gap:12px;align-items:center;border-top:1px solid var(--line);padding-top:10px;margin-top:4px}
.big span{font-family:Lora,Georgia,serif;font-size:32px;font-weight:700;white-space:nowrap}.big p{font-size:13px;margin:0;color:#4A463F}
table{width:100%;border-collapse:collapse;font-size:12.5px;margin:6px 0 10px}
th{text-align:left;font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--mute);border-bottom:1.5px solid var(--ink);padding:5px 4px}
td{border-bottom:1px solid var(--line);padding:6px 4px;vertical-align:top;line-height:1.35}td.hl{color:var(--accent);font-weight:800}
.stats{display:grid;gap:8px;margin-bottom:8px}.stats div{display:grid;grid-template-columns:86px 1fr;gap:2px 10px;border-bottom:1px solid var(--line);padding-bottom:7px}
.stats b{font-family:Lora,Georgia,serif;font-size:22px;color:var(--accent);grid-row:span 2}.stats span{font-size:13px}.stats i{font-size:10.5px;color:var(--mute)}
.timeline{border-left:2px solid var(--accent);margin:4px 0 10px 4px;padding-left:14px}
.timeline div{position:relative;margin-bottom:9px}.timeline div:before{content:"";position:absolute;left:-20px;top:4px;width:10px;height:10px;border-radius:50%;background:var(--accent)}
.timeline b{font-size:12px;letter-spacing:.04em}.timeline p{font-size:13.5px;margin:1px 0 0}
.ul{padding-left:18px;margin:4px 0 10px}.ul li{font-size:13.5px;line-height:1.45;margin-bottom:5px}
.legend{display:flex;gap:14px;font-size:11.5px;margin:2px 0 8px;flex-wrap:wrap}.legend i{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:5px;vertical-align:-1px}
.rule{background:#F2DED3;border-radius:12px;padding:10px 12px;margin-bottom:8px}.rule.g{background:#E4EADB}
.rule h4{margin:0 0 4px;font-size:12px;letter-spacing:.08em;text-transform:uppercase}.rule ol{margin:0;padding-left:18px}.rule li{font-size:13.5px;margin-bottom:4px;line-height:1.4}
.dot{display:inline-block;width:9px;height:9px;border-radius:50%}
img{width:100%;border-radius:12px;margin:2px 0 10px;display:block}
svg{display:block;margin:4px 0 8px;overflow:visible}
.foot{margin-top:auto;padding-top:12px}.next{font-size:12.5px;color:var(--mute);margin-bottom:10px}.next b{color:#B88D5C}
.bar{display:flex;justify-content:space-between;border-top:1px solid var(--line);padding-top:10px;font-size:11px;letter-spacing:.14em;font-weight:800}
@media print{html{background:none}.slide{page-break-after:always;min-height:auto;margin:0;box-shadow:none;border-radius:0}}
'''

def render():
    n = len(SLIDES); out = []
    for i, (sec, title, body, nxt, dots) in enumerate(SLIDES, 1):
        label = SEC.get(sec, sec) or 'PHÚ QUỐC · BÃI KEM'
        dd = ''
        if dots and sec in ('A', 'B', 'E', 'C', 'D'):
            dd = '<div class="dots">' + ''.join(f'<span class="{"on" if k==sec else ""}">{k}</span>' for k in 'ABECD') + '</div>'
        nx = f'<div class="next"><b>Tiếp theo</b> · {nxt}</div>' if nxt else ''
        out.append(f'<section class="slide" id="s{i}"><div class="top"><div class="sec">{label}</div>{dd}</div><h1>{title}</h1>{body}'
                   f'<div class="foot">{nx}<div class="bar"><span>RUBY BÃI KEM</span><span>{i:02d} / {n} →</span></div></div></section>')
    doc = f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ruby Bãi Kem - Slide tư vấn (bản 4, 18/11/2026)</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Lora:wght@600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><main class="deck">{''.join(out)}</main></body></html>'''
    open(OUT, 'w').write(doc); print('wrote', OUT, n, 'slides')

render()
