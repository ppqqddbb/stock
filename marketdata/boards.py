import json,urllib.request,time
H={'User-Agent':'Mozilla/5.0','Referer':'https://quote.eastmoney.com/'}
def get(u):
    for i in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('utf-8'))
        except Exception as e:
            time.sleep(0.5)
    return None
out={}
for kind,fs in [('ind','m:90+t:2'),('con','m:90+t:3')]:
    d=get('https://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=600&po=1&np=1&fltt=2&invt=2&fid=f3&fs=%s&fields=f12,f14'%fs)['data']['diff']
    out[kind]=[(x['f12'],x['f14']) for x in d]
    print(kind,len(d))
json.dump(out,open('marketdata/boards.json','w',encoding='utf-8'),ensure_ascii=False)
