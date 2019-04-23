from io import TextIOWrapper
from sys import stdout
from proxyPool.scheduler import Scheduler

stdout = TextIOWrapper(stdout.buffer, encoding='utf-8')


def main():
    try:
        ## 运行调度器
        sche = Scheduler()
        sche.run()
    except:
        main()

if __name__ == "__main__":
    main()