
a = map(lambda x: x*x, [1, 2, 3])
b = map(lambda x, y: x+y, [1, 2, 3],[4, 5, 6])

def f1(x, y):
    return (x, y)

l1 = [0, 1, 2, 3, 4, 5, 6]
l2 = ['Sun', 'M', 'T', 'W', 'T', 'F', 'S']
l3 = map(f1, l1, l2)

if __name__ == '__main__':
    print(list(a))
    print(list(b))
    print(list(l3))