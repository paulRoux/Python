from queue import Queue

num = 5
q = Queue(num)

print(q.qsize())
print(q.maxsize)

for i in range(5):
    q.put(i)  # 默认阻塞

print(q.full())

for x in range(5):
    print(q.get())  # 默认阻塞

print(q.full())

for i in range(5):
    pass