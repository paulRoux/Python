from datetime import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler

def timeTask():
    print(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])

if __name__ == "__main__":
    # 创建后台执行的 schedulers
    scheduler = BackgroundScheduler()
    # 添加调度方法
    # 调度方法为timeTask，触发器选择 interval(间隔性)，间隔时间为2秒
    scheduler.add_job(timeTask, 'interval', seconds=2, id="jobOne")  #方法1
    # scheduler .add_job(timeTask, 'cron', month='1-3,7-9',day='0, tue', hour='0-3')  ## 方法2
    scheduler.start()
    scheduler.shutdown()  ## wait=False 表示不等待直接结束

    while True:
        print(time.time)
        time.sleep(2)
