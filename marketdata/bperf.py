import json,urllib.request,time
H={'User-Agent':'Mozilla/5.0','Referer':'https://quote.eastmoney.com/'}
codes=json.load(open('marketdata/board_codes.json',encoding='utf-8'))
def kl(bk):
    u='https://push2his.eastmoney.com/api/qt/stock/kline/get?secid=90.%s&ut=fa5fd1943c7b386f172d6893dbfba10b&klt=101&fqt=1&lmt=30&end=20500101&fields1=f1,f2,f3,f4,f5,f6&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61'%bk
    for i in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('utf-8'))['data']
        except Exception: time.sleep(0.5)
print('BOARD 10/20% 5D% 10D% AMT(亿) vs5d')
rows=[]
for n,v in codes.items():
    bk=v.split('|')[0]
    d=kl(bk)
    if not d or 'klines' not in d: print(n,'ERR'); continue
    ks=[k.split(',') for k in d['klines']]
    c=[float(k[2]) for k in ks]; a=[float(k[6]) for k in ks]
    r={'n':n,'p':float(ks[-1][8]),'d5':100*(c[-1]/c[-6]-1),'d10':100*(c[-1]/c[-11]-1),'amt':a[-1]/1e8,'av5':sum(a[-5:])/5/1e8}
    rows.append(r); time.sleep(0.15)
for r in sorted(rows,key=lambda r:-r['p']):
    print('%-10s %+6.2f%% %+6.2f%% %+6.2f%% %6.0f %5.2fx'%(r['n'],r['p'],r['d5'],r['d10'],r['amt'],r['amt']/r['av5']))
