from collections import Counter

users = ["shunxing", "gc", "shunxing", "gc", "gc"]
userCounter = Counter(users)
print(userCounter)

string = "sadsajkdhgsfkhsdskadhslk"
count = Counter(string)  ## 可以传递字符串或者可迭代的对象
count.update("lkhkjknkjjbnjhkn")
string1 = "uhbdsfiudshfdkjsbf"
count.update(string1)
# top k
print(count.most_common(2))
print(count)