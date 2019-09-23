import socket

sk = socket.socket()
sk.bind('127.0.0.1', 8002)

sk.listen()

while True:
    # 获取与连接客户端
    conn, _ = sk.accept()
    # 接收客户端发来的消息
    data = conn.recv(8096)
    data_str = str(data, encoding="utf-8")  # bytes(data, encoding="urf-8")

    # 给客户端回复消息
    conn.send("")