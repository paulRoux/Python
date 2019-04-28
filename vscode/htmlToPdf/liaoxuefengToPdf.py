import os
import re
import time
import logging
import pdfkit
import requests
from lxml import etree
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

headers = {
    "User-Agent": UserAgent().chrome
}


htmlTemplate = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>

"""


class Crawler(object):
    # 爬虫基类
    name = None


    def __init__(self, name, startUrl):
        self.name = name
        self.startUrl = startUrl
        self.domain = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(self.startUrl))


    @staticmethod
    def request(url, **kwargs):
        # 网络请求，返回response对象
        response = requests.get(url, headers=headers, **kwargs)
        return response


    def parseMenu(self, response):
        # 从response解析所有的url
        raise NotImplementedError


    def parseBody(self, response):
        # 解析正文
        raise NotImplementedError


    def run(self):
        start = time.time()
        options = {
            'dpi': '100',
            'quiet': '',  # 不显示中间的过程
            'minimum-font-size': '14',  # 最小的字体
            'page-height': '1.4in',
            'page-width': '1.2in',
            'margin-top': '0.01in',
            'margin-right': '0.01in',
            'margin-bottom': '0.01in',
            'margin-left': '0.01in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }

        htmls = []

        for index, url in enumerate(self.parseMenu(self.request(self.startUrl))):
            html = self.parseBody(self.request(url))
            fileName = ".".join([str(index), "html"])
            with open(fileName, 'wb') as f:
                f.write(html)
            htmls.append(fileName)

        pdfkit.from_file(htmls, "E:/code/Python/vscode/htmlToPdf/" + self.name + ".pdf", options=options)
        for html in htmls:
            os.remove(html)

        totalTime = time.time() - start
        print(u"总共耗时 {} 秒".format(totalTime))


class LiaoxuefengToPdf(Crawler):
    def parseMenu(self, response):
        html = etree.HTML(response.text)
        dirs = html.xpath("//div//ul/div//div/a")
        for dir in dirs:
            link = dir.xpath("string(./@href)")
            if not link.startswith("https"):
                url = "".join([self.domain, link])
            print(url)
            yield url
            # break


    def parseBody(self, response):
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            body = soup.find_all(class_="x-wiki-content")[0]

            # 加入标题, 居中显示
            title = soup.find('h4').get_text()
            centerTag = soup.new_tag("center")
            titleTag = soup.new_tag('h1')
            titleTag.string = title
            centerTag.insert(1, titleTag)
            body.insert(1, centerTag)

            html = str(body)
            # body中的img标签的src相对路径的改成绝对路径
            pattern = "(<img .*?src=\")(.*?)(\")"

            def func(m):
                if not m.group(2).startswith("https"):
                    rtn = "".join([m.group(1), self.domain, m.group(2), m.group(3)])
                    return rtn
                else:
                    return "".join([m.group(1), m.group(2), m.group(3)])

            html = re.compile(pattern).sub(func, html)
            html = htmlTemplate.format(content=html)
            html = html.encode("utf-8")
            return html
        except Exception:
            logging.error("解析错误", exc_info=True)


if __name__ == "__main__":
    startUrl = "https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000"
    crawler = LiaoxuefengToPdf("廖雪峰Git", startUrl)
    crawler.run()