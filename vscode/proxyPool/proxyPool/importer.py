from proxyPool.dataBase import RedisClient

conn = RedisClient()

def set(proxy):
    result = conn.add(proxy)
    print(proxy)
    print(proxy, "录入成功!" if result else "录入失败!")


def scan():
    print("请输入代理，exit退出输入!")
    while True:
        proxy = input()
        if proxy == "exit":
            break
        set(proxy)

if __name__ == "__main__":
    scan()