from socket import *
from multiprocessing import *
from time import sleep

# 处理客户端的请求并为其服务
def dealWithClient(newScoket, destAddr):
    while True:
        recvDaa = newScoket.recv(1024)
        if len(recvDaa)>0:
            print('recv[%s]:%s'%(str(destAddr), recvDaa.decode()))
        else:
            print('[%s]客户端已经关闭'%str(destAddr))
            break

    newScoket.close()

def main():

    serSocket = socket(AF_INET, SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
    localAddr = ('', 7788)
    serSocket.bind(localAddr)
    serSocket.listen(5)

    try:
        while True:
            print('---主进程，等待新客户端的连接----')
            newSocket,destAddr = serSocket.accept()
            print('---主进程，接下来创建一个新的进程负责数据处理[%s]' %str(destAddr))

            client = Process(target=dealWithClient, args=(newSocket, destAddr))
            client.start()

            # 因为已经向子进程copy了一份（引用），并且父进程中这个套接字
            newSocket.close()

    finally:
        # 当为所有的客户端服务完之后再进行关闭，表示不再接收新的客户端的连接
        serSocket.close()

if __name__ == '__main__':
    main()





















