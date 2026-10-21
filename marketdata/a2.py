import json,statistics
zt=json.load(open('marketdata/final_ZT_1020.json',encoding='utf-8'))['data']['pool']
zt19=json.load(open('marketdata/pool_ZT_1019b.json',encoding='utf-8'))['data']['pool']
zt16=json.load(open('marketdata/pool_ZT_20261016.json',encoding='utf-8'))['data']['pool']
def bars(c):
    d=json.load(open('marketdata/tk2/%s.json'%c,encoding='utf-8'))
    k=list(d['data'].keys())[0]; return d['data'][k].get('qfqday') or d['data'][k].get('day')
c20={x['c'] for x in zt}; c19={x['c'] for x in zt19}; c16={x['c'] for x in zt16}
print('10/19 ZT',len(c19),'-> 10/20 continue',len(c19&c20),'rate %.1f%%'%(100*len(c19&c20)/len(c19)))
# premium of 10/19 ZT on 10/20
rets=[]
for x in zt19:
    try:
        b=bars(x['c']); m={r[0]:r for r in b}
        if '2026-10-19' in m and '2026-10-20' in m:
            rets.append(float(m['2026-10-20'][2])/float(m['2026-10-19'][2])-1)
    except: pass
print('10/19ZT premium on 10/20: avg %.2f%% median %.2f%% pos %.1f%% n=%d'%(100*statistics.mean(rets),100*statistics.median(rets),100*sum(1 for r in rets if r>0)/len(rets),len(rets)))
print()
print('CODE NAME LB PCT AMT TURN FLOAT SEAL VOLR G5 G10 DIST20H')
for x in sorted(zt,key=lambda x:(-x['lbc'],x['fbt'])):
    try:
        b=bars(x['c']); m={r[0]:r for r in b}; r=m['2026-10-20']; i=b.index(r)
        cl=float(r[2]); vols=[float(q[5]) for q in b]; cls=[float(q[2]) for q in b]
        volr=vols[i]/(sum(vols[i-5:i])/5)
        g5=100*(cl/cls[i-5]-1); g10=100*(cl/cls[i-10]-1)
        hi20=max(float(q[3]) for q in b[i-19:i+1])
        print('%s %s %d %.2f %.1f %.1f %.1f %.2f %.2f %.1f %.1f %.1f'%(x['c'],x['n'],x['lbc'],x['zdp'],x['amount']/1e8,x['hs'],x['ltsz']/1e8,x['fund']/1e8,volr,g5,g10,100*(cl/hi20-1)))
    except Exception as e: print(x['c'],x['n'],'ERR',e)
