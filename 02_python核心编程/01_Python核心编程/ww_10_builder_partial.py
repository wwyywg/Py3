import functools

def showarg(*args, **kw):
    print(args)
    print(kw)

if __name__ == '__main__':
    p1 = functools.partial(showarg, 1,2,3)
    p1()
    p1(4,5,6)
    p1(a='python',b='itcast')

    p2 = functools.partial(showarg, a=3,b='linux')
    p2()
    p2(1,2)
    p2(a='python',b='itcast')