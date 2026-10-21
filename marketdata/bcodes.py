import json,urllib.request,urllib.parse,time
H={'User-Agent':'Mozilla/5.0','Referer':'https://quote.eastmoney.com/'}
def get(u):
    for i in range(3):
        try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('utf-8'))
        except Exception: time.sleep(0.6)
    return None
names=['半导体','消费电子','通信设备','通用设备','汽车零部件','照明设备','化学制药','软件开发','元件','IT服务','数字媒体','小家电','机器人概念','人形机器人','AI眼镜','CPO概念','存储芯片','工业母机']
out={}
for n in names:
    u='https://searchapi.eastmoney.com/api/suggest/get?input=%s&type=14&token=D43BF722C8E33BDC906FB84D85E326E8&count=10'%urllib.parse.quote(n)
    d=get(u)
    data=((d or {}).get('QuotationCodeTable') or {}).get('Data') or []
    bks=[x for x in data if x.get('Classify')=='BK']
    exact=[x for x in bks if x.get('Name')==n]
    pick=(exact or bks)
    if pick: out[n]=pick[0]['Code']+'|'+pick[0]['Name']
    time.sleep(0.3)
print(json.dumps(out,ensure_ascii=False,indent=0))
json.dump(out,open('marketdata/board_codes.json','w',encoding='utf-8'),ensure_ascii=False)
