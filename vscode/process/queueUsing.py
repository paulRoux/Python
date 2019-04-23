from multiprocessing import Process, Queue

def put(queue):
    queue.put("queue using")

if __name__ == "__main__":
    queue = Queue()
    pro = Process(target=put, args=(queue,))
    pro.start()
    print(queue.get())
    pro.join()