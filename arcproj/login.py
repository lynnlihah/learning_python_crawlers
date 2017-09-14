#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup
import sys
from PIL import Image
import pytesseract
from chaojiying import Chaojiying_Client

# s = requests.Session()
# url_login = 'http://accounts.douban.com/login'
# url_contacts = 'https://www.douban.com/contacts/list'
#
# formdata = {
#     'source': 'index_nav',
#     'redir': 'https://www.douban.com',
#     'form_email': '',
#     'form_password': '',
#     'login': u'登录'
# }
#
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#
# r = s.post(url_login, data=formdata, headers=headers)
# content = r.text
# print(content)
#
# soup = bs(content, 'lxml')
# captcha = soup.find('img', id='captcha_image')

# if captcha:
#     captcha_url = captcha['src']
#     print(captcha_url)
#     re_captcha_id = r'<input type-"hidden" name="captcha-id" value="(.*?)"/'
#     captcha_id = re.findall(re_captcha_id, content)
#     print(captcha_id)
#     print(captcha_url)
#     captcha_text = input('Please input 验证码')
#     formdata['captcha-solution'] = captcha_text
#     formdata['captcha-id'] = captcha_id
#     r = s.post(url_login, data=formdata, headers=headers)
#     print(r.text)
# chaojiying = Chaojiying_Client("", "".encode("utf8"), "")

print("===== 开始登陆 =====")
r1 = requests.get(url="http://user.cbi360.net/Login")
validcode_path = BeautifulSoup(r1.text, 'lxml').find(id='imgValidCode')['src']
# validcode_path = h.xpath("//img[@id='imgValidCode']/@src").extract_first()

print("validcode_path",validcode_path)
validcode_url = "http://user.cbi360.net" + str(validcode_path).replace(" ", "%20")
print(validcode_url)
img = requests.get(validcode_url)
file_name = "validcode.png"
print('开始保存图片')
f = open(file_name, 'ab')
f.write(img.content)
print(file_name, '图片保存成功！')
f.close()

#image = Image.open("validcode.png")

#vcode = pytesseract.image_to_string(image)
#print(vcode)

im = open('validcode.png', 'rb').read()
validcode_value = chaojiying.PostPic(im, 1902).get("pic_str")
print("验证码为: %s" % validcode_value)

#im = open('validcode.png', 'rb').read()
#yield scrapy.Request(url=validcode_url, meta={"cookiejar": response.meta["cookiejar"]}, callback=self.login, dont_filter=True)

# def login(self, response):
#     i = Image.open(BytesIO(response.body))
#     i.save("validcode.png")
#     im = open('validcode.png', 'rb').read()
#     validcode_value = self.chaojiying.PostPic(im, 1902).get("pic_str")
#     print("验证码为: %s" % validcode_value)
#     time.sleep(1)
#     # validcode_value = input("查看validcode.png,输入验证码：")
#     data = {
#         "UserAccount": "",
#         "UserPwd": "",
#         "ValidCode": validcode_value
#     }
#     yield scrapy.FormRequest("http://user.cbi360.net/Login/SubmitLogin?Length=4",
#                              meta={"cookiejar": response.meta["cookiejar"]},
#                              formdata=data, callback=self.parse, dont_filter=True)
#
# def parse(self, response):
#     has_login = response.xpath('//input[@id="btnLogin"]')
#     if len(has_login) == 0:
#         print("===== 登陆成功 =====")