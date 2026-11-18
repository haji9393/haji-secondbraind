import sys; sys.path.insert(0,'/tmp/ruby4')
exec(open('/tmp/ruby4/run3.py').read().split("B=mk(")[0])
O=0.0; F=0.30; FB=0.24
B=mk((0.80,0.60,0.375),other=O,fin=F); table("CO SO",B)
table("DAU TREN",mk((0.85,0.65,0.45),other=O,fin=F))
table("DAU DUOI -10%",mk((0.75,0.525,0.30),other=O,fin=FB,pm=0.9,delay=3,capex=28,vac1=12,vac2=12))
table("XAU 44%",mk((0.65,0.42,0.25),other=O,fin=FB,pm=0.9,delay=3,capex=28,vac1=12,vac2=12))
for adr in [(0.9,0.9,0.9),(0.6,0.6,0.6)]: table(f"ADR {adr}",mk((0.80,0.60,0.375),adr=adr,other=O,fin=F))
table("cap rate 10%",mk((0.80,0.60,0.375),other=O,fin=F,cap=0.10))
d=run(B,'PA4')['detail'][24:36]; print("PA4 bonus/nam %.2f"%sum(x['bon'] for x in d))
print("PA3-PA4 khong bonus, ramp nhu PA3:",round(run(mk((0.80,0.60,0.375),other=O,fin=F,bonus4=0,ramp4=[0.82],tuition=0),'PA4')['total']*.75,1))
print("PA4 khong bonus:",round(run(mk((0.80,0.60,0.375),other=O,fin=F,bonus4=0),'PA4')['total']*.75,1))
# min cumulative buffer needed for PA4 from opening (worst cumulative dip after opening), owner share
for nm,p in [("co so",B),("dau duoi",mk((0.75,0.525,0.30),other=O,fin=FB,pm=0.9,delay=3,capex=28,vac1=12,vac2=12))]:
  for w in ('PA3','PA4'):
    r=run(p,w); cf=r['cf']; om=13+p['delay']; s=0; mn=0
    for t in range(om,om+24): s+=cf[t] - (p['capex']/11 if t==om+11 else 0); mn=min(mn,s)
    print(nm,w,"dip luy ke 24 thang dau (truoc hoan VAT) %.2f ty"%(mn*.75))
