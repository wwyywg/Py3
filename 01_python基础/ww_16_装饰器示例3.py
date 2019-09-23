from time import ctime, sleep

def timefun(func):
    def wrappedfunc(*args, **kwargs):
        print("%s celled at %s" %(func.__name__, ctime()))
        func(*args, **kwargs)
    return wrappedfunc


@timefun
def foo(a, b, c):
    print(a+b+c)


def main():
    foo(3, 5, 7)
    sleep(2)
    foo(2, 4, 9)

if __name__ == '__main__':
    main()