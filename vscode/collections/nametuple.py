from collections import namedtuple

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# basic
User = namedtuple("User", ["name", "age"])
user = User(name = "shuxning", age = 24)
print(user.name, user.age)

# tuple
userTuple = ("shunxing", 24)
user = User(*userTuple)  # or user = User._make(userTuple)
print(user.name, user.age)

# dict
userDict = {
    "name":"shunxing",
    "age":24
}
user = User(**userDict)  # or user = User._make(userDict)
print(user.name, user.age)

# make method: 没有灵活性
userList = ["shunxing", 24]
user = User._make(userList)
print(user.name, user.age)

userInfo = user._asdict()  # sort

# 拆包
name, age = user
print(name, age)


# *args and **kwargs
def ask(*args, **kwargs):
    pass

ask("shunxing", 24)  # args is tuple
ask(name = "shunxing", age = 29)  # kwargs is dict