from multiprocessing import Process, Pipe

def show(conn):
    conn.send("pipe using")
    conn.close()

if __name__ == "__main__":
    ## 返回两个连接对象分别表示管道的两端
    parentConn, childConn = Pipe()
    pro = Process(target=show, args=(childConn,))
    pro.start()
    print(parentConn.recv())
    pro.join()