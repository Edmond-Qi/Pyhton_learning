# -*- coding:utf-8 -*-

import urllib2

# 设置User_agent,反爬虫的第一步
ua_headers ={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
        }
# 通过urllib.Request方法构造一个请求对象
request = urllib2.Request("http://www.baidu.com/",headers=ua_headers)
# 向指定的url地址发送请求，并返回服务器相应的类文件对象
response = urllib2.urlopen(request)

# 服务器返回的类文件对象支持Python文件对象的操作方法
# read()方法就是读取文件里的全部内容，返回字符串
html = response.read()

# 打印HTTP的响应码，成功返回200,
print response.getcode()

# 返回实际数据的URL，防止重定向问题
print response.geturl()

# 打印相应内容
print response.info()
#print html
