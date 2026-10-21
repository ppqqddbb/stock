import json,urllib.request,time
H={'User-Agent':'Mozilla/5.0','Referer':'https://quote.eastmoney.com/'}
def get(u):
    for i in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('utf-8'))
        except Exception: time.sleep(0.5)
names={'603893':('1','瑞芯微'),'688608':('1','恒玄科技'),'300115':('0','长盈精密'),'603626':('1','科森科技'),'603341':('1','龙旗科技'),'002881':('0','美格智能'),'603278':('1','大业股份'),'600860':('1','京城股份'),'002164':('0','宁波东力'),'301313':('0','凡拓数创'),'600148':('1','长春一东'),'002724':('0','海洋王')}
for c,(m,n) in names.items():
    d=get('https://push2.eastmoney.com/api/qt/slist/get?secid=%s.%s&spt=3&fields=f12,f14&pn=1&pz=60&po=1&np=1&fltt=2&invt=2&fid=f3'%(m,c))
    if not d: print(n,'ERR'); continue
    arr=[x['f14'] for x in d['data']['diff']]
    keep=[x for x in arr if any(k in x for k in ['AI','机器人','半导体','消费电子','通信','眼镜','芯片','算力','华为','苹果','特斯拉','减速器','丝杠','智能'])]
    print(n,keep[:15])
    time.sleep(0.2)
