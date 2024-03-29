import threading

# 创建全局ThreadLocal对象：
local_school = threading.local()

def process_student():
    # 获取当前线程的student：
    std = local_school.student
    print("Hello, %s (in %s)"%(std, threading.current_thread().getName()))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('dongGe',), name="Thread-A")
    t2 = threading.Thread(target=process_thread, args=('老王',), name="Thread-B")

    t1.start()
    t2.start()
    t1.join()
    t2.join()