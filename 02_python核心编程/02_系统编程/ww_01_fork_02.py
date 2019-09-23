import os
import time

num = 0

# 注意，for函数，只在Unix/Linux/Mac上运行，Windows不可以
pid = os.fork()

if __name__ == '__main__':

    if pid == 0:
        num += 1
        print("哈哈1---num=%d" %num)
    else:
        time.sleep(1)
        num += 1
        print("哈哈2---num=%d" %num)

    pid = os.fork()
    if pid == 0:
        print("哈哈3")
    else:
        print("哈哈4")

    time.sleep(1)