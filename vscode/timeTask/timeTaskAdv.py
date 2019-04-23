from datetime import datetime
import sched
import time

def timeTask():
    # 初始化 sched 模块的 scheduler 类
    # 无法做到循环定时任务，需要再次添加
    scheduler = sched.scheduler(time.time, time.sleep)
    # 增加调度任务
    scheduler.enter(3, 1, task)
    # 运行
    scheduler.run()

def task():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    timeTask()