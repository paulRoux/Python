from flask import Flask, session

app = Flask(__name__)

# flask默认把session保存到cookie里面
# 加入secret_key防篡改
app.config["SECRET_KEY"] = "roux"


@app.route("/index")
def index():
    name = session.get("name")
    return "hello {}".format(name)


@app.route("/login")
def login():
    session["name"] = "roux"
    session["mobile"] = "13892996577"
    return "login success"


if __name__ == "__main__":
    app.run()