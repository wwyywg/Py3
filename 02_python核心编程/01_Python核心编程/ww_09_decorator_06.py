class Test11(object):
    def __call__(self):
        print('call me!')

class Test(object):
    def __init__(self, func):
        print("---初始化---")
        print("func name is %s" %func.__name__)
        self.__func = func

    def __call__(self, *args, **kwargs):
        print("--装饰器中的功能---")
        self.__func()

"""
1. 当用Test来装作装饰器对test函数进行装饰的时候，首先会创建Test的实例对象
    并且回把test这个函数名当做参数传递到__init__方法中
    即在__init__ 方法中的func变量指向了test函数体
2. test函数相当于指向了用Test创建出来的实例对象
3. 当在使用test()进行调用使，就相当于让这个对象(),因此调用这个对象的__call__方法
4. 为了能够在__call__方法中调用原来test指向的函数体，所以在__init__方法self.__func = func
    所以才有了self.__func = func这句代码，从而在调用__call__方法中能够执行 func方法
"""
@Test
def test():
    print("---test---")

if __name__ == '__main__':
    # t = Test11()
    # t()
    test()