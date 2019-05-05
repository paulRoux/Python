from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


# 限定访问方式
@app.route("/postOnly", methods=["GET", "POST"])
def postOnly():
    return "post only"


# 一个访问路径，两个访问视图函数(路径和请求方式一样)
@app.route("/hello")
def hello1():
    return "hello 1"


@app.route("/hello")
def hello2():
    return "hello 2"


# 两个访问路径，同一个访问视图函数
@app.route("/hello1")
@app.route("/hello2")
def hello():
    return "hello"


@app.route("/direct")
def direct():
    return redirect(url_for("index"))


if __name__ == '__main__':
    # 查看整个flask中的路由信息
    print(app.url_map)
    app.run()
