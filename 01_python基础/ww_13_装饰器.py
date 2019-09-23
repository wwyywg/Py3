def foo():
    print("foo")


# 定义函数：完成数据包装
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


#定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


@makeBold
def test1():
    return "hello world-1"


@makeItalic
def test2():
    return "hello world-2"


@makeBold
@makeItalic
def test3():
    return "hello world-3"


def main():
    # print(foo)
    # foo()
    # foo = lambda x: x + 1
    # foo()
    print(test1())
    print(test3())

if __name__ == '__main__':
    main()