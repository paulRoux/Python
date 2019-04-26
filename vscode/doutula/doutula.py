import requests
import os
import re
from lxml import etree
from fake_useragent import UserAgent
from urllib import request


ua = UserAgent().chrome

headers = {
    "User-Agent": ua
}


def parse(url):
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgsUrl = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']/@data-original")
    imgsName = html.xpath("//div[@class='page-content text-center']//p/text()")
    for url, name in zip(imgsUrl, imgsName):
        imageUrl = str(url).rstrip("!dta")
        suffix = os.path.splitext(imageUrl)[1]
        imageName = re.sub(r'[\??\.，。\* ]', '', name) + suffix
        request.urlretrieve(imageUrl, "doutula/images/{}".format(imageName))


def main():
    for i in range(1, 101):
        url ="http://www.doutula.com/photo/list/?page={}".format(i)
        parse(url)
        break


if __name__ == "__main__":
    main()