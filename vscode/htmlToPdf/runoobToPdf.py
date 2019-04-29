import os
import pdfkit
import requests
import time
from lxml import etree
from urllib.parse import urlparse
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


headers = {
    "User-Agent": UserAgent().chrome
}


startUrl = "https://www.runoob.com/design-pattern/design-pattern-tutorial.html"
fileName = None


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

def getUrlList():
    urls = []
    global fileName
    response = requests.get(startUrl, headers=headers)
    # 网站编码进行了压缩，需要解压缩否则出现中文乱码
    html = etree.HTML(response.content.decode("utf-8"))
    dirs = html.xpath("//div[@class='design']//a")
    fileName = html.xpath("string(//div[@class='design']/a[1]/@title)")
    for dir in dirs[1:]:
        link = dir.xpath("string(./@href)")
        if not link.startswith("https"):
            url = "https://www.runoob.com/" + link
        urls.append(url)
        break
    return urls


def parseHtml(url, name):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        body = soup.find_all(class_="article-intro")

        h = str(body)
        html = h[1:-1]
        html = htmlTemplate.format(content=html)
        html = html.encode("utf-8")
        with open(name, 'wb') as f:
            f.write(html)
        return name

    except Exception as e:
        print(e)


def savePdf(htmls, fileName):
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
    pdfkit.from_file(htmls, "E:/code/Python/vscode/htmlToPdf/" + fileName + ".pdf", options=options)


def main():
    start = time.time()
    urls = getUrlList()
    htmls = [parseHtml(url, str(index) + ".html") for index, url in enumerate(urls)]
    savePdf(htmls, fileName)
    for html in htmls:
        os.remove(html)

    total_time = time.time() - start
    print(u"总共耗时：%f 秒" % total_time)


if __name__ == "__main__":
    main()
