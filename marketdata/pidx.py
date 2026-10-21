raw=open('marketdata/idx_now.txt',encoding='gbk',errors='ignore').read()
for line in raw.strip().split(';'):
    if '="' not in line: continue
    f=line.split('="')[1].strip('"').split('~')
    if len(f)<40: continue
    print('%s %s %+.2f%% amt=%.0f亿 t=%s'%(f[1],f[3],float(f[32]),float(f[37])/1e4,f[30][8:12]))
