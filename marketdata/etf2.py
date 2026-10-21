import urllib.request
H={'User-Agent':'Mozilla/5.0','Referer':'https://gu.qq.com/'}
codes=['sh513500','sz159612','sh513100','sz159941','sh513300','sh513390','sz159509','sh513650','sz159655','sz159632','sh513110']
u='https://qt.gtimg.cn/q='+','.join(codes)
t=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('gbk',errors='ignore')
print('code name price pct amount(亿) turnover% IOPV premium% prevNAV time')
for line in t.strip().split(';'):
    if '="' not in line: continue
    f=line.split('="')[1].strip('"').split('~')
    if len(f)<82: continue
    print('%s %s %s %s%% %.2f %.2f %s %s %s %s'%(f[2],f[1],f[3],f[32],float(f[37])/1e4,float(f[38]),f[78],f[77],f[81],f[30]))
