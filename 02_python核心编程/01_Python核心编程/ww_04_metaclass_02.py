class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__ 是用来创建对象并返回值的方法
    # 而 __init__ 只是用来将传入的参数初始化给对象
    # 你很少用到 __new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，

    def __new__(cls, future_class_name,future_class_parents, future_class_attr):
        # 遍历属性字典，把不是__开头的属性名字变为大写
        newAttr = {}
        for name, value in future_class_attr.items():
            if not name.startswith("__"):
                newAttr[name.upper()] = value

        # 方法1：通过'type'来做类对象的创建
        # return type(future_class_name, future_class_parents, future_class_attr)

        # 方法2：复用type.__new__方法
        # 这就是基本的OOP编程，没有什么魔法
        # return type.__new__(cls, future_class_name, future_class_parents, future_class_attr)

        # 方法3：使用super方法
        return super(UpperAttrMetaClass, cls).__new__(cls, future_class_name, future_class_parents, future_class_attr)

class Foo(object, metaclass=UpperAttrMetaClass):
    bar = 'bip'

if __name__ == '__main__':
    print(hasattr(Foo, 'bar'))

    print(hasattr(Foo, 'BAR'))

    foo = Foo()
    print(foo.BAR)