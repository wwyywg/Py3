def gen():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1

if __name__ == '__main__':
    f = gen()
    # print(next(f))
    # print(next(f))
    # print(next(f))
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    print(f.__next__())
    print(f.send('haha'))
    print(f.__next__())
    print(f.send('haha'))