# -*- coding: utf-8 -*-

import urllib.request
import re
data=urllib.request.urlopen("http://book.jd.com/").read().decode("utf-8","ignore")
pat='<title>(.*?)</title>'
logo=re.compile(pat).findall(data)
print(str(logo[0]))
print(len(data))
