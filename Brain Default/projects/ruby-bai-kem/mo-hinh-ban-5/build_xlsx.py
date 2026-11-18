# Sinh file Excel co cong thuc cho mo hinh ban 5 (PA3 vs PA4). Gia tri dau vao lay tu model5.P().
import sys; sys.path.insert(0,'.')
from model5 import *
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
p=P(); wb=Workbook()
BLUE=Font(color="1F4E99",bold=True); B=Font(bold=True); H=Font(bold=True,color="FFFFFF")
HF=PatternFill("solid",fgColor="7A1F2B"); INP=PatternFill("solid",fgColor="FFF4C2"); SUB=PatternFill("solid",fgColor="F3E6E8")
def hdr(ws,r,vals,c0=1):
    for i,v in enumerate(vals):
        x=ws.cell(r,c0+i,v); x.font=H; x.fill=HF; x.alignment=Alignment(wrap_text=True,vertical="center")
def inp(ws,r,c,v,fmt=None):
    x=ws.cell(r,c,v); x.font=BLUE; x.fill=INP
    if fmt: x.number_format=fmt
    return x
# ---------------- Dau vao
ws=wb.active; ws.title="Đầu vào"; ws.column_dimensions['A'].width=46; ws.column_dimensions['B'].width=14; ws.column_dimensions['C'].width=60
ws['A1']="Ruby Bãi Kem - Mô hình bản 5: công ty vận hành thuê 4 căn (R201, R203, R205, R207), PA3 so với PA4"; ws['A1'].font=Font(bold=True,size=13)
ws['A2']="Đơn vị: triệu đồng. Ô vàng chữ xanh là giả định, sửa được. Tháng vận hành 1 = 11/2027. Javis lập 18/11/2026."
rows=[("Số phòng bán",p['rooms'],"0","Haji: 53 phòng"),
("Công suất mùa cao (12-3)",p['occ'][0],"0%","Haji: 75-85%, lấy giữa"),
("Công suất mùa vừa (4, 7, 8, 11)",p['occ'][1],"0%","Javis đặt 52,5-65%, lấy giữa - cần Haji xác nhận"),
("Công suất mùa thấp (5, 6, 9, 10)",p['occ'][2],"0%","Haji: 30-45%, lấy giữa"),
("ADR thuần mùa cao (triệu/đêm)",p['adr'][0],"0.000","Haji: 600-900k đã trừ commission, VAT, OTA"),
("ADR thuần mùa vừa",p['adr'][1],"0.000","Javis đặt"),
("ADR thuần mùa thấp",p['adr'][2],"0.000",""),
("Hệ số giá (kịch bản)",p['pm'],"0.00","1 = cơ sở; 0,9 = giá -10%"),
("Tăng giá phòng/năm",p['price_g'],"0.0%",""),
("PA3: mức đạt công suất năm 1",p['ramp3'][0],"0%","Nhà vận hành có sẵn kênh bán"),
("PA3: mức đạt năm 2",p['ramp3'][1],"0%",""),
("PA4: mức đạt năm 1",p['ramp4'][0],"0%","Tự dựng kênh, đội mới"),
("PA4: mức đạt năm 2",p['ramp4'][1],"0%",""),
("Chi phí kèm lương (BHXH 21,5% x 80% lương + tháng 13)",p['oncost'],"0.0%",""),
("Tăng lương/năm",p['sal_g'],"0.0%",""),
("Tăng định phí và biến phí/đêm phòng/năm",p['fix_g'],"0.0%",""),
("Buồng thời vụ mùa cao (người)",p['seasonal'],"0",""),
("Lương buồng thời vụ",p['seasonal_w'],"0.0",""),
("Biến phí/đêm phòng có khách (triệu)",p['var_orn'],"0.000","Giặt là 28k + amenities 17k + điện nước biến đổi 30k"),
("Biến phí theo % doanh thu",p['var_pct'],"0.0%","Sửa chữa nhỏ 1% + phí thanh toán, linh tinh 1%"),
("Định phí site ngoài lương (triệu/tháng)",p['site_fix'],"0.0","Điện nước nền 20 + phí khu, bảo hiểm, giấy phép 10 + thang máy, PCCC, internet 10"),
("Tiền thuê khách sạn/căn/tháng",85,"0.0","Haji: giá cơ sở 85 triệu/căn"),
("Số căn thuê",4,"0","R201, R203, R205, R207"),
("Tăng tiền thuê mỗi kỳ",p['rent_step'],"0.0%",""),
("Kỳ tăng tiền thuê (năm)",p['rent_every'],"0",""),
("Quỹ thay thế nội thất (% doanh thu)",p['ffe'],"0.0%",""),
("PA3: phí back office (% doanh thu)",p['bo3'],"0.0%","Haji: 12%"),
("PA4: phí ngoài back office (triệu/tháng)",p['bo4_ext'],"0.0","Dịch vụ kế toán thuế, kiểm toán 7 + phần mềm PMS, channel manager, booking engine, kế toán 9"),
("PA4: back office theo % doanh thu",p['bo4_var'],"0.0%","Marketing 2% + tuyển dụng, đào tạo 1%"),
("PA4: học phí sửa sai năm 1 (triệu)",p['tuition'],"0",""),
("PA4: thưởng GM (% lợi nhuận sau tiền thuê)",p['bonus4'],"0%","Giả định gốc: 20% phần lãi vượt tiền thuê"),
("PA3: trước khai trương + tư vấn 5.000 USD",p['pre3'],"0","720 + 132"),
("PA4: trước khai trương + cố vấn vận hành",p['pre4'],"0","720 + 180"),
("Thuế TNDN",p['cit'],"0%","Chuyển lỗ đơn giản, cần kế toán xác nhận"),
("Vốn hoàn thiện 4 căn (triệu)",27040,"#,##0","12 tr/m² all-in x 2.100 m² + hồ sơ + đồ rời"),
("Thuế cho thuê nhà của cá nhân",0.10,"0%","VAT 5% + TNCN 5%"),
]
R={}
hdr(ws,4,["Giả định","Giá trị","Ghi chú"])
for i,(a,v,f,n) in enumerate(rows):
    r=5+i; ws.cell(r,1,a); inp(ws,r,2,v,f); ws.cell(r,3,n); R[a]=f"'Đầu vào'!$B${r}"
key=lambda s: R[s]
# bang mua
r0=5+len(rows)+2; ws.cell(r0,1,"Bảng tháng lịch").font=B
hdr(ws,r0+1,["Tháng","Mùa (1 cao, 2 vừa, 3 thấp)","Số ngày"])
for c in range(12):
    ws.cell(r0+2+c,1,c+1); ws.cell(r0+2+c,2,SEASON[c]+1); ws.cell(r0+2+c,3,DAYS[c])
SEA=f"'Đầu vào'!$A${r0+2}:$C${r0+13}"
OCC=[key("Công suất mùa cao (12-3)"),key("Công suất mùa vừa (4, 7, 8, 11)"),key("Công suất mùa thấp (5, 6, 9, 10)")]
ADR=[key("ADR thuần mùa cao (triệu/đêm)"),key("ADR thuần mùa vừa"),key("ADR thuần mùa thấp")]
# ---------------- Nhan su
ns=wb.create_sheet("Nhân sự")
for col,w in zip("ABCDEFGH",[38,8,12,12,14,30,30,30]): ns.column_dimensions[col].width=w
ns['A1']="Bộ máy nhân sự (giá năm 1, triệu/tháng)"; ns['A1'].font=Font(bold=True,size=13)
hdr(ns,3,["Vị trí","Số người","Lương gross","Hỗ trợ ở + ăn","Chi phí/tháng","PA3: ai lo","PA4: ai lo","Ghi chú vận hành"])
notes={0:("Haji, lương trên bảng lương khách sạn","Haji, kiêm sales, revenue, marketing, nhân sự","Lương cơ sở 50 triệu, như nhau ở 2 PA"),
1:("Khách sạn","Khách sạn","Kiêm đặt phòng, xử lý phàn nàn, ca hành chính"),
2:("Khách sạn","Khách sạn","24/7 cần ~3,5 người cho 1 vị trí; ca đêm kiêm night audit"),
3:("Khách sạn","Khách sạn","Kiểm phòng, đặt hàng amenities, làm việc với giặt là"),
4:("Khách sạn","Khách sạn","~13 phòng/người/ngày; mùa cao thêm 2 thời vụ"),
5:("Khách sạn, nhà vận hành giám sát","Khách sạn","2 thang máy, hầm, PCCC; hợp đồng bảo trì thuê ngoài"),
6:("Khách sạn","Khách sạn","Khu Sun có an ninh chung; bảo vệ đêm kiêm tạp vụ sảnh")}
r=4
for i,(nm,n,w,h) in enumerate(SITE_STAFF):
    ns.cell(r,1,nm); inp(ns,r,2,n); inp(ns,r,3,w,"0.0"); inp(ns,r,4,h,"0.0")
    ns.cell(r,5,f"=B{r}*(C{r}*(1+{key('Chi phí kèm lương (BHXH 21,5% x 80% lương + tháng 13)')})+D{r})").number_format="0.0"
    a,b,c=notes[i]; ns.cell(r,6,a); ns.cell(r,7,b); ns.cell(r,8,c); r+=1
ns.cell(r,1,"Tổng nhân sự site (như nhau PA3, PA4)").font=B; ns.cell(r,2,f"=SUM(B4:B{r-1})").font=B
ns.cell(r,5,f"=SUM(E4:E{r-1})").font=B; ns.cell(r,5).number_format="0.0"; SITE_TOT=f"'Nhân sự'!$E${r}"; r+=1
ns.cell(r,1,"Buồng thời vụ mùa cao (chỉ tháng 12-3)"); ns.cell(r,5,f"={key('Buồng thời vụ mùa cao (người)')}*{key('Lương buồng thời vụ')}*(1+{key('Chi phí kèm lương (BHXH 21,5% x 80% lương + tháng 13)')})").number_format="0.0"; SEAS_TOT=f"'Nhân sự'!$E${r}"; r+=2
hdr(ns,r,["Back office PA4 tự làm","Số người","Lương gross","Hỗ trợ ở + ăn","Chi phí/tháng","PA3: ai lo","PA4: ai lo","Ghi chú vận hành"]); r+=1; b0=r
bon=[("Nhà vận hành (trong 12%)","Khách sạn","Thu chi, lương, hồ sơ nhân sự; sổ sách thuê dịch vụ kế toán"),("Nhà vận hành (trong 12%)","Khách sạn","OTA, giá, nội dung, quảng cáo; GM duyệt giá")]
for i,(nm,n,w,h) in enumerate(BO4_STAFF):
    ns.cell(r,1,nm); inp(ns,r,2,n); inp(ns,r,3,w,"0.0"); inp(ns,r,4,h,"0.0")
    ns.cell(r,5,f"=B{r}*(C{r}*(1+{key('Chi phí kèm lương (BHXH 21,5% x 80% lương + tháng 13)')})+D{r})").number_format="0.0"
    ns.cell(r,6,bon[i][0]); ns.cell(r,7,bon[i][1]); ns.cell(r,8,bon[i][2]); r+=1
ns.cell(r,1,"Tổng nhân sự back office PA4").font=B; ns.cell(r,5,f"=SUM(E{b0}:E{r-1})").font=B; ns.cell(r,5).number_format="0.0"; BO4_TOT=f"'Nhân sự'!$E${r}"; r+=2
ns.cell(r,1,"Chức năng PA3 mua bằng 12% mà PA4 phải tự gánh").font=B; r+=1
for t in ["Revenue management và chiến lược giá theo ngày: PA4 do GM làm",
          "Sales khách đoàn, đại lý, hợp đồng công ty, hệ thống đặt phòng trung tâm: PA4 do GM làm",
          "Thương hiệu, chương trình khách thân thiết, dữ liệu khách nhiều khách sạn: PA4 không có",
          "Tuyển dụng, đào tạo, quy trình chuẩn (SOP), kiểm tra chất lượng định kỳ: PA4 do GM + cố vấn 6 tháng đầu",
          "Kế toán trưởng, báo cáo quản trị, kiểm soát nội bộ: PA4 thuê dịch vụ kế toán + kế toán nội bộ",
          "Người thay GM khi GM nghỉ hoặc ốm: PA3 có, PA4 phải đào tạo trưởng lễ tân làm phó"]:
    ns.cell(r,1,"- "+t); r+=1
# ---------------- Theo thang
tm=wb.create_sheet("Theo tháng")
cols=["Tháng VH","Tháng lịch","Năm VH","Mùa","Số ngày","Mức đạt PA3","Mức đạt PA4","Công suất PA3","Công suất PA4","Đêm phòng PA3","Đêm phòng PA4","ADR thuần",
 "Doanh thu PA3","Doanh thu PA4","Nhân sự site","Biến phí PA3","Biến phí PA4","Định phí site","Chi phí site PA3","Chi phí site PA4",
 "Back office PA3","Back office PA4","GOP PA3","GOP PA4","Tiền thuê KS","Quỹ nội thất PA3","Quỹ nội thất PA4","Dòng tiền PA3","Dòng tiền PA4","Lũy kế PA3","Lũy kế PA4"]
hdr(tm,1,cols); tm.freeze_panes="B2"
for i in range(len(cols)): tm.column_dimensions[L(i+1)].width=11
oc=key('Chi phí kèm lương (BHXH 21,5% x 80% lương + tháng 13)')
for m in range(1,121):
    r=m+1; g=lambda e: e
    f={}
    f['A']=m; f['B']=f"=DATE(2027,10+A{r},1)"; f['C']=f"=INT((A{r}-1)/12)+1"
    f['D']=f"=VLOOKUP(MONTH(B{r}),{SEA},2,FALSE)"; f['E']=f"=VLOOKUP(MONTH(B{r}),{SEA},3,FALSE)"
    f['F']=f"=IF(C{r}=1,{key('PA3: mức đạt công suất năm 1')},IF(C{r}=2,{key('PA3: mức đạt năm 2')},1))"
    f['G']=f"=IF(C{r}=1,{key('PA4: mức đạt năm 1')},IF(C{r}=2,{key('PA4: mức đạt năm 2')},1))"
    occ=f"CHOOSE(D{r},{OCC[0]},{OCC[1]},{OCC[2]})"
    f['H']=f"=MIN(0.95,{occ}*F{r})"; f['I']=f"=MIN(0.95,{occ}*G{r})"
    f['J']=f"={key('Số phòng bán')}*E{r}*H{r}"; f['K']=f"={key('Số phòng bán')}*E{r}*I{r}"
    f['L']=f"=CHOOSE(D{r},{ADR[0]},{ADR[1]},{ADR[2]})*{key('Hệ số giá (kịch bản)')}*(1+{key('Tăng giá phòng/năm')})^(C{r}-1)"
    f['M']=f"=J{r}*L{r}"; f['N']=f"=K{r}*L{r}"
    sal=f"(1+{key('Tăng lương/năm')})^(C{r}-1)"; fx=f"(1+{key('Tăng định phí và biến phí/đêm phòng/năm')})^(C{r}-1)"
    f['O']=f"=({SITE_TOT}+IF(D{r}=1,{SEAS_TOT},0))*{sal}"
    f['P']=f"=J{r}*{key('Biến phí/đêm phòng có khách (triệu)')}*{fx}+{key('Biến phí theo % doanh thu')}*M{r}"
    f['Q']=f"=K{r}*{key('Biến phí/đêm phòng có khách (triệu)')}*{fx}+{key('Biến phí theo % doanh thu')}*N{r}"
    f['R']=f"={key('Định phí site ngoài lương (triệu/tháng)')}*{fx}"
    f['S']=f"=O{r}+P{r}+R{r}"; f['T']=f"=O{r}+Q{r}+R{r}"
    f['U']=f"={key('PA3: phí back office (% doanh thu)')}*M{r}"
    f['V']=f"={BO4_TOT}*{sal}+{key('PA4: phí ngoài back office (triệu/tháng)')}*{fx}+{key('PA4: back office theo % doanh thu')}*N{r}+IF(C{r}=1,{key('PA4: học phí sửa sai năm 1 (triệu)')}/12,0)"
    f['W']=f"=M{r}-S{r}-U{r}"; f['X']=f"=N{r}-T{r}-V{r}"
    f['Y']=f"={key('Tiền thuê khách sạn/căn/tháng')}*{key('Số căn thuê')}*(1+{key('Tăng tiền thuê mỗi kỳ')})^INT((C{r}-1)/{key('Kỳ tăng tiền thuê (năm)')})"
    f['Z']=f"={key('Quỹ thay thế nội thất (% doanh thu)')}*M{r}"; f['AA']=f"={key('Quỹ thay thế nội thất (% doanh thu)')}*N{r}"
    f['AB']=f"=W{r}-Y{r}-Z{r}"; f['AC']=f"=X{r}-Y{r}-AA{r}"
    f['AD']=(f"=-{key('PA3: trước khai trương + tư vấn 5.000 USD')}+AB{r}" if m==1 else f"=AD{r-1}+AB{r}")
    f['AE']=(f"=-{key('PA4: trước khai trương + cố vấn vận hành')}+AC{r}" if m==1 else f"=AE{r-1}+AC{r}")
    for col,v in f.items():
        x=tm[f"{col}{r}"]; x.value=v
        x.number_format = "mm/yyyy" if col=='B' else "0%" if col in "FGHI" else "0.000" if col=='L' else "#,##0"
# ---------------- Theo nam
yn=wb.create_sheet("Theo năm"); yn.column_dimensions['A'].width=40
hdr(yn,1,["Chỉ tiêu (triệu)"]+[f"Năm {y}" for y in range(1,11)]+["10 năm"])
T="'Theo tháng'!"
def sumy(col,c): return f"=SUMIFS({T}${col}$2:${col}$121,{T}$C$2:$C$121,{c})"
lines=[]
def block(pa,start):
    r=start; yn.cell(r,1,pa).font=B; yn.cell(r,1).fill=SUB; r+=1
    cR,cS,cBO,cG,cF='M' if pa=='PA3' else 'N','S' if pa=='PA3' else 'T','U' if pa=='PA3' else 'V','W' if pa=='PA3' else 'X','Z' if pa=='PA3' else 'AA'
    cO='J' if pa=='PA3' else 'K'
    names=["Đêm phòng bán","Doanh thu phòng thuần","Chi phí site (nhân sự, biến phí, định phí)","  % doanh thu (site)","Back office","  % doanh thu (back office)","GOP (lãi gộp vận hành, trước tiền thuê)","  % doanh thu (GOP)",
      "Tiền thuê khách sạn","  % doanh thu (tiền thuê)","Quỹ nội thất","Incentive nhà vận hành PA3 / thưởng GM PA4","Lợi nhuận trước thuế","Thuế TNDN","Lợi nhuận sau thuế","  bình quân/tháng"]
    idx={}
    for i,nm in enumerate(names): yn.cell(r+i,1,nm); idx[nm]=r+i
    for y in range(1,11):
        c=L(y+1); cell=lambda nm: f"{c}{idx[nm]}"
        yn[cell("Đêm phòng bán")]=sumy(cO,y); yn[cell("Doanh thu phòng thuần")]=sumy(cR,y)
        yn[cell("Chi phí site (nhân sự, biến phí, định phí)")]=sumy(cS,y); yn[cell("Back office")]=sumy(cBO,y)
        yn[cell("GOP (lãi gộp vận hành, trước tiền thuê)")]=sumy(cG,y); yn[cell("Tiền thuê khách sạn")]=sumy('Y',y); yn[cell("Quỹ nội thất")]=sumy(cF,y)
        rv=cell("Doanh thu phòng thuần")
        for a,b in [("  % doanh thu",None)]: pass
        yn.cell(idx["Chi phí site (nhân sự, biến phí, định phí)"]+1,y+1,f"={cell('Chi phí site (nhân sự, biến phí, định phí)')}/{rv}")
        yn.cell(idx["Back office"]+1,y+1,f"={cell('Back office')}/{rv}")
        yn.cell(idx["GOP (lãi gộp vận hành, trước tiền thuê)"]+1,y+1,f"={cell('GOP (lãi gộp vận hành, trước tiền thuê)')}/{rv}")
        yn.cell(idx["Tiền thuê khách sạn"]+1,y+1,f"={cell('Tiền thuê khách sạn')}/{rv}")
        gop=cell('GOP (lãi gộp vận hành, trước tiền thuê)'); mg=f"({gop}/{rv})"
        if pa=='PA3':
            yn[cell("Incentive nhà vận hành PA3 / thưởng GM PA4")]=f"=IF({mg}>=0.5,0.04,IF({mg}>=0.45,0.03,IF({mg}>=0.4,0.02,0)))*MAX(0,{gop})"
        else:
            yn[cell("Incentive nhà vận hành PA3 / thưởng GM PA4")]=f"={key('PA4: thưởng GM (% lợi nhuận sau tiền thuê)')}*MAX(0,{gop}-{cell('Tiền thuê khách sạn')}-{cell('Quỹ nội thất')})"
        pbt=cell("Lợi nhuận trước thuế")
        yn[pbt]=f"={gop}-{cell('Tiền thuê khách sạn')}-{cell('Quỹ nội thất')}-{cell('Incentive nhà vận hành PA3 / thưởng GM PA4')}"
        yn[cell("Thuế TNDN")]=f"={key('Thuế TNDN')}*MAX(0,MIN({pbt},SUM($B{idx['Lợi nhuận trước thuế']}:{pbt})))"
        yn[cell("Lợi nhuận sau thuế")]=f"={pbt}-{cell('Thuế TNDN')}"
        yn[cell("  bình quân/tháng")]=f"={cell('Lợi nhuận sau thuế')}/12"
    for nm,rr in idx.items():
        pct = nm.startswith("  %")
        for y in range(1,12):
            x=yn.cell(rr,y+1); x.number_format="0.0%" if pct else "#,##0"
        if not pct and nm!="  bình quân/tháng": yn.cell(rr,12,f"=SUM(B{rr}:K{rr})").number_format="#,##0"
    for nm in ("GOP (lãi gộp vận hành, trước tiền thuê)","Lợi nhuận sau thuế"):
        for y in range(1,13): yn.cell(idx[nm],y).font=B
    return idx, r+len(names)
i3,nx=block('PA3',3); i4,nx=block('PA4',nx+1)
# ---------------- Tom tat
ts=wb.create_sheet("Tóm tắt",0); ts.column_dimensions['A'].width=52; ts.column_dimensions['B'].width=14; ts.column_dimensions['C'].width=14; ts.column_dimensions['D'].width=50
ts['A1']="Ruby Bãi Kem - Bản 5: PA3 so với PA4 khi khách sạn trả tiền thuê 85 triệu/căn"; ts['A1'].font=Font(bold=True,size=13)
ts['A2']="Số triệu đồng, 100% công ty vận hành. Số tự tính lại khi sửa tab Đầu vào và Nhân sự."
hdr(ts,4,["Chỉ tiêu","PA3","PA4","Đọc thế nào"])
Y="'Theo năm'!"
def yv(idx,nm,col): return f"{Y}{col}{idx[nm]}"
items=[("Doanh thu thuần bình quân/tháng, năm 3",lambda i:f"={yv(i,'Doanh thu phòng thuần','D')}/12","#,##0","Giá năm 3, chỉ doanh thu phòng"),
("Chi phí site % doanh thu, năm 3",lambda i:f"={Y}D{i['Chi phí site (nhân sự, biến phí, định phí)']+1}","0.0%","38% chỉ đúng khi doanh thu ~1 tỷ/tháng"),
("Back office % doanh thu, năm 3",lambda i:f"={Y}D{i['Back office']+1}","0.0%",""),
("GOP % doanh thu, năm 3",lambda i:f"={Y}D{i['GOP (lãi gộp vận hành, trước tiền thuê)']+1}","0.0%","Lãi vận hành trước tiền thuê"),
("Tiền thuê % doanh thu, năm 3",lambda i:f"={Y}D{i['Tiền thuê khách sạn']+1}","0.0%","Tiền thuê lớn hơn GOP là lỗ"),
("Lợi nhuận sau thuế/tháng, năm 1",lambda i:f"={Y}B{i['  bình quân/tháng']}","#,##0",""),
("Lợi nhuận sau thuế/tháng, năm 3",lambda i:f"={Y}D{i['  bình quân/tháng']}","#,##0",""),
("Lợi nhuận sau thuế/tháng, năm 10",lambda i:f"={Y}K{i['  bình quân/tháng']}","#,##0",""),
("Tháng dòng tiền thấp nhất, năm 1",None,"#,##0","Tháng mùa thấp, trước incentive và thuế"),
("Chi trước khai trương",None,"#,##0",""),
("Lợi nhuận sau thuế cộng dồn 10 năm (đã trừ chi trước khai trương)",lambda i:f"={Y}L{i['Lợi nhuận sau thuế']}-{{pre}}","#,##0","Giá trị công ty vận hành tạo ra cuối năm 10"),
("Quỹ tiền phải chuẩn bị (lỗ lũy kế sâu nhất)",None,"#,##0","Vốn lưu động chủ công ty vận hành phải góp"),
("Incentive / thưởng GM cộng dồn 10 năm",lambda i:f"={Y}L{i['Incentive nhà vận hành PA3 / thưởng GM PA4']}","#,##0",""),
("Back office cộng dồn 10 năm",lambda i:f"={Y}L{i['Back office']}","#,##0",""),
]
pre3=key('PA3: trước khai trương + tư vấn 5.000 USD'); pre4=key('PA4: trước khai trương + cố vấn vận hành')
for k,(nm,fn,fmt,note) in enumerate(items):
    r=5+k; ts.cell(r,1,nm); ts.cell(r,4,note)
    for c,(idx,pre,col_cf,col_cum) in enumerate([(i3,pre3,'AB','AD'),(i4,pre4,'AC','AE')]):
        if nm.startswith("Tháng dòng tiền thấp"): v=f"=MIN('Theo tháng'!{col_cf}2:{col_cf}13)"
        elif nm.startswith("Chi trước"): v=f"={pre}"
        elif nm.startswith("Quỹ tiền"): v=f"=-MIN(0,MIN('Theo tháng'!{col_cum}2:{col_cum}121))"
        else: v=fn(idx).replace("{pre}",pre)
        x=ts.cell(r,2+c,v); x.number_format=fmt; x.font=B if "10 năm (đã" in nm else Font()
r=5+len(items)+1
ts.cell(r,1,"Lớp chủ nhà (mỗi căn)").font=B; ts.cell(r,1).fill=SUB; r+=1
cap=key('Vốn hoàn thiện 4 căn (triệu)'); rent=key('Tiền thuê khách sạn/căn/tháng'); tx=key('Thuế cho thuê nhà của cá nhân')
ts.cell(r,1,"Vốn hoàn thiện/căn"); ts.cell(r,2,f"={cap}/{key('Số căn thuê')}").number_format="#,##0"; r+=1
ts.cell(r,1,"Tiền thuê thực nhận/căn/tháng, năm 1 (sau thuế cho thuê)"); ts.cell(r,2,f"={rent}*(1-{tx})").number_format="0.0"; r+=1
ts.cell(r,1,"Tiền thuê thực nhận/căn cộng dồn 10 năm"); ts.cell(r,2,f"=SUM('Theo tháng'!Y2:Y121)/{key('Số căn thuê')}*(1-{tx})").number_format="#,##0"; r+=1
ts.cell(r,1,"Số năm hồi vốn đơn giản (không tính lãi)"); ts.cell(r,2,f"=B{r-3}/(B{r-2}*12)").number_format="0.0"; ts.cell(r,4,"Khớp mốc ~7 năm Haji nêu, NẾU công ty vận hành trả đủ tiền thuê"); r+=2
ts.cell(r,1,"Độ nhạy (tính bằng model5.py, KHÔNG tự cập nhật khi sửa ô)").font=B; ts.cell(r,1).fill=SUB; r+=1
hdr(ts,r,["Kịch bản: lợi nhuận sau thuế cộng dồn 10 năm (tỷ)","PA3","PA4","Ghi chú"]); r+=1
SENS=[("Cơ sở (TB 59%)",P(),""),("Đầu trên (TB 65%)",P(occ=(0.85,0.65,0.45)),""),("Đầu dưới, giá -10% (TB 52,5%)",P(occ=(0.75,0.525,0.30),pm=0.9),""),
 ("Xấu (TB 44%, giá -10%)",P(occ=(0.65,0.42,0.25),pm=0.9),""),("ADR 900k cả năm",P(adr=(0.9,0.9,0.9)),""),("ADR 600k cả năm",P(adr=(0.6,0.6,0.6)),""),
 ("Thuê 75 triệu/căn",P(rent=300),""),("Thuê 70 triệu/căn",P(rent=280),""),("Thuê 60 triệu/căn",P(rent=240),""),
 ("PA4 thuê thêm Sales manager 30 triệu",P(bo4_ext=16+30*(1+P()['oncost'])+2),"Khi GM không kiêm được sales"),
 ("PA4 mức đạt năm 1-2 như PA3",P(ramp4=(0.82,1.0),tuition=0),"Đội tự làm lên nhanh như nhà vận hành")]
for nm,pp,nt in SENS:
    ts.cell(r,1,nm); ts.cell(r,4,nt)
    for c,pa in enumerate(('PA3','PA4')): ts.cell(r,2+c,round(run(pp,pa)['np10']/1000,1)).number_format="0.0"
    r+=1
wb.save("ruby-bai-kem-mo-hinh-ban-5.xlsx"); print("ok")
