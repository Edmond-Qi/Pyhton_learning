# -*- coding:utf-8 -*-

import urllib2

if __name__ == "__main__":
    # ua_header = {"User-Agent":"Mozilla/5.0(Windows"}
    request = urllib2.Request("https://www.baidu.com/")
    response = urllib2.urlopen(request)
    print(response.read())
# !/usr/bin/env python
# -*- coding:utf-8 -*-

# '''PYTHON3'''
# import urllib.request
#
# import urllib.parse
# import json
# import time
# import random
# import hashlib
#
# content = input('请输入需要翻译的句子：')
#
# url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#
# data = {}
#
# u = 'fanyideskweb'
# d = content
# print(time.time())
# f = str(int(time.time()*1000) + random.randint(1,10))
# c = 'rY0D^0\'nM0}g5Mm1z%1G4'
#
# sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()
#
# data['i'] = content
# data['from'] = 'AUTO'
# data['to'] = 'AUTO'
# data['smartresult'] = 'dict'
# data['client'] = 'fanyideskweb'
# data['salt'] = f
# data['sign'] = sign
# data['doctype'] = 'json'
# data['version'] = '2.1'
# data['keyfrom'] = 'fanyi.web'
# data['action'] = 'FY_BY_CL1CKBUTTON'
# data['typoResult'] = 'true'
#
# data = urllib.parse.urlencode(data).encode('utf-8')
# request = urllib.request.Request(url=url,data=data,method='POST')
# response = urllib.request.urlopen(request)
#
# print(response.read().decode('utf-8'))

