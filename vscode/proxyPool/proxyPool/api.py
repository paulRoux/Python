from flask import Flask, g

from proxyPool.dataBase import RedisClient


__all__ = ['app']

app = Flask(__name__)

def getConn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return "<h2>Welcome to Proxy Pool System</h2>"


@app.route('/random')
def getProxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = getConn()
    return conn.random()


@app.route('/count')
def getCount():
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = getConn()
    return str(conn.count())


if __name__ == "__main__":
    app.run()
