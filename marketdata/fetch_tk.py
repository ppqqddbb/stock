import json, urllib.request, time, os
from concurrent.futures import ThreadPoolExecutor
H={'User-Agent':'Mozilla/5.0','Referer':'https://gu.qq.com/'}
zt=json.load(open('marketdata/pool_ZT_1019.json',encoding='utf-8'))['data']['pool']
zt16=json.load(open('marketdata/pool_ZT_20261016.json',encoding='utf-8'))['data']['pool']
zb=json.load(open('marketdata/pool_ZB_1019.json',encoding='utf-8'))['data']['pool']
codes={}
for x in zt+zt16+zb:
    codes[x['c']]=(x['m'],x['n'])
idx={'000001':'sh000001','399001':'sz399001','399006':'sz399006','000688':'sh000688','399905':'sz399905'}
os.makedirs('marketdata/tkline',exist_ok=True)
def sym(code):
    return ('sh' if code[0]=='6' else 'sz')+code
def fetch(item):
    code,(m,name)=item
    fp='marketdata/tkline/%s.json'%code
    if os.path.exists(fp) and os.path.getsize(fp)>100:
        try: return code,json.load(open(fp,encoding='utf-8'))
        except: pass
    s=sym(code)
    u='https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param=%s,day,,,120,qfq'%s
    for i in range(4):
        try:
            req=urllib.request.Request(u,headers=H)
            d=json.loads(urllib.request.urlopen(req,timeout=20).read().decode('utf-8'))
            json.dump(d,open(fp,'w',encoding='utf-8'),ensure_ascii=False)
            return code,d
        except Exception as e:
            if i==3: return code,{'err':str(e)}
            time.sleep(0.4*(i+1))
res={}
with ThreadPoolExecutor(max_workers=5) as ex:
    for code,d in ex.map(fetch,codes.items()): res[code]=d
ok=sum(1 for d in res.values() if d.get('code')==0)
print('ok',ok,'fail',len(res)-ok)
print([c for c,d in res.items() if d.get('code')!=0][:8])
# indices
for k,s in idx.items():
    u='https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param=%s,day,,,120,qfq'%s
    try:
        d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('utf-8'))
        json.dump(d,open('marketdata/tkline/idx_%s.json'%k,'w',encoding='utf-8'),ensure_ascii=False)
        print('idx',k,d.get('code'),list((d.get('data') or {}).keys())[:2])
    except Exception as e: print('idxfail',k,e)
