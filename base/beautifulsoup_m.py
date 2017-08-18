#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 原blog地址：http://www.cnblogs.com/Albert-Lee/p/6232745.html
# 使用BeautifulSoup模块 - 官方文档：http://beautifulsoup.readthedocs.io/zh_CN/latest/
# pip install beautifulsoup4
# pip install lxml

from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构，每个节点都是Python对象。所有对象可以归纳为4种类型:
# Tag , NavigableString(标签中的文本内容，不包含标签) , BeautifulSoup（BeautifulSoup对象表示一个文档的全部内容。
# 支持遍历文档树和搜索文档树。）, Comment（注释-有些时候，我们并不想获取HTML中的注释内容，所以用这个类型来判断是否是注释。）
# if type(SomeString) == bs4.element.Comment:
#     print('该字符是注释')
# else:
    # print('该字符不是注释')
soup = BeautifulSoup(html_doc, 'lxml')  #声明BeautifulSoup对象
find = soup.find('p')  #使用find方法查到第一个p标签
print("find's return type is ", type(find))  #输出返回值类型
print("find's content is", find)  #输出find获取的值
print("find's Tag Name is ", find.name)  #输出标签的名字
print("find's Attribute(class) is ", find['class'])  #输出标签的class属性值
# find's return type is  <class 'bs4.element.Tag'>
# find's content is <p class="title"><b>The Dormouse's story</b></p>
# find's Tag Name is  p
# find's Attribute(class) is  ['title']

# 4.2 BeautifulSoup遍历方法
# 4.2.1 节点和标签名

# 可以使用子节点、父节点、 及标签名的方式遍历：

soup.head #查找head标签
soup.p #查找第一个p标签

#对标签的直接子节点进行循环
# for child in title_tag.children:
#     print(child)

soup.parent #父节点

# 所有父节点
# for parent in link.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)

# 兄弟节点
# sibling_soup.b.next_sibling #后面的兄弟节点
# sibling_soup.c.previous_sibling #前面的兄弟节点

# 所有兄弟节点
for sibling in soup.a.next_siblings:
    print(repr(sibling))

for sibling in soup.find(id="link3").previous_siblings:
    print(repr(sibling))

# 4.2.2 搜索文档树
#
# 最常用的当然是find()和find_all()啦，当然还有其他的。比如find_parent() 和 find_parents()、 find_next_sibling() 和 find_next_siblings() 、find_all_next() 和 find_next()、find_all_previous() 和 find_previous() 等等。
# 我们就看几个常用的，其余的如果用到就去看官方文档哦。

# find_all()
# 搜索当前tag的所有tag子节点，并判断是否符合过滤器的条件。返回值类型是bs4.element.ResultSet。
# 完整的语法：
# find_all( name , attrs , recursive , string , **kwargs )
# 这里有几个例子

soup.find_all("title")
# [<title>The Dormouse's story</title>]
#
soup.find_all("p", "title")
# [<p class="title"><b>The Dormouse's story</b></p>]
#
soup.find_all("a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
#
soup.find_all(id="link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
#
import re
soup.find(string=re.compile("sisters"))
# u'Once upon a time there were three little sisters; and their names were\n'
# name 参数：可以查找所有名字为 name 的tag。
# attr 参数：就是tag里的属性。
# string 参数：搜索文档中字符串的内容。
# recursive 参数： 调用tag的 find_all() 方法时，Beautiful Soup会检索当前tag的所有子孙节点。如果只想搜索tag的直接子节点，可以使用参数 recursive=False 。

# find()
# 与find_all()类似，只不过只返回找到的第一个值。返回值类型是bs4.element.Tag。
# 完整语法：
# find( name , attrs , recursive , string , **kwargs )
# 看例子：

soup.find('title')
# <title>The Dormouse's story</title>
#
soup.find("head").find("title")
# <title>The Dormouse's story</title>