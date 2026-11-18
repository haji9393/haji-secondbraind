import sys; sys.path.insert(0,'.')
from model5 import *
def occavg(o): return sum(o)/3
p=P(occ=(0.95,0.80,0.55)); v=run(p,'PA3')['years'][2]; print("calib R/thang",round(v['R']/12),"site%",round(100*v['site']/v['R'],1))
SC={'Co so (TB 59%)':P(),'Dau tren (TB 65%)':P(occ=(0.85,0.65,0.45)),
    'Dau duoi, gia -10% (TB 52.5%)':P(occ=(0.75,0.525,0.30),pm=0.9),'Xau (TB 44%, gia -10%)':P(occ=(0.65,0.42,0.25),pm=0.9),
    'ADR 900k ca nam':P(adr=(0.9,0.9,0.9)),'ADR 600k ca nam':P(adr=(0.6,0.6,0.6))}
for k,p in SC.items():
    out=[]
    for pa in ('PA3','PA4'):
        r=run(p,pa); y=r['years']
        out.append("%s: R3/th %4.0f site3 %2.0f%% LN3/th %5.0f LN10/th %5.0f LN10nam %6.0f quy %5.0f"%(pa,y[2]['R']/12,100*y[2]['site']/y[2]['R'],y[2]['np']/12,y[9]['np']/12,r['np10'],r['need']))
    print(k); [print("  ",o) for o in out]
# suc tra tien thue: muc thue/can de LN 10 nam = 0 (sau thue) va de LN = 10% DT
def solve(f,lo,hi):
    for _ in range(50):
        m=(lo+hi)/2
        if f(m)>0: lo=m
        else: hi=m
    return m
for pa in ('PA3','PA4'):
    b=solve(lambda x: run(P(rent=x*4),pa)['np10'],0,150)
    o=solve(lambda k: -run(P(occ=(0.80*k,0.60*k,0.375*k)),pa)['np10'],0.5,2.0)
    a=solve(lambda k: -run(P(adr=(0.9*k,0.75*k,0.6*k)),pa)['np10'],0.5,2.0)
    print(pa,"thue/can hoa von 10 nam %.1f tr"%b,"| cong suat TB can %.1f%%"%(100*o*occavg((0.80,0.60,0.375))),"| ADR TB can %.0fk"%(1000*a*0.75))
for rent in (85,75,70,60):
    print("rent",rent,[ (pa,round(run(P(rent=rent*4),pa)['np10']/1000,2), round(run(P(rent=rent*4),pa)['years'][2]['np']/12)) for pa in ('PA3','PA4')])
