# -*- coding:utf-8 -*-

import urllib
import urllib2


def load_page(url,header):
    '''
    下载并返回要爬去的页面
    '''
    print("正在读！")
    request = urllib2.Request(url, headers=header)
    response = urllib2.urlopen(request)
    return response.read()


def write_page(page_number,html):
    '''
    保存爬去下来的页面
    '''
    print("正在写！")
    file_name = u"第"+ str(page_number) + u"页.html"
    with open(file_name, "w") as f:
        f.write(html)


def page_spider(kw, start_page, end_page):
    '''
    爬去网页的主要逻辑
        kw: 要爬取的贴吧名
        start_page: 起始页
        end_page: 终止页
    '''
    keywords = urllib.urlencode({"kw":kw})
    url = "http://tieba.baidu.com/f?" + keywords + "&pn="
    u_header={"User-Agent": "Mozilla/5.0(Windows"}

    for page_number in range(start_page, end_page+1):
        furl = url + str(page_number-1)
        html = load_page(furl, u_header)
        write_page(page_number, html)
        print "*"*16
    print "感谢您的使用！"


if __name__ == "__main__":
    '''用户输入数据，然后启动爬虫程序'''
    kw = raw_input("请输入要爬去的贴吧名：")
    start_page = int(raw_input("请输入起始页："))
    end_page = int(raw_input("请输入终止页："))

    page_spider(kw, start_page, end_page)