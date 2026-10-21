import json, urllib.request, time
H={'User-Agent':'Mozilla/5.0','Referer':'https://gu.qq.com/'}
zt=json.load(open('marketdata/pool_ZT_1019.json',encoding='utf-8'))['data']['pool']
zb=json.load(open('marketdata/pool_ZB_1019.json',encoding='utf-8'))['data']['pool']
def sym(c): return ('sh' if c[0]=='6' else 'sz')+c
codes=[x['c'] for x in zt]+[x['c'] for x in zb]
out={}
for i in range(0,len(codes),40):
    q=','.join(sym(c) for c in codes[i:i+40])
    u='https://qt.gtimg.cn/q='+q
    txt=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('gbk',errors='ignore')
    for line in txt.strip().split(';'):
        if '="' not in line: continue
        key=line.split('=')[0].strip().replace('v_','')
        f=line.split('="')[1].strip('"').split('~')
        if len(f)>50: out[key[2:]]=f
    time.sleep(0.2)
print('got',len(out))
print('CODE NAME PRICE PCT OPEN HIGH LOW VOL(手) AMT(万) TURN% VOLR LIMITUP B1 B1V A1')
for x in sorted(zt,key=lambda x:(-x['lbc'],x['fbt'])):
    f=out.get(x['c'])
    if not f: continue
    print('%s %s %s %s%% %s %s %s %s %s %s %s %s %s %s %s'%(x['c'],x['n'],f[3],f[32],f[5],f[33],f[34],f[36],f[37],f[38],f[49],f[47],f[9],f[10],f[19]))
print('--- 炸板股竞价')
for x in zb:
    f=out.get(x['c'])
    if not f: continue
    print('%s %s %s %s%% open=%s B1=%s A1=%s'%(x['c'],x['n'],f[3],f[32],f[5],f[9],f[19]))
