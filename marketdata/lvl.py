import json
codes=['603626','603236','300115','603068','002881','603278','600860','603119','603893','688608','002164','002313']
for c in codes:
    d=json.load(open('marketdata/tk2/%s.json'%c,encoding='utf-8'))
    k=list(d['data'].keys())[0]; b=d['data'][k].get('qfqday') or d['data'][k].get('day')
    r=b[-1]; c0=float(r[2]); c1=float(b[-2][2])
    ma5=sum(float(x[2]) for x in b[-5:])/5; ma10=sum(float(x[2]) for x in b[-10:])/10; ma20=sum(float(x[2]) for x in b[-20:])/20
    lim=round(c0*1.1+1e-8,2) if not c.startswith(('30','68')) else round(c0*1.2+1e-8,2)
    print('%s close=%.2f 10/19=%.2f lim=%.2f low=%.2f MA5=%.2f MA10=%.2f MA20=%.2f'%(c,c0,c1,lim,float(r[4]),ma5,ma10,ma20))
