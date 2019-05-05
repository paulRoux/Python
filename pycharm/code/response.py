from flask import Flask, make_response, jsonify, request
# import json

app = Flask(__name__)


@app.route("/")
def route():
    return "hello flask"


@app.route("/index", methods=["GET", "POST"])
def index():
    # 返回自定义的响应信息
    # return "index page", 400, [("roux", "ok"), ("name", "sen")]
    # return "index page", 400, {"roux": "ok", "name": "sen"}
    # return "index page", 666, {"roux": "ok", "name": "sen"}
    # return "index page", "666 roux", {"roux": "ok", "name": "sen"}
    # return "index page", "666 roux"

    # make_response
    resp = make_response("index page 2")
    resp.status = "555 roux"
    resp.headers = {"roux": "ok"}
    return resp


@app.route("/json")
def jsonHandler():
    data = {
        "name": "roux",
        "age": 18
    }

    # json.dumps(data)
    # print(type(data), data)
    # json.loads(data)
    # print(type(data), data)
    # return data, 200, {"Content-Type": "application/json"}

    # 上面的所有操作由这个函数进行处理
    return jsonify(data)
    # 可以传参进行转换
    # return jsonify(name="roux", age=24)


@app.route("/cookie/set")
def setCookie():
    resp = make_response("success")
    # 设置cookie，默认有效期是临时有效，浏览器关闭就清除
    # resp.set_cookie("roux", "ok")
    # 指定有效期
    # resp.set_cookie("roux", "ok", max_age=3600)
    resp.headers["Set-Cookie"] = "roux=ok; hello=world, i am ok; Max-Age=3600"
    return resp


@app.route("/cookie/get")
def getCookie():
    cookie = request.cookies.get("roux")
    return cookie


@app.route("/cookie/delete")
def deleteCookie():
    resp = make_response("del success")
    # 删除cookie 相当于设置过期时间让它过期
    resp.delete_cookie("roux")
    return resp


if __name__ == "__main__":
    app.run()
