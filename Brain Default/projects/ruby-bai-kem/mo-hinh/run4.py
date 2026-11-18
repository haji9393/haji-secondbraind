import sys; sys.path.insert(0,'/tmp/ruby4')
exec(open('/tmp/ruby4/run3.py').read().split("B=mk(")[0])
p=mk((0.80,0.60,0.375),other=0.0); p['site_fix']=0.196
table("CO SO, bo DT khac, giu dinh phi",p)
for adr in [(0.9,0.9,0.9),(0.6,0.6,0.6)]:
    table(f"CO SO ADR {adr}",mk((0.80,0.60,0.375),adr=adr))
