from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
app.config["SECRET_KEY"] = "roux"


class RegisterForm(FlaskForm):
    username = StringField(label="用户名:", validators=[DataRequired("用户名不能为空")])
    password = PasswordField(label="密码:", validators=[DataRequired("密码不能为空")])
    password2 = PasswordField(label="确认密码:", validators=[DataRequired("确认密码不能为空"),
                                                         EqualTo("password", "两次密码不一致")])
    submit = SubmitField(label="提交")


@app.route("/register", methods=["GET", "POST"])
def register():
    # 创建表单对象，如果是post请求，前端发送了数据，flask会把数据在构造form对象的时候存放到对象中
    form = RegisterForm()
    # 判断对象数据是否合理
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print((username, password))
        session["username"] = username
        return redirect(url_for("index"))

    return render_template("register.html", form=form)


@app.route("/")
def index():
    username = session.get("username", "")
    return "hello {}".format(username)


if __name__ == "__main__":
    app.run()
