from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "hello flask"


# 钩子自己不会区分视图，需要我们自己区分，使用request.path

@app.before_first_request
def handle_before_first_request():
    print("handle_before_first_request")


@app.before_request
def handle_before_request():
    print("handle_before_request")


@app.after_request
def after_request(response):
    print("after_request")
    return response


@app.teardown_request
def teardown_request(response):
    # 忽略视图出现的异常
    print(request.path)
    print("teardown_request")
    return response


if __name__ == "__main__":
    app.run()
