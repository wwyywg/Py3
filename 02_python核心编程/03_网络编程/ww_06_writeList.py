#coding=utf-8
import socket
from queue import Queue
from select import select

SERVER_IP = ('', 9999)

# 保存客户端发送过来的消息，将消息放入队列中
message_queue   = {}
input_list      = []
output_list     = []

if __name__ == '__main__':
    server = socket.socket()
    server.bind(SERVER_IP)
    server.listen(10)
    # 设置为非阻塞
    server.setblocking(False)

    # 初始化将服务端加入监听列表
    input_list.append(server)

    while True:
        # 开始 select 监听，对input_list的服务端server进行监听
        stdinput, stdoutput, stderr = select(input_list, output_list, 5)

        # 循环判断是否有客户端连接进来，当有客户端连接进来时select将出发
        for obj in stdinput:
            # 判断当前触发的是不是服务端对象，当触发的对象是服务器对象时，
            if obj == server:
                # 接收客户端的连接，获取客户端对象和客户端地址信息
                conn, addr = server.accept()
                print("Client %s connected!"%str(addr))
                # 将客户端对象也加入到监听的列表中，当客户端发送消息时
                input_list.append(conn)
                # 为连接的客户端单独创建一个消息队列，用来保存客户端发送的消息
                message_queue[conn] = Queue()
            else:
                # 由于客户端连接进来时服务器接收客户端连接请求
                # 判断是否是客户端触发
                try:
                    recv_data = obj.recv(1024)
                    # 客户端未断开
                    if recv_data:
                        print("received %s from client %s" %(recv_data))
                        # 将收到的消息放入到各客户端的消息队列中
                        message_queue[obj].put(recv_data)

                        # 将回复操作放到output列表中，让select监听
                        if obj not in output_list:
                            output_list.append(obj)

                except ConnectionResetError:
                    # 客户端断开连接了，将客户端的监听从input列表中移出
                    input_list.remove(obj)
                    #移出客户端对象的消息队列
                    del message_queue[obj]
                    print("\n[input] Client %s disconnected" %str(obj))

        # 如果现在没有客户端请求，也没有客户端发送消息时，开始对发送消息列表
        for sendobj in output_list:
            try:
                # 如果消息队列中有消息，从消息队列中获取要发送的消息
                if not message_queue[sendobj].empty():
                    # 从该客户端对象的消息队列中获取要发送的消息
                    send_data = message_queue[sendobj].get()
                    sendobj.send(send_data)
                else:
                    # 将监听移出等待下一次客户端发送消息
                    output_list.remove(sendobj)
            except ConnectionResetError:
                # 客户端连接断开
                del message_queue[sendobj]
                output_list.remove(sendobj)
                print("\n[output] Client %s disconnected" %str(sendobj))


























