def fib(times):
    n = 0
    a,b = 0,1
    while n < times:
        print(b)
        a, b = b, a+b
        n+=1
    return 'done'

def fib2(times):
    n = 0
    a,b = 0,1
    while n < times:
        yield b
        a, b = b, a+b
        n+=1
    return 'done'

if __name__ == '__main__':
    # 创建生成器方法1
    L = [x*2 for x in range(5)]
    G = (x*2 for x in range(5))
    # for n in fib2(5):
    #     print(n)
    g= fib2(5)
    while True:
        try:
            x= next(g)
            print("value:%d" %x)
        except StopIteration as e:
            print("生成器返回值：%s" %e.value)
            break