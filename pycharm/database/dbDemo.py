from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, func
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/demo"
    # 设置自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# 创建DB对象
db = SQLAlchemy(app)


# 创建数据库模型类
class User(db.Model):
    # 指定数据库的表名
    __tablename__ = "tbl_users"

    # 整型的逐渐，会默认自增
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("tbl_roles.id"))

    def __repr__(self):
        # 定义对象的显示
        return "Role object: name={}".format(self.name)


class Role(db.Model):
    __tablename__ = "tbl_roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    # 建立模型类的关联，用来查找Users，使用user.role直接找到user对应的role
    users = db.relationship("User", backref="role")

    def __repr__(self):
        # 定义对象的显示
        return "Role object: name={}".format(self.name)


# @app.route("/")
# def index():
#     pass


if __name__ == '__main__':
    # app.run()
    # 清除数据库的所有数据
    db.drop_all()
    # 创建所有的表
    db.create_all()

    # 创建对象
    role = Role(name="admin")
    # session记录对象任务
    db.session.add(role)
    # 提交事务
    db.session.commit()

    user = User(name="roux", email="roux@qq.com", password="111", role_id=role.id)
    db.session.add(user)
    # 提交多条数据
    # db.session.add_all([])
    db.session.commit()

    # all 返回的是列表
    # db.session.query(Role).all()  # Role.query.all()
    # get只能传id
    # db.session.query(Role).get(1)
    db.session.query(Role).first()

    # 如果查询不存在返回None类型
    # User.query.filter_by(name="roux").all()
    # User.query.filter_by(name="roux", role_id=1).first()
    User.query.filter(User.name == "roux", User.role_id == 1).first()
    User.query.filter(or_(User.name == "roux", User.email.endswith("qq.com"))).all()

    # 从第二条元素开始取
    User.query.offset(2).all()
    User.query.offset(1).limit(2).all()
    # User.query.order_by("-id").all()  # 不推荐
    User.query.order_by(User.id.desc()).all()
    db.session.query(User.role_id, func.count(User.role_id)).group_by(User.role_id).all()

    User.query.filter_by(name="roux").update({"name": "shirsen", "email": "shirsen@qq.com"})
    db.session.commit()

    # 删除 data这条数据
    data = User()
    db.session.delete(data)
