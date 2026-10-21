import json
zt=json.load(open('marketdata/final_ZT_1020.json',encoding='utf-8'))['data']['pool']
raw=open('marketdata/live21.txt',encoding='gbk',errors='ignore').read()
out={}
for line in raw.strip().split(';'):
    if '="' not in line: continue
    f=line.split('="')[1].strip('"').split('~')
    if len(f)>50: out[f[2]]=f
rows=[]
for x in zt:
    f=out.get(x['c'])
    if not f: continue
    rows.append((float(f[32]),x['c'],x['n'],x['lbc'],f[3],f[5],f[37],f[38],f[47],f[9],f[10],f[19],f[30]))
print('LIVE',rows[0][-1][:14] if rows else '')
for r in sorted(rows,reverse=True):
    print('%+7.2f%% %s %-7s %d板 px=%7s open=%7s amt=%8s万 turn=%5s%% lim=%7s b1=%s(%s) a1=%s'%(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11]))
