import threading
from time import sleep
from threading import Thread
from random import randint


MONEY = 1000
TOTAL_TIME = 10
LOCK = threading.Lock()


class Producer(Thread):
    def run(self):
        global MONEY, TOTAL_TIME
        while True:
            money = randint(100, 1000)
            LOCK.acquire()
            if TOTAL_TIME <= 0:
                LOCK.release()
                break
            TOTAL_TIME -= 1
            MONEY += money
            print("{} 生产了 {} 元，共有{}元！".format(threading.current_thread(), money, MONEY))
            LOCK.release()
            sleep(0.5)


class Consumer(Thread):
    def run(self):
        global MONEY, TOTAL_TIME
        while True:
            money = randint(100, 1000)
            LOCK.acquire()
            if TOTAL_TIME <= 0:
                LOCK.release()
                break
            if MONEY >= money:
                MONEY -= money
                print("{} 消费了 {} 元， 剩余 {} 元！".format(threading.current_thread(), money, MONEY))
            LOCK.release()
            sleep(0.5)


def main():
    for p in range(5):
        pro = Producer(name="生产者%d" % p)
        pro.start()

    for c in range(3):
        con = Consumer(name="消费者%d" % c)
        con.start()


if __name__ == "__main__":
    main()