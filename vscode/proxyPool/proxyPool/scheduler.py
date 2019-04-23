from time import sleep
from multiprocessing import Process
from proxyPool.api import app
from proxyPool.getter import Getter
from proxyPool.tester import Tester
from proxyPool.setting import TESTER_CYCLE, GETTER_CYCLE, API_HOST, API_PORT, \
    TESTER_ENABLED, GETTER_ENABLED, API_ENABLED


class Scheduler():
    def scheduleTest(self, cycle=TESTER_CYCLE):
        """
        定时测试代理
        """
        test = Tester()
        while True:
            print("测试器开始运行!")
            test.run()
            sleep(cycle)


    def scheduleGet(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        """
        get = Getter()
        while True:
            print("开始抓取代理!")
            get.run()
            sleep(cycle)


    def scheduleApi(self):
        """
        开启API
        """
        app.run(API_HOST, API_PORT)


    def run(self):
        print("代理池开始运行!")
        if TESTER_ENABLED:
            testProcess = Process(target=self.scheduleTest)
            testProcess.start()

        if GETTER_ENABLED:
            getProcess = Process(target=self.scheduleGet)
            getProcess.start()

        if API_ENABLED:
            apiProcess = Process(target=self.scheduleApi)
            apiProcess.start()