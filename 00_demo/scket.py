import socket

# 生成socket实例对象
sk = socket.socket()
# 绑定IP和端口
sk.bind(("127.0.0.1", 8001))
# 监听
sk.listen()

def yimi(url):
    ret = 'hello {}'.format(url)
    return bytes(ret, encoding="utf-8")

def yimi1(url):
    with open('index.html', 'rb') as f:
        ret = f.read()
    return ret

def xiaohei(url):
    ret = 'hello {}'.format(url)
    return bytes(ret, encoding="utf-8")

def f404(url):
    ret = "你访问的这个{}找不到".format(url)
    return bytes(ret, encoding="utf-8")

url_func = [
    ("/yimi/", yimi),
    ("/xiaohei/", xiaohei)
]

# 客户端连接
while True:
    # 获取与客户端的连接
    conn, _ = sk.accept()
    # 接收客户端发来的消息
    data = conn.recv(8096)
    data_str = str(data, encoding="utf-8")
    l1 = data_str.split("\r\n")
    # print(data)
    l2 = l1[0].split()

    url = l2[1]

    # 给客户端回复消息
    conn.send(b'HTTP/1.1 200 OKcontent-type:text/html; charset=utf-8\r\n\r\n')
    # conn.send(b'<h1>hello s10</h1>')
    for i in url_func:
        if i[0] == url:
            func = i[1]
            break
    else:
        func = f404

    # 拿到函数的执行结果
    response = func(url)
    # 将函数返回的结果返送给浏览器
    conn.send(response)
    # 关闭
    conn.close()
    sk.close()