import json,statistics
zt=json.load(open('marketdata/final_ZT_1020.json',encoding='utf-8'))['data']['pool']
raw=open('marketdata/live21.txt',encoding='gbk',errors='ignore').read()
out={}
for line in raw.strip().split(';'):
    if '="' not in line: continue
    f=line.split('="')[1].strip('"').split('~')
    if len(f)>50: out[f[2]]=f
vals=[(float(out[x['c']][32]),x['n'],x['lbc']) for x in zt if x['c'] in out]
print('n',len(vals),'avg %.2f%% median %.2f%% pos %.1f%%'%(statistics.mean(v[0] for v in vals),statistics.median(v[0] for v in vals),100*sum(1 for v in vals if v[0]>0)/len(vals)))
for h in [1,2,3,4]:
    s=[v[0] for v in vals if v[2]==h]
    if s: print(' %d板 n%d avg%.2f%%'%(h,len(s),statistics.mean(s)))
