'''
闭包
'''

def test(number):

    # 在函数内部再定义一个函数，并且这个函数用到了外边函数的变量，那么将这个方法
    def test_in(number_in):
        print("in test_in 函数，number_in is %d" %number_in)
        return number + number_in
    # 其实这里返回的就是闭包的结果
    return test_in

def counter(start=0):
    count = [start]
    def incr():
        count[0] += 1
        return count[0]
    return incr

if __name__ == '__main__':
    # 给test 函数赋值，这个20就是给参数number
    ret = test(20)

    # 注意这里的100其实给参数number_in
    print(ret(100))

    # 注意这里的200其实给参数number_in
    print(ret(200))