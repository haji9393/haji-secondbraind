# Ruby Bai Kem - mo hinh theo thang, ban 4 (Javis, 18/11/2026). Don vi: ty dong. 100% 4 can.
SEAS=[1.30,1.30,1.10,1.00,0.90,1.00,1.10,1.00,0.90,0.73,0.90,1.10]; SAVG=sum(SEAS)/12
PRICE=[1.25,1.25,1.25,1.0,0.8,0.8,1.0,1.0,0.8,0.8,1.0,1.25]  # trieu/dem gom VAT
DAYS=[31,28,31,30,31,30,31,31,30,31,30,31]
ROOMS=53; OTHER=0.1982 # trieu/dem phong ban
N=132; START_CAL=10  # thang 1 cua mo hinh = 11/2026 (index lich 10)
r_m=1.065**(1/12)-1
def cal(t): return (START_CAL+t-1)%12
def yr(t): return (t-1)//12   # 0 = nam thi cong
def P(**kw):
    p=dict(occ=0.65,pm=1.0,delay=0,capex=27.04,pocket=30.0,
      raw=0.140,fin=0.350,vac1=6,vac2=6,
      demo=0.325e-3*2100,repair=2.5e-3*2100,        # PA1 cuoi ky (gia hom nay)
      refurb=0.15, cap=0.08, cond=0.70,
      site_fix=0.218, site_var=0.17,                  # site 38% DT o 65%
      bo3=0.12, consult=5000*26400/1e9, preopen=0.72,
      bo4_fix=0.095, bo4_var=0.03, advisor=0.18, tuition=0.30,
      ramp3=[0.82], ramp4=[0.70,0.90], bonus4=0.20, ffe=0.03, cit=0.17, div=0.05)
    p.update(kw); return p
SEASON=[0,0,0,1,2,2,1,1,2,2,1,0]  # 0 cao (12-3), 1 vua (4,7,8,11), 2 thap (5,6,9,10)
def hotel_rev(p,t,open_m,ramp):
    if 'occs' in p: return hotel_rev2(p,t,open_m,ramp)
    return hotel_rev1(p,t,open_m,ramp)
def hotel_rev2(p,t,open_m,ramp):
    if t<open_m: return 0.0
    k=(t-open_m)//12; f=ramp[k] if k<len(ramp) else 1.0
    c=cal(t); se=SEASON[c]; occ=min(0.95,p['occs'][se]*f)
    nights=ROOMS*DAYS[c]*occ; idx=1.04**max(0,yr(t)-1)
    room=nights*p['adr'][se]*p['pm']/1000   # ADR thuan (da tru VAT, OTA)
    oth=nights*p['other']*p['pm']/1000
    return (room+oth)*idx
def hotel_rev1(p,t,open_m,ramp):
    if t<open_m: return 0.0
    k=(t-open_m)//12; f=ramp[k] if k<len(ramp) else 1.0
    c=cal(t); occ=min(0.95,p['occ']*SEAS[c]/SAVG*f)
    nights=ROOMS*DAYS[c]*occ; idx=1.04**max(0,yr(t)-1)
    room=nights*PRICE[c]*p['pm']/1.1*(1-0.155)/1000
    oth=nights*OTHER*p['pm']/1000
    return (room+oth)*idx
def run(p,which):
    infl=lambda t:1.04**max(0,yr(t)-1); sinf=lambda t:1.07**max(0,yr(t)-1)
    open_m=13+p['delay']; cf=[0.0]*(N+1); cf[0]=0
    endval=0; endcost=0; detail=[]
    if which=='PA1':
        # cho thue tho: vac1 thang dau (tim khach + mien phi fit-out), vac2 thang o nam 5 (doi khach)
        for t in range(1,N+1):
            vac = t<=p['vac1'] or (60<t<=60+p['vac2'])
            rent=0 if vac else p['raw']*1.04**(t//12)
            cf[t]=rent*0.9+ (0.025/12 if rent else 0); detail.append(rent)
        endcost=(p['demo']+p['repair'])*1.05**11
    elif which=='PA2':
        cf[1]-=p['capex']
        for t in range(1,N+1):
            vac = t<open_m+p['vac1'] or (open_m+48<=t<open_m+48+p['vac2'])
            rent=0 if vac else p['fin']*1.04**max(0,yr(t)-1)
            cf[t]+=rent*0.9+(0.025/12 if rent else 0); detail.append(rent)
        endcost=p['refurb']*p['capex']*1.05**10
    else:
        pa3 = which.startswith('PA3'); switch = which=='PA3>PA4'
        ramp = p['ramp3']
        cf[1]-=p['capex']+p['preopen']+(p['consult'] if pa3 else p['advisor']+p['consult']*0)
        if not pa3: ramp=p['ramp4']
        dep=p['capex']/1.1/15/12; year_tax={}
        for t in range(1,N+1):
            R=hotel_rev(p,t,open_m,ramp)
            if R==0: continue
            site=(p['site_fix']*sinf(t)+p['site_var']*R)
            gop=R-site
            m_op = (t-open_m)//12  # nam van hanh 0..
            self_run = (not pa3) or (switch and m_op>=3)
            if self_run:
                bo=p['bo4_fix']*sinf(t)+p['bo4_var']*R
                if switch and m_op==3 and (t-open_m)%12==0: bo+= p['tuition']  # chuyen giao
                if not pa3 and m_op==0: bo+=p['tuition']/12
                gop2=gop-bo; inc=0
                bon=p['bonus4']*max(0,gop2-p['ffe']*R-p['fin']*1.04**max(0,yr(t)-1))
            else:
                bo=p['bo3']*R; gop2=gop-bo
                mg=gop2/R
                rate=0.04 if mg>=0.50 else 0.03 if mg>=0.45 else 0.02 if mg>=0.40 else 0.0
                inc=rate*max(0,gop2); bon=0
            pre=gop2-inc-bon-p['ffe']*R
            taxable=max(0,pre-dep); tax=p['cit']*taxable; d=p['div']*max(0,pre-tax)
            cf[t]+=pre-tax-d + (p['capex']/11 if t==open_m+11 else 0)
            detail.append(dict(t=t,R=R,site=site,bo=bo,inc=inc,bon=bon,pre=pre))
        # tien du tru: 6 thang dinh phi phai co san (chi tinh vao 'tien can co')
    up = 0 if which=='PA1' else (p['fin']*1.04**9*12 - p['raw']*1.04**10*12)/p['cap']*p['cond']
    # so du ngan hang
    bal=p['pocket']; minbal=bal; series=[]; inc_m=[0.0]*(N+1)
    for t in range(1,N+1):
        inc_m[t]=bal*r_m; bal=bal+inc_m[t]+cf[t]; minbal=min(minbal,bal); series.append(bal)
    bank=p['pocket']*(1+r_m)**N
    total=bal-endcost+up
    # tien ve thang: binh quan nam van hanh 3 va 10, thang thap nhat/cao nhat nam 3
    tot=[cf[t]+inc_m[t] for t in range(N+1)]
    y3=tot[open_m+24:open_m+36]; y10=tot[N-11:N+1]; y1=tot[open_m:open_m+12]
    cum=-0.0; pb=None; s=0
    for t in range(1,N+1):
        s+=cf[t]
        if pb is None and t>open_m and s>=0 and which!='PA1': pb=(t-open_m)//12+1
    return dict(cash=bal,endcost=endcost,up=up,total=total,noup=bal-endcost,bank=bank,
        m3=sum(y3)/12*1000, m3lo=min(y3)*1000, m3hi=max(y3)*1000, m10=sum(y10)/12*1000, m1=sum(y1)/12*1000, m1lo=min(y1)*1000, int3=sum(inc_m[open_m+24:open_m+36])/12*1000,
        minbal=minbal,pb=pb,cf=cf,detail=detail,series=series)
PLANS=['PA1','PA2','PA3','PA4','PA3>PA4']
