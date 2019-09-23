import os

# 注意，fork函数，只在Unix/Linux/Mac上运行，Windows不可以
rpid = os.fork()

if __name__ == '__main__':
    if rpid < 0:
        print("fork调用失败。")
    elif rpid == 0:
        print("我是子进程（%s），我的父进程是（%s）" %(os.getpid(),os.getppid()))
        # x += 1
    else:
        print("我是父进程（%s），我的子进程是（%s）" %(os.getpid(),rpid))

    print("父子进程都可以执行这的代码")