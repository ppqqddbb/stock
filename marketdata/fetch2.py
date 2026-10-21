import json, urllib.request, time, os
from concurrent.futures import ThreadPoolExecutor
H={'User-Agent':'Mozilla/5.0','Referer':'https://gu.qq.com/'}
zt=json.load(open('marketdata/final_ZT_1020.json',encoding='utf-8'))['data']['pool']
zb=json.load(open('marketdata/final_ZB_1020.json',encoding='utf-8'))['data']['pool']
codes={x['c']:x['n'] for x in zt+zb}
print('codes',len(codes))
os.makedirs('marketdata/tk2',exist_ok=True)
def sym(c): return ('sh' if c[0]=='6' else ('bj' if c[0]=='9' or c[:2]=='92' else 'sz'))+c
def fetch(item):
    c,n=item
    fp='marketdata/tk2/%s.json'%c
    if os.path.exists(fp) and os.path.getsize(fp)>100:
        try: return c,json.load(open(fp,encoding='utf-8'))
        except: pass
    u='https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param=%s,day,,,140,qfq'%sym(c)
    for i in range(3):
        try:
            d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('utf-8'))
            json.dump(d,open(fp,'w',encoding='utf-8'),ensure_ascii=False); return c,d
        except Exception as e:
            if i==2: return c,{'err':str(e)}
            time.sleep(0.5)
res={}
with ThreadPoolExecutor(max_workers=5) as ex:
    for c,d in ex.map(fetch,codes.items()): res[c]=d
ok=sum(1 for d in res.values() if d.get('code')==0)
print('ok',ok,'fail',len(res)-ok,[c for c,d in res.items() if d.get('code')!=0][:10])
