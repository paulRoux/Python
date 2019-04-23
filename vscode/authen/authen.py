import requests

BASEURL = 'https://api.github.com'

def constructUrl(endPoint):
    return '/'.join([BASEURL, endPoint])

def baseAuth():
    "基本认证"
    response = requests.get(constructUrl('user'), auth = ('imoocdemo', 'imoocdemo123'))
    print(response.text)
    print(response.request.headers)

def baseOauth():
    headers = {'Authorization': 'token dd6322fa6c57a548268453dc245cbcdc352a7811'}
    # user/emails
    response = requests.get(constructUrl('user/emails'), headers = headers)
    print(response.request.headers)
    print(response.text)
    print(response.status_code)

from requests.auth import AuthBase

class GithubAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        # requests + headers
        r.headers['Authorization'] = ' '.join(['token', self.token])
        return r

def advanceAuth():
    auth = GithubAuth('dd6322fa6c57a548268453dc245cbcdc352a7811')
    response = requests.get(constructUrl('user/emails'), auth = auth)
    print(response.text)


if __name__ == '__main__':
    #baseOauth() #得到的结果可以通过base64解码，不安全
    advanceAuth()