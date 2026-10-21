import json,urllib.request,time
H={'User-Agent':'Mozilla/5.0','Referer':'https://gu.qq.com/'}
zt=json.load(open('marketdata/final_ZT_1020.json',encoding='utf-8'))['data']['pool']
def sym(c): return ('sh' if c[0]=='6' else 'sz')+c
out={}
codes=[x['c'] for x in zt]
for i in range(0,len(codes),40):
    u='https://qt.gtimg.cn/q='+','.join(sym(c) for c in codes[i:i+40])
    t=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('gbk',errors='ignore')
    for line in t.strip().split(';'):
        if '="' not in line: continue
        f=line.split('="')[1].strip('"').split('~')
        if len(f)>50: out[f[2]]=f
    time.sleep(0.2)
rows=[]
for x in zt:
    f=out.get(x['c'])
    if not f: continue
    rows.append((float(f[32]),x['c'],x['n'],x['lbc'],f[3],f[5],f[37],f[38],f[47],f[9],f[10],f[19],f[49]))
print('AUCTION',time.strftime('%H:%M:%S'))
for r in sorted(rows,reverse=True):
    print('%+7.2f%% %s %-6s %d板 px=%s open=%s amt=%s万 turn=%s%% lim=%s b1=%s(%s) a1=%s volr=%s'%(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12]))
