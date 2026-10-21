import json,statistics
p=json.load(open('marketdata/pool_ZT_1019b.json',encoding='utf-8'))['data']['pool']
rets=[]
for x in p:
    try:
        d=json.load(open('marketdata/tk3/%s.json'%x['c'],encoding='utf-8'))
        k=list(d['data'].keys())[0]; b=d['data'][k].get('qfqday') or d['data'][k].get('day')
        m={r[0]:r for r in b}
        rets.append((float(m['2026-10-20'][2])/float(m['2026-10-19'][2])-1,x['n'],x['lbc']))
    except: pass
print('n',len(rets),'avg %.2f%% median %.2f%% pos %.1f%%'%(100*statistics.mean(r[0] for r in rets),100*statistics.median(r[0] for r in rets),100*sum(1 for r in rets if r[0]>0)/len(rets)))
for h in [1,2,3]:
    s=[r[0] for r in rets if r[2]==h]
    if s: print(' %d板 n%d avg%.2f%%'%(h,len(s),100*statistics.mean(s)))
print('worst');
for r in sorted(rets)[:5]: print(' %.2f%% %s %d板'%(100*r[0],r[1],r[2]))
