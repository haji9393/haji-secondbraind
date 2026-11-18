import sys; sys.path.insert(0,'/tmp/ruby4')
from model import *
S=0.75
def table(title,p):
    print("\n==",title,"bank",round(run(p,'PA1')['bank']*S,1))
    for w in PLANS:
        r=run(p,w)
        print(f"{w:8} TOTAL {r['total']*S:5.1f} noup {r['noup']*S:5.1f} endc {r['endcost']*S:4.1f} up {r['up']*S:4.1f} | y1 {r['m1']*S:4.0f} (lo {r['m1lo']*S:4.0f}) y3 {r['m3']*S:4.0f} [lai {r['int3']*S:3.0f}] lo {r['m3lo']*S:4.0f} hi {r['m3hi']*S:4.0f} y10 {r['m10']*S:4.0f} | pb {r['pb']}")
B=P(); X45=P(occ=0.45,pm=0.9,delay=3,capex=28,vac1=12,vac2=12,fin=0.28); X40=dict(X45,occ=0.40)
table("CO SO 65%",B); table("XAU 45%",X45); table("XAU 40%",X40)
table("CO SO, site theo ban 2 (~50% DT)",P(site_fix=0.34))
table("CO SO, PA4 khong tra 20% cho GD",P(bonus4=0))
table("CO SO, PA4 ramp giong PA3",P(ramp4=[0.82],tuition=0))
for o in (0.55,0.60,0.70,0.75):
    q=P(occ=o); print(o, {w:round(run(q,w)['total']*S,1) for w in PLANS})
