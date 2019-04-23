import threading
import time

num = 0
mutex = threading.Lock()

## 重入锁
# mutex = threading.RLock()

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):
            num += 1
            msg = self.name + ': num value is ' + str(num)
            print(msg)
            mutex.release()

if __name__ == "__main__":
    for i in range(5):
        th = MyThread()

        ## 守护线程(需要在start之前启动)
        # th.setDaemon(bool)

        ## 定时器
        # th = threading.Timer(1, run)
        th.start()