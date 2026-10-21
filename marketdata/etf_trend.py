import json,urllib.request
H={'User-Agent':'Mozilla/5.0','Referer':'https://gu.qq.com/'}
for code in ['sh513650','sh513390','sh513500','sh513100','sz159941']:
    u='https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param=%s,day,,,120,qfq'%code
    d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('utf-8'))
    k=list(d['data'].keys())[0]; b=d['data'][k].get('qfqday') or d['data'][k].get('day')
    c=[float(x[2]) for x in b]
    print(code,k,b[-1][0],'close=%.3f'%c[-1],'5d=%.2f%%'%(100*(c[-1]/c[-6]-1)),'20d=%.2f%%'%(100*(c[-1]/c[-21]-1)),'60d=%.2f%%'%(100*(c[-1]/c[-61]-1)),'MA5=%.3f MA20=%.3f'%(sum(c[-5:])/5,sum(c[-20:])/20),'20dhigh=%.3f'%max(float(x[3]) for x in b[-20:]))
