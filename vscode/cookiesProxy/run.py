from cookiesProxy.scheduler import Scheduler

def main():
    try:
        ## 运行调度器
        sche = Scheduler()
        sche.run()
    except:
        main()

if __name__ == "__main__":
    main()