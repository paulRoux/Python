from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


# 创建Flask应用程序实例
# 需要传入__name__，确定资源所在路径
app = Flask(__name__)

app.secret_key = 'roux'


# 定义路由及视图函数
# Flask中定义路由是由装饰器实现的
# 默认的路由只支持GET
# @app.route('/', methods=['GET', 'POST'])
# def hello_world():
#     return 'Hello Flask!'


# @app.route('/')
# def index():
#     url = 'www.baidu.com'
#     list = [1, 2, 3, 4, 5]
#     dict = {
#         'name': '百度',
#         'url': 'www.baidu.com'
#     }
#     return render_template('index.html', url=url, list=list, dict=dict)


class LoginForm(FlaskForm):
    username = StringField('用户名:', validators=[DataRequired()])
    password = PasswordField('密码:', validators=[DataRequired()])
    password2 = PasswordField('确认密码:', validators=[DataRequired(), EqualTo('password', '密码不一致')])
    submit = SubmitField('提交')


@app.route('/form', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if login_form.validate_on_submit():
            return 'successful'
        else:
            flash('参数有误')

    return render_template('login.html', login_form=login_form)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if not all([username, password, password2]):
            # print("参数不完整！")
            flash(u"参数不完整！")
        elif password != password2:
            # print("密码不一致！")
            flash(u"密码不一致！")
        else:
            return 'successful'
    else:
        return



# 使用同一个视图，来显示不同用户的订单信息
# <>来定义一个路由参数
@app.route('/orders/<int:order_id>')
def get_order_id(order_id):

    # 参数类型默认为字符串 unicode
    print(type(order_id))

    # 需要在函数内传入参数,后面的代码才能使用
    return 'order_id is {}'.format(order_id)


# 启动程序
if __name__ == '__main__':
    app.run()
