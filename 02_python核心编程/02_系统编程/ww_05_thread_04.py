#coding=utf-8
import threading
import time

class MyThread(threading.Thread):
    def run(self) -> None:
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + " @ " + str(i)
            print(msg)

def test():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    # t = MyThread()
    # t.start()
    test()