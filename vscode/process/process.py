from multiprocessing import Process

def show(name):
    print("Process name is: ", name)

if __name__ == "__main__":
    proc = Process(target=show, args=("subprocess",))
    proc.start()
    proc.join()