#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib,math,random,time,os,re,json,threading
import http.cookiejar
# import urllib.request
import requests
from pytesseract import *
from PIL import Image
from PIL import ImageEnhance
from io import BytesIO
from bs4 import BeautifulSoup
from queue import Queue

class LoginModule:
    def __init__(self):
        self.web_url = 'http://hhb.cbi360.net/Login'  # 要访问的网页地址
        self.folder_path = 'D:\Output'  # 设置图片要存放的文件目录
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Connection": "keep-alive",
            "Host": "user.cbi360.net"
        }
        #self.chaojiying = Chaojiying_Client()
        self.UserAccount = ""
        self.UserPwd = ""

    def login(self):
        print('开始网页get请求')
        r = self.request(self.web_url)
        print(r)
        print('开始创建文件夹')
        self.mkdir(self.folder_path)
        #print('开始切换文件夹')
        #os.chdir(self.folder_path)  # 切换路径至上面创建的文件夹

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已经存在了，不再创建')

    def request(self, url):  # 返回网页的response
        r = requests.get(url, headers=self.headers)
        return r

# 主程序开始
l = LoginModule()
l.login()

