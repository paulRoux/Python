from cookiesProxy.dataBase import RedisClient


def getConn(type="type", websites="website"):
    conn = RedisClient(type, websites)
    return conn


def set(account, type="type", websites="website", sep="---"):
    username, password = account.split(sep)
    result = getConn().set(username, password)
    print("账号: {} 密码 {}".format(username, password))
    print("录入成功！" if result else "录入失败！")


def scan(type="type", websites="website"):
    print("请输入账号密码组，输入exit退出读入！")
    while True:
        account = input()
        if account == "exit":
            break
        set(account, type, websites,)


if __name__ == "__main__":
    scan("accounts", "weibo")