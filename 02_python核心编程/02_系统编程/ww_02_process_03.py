# coding=utf-8
from multiprocessing import Process
import time
import os

# 两个字进城将会调用的两个方法
def worker_1(interval):
    print("worker_1,父进程(%s),当前进城(%s)" %(os.getppid(),os.getpid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("worker_1,执行时间为'%0.2f'秒" %(t_end - t_start))

def worker_2(interval):
    print("worker_2,父进程(%s),当前进城(%s)" %(os.getppid(),os.getpid()))
    t_start = time.time()
    time.sleep(interval)
    t_end = time.time()
    print("worker_2,执行时间为'%0.2f'秒" %(t_end - t_start))

if __name__ == '__main__':
    print("进城ID：%s" %os.getpid())

    p1 = Process(target=worker_1, args=(2,))
    p2 = Process(target=worker_2, name="dongGe", args=(1,))

    p1.start()
    p2.start()

    # 同时父进程乃然往下执行，如果p2进城还在执行，将会返回True
    print("p2.is_alive=%s" %p2.is_alive())

    # 输出p1和p2进城的别名和pid
    print("p1.name=%s"%p1.name)
    print("p1.pid=%s"%p1.pid)
    print("p2.name=%s"%p2.name)
    print("p2.pid=%s"%p2.pid)

    # join括号中不携带参数，表示父进程在这个位置要等待p1进程执行完
    # 一般用于进城间的数据同步
    p1.join(1)
    print("p1.is_alive=%s"%p1.is_alive())