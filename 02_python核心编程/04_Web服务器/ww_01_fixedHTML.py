#coding=utf-8
import socket
from multiprocessing import Process

def handleClient(clientSocket):
    '用一个新的进程，为一个客户端进行服务'
    recvData = clientSocket.recv(2014)
    requestHeaderLines = recvData.splitlines()
    for line in requestHeaderLines:
        print(line)

    responseHeaderLines = "HTTP/1.1 200 OK\r\n"
    responseHeaderLines += "\r\n"
    responseBody = "hello world"

    response = responseHeaderLines + responseBody
    clientSocket.send(response.encode())
    clientSocket.close()

def main():
    '作为程序的主控制入口'

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind(("", 7788))
    serverSocket.listen(10)

    while True:
        clientSocket, clientAddr = serverSocket.accept()
        clientP = Process(target=handleClient, args=(clientSocket,))
        clientP.start()
        clientSocket.close()

if __name__ == '__main__':
    main()





















