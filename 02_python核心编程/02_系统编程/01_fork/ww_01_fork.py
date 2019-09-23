import os

if __name__ == '__main__':
    pid = os.fork()

    if pid == 0:
        print('哈哈1')
    else:
        print('哈哈2')