import json, urllib.request, time, os
from concurrent.futures import ThreadPoolExecutor
H={'User-Agent':'Mozilla/5.0','Referer':'https://gu.qq.com/'}
p=json.load(open('marketdata/pool_ZT_1019b.json',encoding='utf-8'))['data']['pool']
codes={x['c']:x['n'] for x in p}
os.makedirs('marketdata/tk3',exist_ok=True)
def sym(c): return ('sh' if c[0]=='6' else 'sz')+c
def f(item):
    c,n=item; fp='marketdata/tk3/%s.json'%c
    if os.path.exists(fp) and os.path.getsize(fp)>100:
        try: return c,json.load(open(fp,encoding='utf-8'))
        except: pass
    u='https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param=%s,day,,,140,qfq'%sym(c)
    for i in range(3):
        try:
            d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('utf-8'))
            json.dump(d,open(fp,'w',encoding='utf-8'),ensure_ascii=False); return c,d
        except Exception:
            time.sleep(0.4)
    return c,{}
res={}
with ThreadPoolExecutor(max_workers=5) as ex:
    for c,d in ex.map(f,codes.items()): res[c]=d
print('ok',sum(1 for d in res.values() if d.get('code')==0),'/',len(res))
