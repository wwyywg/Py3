#coding=utf-8
import os
import time

"""
父进程、子进程执行顺序没有规律，完全取决于操作系统的调度算法
"""

if __name__ == '__main__':
    pid = os.fork()
    if pid == 0:
        print('哈哈1')
    else:
        print('哈哈2')

    pid = os.fork()
    if pid == 0:
        print('哈哈3')
    else:
        print('哈哈4')

    time.sleep(1)