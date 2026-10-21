import json,glob,statistics
from collections import Counter,defaultdict
rows={}
for fp in sorted(glob.glob('marketdata/live_pages/*.json')):
    try: d=json.load(open(fp,encoding='utf-8'))['data']
    except: continue
    if not d or not d.get('diff'): continue
    for x in d['diff']:
        if isinstance(x.get('f2'),(int,float)) and isinstance(x.get('f3'),(int,float)):
            rows[x['f12']]=x
print('valid',len(rows))
def lim(code,name):
    if 'ST' in name.upper(): return 5.0
    if code.startswith(('300','301','688')): return 20.0
    return 10.0
up=sum(1 for x in rows.values() if x['f3']>0); dn=sum(1 for x in rows.values() if x['f3']<0); fl=len(rows)-up-dn
zt=[];dt=[]
for x in rows.values():
    L=lim(x['f12'],x['f14'])
    if x['f3']>=L-0.3: zt.append(x)
    if x['f3']<=-(L-0.3): dt.append(x)
print('up',up,'down',dn,'flat',fl,'up%% %.1f'%(100*up/len(rows)))
print('zt',len(zt),'dt',len(dt))
buckets=[(-100,-9),(-9,-7),(-7,-5),(-5,-3),(-3,-1),(-1,0),(0,1),(1,3),(3,5),(5,7),(7,9),(9,100)]
for a,b in buckets:
    c=sum(1 for x in rows.values() if a<=x['f3']<b)
    print('%d~%d: %d'%(a,b,c))
print('--- top amount')
for x in sorted(rows.values(),key=lambda x:-x['f6'])[:15]:
    print(x['f12'],x['f14'],'%.2f%%'%x['f3'],'%.1f亿'%(x['f6']/1e8),'turn%.1f%%'%x['f8'],x['f100'])
print('--- top gainers non-zt')
for x in sorted(rows.values(),key=lambda x:-x['f3'])[:20]:
    print(x['f12'],x['f14'],'%.2f%%'%x['f3'],'%.1f亿'%(x['f6']/1e8),'turn%.1f%%'%x['f8'],'volr',x['f10'],x['f100'])
print('--- industry breadth')
ind=defaultdict(list); amt=defaultdict(float); ztc=Counter()
for x in rows.values():
    ind[x['f100']].append(x['f3']); amt[x['f100']]+=x['f6']
for k,v in ind.items():
    if len(v)>=5: ztc[k]=sum(1 for x in rows.values() if x['f100']==k and x['f3']>=lim(x['f12'],x['f14'])-0.3)
for k,v in sorted(ind.items(),key=lambda kv:-statistics.mean(kv[1]))[:15]:
    print(k,'n%d avg%.2f%% med%.2f%% zt%d amt%.0f亿'%(len(v),statistics.mean(v),statistics.median(v),ztc[k],amt[k]/1e8))
