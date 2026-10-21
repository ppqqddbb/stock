import json,urllib.request,time
from collections import Counter
H={'User-Agent':'Mozilla/5.0','Referer':'https://quote.eastmoney.com/'}
zt=json.load(open('marketdata/final_ZT_1020.json',encoding='utf-8'))['data']['pool']
def get(u):
    for i in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=15).read().decode('utf-8'))
        except Exception: time.sleep(0.4)
cnt=Counter(); per={}
for x in zt:
    m='1' if x['c'][0]=='6' else '0'
    d=get('https://push2.eastmoney.com/api/qt/slist/get?secid=%s.%s&spt=3&fields=f12,f14&pn=1&pz=60&po=1&np=1&fltt=2&invt=2&fid=f3'%(m,x['c']))
    arr=[y['f14'] for y in (d or {}).get('data',{}).get('diff',[]) or []]
    per[x['n']]=[a for a in arr if a in ('AI眼镜','人形机器人','机器人概念','消费电子','半导体','通信设备','通用设备','汽车零部件','减速器','AI芯片','CPO概念','存储芯片','算力概念')]
    for a in arr: cnt[a]+=1
    time.sleep(0.12)
json.dump(per,open('marketdata/zt_boards.json','w',encoding='utf-8'),ensure_ascii=False)
for k,v in cnt.most_common(25): print(k,v)
print('---')
for n,v in per.items():
    if any(a in v for a in ('AI眼镜','人形机器人','机器人概念')): print(n,v)
