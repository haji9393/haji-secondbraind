import sys,json; sys.path.insert(0,'/tmp/ruby4')
exec(open('/tmp/ruby4/run3.py').read().split("B=mk(")[0])
O=0.0;F=0.30
B=mk((0.80,0.60,0.375),other=O,fin=F)
out={}
# monthly cash avg per operating year (owner, tr), incl interest
for w in PLANS:
    r=run(B,w); cf=r['cf']; bal=B['pocket']; tot=[0]
    for t in range(1,N+1):
        i=bal*r_m; bal+=i+cf[t]; tot.append(cf[t]+i)
    om=13; yrs=[round(sum(tot[om+12*k:om+12*k+12])/12*1000*S) for k in range(10)]
    yrs_novat=[round((sum(tot[om+12*k:om+12*k+12]) - (B['capex']/11 if k==0 and w not in('PA1','PA2') else 0))/12*1000*S) for k in range(10)]
    out[w]=dict(yrs=yrs,yrs_novat=yrs_novat,total=round(r['total']*S,1),noup=round(r['noup']*S,1),up=round(r['up']*S,1),endcost=round(r['endcost']*S,1),pb=r['pb'],cash=round(r['cash']*S,1))
    # year3 monthly profile
    out[w]['y3m']=[round(tot[t]*1000*S) for t in range(om+24,om+36)]
    out[w]['y1m']=[round((tot[t]-(B['capex']/11 if t==om+11 and w not in('PA1','PA2') else 0))*1000*S) for t in range(om,om+12)]
print(json.dumps(out))
# cost structure year 3 PA3 PA4 (100%, tr/thang)
for w in ('PA3','PA4'):
    d=run(B,w)['detail'][24:36]; R=sum(x['R'] for x in d)
    k=lambda f: round(sum(x[f] for x in d)/12*1000)
    ffe=round(0.03*R/12*1000)
    print(w,"R",round(R/12*1000),"site",k('site'),"bo",k('bo'),"inc",k('inc'),"bon",k('bon'),"ffe",ffe,"pre",k('pre'))
# 10-yr fees
for w in ('PA3','PA4'):
    d=run(B,w)['detail']; print(w,"10y bo+inc+bon (100%)",round(sum(x['bo']+x['inc']+x['bon'] for x in d),2),"R10y",round(sum(x['R'] for x in d),1))
# thresholds by occ scale
def tot(k,w,**kw):
    o=(0.80*k,0.60*k,0.375*k); return run(mk(o,other=O,fin=F,**kw),w)['total']*S
pa2=tot(1,'PA2'); pa1=tot(1,'PA1'); bank=run(B,'PA1')['bank']*S
def solve(w,target):
    lo,hi=0.5,1.4
    for _ in range(40):
        m=(lo+hi)/2
        if tot(m,w)<target: lo=m
        else: hi=m
    return round(100*m*occavg((0.80,0.60,0.375)),1)
for w in ('PA3','PA4'):
    print(w,"occ hoa PA2",solve(w,pa2),"hoa PA1",solve(w,pa1),"hoa bank",solve(w,bank))
# ADR thresholds: uniform scale of adr
def tadr(k,w): return run(mk((0.80,0.60,0.375),adr=(0.9*k,0.75*k,0.6*k),other=O,fin=F),w)['total']*S
for w in ('PA3','PA4'):
    lo,hi=0.5,1.5
    for _ in range(40):
        m=(lo+hi)/2
        if tadr(m,w)<pa1: lo=m
        else: hi=m
    print(w,"ADR TB hoa PA1 (tr)",round(m*(0.9+0.75+0.6)/3,3))
# sensitivity tornado on PA3, PA4 base
base={w:tot(1,w) for w in ('PA3','PA4')}
tests={'Cong suat -10%':dict(k=0.9),'Cong suat +10%':dict(k=1.1),'ADR -10%':dict(pm=0.9),'ADR +10%':dict(pm=1.1),'Von xay 28 ty':dict(capex=28),'Khai truong tre 3 thang':dict(delay=3),'Site cost +10%':dict(site=1.1),'Khong tinh gia tri nha':dict(cap=1e9)}
for nm,t in tests.items():
    row=[]
    for w in ('PA3','PA4'):
        kw=dict(t); k=kw.pop('k',1); sc=kw.pop('site',None)
        p=mk((0.80*k,0.60*k,0.375*k),other=O,fin=F,**kw)
        if sc: p['site_fix']*=sc; p['site_var']*=sc
        row.append(round(run(p,w)['total']*S-base[w],1))
    print("SENS",nm,row)
# PA4 with second property effect: back office fix shared 50% 
print("PA4 bo_fix chia doi (toa 2):",round(tot(1,'PA4',bo4_fix=0.0475),1))
print("PA4 GM bonus 10%:",round(tot(1,'PA4',bonus4=0.10),1))
print("PA4 ramp nhu PA3:",round(tot(1,'PA4',ramp4=[0.82]),1))
print("PA3 bo 15%:",round(tot(1,'PA3',bo3=0.15),1),"PA3 bo 10%:",round(tot(1,'PA3',bo3=0.10),1))
