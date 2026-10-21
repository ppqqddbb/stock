import json
zt=json.load(open('marketdata/final_ZT_1020.json',encoding='utf-8'))['data']['pool']
def bars(c):
    d=json.load(open('marketdata/tk2/%s.json'%c,encoding='utf-8'))
    k=list(d['data'].keys())[0]; return d['data'][k].get('qfqday') or d['data'][k].get('day')
out=[]
for x in zt:
    try:
        b=bars(x['c']); m={r[0]:r for r in b}; r=m['2026-10-20']; i=b.index(r)
        cl=float(r[2]); cls=[float(q[2]) for q in b]
        if i<21: continue
        g5=100*(cl/cls[i-5]-1); g10=100*(cl/cls[i-10]-1)
        hi20=max(float(q[3]) for q in b[i-19:i+1])
        out.append((x['lbc'],x['fbt'],x['c'],x['n'],x['zdp'],x['amount']/1e8,x['hs'],x['ltsz']/1e8,x['fund']/1e8,x['zbc'],g5,g10,100*(cl/hi20-1),x['hybk']))
    except Exception as e: print('ERR',x['c'],e)
for o in sorted(out,key=lambda o:(-o[0],o[1])):
    print('%d %s %s %-6s %5.2f %5.1f %5.1f %5.0f %5.2f %2d %+6.1f %+6.1f %+6.1f %s'%(o[0],str(o[1]).zfill(6),o[2],o[3],o[4],o[5],o[6],o[7],o[8],o[9],o[10],o[11],o[12],o[13]))
