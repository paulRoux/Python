from flask import Flask, request, abort, Response

app = Flask(__name__)


@app.route("/index", methods=["GET", "POST"])
def index():
    # request包含前端发送的数据
    # 通过form可以直接提取表单格式的数据，是一个类字典的对象，其余的数据可以使用data提取
    # 通过postman进行测试
    name = request.form.get("name")  # 如果有重复的参数，那么会默认取第一个。如果要取所有的使用getlist方法
    age = request.form.get("age")
    print(request.data)
    # args可以获取url?后面的查询字符串，是一个类字典对象
    city = request.args.get("city")
    return "hello name={} age={} city={}".format(name, age, city)


# 文件操作
@app.route("/upload", methods=["GET", "POST"])
def upload():
    pic = request.files.get("pic")
    if pic is None:
        return "no file"
    else:
        # data = pic.read()
        # with open("./demo.png", "wb") as f:
        #     f.write(data)

        # 因为flask进行了封装，所以可以省略上面的步骤，直接调用save方法保存
        pic.save("./demo.png")
        return "successfully"


# abort 操作
@app.route("/login", methods=["GET"])
def login():
    name = ""
    pwd = ""
    if name is None and pwd is None:
        # 使用abort可以立即终止视图函数，并给前端返回特定的错误信息
        abort(404)
        # resp = Response("login failed")
        # abort(resp)

    return "login success"


# 自定义错误处理
@app.errorhandler(404)
def handler_404_error(err):
    # 此函数返回值为前端所展示的结果
    return "login page not found. {}".format(err)


if __name__ == "__main__":
    app.run()
