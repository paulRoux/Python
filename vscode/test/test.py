from urllib import request
from fake_useragent import UserAgent
import re


headers = {
    "User-Agent": UserAgent().chrome
}


def main():
    url = "https://www.baidu.com"
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    html = response.read().decode("utf-8")
    print(html)

    reg = r'<div id="lg".*?src=(.*?) width=.*?'
    reg_img = re.compile(reg)
    imglist = re.findall(reg_img, html)
    print(imglist)


if __name__ == "__main__":
    main()