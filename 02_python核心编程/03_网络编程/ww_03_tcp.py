#coding=utf-8
from socket import *

# 创建socket
tcpSerSocket = socket(AF_INET, SOCK_STREAM)

# 绑定本地信息
address = ('', 7788)
tcpSerSocket.bind(address)

# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的
tcpSerSocket.listen(5)

# 如果有新的客户端连接服务器，那么就产生一个新的套接字专门为这个客户端服务
# newSocket用来为这个客户端服务
# tcpSerSocket就可以省下来专门等待其他新客户端的连接
newSocket, clientAddr = tcpSerSocket.accept()

# 接收对方发送过来的数据，最大接收1024个字节
recvData = newSocket.recv(1024)
print('接收到的数据为：', recvData)

# 发送一些数据到客户端
newSocket.send("thank you !".encode('utf-8'))

# 关闭为这个客户端的套接字，只要关闭了，就意味着不能再为这个客户端服务
newSocket.close()

# 关闭监听套接字，只要这个套接字关闭了，就意味着整个程序不能再接收任何新的客户端信息
tcpSerSocket.close()















