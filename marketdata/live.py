import json,urllib.request
H={'User-Agent':'Mozilla/5.0','Referer':'https://gu.qq.com/'}
codes=['sh600178','sz003029','sh603278','sh603197','sh600148','sz002724','sz301313','sh603859','sz002164','sz002085','sz000576','sz002889','sh603348','sz300852','sh601778','sh603693','sh600267','sz002368','sh600860']
u='https://qt.gtimg.cn/q='+','.join(codes)
t=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('gbk',errors='ignore')
for line in t.strip().split(';'):
    if '="' not in line: continue
    f=line.split('="')[1].strip('"').split('~')
    if len(f)<50: continue
    print('%s %s %s %s%% open=%s high=%s low=%s amt=%s万 turn=%s%% b1=%s(%s) a1=%s'%(f[2],f[1],f[3],f[32],f[5],f[33],f[34],f[37],f[38],f[9],f[10],f[19]))
