#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 课程地址（phatomjs和selenium简介）：http://www.cnblogs.com/Albert-Lee/p/6238866.html

# PhatomJS是一个WebKit内核的浏览器引擎，它能像浏览器一样（它就是
# 一个浏览器，只不过没有界面）解析网页，以及运行JavaScript脚本。
# 网页中有些数据是用js动态加载的，这样，我们使用使用http请求获得的数据中并不包含js动态加载的内容。
# 右键查看网页源码，如果搜索不到想查看的文字内容，那就是动态加载的。不是从控制台看
# PhatomJS下载 http://phantomjs.org/download.html
# PhatomJS官方文档 http://phantomjs.org/quick-start.html

# 课程地址（phatomjs结合selenium使用）：http://www.cnblogs.com/Albert-Lee/p/6275146.html
# 使用selenium 执行 js 代码 - 下拉操作
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

