def counter(start=0):
    def incr():
        nonlocal start
        start += 1
        return start
    return incr

def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

if __name__ == '__main__':
    c1 = counter(5)
    print(c1())
    print(c1())

    c2 = counter(50)
    print(c2())
    print(c2())

    print(c1())
    print(c1())

    print(c2())
    print(c2())

    line1 = line_conf(1, 1)
    line2 = line_conf(4, 5)

    print(line1(5))
    print(line2(5))