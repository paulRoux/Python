from multiprocessing import Process
import time

class MyPrcess(Process):
    def __init__(self, name):
        super(MyPrcess, self).__init__()
        self.name = name

    def run(self):
        print("process name is: " + str(self.name))
        time.sleep(1)

if __name__ == "__main__":
    for i in range(3):
        pro = MyPrcess(str(i))
        pro.start()

    for i in range(3):
        pro.join()