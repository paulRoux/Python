from flask_script import Manager
from app import app, db
from modelsSql import User
from modelsNosql import User


manager = Manager(app)


@manager.command
def save():
    # Sql
    # user = User(1, 'roux')
    # db.session.add(user)
    # db.session.commit()

    # Nosql
    # user = User("roux", "roux@qq.com")
    # user.save()

    user = User("shirsen", "shirsen@qq.com")
    user.save()



@manager.command
def queryAll():
    # Sql
    # users = User.query.all()
    # for user in users:
    #     print(user)

    # Nosql
    # users = User.quertUser()
    # for user in users:
    #     print(user)

    users = User.objects.all()
    for user in users:
        print(user)


if __name__ == "__main__":
    manager.run()
