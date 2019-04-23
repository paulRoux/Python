import asyncio
import aiohttp
from sys import stdout
from time import sleep
from proxyPool.dataBase import RedisClient
from proxyPool.setting import VALID_STATUS_CODES, TEST_URL, BATCH_TEST_SIZE
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError



class Tester(object):
    def __init__(self):
        self.redis = RedisClient()

    async def testSingleProxy(self, proxy):
        """
        测试单个代理
        :param proxy:
        :return:
        """
        conn = aiohttp.TCPConnector(verify_ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy, bytes):
                    proxy = proxy.decode('utf-8')
                realProxy = 'http://' + proxy
                print('正在测试: ', proxy)
                async with session.get(TEST_URL, proxy=realProxy, timeout=15, allow_redirects=False) as response:
                    if response.status in VALID_STATUS_CODES:
                        self.redis.max(proxy)
                        print('代理可用', proxy)
                    else:
                        self.redis.decrease(proxy)
                        print('请求响应码不合法 ', response.status, 'IP', proxy)
            except (ClientError, aiohttp.client_exceptions.ClientConnectorError, asyncio.TimeoutError, AttributeError):
                print('代理请求失败: ', proxy)
                self.redis.decrease(proxy)

    def run(self):
        """
        测试主函数
        :return:
        """
        print('测试器开始运行!')
        try:
            count = self.redis.count()
            print('当前剩余', count, '个代理')
            for i in range(0, count, BATCH_TEST_SIZE):
                start = i
                end = min(i + BATCH_TEST_SIZE, count)
                print('正在测试第', start + 1, '-', end, '个代理')
                testProxies = self.redis.batch(start, end)
                loop = asyncio.get_event_loop()
                tasks = [self.testSingleProxy(proxy) for proxy in testProxies]
                loop.run_until_complete(asyncio.wait(tasks))
                stdout.flush()
                sleep(5)
        except Exception as e:
            print('测试器发生错误', e.args)
