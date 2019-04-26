import requests
import os
import re
import threading
from lxml import etree
from fake_useragent import UserAgent
from urllib import request
from queue import Queue


class Producer(threading.Thread):
    ua = UserAgent().chrome

    headers = {
        "User-Agent": ua
    }

    def __init__(self, pageQueue, imgQueue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.pageQueue = pageQueue
        self.imgQueue = imgQueue


    def run(self):
        while True:
            if self.pageQueue.empty():
                break
            url = self.pageQueue.get()
            self.parse(url)


    def parse(self, url):
        response = requests.get(url, headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        imgsUrl = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']/@data-original")
        imgsName = html.xpath("//div[@class='page-content text-center']//p/text()")
        for url, name in zip(imgsUrl, imgsName):
            imageUrl = str(url).rstrip("!dta")
            suffix = os.path.splitext(imageUrl)[1]
            imageName = re.sub(r'[\??\.，。\* ]', '', name) + suffix
            self.imgQueue.put(imageUrl, imageName)


class Consumer(threading.Thread):
    def __init__(self, pageQueue, imgQueue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.pageQueue = pageQueue
        self.imgQueue = imgQueue


    def run(self):
        while True:
            if self.imgQueue.empty() and self.pageQueue.empty():
                break
            imgUrl, fileName = self.imgQueue.get()
            request.urlretrieve(imgUrl, "doutula/images/{}".format(fileName))



def main():
    pageQueue = Queue(100)
    imageQueue = Queue(1000)

    for i in range(1, 101):
        url ="http://www.doutula.com/photo/list/?page={}".format(i)
        pageQueue.put(url)
        # break

    for x in range(5):
        pro = Producer(pageQueue, imageQueue)
        pro.start()

    for x in range(3):
        con = Consumer(pageQueue, imageQueue)
        con.start()


if __name__ == "__main__":
    main()