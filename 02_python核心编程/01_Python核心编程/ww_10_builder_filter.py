
a = filter(lambda x: x%2, [1, 2, 3, 4])
b = filter(None, "she")

if __name__ == '__main__':
    print(list(a))
    print(list(b))
