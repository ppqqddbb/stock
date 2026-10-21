import json, urllib.request, time, os
H={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36','Referer':'https://quote.eastmoney.com/'}
def get(url,tries=4):
    for i in range(tries):
        try:
            req=urllib.request.Request(url,headers=H)
            return json.loads(urllib.request.urlopen(req,timeout=20).read().decode('utf-8'))
        except Exception as e:
            if i==tries-1: raise
            time.sleep(0.5*(i+1))
fs='m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23'
fields='f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f22,f23,f24,f25,f26,f62,f100,f115'
rows=[]
for pn in range(1,61):
    try:
        d=get('https://push2.eastmoney.com/api/qt/clist/get?pn=%d&pz=100&po=1&np=1&fltt=2&invt=2&fid=f3&fs=%s&fields=%s'%(pn,fs,fields))['data']
        if not d or not d.get('diff'): break
        rows.extend(d['diff']); print(pn,len(rows),end='; ',flush=True)
        if len(rows)>=d['total']: break
    except Exception as e:
        print('fail',pn,e); break
json.dump(rows,open('marketdata/all.json','w',encoding='utf-8'),ensure_ascii=False)
print('\nstocks',len(rows))
