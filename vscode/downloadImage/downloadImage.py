import requests

def downloadImage():
    "download image"
    url = "http://img4.imgtn.bdimg.com/it/u=3379997488,1338306262&fm=26&gp=0.jpg"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36', 'Referer': 'http://image.baidu.com'}
    #headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'}
    response = requests.get(url, headers = headers, stream = True)
    with open('demo.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)

def downloadImageImprove():
    "download image"
    url = "http://img4.imgtn.bdimg.com/it/u=3379997488,1338306262&fm=26&gp=0.jpg"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36', 'Referer': 'http://image.baidu.com'}
    response = requests.get(url, headers = headers, stream = True)
    from contextlib import closing
    with closing(requests.get(url, headers = headers, stream = True)):
        with open('demo1.jpg', 'wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)


if __name__ == "__main__":
    downloadImageImprove()