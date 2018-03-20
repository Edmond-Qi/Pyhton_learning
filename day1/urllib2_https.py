# -*- coding:utf-8 -*-

import urllib2
import ssl

if __name__ == "__main__":
    url = "https://www.12306.cn/mormhweb/"

    # 忽略SSL安全认证
    context = ssl._create_unverified_context()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
    }

    request = urllib2.Request(url, headers=headers)

    print urllib2.urlopen(request, context=context).read()