import json
from flask import Flask, g
from cookiesProxy.dataBase import RedisClient
from cookiesProxy.config import GENERATOR_MAP

__all__ = ["app"]

app = Flask(__name__)


def getConn():
    """
    获取
    :return:
    """
    for website in GENERATOR_MAP:
        print(website)
        if not hasattr(g, website):
            setattr(g, website + "_cookies", eval("RedisClient" + "('cookies', '"+ website + "')"))
            setattr(g, website + "_accounts", eval("RedisClient" + "('accounts', '"+ website + "')"))
    return g



@app.route('/')
def index():
    return "<h2>Welcome to Cookies Pool System</h2>"


@app.route('/<websites>/random')
def random(websites):
    """
    获取随机的Cookie, 访问地址如 /weibo/random
    :return: 随机Cookie
    """
    g = getConn()
    cookies = getattr(g, websites + "_cookies").random()
    return cookies


@app.route('/<website>/add/<username>/<password>')
def add(websites, username, password):
    """
    添加用户, 访问地址如 /weibo/add/user/password
    :param website: 站点
    :param username: 用户名
    :param password: 密码
    :return:
    """
    g = getConn()
    print(username, password)
    getattr(g, websites + "_accounts").set(username, password)
    return json.dumps({"status": "1"})


@app.route("/<website>/count")
def count(websites):
    """
    获取Cookies总数
    """
    g = getConn()
    count = getattr(g, websites + "_cookies").count()
    return json.dumps({"status": "1", "count": count})


if __name__ == "__main__":
    app.run(host="127.0.0.1")