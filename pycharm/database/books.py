from flask import Flask, render_template, request, \
    redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)


class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/demo"
    # 设置自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "roux"


app.config.from_object(Config)

db = SQLAlchemy(app)

# 创建脚本管理对象
manager = Manager(app)

# 创建数据库迁移工具
Migrate(app, db)

# 给manager对象添加数据库操作指令
manager.add_command("db", MigrateCommand)


class Author(db.Model):
    __tablename__ = "tbl_author"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    books = db.relationship("Book", backref="author")


class Book(db.Model):
    __tablename__ = "tbl_book"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_author.id"))


class AuthorForm(FlaskForm):
    authorName = StringField(label="作者:", validators=[DataRequired("作者必填!")])
    bookName = StringField(label="书籍:", validators=[DataRequired("书籍必填!")])
    submit = SubmitField(label="保存")


@app.route("/", methods=["GET", "POST"])
def index():
    form = AuthorForm()
    if form.validate_on_submit():
        name = form.authorName.data
        book = form.bookName.data
        author = Author(name=name)
        if name != Author.query.filter_by(name=name).first().name:
            db.session.add(author)
            db.session.commit()

        if book != Book.query.filter_by(name=name).first().name:
            books = Book(name=book, author_id=author.id)
            db.session.add(books)
            db.session.commit()

    authors = Author.query.all()
    return render_template("books.html", authors=authors, form=form)


@app.route("/delete/book", methods=["POST"])
def delete():
    # get_json要求前端发送的请求数据是json格式，会自动解析为字典
    # Content-Type是application/json
    req = request.get_json()
    bookId = req.get("book_id")

    book = Book.query.get(bookId)
    db.session.delete(book)
    db.session.commit()

    # return redirect(url_for("index"))
    return jsonify(code=0, message="OK")


if __name__ == "__main__":
    # db.drop_all()
    # db.create_all()
    # au_zh = Author(name="zhangsan")
    # au_li = Author(name="lisi")
    # db.session.add_all([au_zh, au_li])
    # db.session.commit()
    #
    # bk_zh = Book(name="Python", author_id=au_zh.id)
    # bk_li = Book(name="CPP", author_id=au_li.id)
    # db.session.add_all([bk_zh, bk_li])
    # db.session.commit()

    # app.run()
    manager.run()
    # 下面的db就是manager.add_command("db", MigrateCommand)里面的db
    # 终端操作第一步：python [filename] db init
    # 第二步：python [filename] db migrate [-m]
    # 第三步：python [filename] db upgrade
    # 历史查看：python [filename] db history
    # 回退版本：python [filename] db downgrade id
