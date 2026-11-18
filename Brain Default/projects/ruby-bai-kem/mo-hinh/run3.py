import sys; sys.path.insert(0,'/tmp/ruby4')
from model import *
S=0.75
def avgR(p):  # doanh thu thuan binh quan thang, nam on dinh gia nam 1
    q=dict(p); 
    return sum(hotel_rev2(q,t,13,[1.0]) for t in range(13,25))/12
def mk(occs,adr=(0.9,0.75,0.6),other=0.1982,**kw):
    p=P(occs=occs,adr=adr,other=other,**kw)
    base=P(occs=(0.80,0.60,0.375),adr=(0.9,0.75,0.6),other=other)
    R=avgR(base); p['site_fix']=0.55*0.38*R; p['site_var']=0.45*0.38
    return p
def occavg(o): return (4*o[0]+4*o[1]+4*o[2])/12
def table(title,p):
    print("\n==",title,"occ TB %.1f%%"%(100*occavg(p['occs'])),"DT thuan/thang %.0ftr"%(avgR(p)*1000),"site_fix %.0f"%(p['site_fix']*1000),"bank",round(run(p,'PA1')['bank']*S,1))
    for w in PLANS:
        r=run(p,w)
        print(f"{w:8} TOTAL {r['total']*S:5.1f} noup {r['noup']*S:5.1f} up {r['up']*S:4.1f} | y1 {r['m1']*S:4.0f} lo {r['m1lo']*S:4.0f} y3 {r['m3']*S:4.0f} lo {r['m3lo']*S:4.0f} hi {r['m3hi']*S:4.0f} y10 {r['m10']*S:4.0f} | pb {r['pb']} minbal {r['minbal']:.1f}")
B=mk((0.80,0.60,0.375)); table("CO SO (giua khoang)",B)
G=mk((0.85,0.65,0.45)); table("TOT (dau tren)",G)
T=mk((0.75,0.525,0.30),pm=0.9,delay=3,capex=28,vac1=12,vac2=12,fin=0.28); table("THAN TRONG (dau duoi, gia -10%)",T)
X=mk((0.65,0.42,0.25),pm=0.9,delay=3,capex=28,vac1=12,vac2=12,fin=0.28); table("XAU ~44%",X)
table("CO SO, bo doanh thu khac",mk((0.80,0.60,0.375),other=0.0))
table("CO SO, bo doanh thu khac, PA2 thue 350",mk((0.80,0.60,0.375),other=0.0))
# PA3 cost check year3
r=run(B,'PA3'); d=r['detail'][24:36]; R=sum(x['R'] for x in d)
print("PA3 y3 site %.1f%% bo %.1f%% inc %.2f%% pre %.1f%% R/thang %.0f"%(100*sum(x['site'] for x in d)/R,100*sum(x['bo'] for x in d)/R,100*sum(x['inc'] for x in d)/R,100*sum(x['pre'] for x in d)/R,R/12*1000))
lo=[x for x in d if SEASON[cal(x['t'])]==2]; print("thang thap diem PA3 site%%: %.0f"%(100*sum(x['site'] for x in lo)/sum(x['R'] for x in lo)))
