# -*- coding:utf-8 -*-

import urllib2
import urllib

if __name__ == "__main__":
    # 1. url和Useragent
    url = "http://www.baidu.com/s"
    ua = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"}

    # 2.构造新的访问地址
    keywords = {"wd":"传智播客"}
    wd = urllib.urlencode(keywords)
    newurl = url + "?" + wd

    # 3.生成并发出请求
    request = urllib2.Request(newurl,headers=ua)
    response = urllib2.urlopen(request)

    print response.read()


