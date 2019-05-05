from flask import Flask, current_app

# 默认以当前模块的目录为总目录，默认这个目录下的static为静态目录，templates为模板目录
# app = Flask(__name__)

# 初始化参数
app = Flask(
    __name__,
    static_url_path="/static",  # url访问的路径
    static_folder="static",  # 静态文件的目录， 默认相对路径static
    template_folder="templates"  # 模板文件的目录， 默认相对路径templates
)


# 配置参数
# 使用配置文件
# app.config.from_pyfile("config.cfg")

# 使用对象配置参数
class Config(object):
    DEBUG = True
    ROUX = True


app.config.from_object(Config)

# 直接操作config字典
app.config["DEBUG"] = True


@app.route('/')
def hello_world():
    # 从全局对象app的config的字典中取值
    print(app.config.get("ROUX"))

    # 通过current_app获取
    print(current_app.config.get("ROUX"))

    return 'Hello World!'


if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0", port=5000)
    # app.run(host="0.0.0.0", host=5000, debug=True)
