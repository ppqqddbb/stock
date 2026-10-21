import json
zt=json.load(open('marketdata/final_ZT_1020.json',encoding='utf-8'))['data']['pool']
codes=','.join(('sh' if x['c'][0]=='6' else 'sz')+x['c'] for x in zt)
open('marketdata/q_codes.txt','w').write(codes)
print(len(zt))
