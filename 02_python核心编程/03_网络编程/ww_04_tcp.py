from socket import *

serSocket = socket(AF_INET, SOCK_STREAM)

# 重复使用绑定的信息
serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

localAddr = ('', 7788)
serSocket.bind(localAddr)

serSocket.listen(5)

while True:
    print('---主进程，等待新客户端连接')

    newSocket, destAddr = serSocket.accept()

    print('---主进程，接下来负责数据处理[%s]---'%str(destAddr))

    try:
        while True:
            recvData = newSocket.recv(1024)
            if len(recvData)>0:
                print('recv[%s]:%s'%(str(destAddr), recvData.decode()))
            else:
                break
    finally:
        newSocket.close()

serSocket.close()















