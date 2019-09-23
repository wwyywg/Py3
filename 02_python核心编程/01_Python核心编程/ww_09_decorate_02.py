from time import ctime, sleep

'''
foo = timefun(foo)
# foo先作为参数赋值给func后，foo接收指向timefun返回的wrappedfunc
foo()
# 调用foo()，即等价调用wrappedfunc()
# 内部函数wrappedfunc被引用，所以外部函数的func变量(自由变量)并没有释放
# func 里保存的是原foo函数对象
'''

def timefun(func):
    def wrappedfunc():
        print("%s called at %s" %(func.__name__, ctime()))
        func()
    return wrappedfunc

@timefun
def foo():
    print("I am foo")

def timefun2(func):
    def wrappedfunc(a, b):
        print("%s called at %s" %(func.__name__, ctime()))
        print(a, b)
        func(a, b)
    return wrappedfunc

@timefun2
def foo2(a, b):
    print(a+b)

if __name__ == '__main__':
    foo()
    sleep(2)
    foo()

    foo2(3, 5)
    sleep(2)
    foo2(2, 4)