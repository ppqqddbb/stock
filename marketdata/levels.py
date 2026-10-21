import json
codes=['003029','002889','002724','600860','600148','603197','600178','603348','000576','002085','603278','603859','002164','301313','603119','601778','603693','001323']
for c in codes:
    d=json.load(open('marketdata/tkline/%s.json'%c,encoding='utf-8'))
    k=list(d['data'].keys())[0]; b=d['data'][k]['qfqday']
    closes=[float(x[2]) for x in b]; vols=[float(x[5]) for x in b]
    i=len(b)-1
    ma5=sum(closes[-5:])/5; ma10=sum(closes[-10:])/10; ma20=sum(closes[-20:])/20
    lows=[float(x[4]) for x in b]
    print('%s %s close=%.2f ma5=%.2f ma10=%.2f ma20=%.2f 10/16low=%.2f 10/19low=%.2f 20dhigh=%.2f 5dvolavg=%.0f'%(c,d['data'][k].get('qt',{}).get(k,['','?'])[1] if False else '',closes[-1],ma5,ma10,ma20,lows[-2],lows[-1],max(float(x[3]) for x in b[-20:]),sum(vols[-5:])/5))
