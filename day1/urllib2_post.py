# -*- coding:utf-8 -*-

import urllib
import urllib2


url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {
# "Host" : "fanyi.youdao.com",
# "Connection" : "keep-alive",
"Accept" : "application/json, text/javascript, */*; q=0.01",
# "Origin" : "http://fanyi.youdao.com",
"X-Requested-With" : "XMLHttpRequest",
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
# "Referer" : "http://fanyi.youdao.com/",
# "Accept-Encoding" : "gzip, deflate",
# "Accept-Language" : "en-US,en;q=0.9",
# "Cookie" : "OUTFOX_SEARCH_USER_ID=63887441@114.242.249.57; JSESSIONID=aaahkLh-X6yL0e0ajpXhw; OUTFOX_SEARCH_USER_ID_NCOO=1650401331.0228124; ___rl__test__cookies=1520173705452"
}

key = raw_input("请输入要翻译的内容：")

data_form = {
    "i" : key,
    "from" : "AUTO",
    "to" : "AUTO",
    "smartresult" : "dict",
    "client" : "fanyideskweb",
    # "salt" : "1520171815871",
    # "sign" : "752a691308d08dea986ecf0a05a171ec",
    "doctype" : "json",
    "version" : "2.1",
    "keyfrom" : "fanyi.web",
    "action" : "FY_BY_REALTIME",
    "typoResult" : "false"
}

data = urllib.urlencode(data_form)

request = urllib2.Request(url, data=data, headers=headers)

print urllib2.urlopen(request).read()