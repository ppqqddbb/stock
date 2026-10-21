import json
zt=json.load(open('marketdata/pool_ZT_1019.json',encoding='utf-8'))['data']
zb=json.load(open('marketdata/pool_ZB_1019.json',encoding='utf-8'))['data']
print('qdate',zt['qdate'],'tc',zt['tc'])
from collections import Counter
print('heights',Counter(x['lbc'] for x in zt['pool']))
print('sectors',Counter(x['hybk'] for x in zt['pool']).most_common(12))
for x in sorted(zt['pool'],key=lambda x:(-x['lbc'],x['fbt'])):
    print(x['lbc'],x['c'],x['n'],x['p']/1000,x['zdp'],x['amount']/1e8,x['hs'],x['fbt'],x['zbc'],x['fund']/1e8,x['hybk'])
print('---炸板',zb['tc'])
for x in zb['pool']:
    print(x.get('c'),x.get('n'),x.get('zdp'),x.get('amount',0)/1e8,x.get('hybk'),x.get('zbc'))
