from datetime import datetime
from threading import Timer
import time

def timeTask():
    '''
    第一个参数: 延迟多长时间执行任务(单位: 秒)
    第二个参数: 要执行的任务, 即函数
    第三个参数: 调用函数的参数(tuple)
    '''
    Timer(3, task, ()).start()

def task():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    timeTask()
    while True:
        print(time.time())
        time.sleep(5)