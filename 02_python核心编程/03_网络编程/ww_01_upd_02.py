#coding=utf-8

from socket import *

#1. 创建套接字
updSocket = socket(AF_INET, SOCK_DGRAM)

#2. 绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
bindAddr = ('', 7788)   # ip地址和端口号，ip一般不用写
updSocket.bind(bindAddr)

num = 1
while True:
    #3. 等待接收对方发送的数据
    recvData = updSocket.recvfrom(1024) # 1024表示本次接收的最大字节数

    #4. 将接收到的数据再发送给对方
    updSocket.sendto(recvData[0], recvData[1])
    #5. 显示接收到的数据
    print('已经将接收到的第%d个数据返回给对方,内容为:%s'%(num, recvData[num]))
    num += 1

#5. 关闭套接字
updSocket.close()