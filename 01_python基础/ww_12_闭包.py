# 定义一个函数

def test(number):

    # 在函数内部再定义一个函数,并且这个函数用到了外边函数的变量,那么将这个函数以及用到的一些变量称之为闭包
    def test_in(number_in):
        print("in test_in 函数, number_in is %d" % number_in)
        return number + number_in

    # 其实这里返回的就是闭包的结果
    return test_in


def counter(start=0):
    count = [start]
    def incr():
        count[0] += 1
        return count[0]
    return incr


def counter2(start=0):
    def incr():
        nonlocal start
        start += 1
        return start
    return incr


def line_conf(a, b):
    def line(x):
        return a * x + b
    return line


def main():
    # # 给test函数赋值，这个20就是给参数number
    # ret = test(20)
    # # 注意这里的100其实给参数number_in
    # print(ret(100))
    # # 注意这里的200其实给参数number_in
    # print(ret(200))

    # c1 = counter2(5)
    # print(c1())
    # print(c1())

    line1 = line_conf(1, 1)
    line2 = line_conf(4, 5)
    print(line1(5))
    print(line2(5))

if __name__ == '__main__':
    main()