class Test:
    def __init__(self):
        self._num = 100

    def setNum(self, newNum):
        print("-----setter-----")
        self._num = newNum

    def getNum(self):
        print("-----getter-----")

        return self._num

    num = property(getNum, setNum)

if __name__ == '__main__':
    t = Test()
    print(t.getNum())

    t.setNum(200)
    print(t.getNum())

    t.num = 300
    print(t.getNum())