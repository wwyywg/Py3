# coding=utf-8
import os
import time

"""
多进程中，每个进城所有数据（包括全局变量）都各拥有一份，互不影响
"""

num = 0

pid = os.fork()

if __name__ == '__main__':
    if pid == 0:    # 子进程执行
        num+=1
        print("哈哈1---num=%d"%num)
    else:
        time.sleep(1)
        num+=1
        print("哈哈2---num=%d"%num)
