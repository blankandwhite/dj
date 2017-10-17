import urllib.request
import re
import random
keyname="nike"
key=urllib.request.quote(keyname)
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    ]

def ua(uapools):
    thisua=random.choice(uapools)
    print(thisua)
    headers=("User-Agent",thisua)
    opener=urllib.request.build_opener()
    opener.addheaders=[headers]
    #安装为全局
    urllib.request.install_opener(opener)
for i in range(1,3):
    url="https://zh.airbnb.com/rooms/6596814"
    ua(uapools)
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    print(len(data))
    #pat='"pic_url":"//(.*?)"'
    #imglist=re.compile(pat).findall(data)
    #for j in range(0,len(imglist)):
      
