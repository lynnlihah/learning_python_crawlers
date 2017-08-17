#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
# get 请求
r = requests.get('https://unsplash.com')
# print(r.text) # 网页的html
print(type(r)) # <class 'requests.models.Response'>

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
# print(r.text)
# 上面代码向服务器发送的请求中包含了两个参数key1和key2，以及两个参数的值。实际上它构造成了如下网址：
# http://httpbin.org/get?key1=value1&key2=value2
# output
# {
#   "args": {
#     "key1": "value1",
#     "key2": "value2"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.18.4"
#   },
#   "origin": "124.17.24.248",
#   "url": "http://httpbin.org/get?key1=value1&key2=value2"
# }

# post
# 无参数的post请求：
r = requests.post("http://httpbin.org/post")
# 有参数的post请求：
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
# post请求多用来提交表单数据，即填写一堆输入框，然后提交

# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")