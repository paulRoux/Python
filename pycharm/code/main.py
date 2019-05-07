from flask import Flask
from bluePrint import app_orders
from cart import app_cart

app = Flask(__name__)


# 循环引用的解决方法，可以让一方先完成，另一方推迟
# 或者可以利用装饰器的特性，可以先定义函数，后用装饰器装饰

# 注册蓝图
app.register_blueprint(app_orders, url_prefix="/orders")
app.register_blueprint(app_cart, url_prefix="/cart")


@app.route("/")
def index():
    return "index page"


if __name__ == "__main__":
    print(app.url_map)
    app.run()
