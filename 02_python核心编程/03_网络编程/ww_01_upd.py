#coding=utf-8
from socket import *

# 1. 创建套接字
updSocket = socket(AF_INET, SOCK_DGRAM)

# 2. 准备接收方的地址
sendAddr = ('192.168.1.101', 8080)

# 3. 从键盘获取数据
sendData = input("请输入要发送的数据：")

# 4. 发送数据到指定的电脑上
updSocket.sendto(sendData.encode("utf-8"), sendAddr)

# 5. 等待接收对方发送的数据
recvData = updSocket.recvfrom(1024)

# 6. 显示对方发送的数据
print(recvData)

# 7. 关闭套接字
updSocket.close()