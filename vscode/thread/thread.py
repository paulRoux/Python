import threading

def run(args):
    print("current task: ", args)

if __name__ == "__main__":
    thread1 = threading.Thread(target=run, args=("thread 1",))
    thread2 = threading.Thread(target=run, args=("thread 2",))

    threads = []
    threads.append(thread1)
    threads.append(thread2)

    for th in threads:
        th.start()

    for th in threads:
        th.join()