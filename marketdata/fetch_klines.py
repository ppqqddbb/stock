import json, urllib.request, time, os
from concurrent.futures import ThreadPoolExecutor
H={'User-Agent':'Mozilla/5.0','Referer':'https://quote.eastmoney.com/'}
zt=json.load(open('marketdata/pool_ZT_1019.json',encoding='utf-8'))['data']['pool']
zt16=json.load(open('marketdata/pool_ZT_20261016.json',encoding='utf-8'))['data']['pool']
zb=json.load(open('marketdata/pool_ZB_1019.json',encoding='utf-8'))['data']['pool']
codes={}
for x in zt+zt16+zb:
    codes[x['c']]=(x['m'],x['n'])
print('codes',len(codes))
os.makedirs('marketdata/kline',exist_ok=True)
def fetch(item):
    code,(m,name)=item
    fp='marketdata/kline/%s.json'%code
    if os.path.exists(fp):
        try:
            return code,json.load(open(fp,encoding='utf-8'))
        except: pass
    u=('https://push2his.eastmoney.com/api/qt/stock/kline/get?secid=%d.%s&ut=fa5fd1943c7b386f172d6893dbfba10b&klt=101&fqt=1&lmt=120&end=20500101&fields1=f1,f2,f3,f4,f5,f6&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61'%(m,code))
    for i in range(4):
        try:
            req=urllib.request.Request(u,headers=H)
            d=json.loads(urllib.request.urlopen(req,timeout=20).read().decode('utf-8'))['data']
            json.dump(d,open(fp,'w',encoding='utf-8'),ensure_ascii=False)
            return code,d
        except Exception as e:
            if i==3: return code,{'err':str(e)}
            time.sleep(0.6*(i+1))
res={}
with ThreadPoolExecutor(max_workers=4) as ex:
    for code,d in ex.map(fetch,codes.items()):
        res[code]=d
ok=sum(1 for d in res.values() if d and 'klines' in d)
print('ok',ok,'fail',len(res)-ok)
print([c for c,d in res.items() if not d or 'klines' not in d][:10])
