from collections import ChainMap

userDict1 = {"a": "xsx", "b": "gc"}
userDict2 = {"b": "gc", "d": "shirsen"}
## 重复太多
for key, value in userDict1.items():
    print(key, value)
for key, value in userDict2.items():
    print(key, value)

newDict = ChainMap(userDict1, userDict2)
for key, value in newDict.items():
    print(key, value)

newDict.new_child({"e": "shunxing"})
## maps 是指向，不是拷贝
print(newDict.maps)
newDict.maps[0]["a"] = "hello world!"