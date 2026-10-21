import json,urllib.request
H={'User-Agent':'Mozilla/5.0','Referer':'https://gu.qq.com/'}
u='https://qt.gtimg.cn/q=sh000001,sz399001,sz399006,sh000688,sz399905,sh000016,sh000852'
t=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('gbk',errors='ignore')
for line in t.strip().split(';'):
    if '="' not in line: continue
    f=line.split('="')[1].strip('"').split('~')
    if len(f)<40: continue
    print('%s %s %s%% amt=%.0f亿 time=%s'%(f[1],f[3],f[32],float(f[37])/1e4,f[30]))
