import json, statistics
def load(code): return json.load(open('marketdata/tkline/%s.json'%code,encoding='utf-8'))
def bars(d):
    k=list(d['data'].keys())[0]
    v=d['data'][k]
    return v.get('qfqday') or v.get('day')
def get(code):
    d=load(code); b=bars(d)
    return d,b
zt=json.load(open('marketdata/pool_ZT_1019.json',encoding='utf-8'))['data']['pool']
zt16=json.load(open('marketdata/pool_ZT_20261016.json',encoding='utf-8'))['data']['pool']
zt15=json.load(open('marketdata/pool_ZT_20261015.json',encoding='utf-8'))['data']['pool']
zb=json.load(open('marketdata/pool_ZB_1019.json',encoding='utf-8'))['data']['pool']
# advance rates
c19={x['c'] for x in zt}; c16={x['c'] for x in zt16}; c15={x['c'] for x in zt15}
print('10/16 ZT',len(c16),'-> 10/19 continued',len(c16&c19),'rate %.1f%%'%(100*len(c16&c19)/len(c16)))
print('10/15 ZT',len(c15),'-> 10/16 continued',len(c15&c16),'rate %.1f%%'%(100*len(c15&c16)/len(c15)))
# premium for 10/16 ZT on 10/19
rets=[]
for x in zt16:
    try:
        d,b=get(x['c'])
        # find 10/16 close and 10/19 close
        m={r[0]:r for r in b}
        if '2026-10-16' in m and '2026-10-19' in m:
            rets.append(float(m['2026-10-19'][2])/float(m['2026-10-16'][2])-1)
    except: pass
print('yesterday ZT premium avg %.2f%% median %.2f%% n=%d'%(100*statistics.mean(rets),100*statistics.median(rets),len(rets)))
print('positive %.1f%%'%(100*sum(1 for r in rets if r>0)/len(rets)))
# index MAs
for name,code in [('上证','idx_000001'),('深成','idx_399001'),('创业板','idx_399006'),('科创50','idx_000688'),('中证500','idx_399905')]:
    d=json.load(open('marketdata/tkline/%s.json'%code,encoding='utf-8'))
    b=bars(d); c=[float(r[2]) for r in b]
    print(name,b[-1][0],c[-1],'MA5 %.2f MA10 %.2f MA20 %.2f'%(sum(c[-5:])/5,sum(c[-10:])/10,sum(c[-20:])/20),'chg5 %.2f%%'%(100*(c[-1]/c[-6]-1)))
print('\nCODE NAME LB CLOSE PCT AMT(亿) TURN% FLOAT(亿) SEAL(亿) FBT ZBC TYPE VOLR G5% G10% DIST20H%')
for x in sorted(zt,key=lambda x:(-x['lbc'],x['fbt'])):
    try:
        d,b=get(x['c']); m={r[0]:r for r in b}; r=m['2026-10-19']
        o,cl,h,l=float(r[1]),float(r[2]),float(r[3]),float(r[4])
        vols=[float(q[5]) for q in b]; cl_all=[float(q[2]) for q in b]
        i=b.index(r)
        volr=vols[i]/(sum(vols[i-5:i])/5)
        typ='一字' if o==cl==h==l else ('T字' if o==cl else '换手')
        g5=100*(cl/cl_all[i-5]-1); g10=100*(cl/cl_all[i-10]-1)
        hi20=max(float(q[3]) for q in b[i-19:i+1]); dh=100*(cl/hi20-1)
        print('%s %s %d %.2f %.2f %.1f %.1f %.1f %.2f %s %d %s %.1f %.1f %.1f %.1f'%(x['c'],x['n'],x['lbc'],cl,x['zdp'],x['amount']/1e8,x['hs'],x['ltsz']/1e8,x['fund']/1e8,str(x['fbt']).zfill(6),x['zbc'],typ,volr,g5,g10,dh))
    except Exception as e: print(x['c'],x['n'],'ERR',e)
