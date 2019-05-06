from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = {
        "name": "roux",
        "age": 18,
        "myDict": {
            "city": "xian"
        },
        "myList": [1, 2, 3, 4, 5]
    }
    # return render_template("index.html", name="roux", age=18)
    return render_template("index.html", **data)


def listStep2(li):
    # 自定义过滤器
    return li[::2]


# 注册过滤器
app.add_template_filter(listStep2, "myList2")


@app.template_filter("myList3")
def listStep3():
    return li[::2]


if __name__ == "__main__":
    # app.run()
    app.run()
