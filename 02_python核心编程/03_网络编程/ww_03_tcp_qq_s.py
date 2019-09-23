#coding=utf-8
from socket import *

# 创建socket
tcpSerSocket = socket(AF_INET, SOCK_STREAM)

# 绑定本地信息
address = ('127.0.0.1', 7788)
tcpSerSocket.bind(address)

# 使用socket创建的套接字默认的属性是主动，使用listen将其变为被动的
tcpSerSocket.listen(5)

while True:
    # 如果有新的客户端来连接服务器，那么就产生一个新的套接字专门为这个客户端
    # newSocket用来为这个客户端服务
    # tcpSerSocket就可以省下来专门等待其他新客户端的连接
    newSocket, clientAddr = tcpSerSocket.accept()
    while True:
        # 接收对方发送过来的数据，最大接收1024个字节
        recvData = newSocket.recv(1024)

        # 如果接收的数据的长度为0，则意味着客户端关闭了连接
        if len(recvData)>0:
            print('recv:', recvData.decode())
        else:
            break

        # 发送一些数据到客户端
        sendData = input("send:")
        newSocket.send(sendData.encode())

    # 关闭为这个客户端服务的套接字，只要关闭了，
    newSocket.close()