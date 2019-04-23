from collections import defaultdict

users = ["shunxing", "gc", "shunxing", "gc", "gc"]
userDict = {}

# 判断容易出错并且代码过多显不清晰
for user in users:
    if user not in userDict:
        userDict[user] = 1
    else:
        userDict[user] += 1
print(userDict)
userDict.clear()

# version 1.0
for user in users:
    userDict.setdefault(user, 0)  # 少做一次查询操作
    userDict[user] += 1
print(userDict)

# version 2.0
"""
自动进行初始化为所传的对象的类型，并且只能传递可调用对象的名称
例如嵌套的dict就无法传递
"""
# default
defaultDict = defaultdict(int)
for user in users:
    defaultDict[user] += 1
print(defaultDict)

# func callable 解决无法传递嵌套的可调用对象
def genDefault():
    return {
        "name": "gc",
        "age": 23
    }
defaultDict = defaultdict(genDefault)
print(defaultDict["name"])