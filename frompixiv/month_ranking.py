# study from : http://blog.csdn.net/elicococoo/article/details/52448947
import os, json, urllib, threading
from bs4 import BeautifulSoup
# python2
# import urllib2 ,cookielib, Queue
# python3
import urllib.request
import http.cookiejar
from queue import Queue

class PixivSpider:
    def __init__(self):
        self.imgs = []
        self.__html = "http://www.pixiv.net/ranking.php?mode=monthly&content=illust" # 月榜页面
        self.__originalLink =  "http://www.pixiv.net/member_illust.php?mode=medium&illust_id=" # prefix of image url
        self.__opener = None
        self.q = Queue.Queue()

    def CreateDir(self, path = "img/"):
        if not os.path.exists(path): os.makedirs(path)

    def __MakeJsonUrl(self, page):
        return self.__html + "&p=" + str(page) + "$format=json"

    def __GetJsonData(self, html):
        data = json.loads(urllib.urlopen(html).read())
        if data is None:
            return None
        else:
            for info in data["contents"]:
                img = {}
                img["id"] = info["illust_id"]
                img["rank"] = info["rank"]
                self.imgs.append(img)
                print("img id: ", img["id"], '\t', "img rank: ", img["rank"])

    def __loginRequest(self):
        cookie = http.cookiejar.MozillaCookieJar("cookie.txt")
        self.__opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
        header  = {
            "Accept-Language": "zh-CN,zh;q=0.8",
            'Referer': 'https://www.pixiv.net/login.php?return_to=0',
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
        }
        loginInfo = urllib.urlencode({
            'mode': 'login',
            'pass': 'password',
            'pixiv_id': 'username',
        })
        loginUrl = "https://www.pixiv.net/login.php"
        request  urllib.request.Request(loginUrl, data=loginInfo, headers=header)
        self.__opener.open(request)
        cookie.save(ignore_discard=True, ignore_expires=True)

    def __DownloadRequest(selfs, refererUrl, orginalUrl):
        header = {
            "Accept-Language": "zh-CN,zh;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
        }
        header['referer'] = refererUrl
        request = urllib.request.Request(originalUrl, headers=header)

        return self.__opener.open(request).read()

    class MyThread(threading.Thread):
        def __init__(self, filename, referer, src, opener, q, idx, total):
            threading.Thread.__init__(self)
            self.filename = filename
            self.referer = referer
            self.src = src
            self.opener = opener
            self.q = q
            self.total = total
            self.idx = idx

        def run(self):
            header = {
                "Accept-Language": "zh-CN,zh;q=0.8",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
            }
            header['referer'] = self.referer
            request = urllib.request.Request(self.src, headers=header)
            data = self.opener.open(request).read()
            file = open(self.filename, "wb")
            file.write(data)
            file.close()
            self.q.put(self.idx)
            print("Finished:", self.idx, "/", self.total)

        def GetImage(self):
            self.CreateDir()
            for i in range(1, 7, 1):
                self.__GetJsonData(self.__MakeJsonUrl(i))
            self.__loginRequest()
            total = len(self.imgs)
            t1 = datetime.now()
            print(t1)
            count = 1
            for img in self.imgs:
                id = img["id"]
                referer = self.__originalLink + str(id)
                data = self.__opener.open(referer).read()
                soup = BeautifulSoup(data, "lxml")
                tags = soup.find_all("img", attrs={"class": "original-image"})
                if len(tags) > 0:
                    src = tags[0].attrs['data-src']
                    # print "#" + str(img["rank"]), src
                    # file = open(self.__fatherPath + "#" + str(img["rank"]).zfill(3) + src[-4 : len(src)], 'wb')
                    # file.write(self.__DownloadRequest(referer, src))
                    # file.close()
                    mt = self.MyThread("img/" + "#" + str(img["rank"])).zfill(3) + src[-4 : len]


