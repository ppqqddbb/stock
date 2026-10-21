import urllib.request
H={'User-Agent':'Mozilla/5.0','Referer':'https://gu.qq.com/'}
u='https://qt.gtimg.cn/q=sh513500,sh513100,sz159941'
t=urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read().decode('gbk',errors='ignore')
for line in t.strip().split(';'):
    if '="' not in line: continue
    f=line.split('="')[1].strip('"').split('~')
    print('---',f[1],len(f))
    for i in range(55,min(90,len(f))):
        print(i,repr(f[i]))
    break
