import json
from collections import Counter
zt=json.load(open('marketdata/final_ZT_1020.json',encoding='utf-8'))['data']['pool']
def hh(x): return str(x['fbt']).zfill(6)[:2]
print('seal hour dist',Counter(hh(x) for x in zt).most_common())
print('zbc dist',Counter(x['zbc'] for x in zt).most_common())
print('early(<=10:00) n',sum(1 for x in zt if x['fbt']<=100000))
print()
print('CODE NAME LB PCT AMT TURN FLOAT SEAL BRK TIME 5D 10D DIST20H')
def bars(c):
    d=json.load(open('marketdata/tk2/%s.json'%c,encoding='utf-8'))
    k=list(d['data'].keys())[0]; return d['data'][k].get('qfqday') or d['data'][k].get('day')
for x in sorted(zt,key=lambda x:(-x['lbc'],x['fbt'])):
    b=bars(x['c']); m={r[0]:r for r in b}; r=m['2026-10-20']; i=b.index(r)
    cl=float(r[2]); cls=[float(q[2]) for q in b]
    g5=100*(cl/cls[i-5]-1); g10=100*(cl/cls[i-10]-1)
    hi20=max(float(q[3]) for q in b[i-19:i+1])
    print('%s %s %d %5.2f %5.1f %5.1f %5.0f %5.2f %d %s %+6.1f %+6.1f %+6.1f'%(x['c'],x['n'],x['lbc'],x['zdp'],x['amount']/1e8,x['hs'],x['ltsz']/1e8,x['fund']/1e8,x['zbc'],str(x['fbt']).zfill(6),g5,g10,100*(cl/hi20-1)))
