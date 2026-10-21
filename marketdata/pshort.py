raw=open('marketdata/short.txt',encoding='gbk',errors='ignore').read()
for line in raw.strip().split(';'):
    if '="' not in line: continue
    f=line.split('="')[1].strip('"').split('~')
    if len(f)<50: continue
    print('%-8s %7s %+7s%% amt=%7s万 turn=%5s%% high=%7s low=%7s b1=%s(%s) t=%s'%(f[1],f[3],f[32],f[37],f[38],f[33],f[34],f[9],f[10],f[30][8:12]))
