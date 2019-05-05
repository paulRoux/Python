from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# 提取参数
@app.route("/goods/<int:goodsId>")
def goods(goodsId):
    return "goods detail {}".format(goodsId)


# 定义自己的通用转换器
class RegexConverter(BaseConverter):
    # url_map是固定参数类型，是整个flask的路由列表
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，flask使用其路由匹配
        self.regex = regex

    # 可以在这个父类的方法中做一些更高级的操作，比如过滤等。最终的return才会被视图函数的参数接收
    # value是被正则提取出来的参数
    def to_python(self, value):
        print("to_python method")
        return value

    # 这个方法接收的是url_for的参数，然后处理返回最终拼接成url
    def to_url(self, value):
        print("to_url method")
        return value


# 添加自定义的转换器到flask里面， 名字自己取
app.url_map.converters["re"] = RegexConverter


# 自定义正则表达式，需要构建一个类re，然后接受参数为一个正则表达式(r'')
@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
def sendMsg(mobile):
    return "send msg to {}".format(mobile)


@app.route("/index")
def index():
    # 由于sendMsg里面含有正则等，无法转换直接传递
    # return redirect(url_for("sendMsg"))
    return redirect(url_for("sendMsg", mobile="13892996577"))


if __name__ == '__main__':
    # 查看整个flask中的路由信息
    print(app.url_map)
    app.run()
