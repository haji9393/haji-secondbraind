import formulas, sys, warnings; warnings.filterwarnings("ignore")
sys.path.insert(0,'.'); from model5 import *
xl=formulas.ExcelModel().loads("ruby-bai-kem-mo-hinh-ban-5.xlsx").finish(); sol=xl.calculate()
def g(sheet,cell):
    for k,v in sol.items():
        if k.upper().endswith(f"{sheet.upper()}'!{cell}"): return v.value[0][0]
for r in range(5,19): print(g("TÓM TẮT",f"A{r}") if False else r, g("TÓM TẮT",f"B{r}"), g("TÓM TẮT",f"C{r}"))
p=P()
for pa in ('PA3','PA4'):
    x=run(p,pa); y=x['years']; print(pa,"py: R3/th",round(y[2]['R']/12,1),"site3",round(y[2]['site']/y[2]['R'],4),"NP1/th",round(y[0]['np']/12,1),"NP3/th",round(y[2]['np']/12,1),"NP10/th",round(y[9]['np']/12,1),"np10",round(x['np10'],1),"need",round(x['need'],1),"min y1",round(min(r['gop']-r['rent']-r['ffe'] for r in x['rows'][:12]),1))
