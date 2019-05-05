from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # 查看整个flask中的路由信息
    print(app.url_map)
    app.run()
