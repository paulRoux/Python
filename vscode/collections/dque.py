from collections import deque

## deque:线程安全(GIL), list:不是线程安全

userList = ["shunxing", 24]
userAge = userList.pop()
print(userAge, userList)

# 尽量保存相同类型的数据
userDeque = deque(("shunxing", 24, ["hello", "world"]))  ## 接受一个可迭代的对象
userDeque.append("gc")
userDeque.appendleft("xia")

userDeque1 = userDeque.copy()  ## 进行的是浅拷贝，如果里面有可变元素，拷贝的修改会影响原始数据
## 进行深拷贝
import copy
userDeque1 = copy.deepcopy(userDeque)
userDeque1[2] = 100
userDeque1[3].append("!")

print(id(userDeque), id(userDeque1))
print(userDeque)
print(userDeque1)

userDeque2 = deque(["i", "am"])
userDeque2.extend(userDeque)  ## 没有返回值
print(userDeque2)
