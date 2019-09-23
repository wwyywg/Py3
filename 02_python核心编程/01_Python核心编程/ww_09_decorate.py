# 定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

# 定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makeItalic
def test2():
    return "hello world-1"

@makeBold
@makeItalic
def test3():
    return "hello world-3"

@makeBold
def test1():
    return "hello world-1"

if __name__ == '__main__':
    print(test1())
    print(test2())
    print(test3())