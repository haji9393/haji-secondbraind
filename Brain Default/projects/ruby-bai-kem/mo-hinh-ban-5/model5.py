# Ruby Bai Kem - ban 5 (18/11/2026): OpCo khach san thue 4 can (R201,R203,R205,R207), PA3 vs PA4.
# Don vi: trieu dong. Thang van hanh 1 = 11/2027.
DAYS=[31,28,31,30,31,30,31,31,30,31,30,31]
SEASON=[0,0,0,1,2,2,1,1,2,2,1,0]      # 0 cao (12-3), 1 vua (4,7,8,11), 2 thap (5,6,9,10)
START=10                               # thang 11
# ---- bang nhan su site (giong nhau PA3, PA4): (vi tri, so nguoi, luong gross tr/thang, ho tro o+an)
SITE_STAFF=[("Tong quan ly (GM) - Haji",1,50,0),("Truong le tan kiem dat phong",1,13,2),
 ("Le tan 3 ca (ca dem kiem truc dem)",3,8.5,2),("Giam sat buong",1,10,2),("Nhan vien buong phong",4,7.5,2),
 ("Ky thuat kiem bao tri",1,10,2),("Bao ve dem kiem tap vu sanh",1,7,2)]
BO4_STAFF=[("Ke toan noi bo kiem thu ngan, nhan su",1,13,2),("Dat phong, OTA va marketing so",1,15,2)]
def staff_cost(lst,oncost):  # oncost: BHXH 21.5% tren 80% luong + thang 13
    return sum(n*(w*(1+oncost)+h) for _,n,w,h in lst)
def P(**kw):
    p=dict(rooms=53, occ=(0.80,0.60,0.375), adr=(0.90,0.75,0.60), pm=1.0, price_g=0.04,
      ramp3=(0.82,1.0), ramp4=(0.70,0.90),
      oncost=0.215*0.8+1/12, sal_g=0.05, fix_g=0.04,
      seasonal=2, seasonal_w=9,          # buong thoi vu thang cao diem
      var_orn=0.075,                     # giat la 28k + amenities 17k + dien nuoc bien doi 30k / dem phong
      var_pct=0.020,                     # sua chua nho 1% + phi thanh toan, linh tinh 1%
      site_fix=40,                       # dien nuoc nen 20 + phi khu, bao hiem, giay phep 10 + thang may, PCCC, internet 10
      rent=85*4, rent_step=0.05, rent_every=3,
      ffe=0.03,
      bo3=0.12, tiers=((0.50,0.04),(0.45,0.03),(0.40,0.02)),
      bo4_ext=16,                        # dich vu ke toan thue, kiem toan 7 + phan mem PMS/channel/booking/ke toan 9
      bo4_var=0.03,                      # marketing 2% + tuyen dung dao tao 1%
      tuition=300, bonus4=0.20,
      pre3=720+132, pre4=720+180,        # truoc khai truong + tu van 5.000 USD (PA3) / co van van hanh (PA4)
      cit=0.17)
    p.update(kw); return p
def run(p,pa):
    st=staff_cost(SITE_STAFF,p['oncost']); bo4s=staff_cost(BO4_STAFF,p['oncost'])
    ramp=p['ramp3'] if pa=='PA3' else p['ramp4']
    rows=[]
    for m in range(1,121):
        y=(m-1)//12; c=(START+m-1)%12; se=SEASON[c]
        f=ramp[y] if y<len(ramp) else 1.0
        occ=min(0.95,p['occ'][se]*f); orn=p['rooms']*DAYS[c]*occ
        R=orn*p['adr'][se]*1000*p['pm']*(1+p['price_g'])**y/1000
        sal=(1+p['sal_g'])**y; fx=(1+p['fix_g'])**y
        staff=st*sal + (p['seasonal']*(p['seasonal_w']*(1+p['oncost'])) *sal if se==0 else 0)
        var=orn*p['var_orn']*fx + p['var_pct']*R
        site=staff+var+p['site_fix']*fx
        if pa=='PA3': bo=p['bo3']*R
        else: bo=bo4s*sal+p['bo4_ext']*fx+p['bo4_var']*R+(p['tuition']/12 if y==0 else 0)
        rent=p['rent']*(1+p['rent_step'])**(y//p['rent_every'])
        ffe=p['ffe']*R
        rows.append(dict(m=m,y=y,c=c,occ=occ,orn=orn,R=R,staff=staff,var=var,sitefix=p['site_fix']*fx,site=site,bo=bo,gop=R-site-bo,rent=rent,ffe=ffe))
    # nam: incentive PA3 theo bien GOP nam; thuong GM PA4 20% loi nhuan sau thue nha (truoc thuong)
    years=[]; cum=0
    for y in range(10):
        r=[x for x in rows if x['y']==y]; R=sum(x['R'] for x in r); gop=sum(x['gop'] for x in r)
        rent=sum(x['rent'] for x in r); ffe=sum(x['ffe'] for x in r)
        inc=0; bon=0
        if pa=='PA3':
            mg=gop/R; rate=next((t for th,t in p['tiers'] if mg>=th),0); inc=rate*max(0,gop)
        pre_b=gop-rent-ffe-inc
        if pa=='PA4': bon=p['bonus4']*max(0,pre_b)
        pbt=pre_b-bon
        tax=p['cit']*max(0,min(pbt,cum+pbt)); cum+=pbt
        years.append(dict(y=y+1,R=R,orn=sum(x['orn'] for x in r),staff=sum(x['staff'] for x in r),var=sum(x['var'] for x in r),
          sitefix=sum(x['sitefix'] for x in r),site=sum(x['site'] for x in r),bo=sum(x['bo'] for x in r),gop=gop,rent=rent,ffe=ffe,inc=inc,bon=bon,pbt=pbt,tax=tax,np=pbt-tax))
    pre=p['pre3'] if pa=='PA3' else p['pre4']
    # quy dem: lo luy ke lon nhat theo thang (truoc thue, chua tinh incentive/thuong nam)
    s=-pre; mn=s
    for x in rows:
        s+=x['gop']-x['rent']-x['ffe']; mn=min(mn,s)
    return dict(rows=rows,years=years,pre=pre,need=-mn,np10=sum(v['np'] for v in years)-pre,staff_m=st,bo4_m=bo4s)
if __name__=='__main__':
    p=P()
    for pa in ('PA3','PA4'):
        r=run(p,pa); print("\n",pa,"site staff/thang",round(r['staff_m'],1),"BO4 staff",round(r['bo4_m'],1),"quy can",round(r['need']),"LN rong 10 nam",round(r['np10']))
        for v in r['years']:
            print(" Y%d R %5.0f site %4.0f%% bo %4.1f%% GOP %5.0f (%2.0f%%) rent %5.0f inc %3.0f bon %3.0f PBT %6.0f NP %6.0f /thang %5.0f"%(v['y'],v['R'],100*v['site']/v['R'],100*v['bo']/v['R'],v['gop'],100*v['gop']/v['R'],v['rent'],v['inc'],v['bon'],v['pbt'],v['np'],v['np']/12))
