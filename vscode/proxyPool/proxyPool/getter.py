from proxyPool.dataBase import RedisClient
from proxyPool.crawler import Crawler
from proxyPool.setting import POOL_UPPER

class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()


    def isOverPool(self):
        """
        判断是否达到了代理池的上限
        """
        if self.redis.count() >= POOL_UPPER:
            return True
        else:
            return False


    def run(self):
        print("获取器开始执行!")
        if not self.isOverPool():
            for callFuncLabel in range(self.crawler.__CrawlFuncCount__):
                callFunc = self.crawler.__CrawlFunc__[callFuncLabel]
                # 获取代理
                proxies = self.crawler.getProxies(callFunc)
                for proxy in proxies:
                    self.redis.add(proxy)