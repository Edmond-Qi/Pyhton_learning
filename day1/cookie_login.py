# -*- coding:utf-8 -*-

import urllib2

if __name__ == "__main__":
    url = "http://www.renren.com/345161295/profile"

    headers = {
        "Host": "wpi.renren.com",
        "Connection": "keep-alive",
        "Accept": "text/plain, */*; q=0.01",
        # "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "http://wpi.renren.com/ajaxproxy.htm",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": "anonymid=jedr1vk1wp1x1n; depovince=BJ; jebecookies=9d65d7a9-ad42-4ef2-8000-1f9cf5f036a0|||||; _r01_=1; ick_login=9acb267b-2eb1-4e2f-9518-6d1023cada48; _de=15AAE488B164AD1262C07BAAD5B8A6276DEBB8C2103DE356; p=547276b703a83041c5e5f394eff1413f9; first_login_flag=1; ln_uact=1039424318@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20141011/2135/h_main_PwSt_3f93000474051986.jpg; t=83dc42852dc45c21eea149b532807a6d9; societyguester=83dc42852dc45c21eea149b532807a6d9; id=340631459; xnsid=b7e6469; loginfrom=syshome; ch_id=10016; springskin=set; jebe_key=24b26ec6-3135-46f5-bdeb-d31a67239e6c%7C01e51464570bd12dd8bdce505e40e139%7C1520225592557%7C1%7C1520225592976; vip=1; wpsid=14789603197251; wp_fold=0"
    }

    request = urllib2.Request(url, headers=headers)

    print urllib2.urlopen(request).read()

super.mro()

