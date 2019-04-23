from time import sleep
from multiprocessing import Process
from cookiesProxy.api import app
from cookiesProxy.config import TESTER_MAP, CYCLE, GENERATOR_MAP, API_HOST, API_PORT, \
    API_PROCESS, GENERATOR_PROCESS, VALID_PROCESS


class Scheduler(object):
    @staticmethod
    def validCookie(cycle=CYCLE):
        while True:
            print("Cookies检测程序开始运行!")
            try:
                for websites, cls in TESTER_MAP.items():
                    tester = eval(cls + "(websites='" + websites + "')")
                    tester.run()
                    print("Cookies检测完成!")
                    del tester
                    sleep(cycle)
            except Exception as e:
                print(e.args)


    @staticmethod
    def generateCookie(cycle=CYCLE):
        while True:
            print("Cookies生成进程开始运行!")
            try:
                for websites, cls in GENERATOR_MAP.items():
                    generator = eval(cls + "(websites='" + websites + "')")
                    generator.run()
                    print("Cookies生成完成!")
                    generator.close()
                    sleep(cycle)
            except Exception as e:
                print(e.args)


    @staticmethod
    def api():
        print("Api接口开始运行!")
        app.run(host=API_HOST, port=API_PORT)


    def run(self):
        if API_PROCESS:
            apiProcess = Process(target=Scheduler.api)
            apiProcess.start()

        if GENERATOR_PROCESS:
            generateProcess = Process(target=Scheduler.generateCookie)
            generateProcess.start()

        if VALID_PROCESS:
            validProcess = Process(target=Scheduler.validCookie)
            validProcess.start()
