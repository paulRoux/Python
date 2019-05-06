from flask import Flask, render_template, flash

app = Flask(__name__)
flag = True

app.config["SECRET_KEY"] = "roux"


@app.route("/")
def index():
    global flag
    if flag:
        flash("hello roux")
        flag = False
    return render_template("macro.html")


if __name__ == "__main__":
    app.run()
