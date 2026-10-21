import json, urllib.request, urllib.parse
from concurrent.futures import ThreadPoolExecutor
H={'User-Agent':'Mozilla/5.0','Referer':'https://quote.eastmoney.com/'}
def get(url):
    req=urllib.request.Request(url,headers=H)
    return json.loads(urllib.request.urlopen(req,timeout=30).read().decode('utf-8'))
fs='m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23'
fields='f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f22,f23,f24,f25,f26,f62,f100,f115'
def page(pn):
    u=('https://push2.eastmoney.com/api/qt/clist/get?pn=%d&pz=100&po=1&np=1&fltt=2&invt=2&fid=f3&fs=%s&fields=%s'%(pn,fs,fields))
    return get(u)['data']['diff']
first=get('https://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=100&po=1&np=1&fltt=2&invt=2&fid=f3&fs=%s&fields=%s'%(fs,fields))
total=first['data']['total']; pages=(total+99)//100
rows=list(first['data']['diff'])
with ThreadPoolExecutor(max_workers=10) as ex:
    for d in ex.map(page,range(2,pages+1)): rows.extend(d)
json.dump(rows,open('marketdata/all.json','w',encoding='utf-8'),ensure_ascii=False)
print('stocks',len(rows),'total',total)

for name,fs2 in [('industry','m:90+t:2+f:!50'),('concept','m:90+t:3+f:!50')]:
    u='https://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=100&po=1&np=1&fltt=2&invt=2&fid=f3&fs=%s&fields=f12,f14,f3,f6,f8,f104,f105,f128,f140,f141'%fs2
    d=get(u)['data']
    json.dump(d['diff'],open('marketdata/%s.json'%name,'w',encoding='utf-8'),ensure_ascii=False)
    print(name,len(d['diff']))

def pool(kind,date):
    u=('https://push2ex.eastmoney.com/getTopic%sPool?ut=7eea3edcaed734bea9cbfc24409ed989&dpt=wz.ztzt&Pageindex=0&pagesize=1000&sort=fbt:asc&date=%s'%(kind,date))
    return get(u)
for kind in ['ZT','ZB','DT']:
    d=pool(kind,'20261019')
    data=d.get('data') or {}
    json.dump(data,open('marketdata/pool_%s_1019.json'%kind,'w',encoding='utf-8'),ensure_ascii=False)
    print(kind,data.get('tc'),len(data.get('pool',[]) or []))
for date in ['20261016','20261015']:
    d=pool('ZT',date); data=d.get('data') or {}
    json.dump(data,open('marketdata/pool_ZT_%s.json'%date,'w',encoding='utf-8'),ensure_ascii=False)
    print('ZT',date,data.get('tc'))
