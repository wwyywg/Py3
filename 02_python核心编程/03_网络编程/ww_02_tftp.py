#coding=utf-8

from socket import *
import struct
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('-' * 30)
        print('tips:')
        print('python xxx.py 192.168.1.1')
        print('-' * 30)
        exit()
    else:
        ip = sys.argv[1]

    # 创建upd套接字
    updSocket = socket(AF_INET, SOCK_DGRAM)

    # 构造下载请求数据
    cmd_buf = struct.pack("!H8sb5sb", 1, "test.jpg", 0, "octet", 0)

    # 发送下载文件请求数据到指定服务器
    sendAddr = (ip, 69)
    updSocket.sendto(cmd_buf, sendAddr)

    p_num = 0

    recvFile = ''

    while True:
        recvData, recvAddr = updSocket.recvfrom(1024)

        recvDataLen = len(recvData)

        # print(recvAddr)
        # print(len(recvData))

        cmdTuple = struct.unpack("!HH", recvData[:4])

        # print(cmdTuple)

        cmd = cmdTuple[0]

        currentPackNum = cmdTuple[1]

        if cmd == 3:    #  是否为数据包

            # 如果是第一次接收数据，那么就创建文件
            if currentPackNum == 1:
                recvFile = open("test.jpg", "a")

            # 包编号是否和上次相等
            if p_num + 1 == currentPackNum:
                recvFile.write(recvData[4:])
                p_num += 1
                print('(%d)次接收到的数据'%(p_num))

                ackBuf = struct.pack("!HH", 4, p_num)

                updSocket.sendto(ackBuf, recvAddr)

            # 如果收到的数据小于516则认为出错
            if recvDataLen < 516:
                recvFile.close()
                print("已经成功下载！！！")
                break

        elif cmd == 5:  # 是否为错误应答
            print("error num:%d"%currentPackNum)
            break

    updSocket.close()












