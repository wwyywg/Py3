from time import ctime, sleep

# 无参数的函数
def timefun(func):
    def wrappedfunc():
        print("%s called at %s" %(func.__name__, ctime()))
        func()
    return wrappedfunc


@timefun
def foo():
    print("I am foo")


def main():
    foo()
    sleep(2)
    foo()


if __name__ == '__main__':
    main()