#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from chaojiying import Chaojiying_Client
import http.cookiejar
import urllib


# chaojiying = Chaojiying_Client("", "".encode("utf8"), "")

print("===== 开始登陆 =====")
r1 = requests.get(url="http://user.cbi360.net/Login")
validcode_path = BeautifulSoup(r1.text, 'lxml').find(id='imgValidCode')['src']

print("validcode_path",validcode_path)
validcode_url = "http://user.cbi360.net" + str(validcode_path).replace(" ", "%20")
print(validcode_url)
img = requests.get(validcode_url)
file_name = "validcode.png"
print('开始保存图片')
f = open(file_name, 'wb+')
f.write(img.content)
print(file_name, '图片保存成功！')
f.close()


im = open(file_name, 'rb').read()
#validcode_value = chaojiying.PostPic(im, 1902).get("pic_str")
validcode_value = input("查看validcode.png,输入验证码：")
print("验证码为: %s" % validcode_value)

data = {
    'UserAccount': '',
    'UserPwd': '',
    'ValidCode': validcode_value
}

login_url = 'http://user.cbi360.net/Login/SubmitLogin?Length=4'
# login_url = "http://user.cbi360.net/Login"
# login_url = "http://user.cbi360.net/Login?url=http%3A%2F%2Fhhb.cbi360.net%2F"
header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            # "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Host": "user.cbi360.net",
            "cookie": "div_cbi_top_user_active=true; UM_distinctid=15e7e8a5936a8e-0b6dba46ecdce3-3a3e5f04-1fa400-15e7e8a5937c88; ASP.NET_SessionId=chxgejk5kvfunl2h54wfnf33; CBIFullShow_20170908=true; CBI360StatsUV=UVKey=32193e1f-d13e-4ad6-be18-5912300d57d6; CNZZDATA30036250=cnzz_eid%3D2017749833-1505358897-%26ntime%3D1505461536; Hm_lvt_61b5af2f07b8b10df4641a219a7ddd8d=1505447860,1505454752,1505460311,1505460558; Hm_lpvt_61b5af2f07b8b10df4641a219a7ddd8d=1505461566; CNZZDATA30040783=cnzz_eid%3D1530393429-1505360890-%26ntime%3D1505458107; Hm_lvt_2c83b793310ff6a04ed72f97dfc92eb9=1505447860,1505454752,1505460311,1505460558; Hm_lpvt_2c83b793310ff6a04ed72f97dfc92eb9=1505461566; Hm_lvt_9f1a930c5ecc26fe983d898c26bd5fea=1505454397; Hm_lpvt_9f1a930c5ecc26fe983d898c26bd5fea=1505461716; CBI360=UserID=8FE7EE37026AB64278C0844A47DCB47A0681A1282E09A94A717072822C3829C48434395C2668C758&UserName=%e4%b8%ad%e9%93%81%e5%bb%ba%e5%b7%a5%e9%9d%92%e5%b2%9b&UserPopedom=reg,hhb,zb,hhb&UserAccount=13953205832&IsVip=1&VipLevel=1&AuditTime=2013%e5%b9%b408%e6%9c%8824%e6%97%a5&VipOutDate=2017%e5%b9%b411%e6%9c%8822%e6%97%a5&SaveLogin=1&onlineStats=124.17.24.248&IsCollect=1&IsRelease=1&sign=ed6c037b-764b-415f-a6e9-6135d15bfc82"
        }
# session = requests.Session()
# print(data)
# r = session.post(login_url, data=data, headers=header)
# # print(r)
# content = r.text
# # print(content)
#
# soup = BeautifulSoup(content, 'lxml')
# flag = soup.find(id='btnLogin')
# print(flag)
#
# # print(h.text)
home_url = "http://hhb.cbi360.net"
# # with open('get.html', 'wt+', encoding="utf8", errors='ignore') as f:
# #     print(content, file=f)
# # print(session.get("http://user.cbi360.net/").text)
#
#
# print(ret.text)
# # requests.get(url="http://user.cbi360.net/Login", headers=header, getvalidcode,
# #                                  meta={"cookiejar": 1}, dont_filter=True)
#
# print(r.cookies.get_dict())
# print("-----------")
# print("Going to profile page...")
# r = requests.get("http://pythonscraping.com/pages/cookies/profile.php",
#                  cookies=r.cookies)
# print(r.text)

# req = urllib.request.Request(login_url,data,header)
# print(urllib.request.urlopen(req).read().decode('utf-8'))

# session = requests.Session()
# s = session.post(login_url, data, header)
# print("url:", login_url, "params:", data)
# print(s.cookies)
# print(s.cookies.get_dict())
# print(urllib.request.urlopen(s).read().decode('utf-8'))
# l = session.get(home_url)
# print(l.text)

# cookie = http.cookiejar.CookieJar()
# handler= urllib.request.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib.request.build_opener(handler)
# #此处的open方法同urllib2的urlopen方法，也可以传入request
# response = opener.open("http://hhb.cbi360.net/")
# print({c.name: c.value for c in cookie})


r = requests.get(home_url, header)
print(r.text)