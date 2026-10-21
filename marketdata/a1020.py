import json
from collections import Counter
d=json.load(open('marketdata/final_ZT_1020.json',encoding='utf-8'))['data']
print('TC',d['tc'],'heights',Counter(x['lbc'] for x in d['pool']))
print('sectors',Counter(x['hybk'] for x in d['pool']).most_common(15))
print('CODE NAME LB PCT AMT(亿) TURN% SEAL(亿) FBT ZBC SECTOR')
for x in sorted(d['pool'],key=lambda x:(-x['lbc'],x['fbt'])):
    print('%s %s %d %.2f%% %.1f %.1f %.2f %s %d %s'%(x['c'],x['n'],x['lbc'],x['zdp'],x['amount']/1e8,x['hs'],x['fund']/1e8,str(x['fbt']).zfill(6),x['zbc'],x['hybk']))
print('--- ZB',json.load(open('marketdata/final_ZB_1020.json',encoding='utf-8'))['data']['tc'])
for x in json.load(open('marketdata/final_ZB_1020.json',encoding='utf-8'))['data']['pool']:
    print(x['c'],x['n'],'%.2f%%'%x['zdp'],'%.1f亿'%(x.get('amount',0)/1e8),x['hybk'])
