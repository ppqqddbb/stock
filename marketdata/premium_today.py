import json,urllib.request,statistics
H={'User-Agent':'Mozilla/5.0','Referer':'https://gu.qq.com/'}
zt=json.load(open('marketdata/pool_ZT_1019.json',encoding='utf-8'))['data']['pool']
def sym(c): return ('sh' if c[0]=='6' else 'sz')+c
codes=[x['c'] for x in zt]
out={}
for i in range(0,len(codes),40):
    u='https://qt.gtimg.cn/q='+','.join(sym(c) for c in codes[i:i+40])
    t=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('gbk',errors='ignore')
    for line in t.strip().split(';'):
        if '="' not in line: continue
        f=line.split('="')[1].strip('"').split('~')
        if len(f)>50: out[f[2]]=f
vals=[]
for x in zt:
    f=out.get(x['c'])
    if not f: continue
    pct=float(f[32]); vals.append((pct,x['n'],x['lbc'],f[3],f[37]))
print('n',len(vals),'avg %.2f%% median %.2f%% positive %.1f%%'%(statistics.mean(v[0] for v in vals),statistics.median(v[0] for v in vals),100*sum(1 for v in vals if v[0]>0)/len(vals)))
print('top')
for v in sorted(vals,reverse=True)[:8]: print(' %.2f%% %s %d板 price%s amt%s万'%(v[0],v[1],v[2],v[3],v[4]))
print('bottom')
for v in sorted(vals)[:8]: print(' %.2f%% %s %d板 price%s amt%s万'%(v[0],v[1],v[2],v[3],v[4]))
print('by height')
for h in [1,2,3]:
    s=[v[0] for v in vals if v[2]==h]
    if s: print(' %d板 n%d avg%.2f%%'%(h,len(s),statistics.mean(s)))
