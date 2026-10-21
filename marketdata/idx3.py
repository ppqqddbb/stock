import json,urllib.request
H={'User-Agent':'Mozilla/5.0','Referer':'https://gu.qq.com/'}
for code,name in [('sh000001','上证'),('sz399001','深成'),('sz399006','创业板'),('sh000688','科创50'),('sz399905','中证500'),('sh000852','中证1000'),('sh000016','上证50')]:
    u='https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param=%s,day,,,120,qfq'%code
    d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('utf-8'))
    k=list(d['data'].keys())[0]; b=d['data'][k].get('qfqday') or d['data'][k].get('day')
    c=[float(x[2]) for x in b]; hi=max(float(x[3]) for x in b[-20:])
    print('%s %s %.2f %.2f%% MA5=%.2f MA10=%.2f MA20=%.2f 5D=%+.2f%% 10D=%+.2f%% 20Dhigh=%.2f dist=%+.2f%%'%(name,b[-1][0],c[-1],100*(c[-1]/c[-2]-1),sum(c[-5:])/5,sum(c[-10:])/10,sum(c[-20:])/20,100*(c[-1]/c[-6]-1),100*(c[-1]/c[-11]-1),hi,100*(c[-1]/hi-1)))
