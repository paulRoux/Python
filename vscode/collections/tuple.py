
# tuple是不可变的，并且有自动解析的功能
userTuple = ("shunxing", 24, "beijing", "edu")
name, age, home, edu = userTuple
name, *others = userTuple
print(name, others)


# 在tuple里面存放可变对象，导致tuple相对可变
nameTuple = ("gc", 23, ["shanxi", "off"])
print(nameTuple)
nameTuple[2].append("hello")
print(nameTuple)

userInfoDict = {}
userInfoDict[userTuple] = "xia"
print(userInfoDict)
