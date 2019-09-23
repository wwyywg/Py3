#coding=utf-8

from socket import *
from time import ctime

#1. 创建套接字
updSocket = socket(AF_INET, SOCK_DGRAM)

#2. 绑定本地的相关信息
bindAddr = ('', 7789)
updSocket.bind(bindAddr)

while True:
    #3. 等待接收对方的数据
    recvData = updSocket.recvfrom(1024)

    #4. 打印信息
    print('【%s】%s:%s'%(ctime(),recvData[1][0],recvData[0]))

#5. 关闭套接字
updSocket.close()