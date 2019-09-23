from threading import Thread
import time

'''
多线程-共享全局变量
'''

g_num = 100

def work1():
    global g_num
    for i in range(3):
        g_num += 1

    print("---in work1, g_num is %d---"%g_num)

def work2():
    global  g_num
    print("---in work2, g_num is %d---"%g_num)

if __name__ == '__main__':

    print("---线程创建之前g_num is %d---"%g_num)

    t1 = Thread(target=work1)
    t1.start()

    # 延时一会
    time.sleep(1)

    t2 = Thread(target=work2)
    t2.start()