# -*- coding:utf-8 -*-

import urllib
import urllib2

if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list?type=19&interval_id=100%3A90&action="

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"

    }

    formdata = {

        "start": "0",
        "limit": "20"
    }

    data = urllib.urlencode(formdata)
    request = urllib2.Request(url, data=data, headers=headers)
    print urllib2.urlopen(request).read()


