from functools import reduce

a = reduce(lambda x, y: x+y, [1,2,3,4])
b = reduce(lambda x, y: x+y, [1,2,3,4],5)
c = reduce(lambda x, y:x+y, ['aa','bb','cc'], 'dd')

if __name__ == '__main__':
    print(a)
    print(b)
    print(c)