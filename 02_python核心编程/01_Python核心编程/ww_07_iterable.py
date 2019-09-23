from collections.abc import Iterable, Iterator

if __name__ == '__main__':
    # 判断是否可以迭代
    # print(isinstance([], Iterable))
    # print(isinstance({}, Iterable))
    # print(isinstance('abc', Iterable))
    # print(isinstance((x for x in range(10)), Iterable))
    # print(isinstance(100, Iterable))

    # 迭代器
    print(isinstance((x for x in range(10)), Iterator))
    print(isinstance([], Iterator))
    print(isinstance({}, Iterator))
    print(isinstance('abc', Iterator))
    print(isinstance(100, Iterator))

    print(isinstance(iter([]), Iterator))
    print(isinstance(iter('abc'), Iterator))