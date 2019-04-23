from collections import OrderedDict

## 有序的，先添加的在前面后添加的在后面
userDict = OrderedDict()
userDict["a"] = "shunxing"
userDict["b"] = "gc"
userDict["c"] = "xsx"
#print(userDict.popitem())
#print(userDict.pop("b"))

print(userDict.move_to_end("b"))
print(userDict)