# -*- coding:utf-8 -*-

import urllib2
import random

if __name__ == "__main__":

    url = "http://www.baidu.com/"

    ua_list = [
        "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
        "Mozilla/5.0 (Macintosh; Intel Mac OS... "
    ]

    user_agent = random.choice(ua_list)

    # ua_header = {
    #     "User-Agent":user_agent
    # }
    # request = urllib2.Request(url,headers=ua_header)

    request = urllib2.Request(url)

    # 第一个字母大写，后面全小写
    request.add_header("User-Agent",user_agent)

    print request.get_header("User-agent")

    response = urllib2.urlopen(request)

    print response.info()

