# -*- coding:utf-8 -*-
#########################
##服务端
#########################
'''
1.创建套接字，绑定套接字到本地IP与端口：socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.bind()
2.开始监听连接：s.listen()
3.进入循环，不断接受客户端的连接请求：s.accept()
4.接收传来的数据，或者发送数据给对方：s.recv() , s.sendall()
5.传输完毕后，关闭套接字：s.close()
'''
# 单线程
# !/usr/bin/env python
import socket

ip_port = ('127.0.0.1', 9999)

sk = socket.socket()  # 创建套接字
sk.bind(ip_port)  # 绑定服务地址
sk.listen(5)  # 监听连接请求
print('启动socket服务，等待客户端连接...')
conn, address = sk.accept()  # 等待连接，此处自动阻塞
while True:  # 一个死循环，直到客户端发送‘exit’的信号，才关闭连接
    client_data = conn.recv(1024).decode()  # 接收信息
    if client_data == "exit":  # 判断是否退出连接
        exit("通信结束")
    print("来自%s的客户端向你发来信息：%s" % (address, client_data))
    conn.sendall('服务器已经收到你的信息'.encode())  # 回馈信息给客户端
conn.close()     # 关闭连接

#多线程
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import threading        # 导入线程模块

def link_handler(link, client):
    """
    该函数为线程需要执行的函数，负责具体的服务器和客户端之间的通信工作
    :param link: 当前线程处理的连接
    :param client: 客户端ip和端口信息，一个二元元组
    :return: None
    """
    print("服务器开始接收来自[%s:%s]的请求...." % (client[0], client[1]))
    while True:     # 利用一个死循环，保持和客户端的通信状态
        client_data = link.recv(1024).decode()
        if client_data == "exit":
            print("结束与[%s:%s]的通信..." % (client[0], client[1]))
            break
        print("来自[%s:%s]的客户端向你发来信息：%s" % (client[0], client[1], client_data))
        link.sendall('服务器已经收到你的信息'.encode())
    link.close()

ip_port = ('127.0.0.1', 9999)
sk = socket.socket()            # 创建套接字
sk.bind(ip_port)                # 绑定服务地址
sk.listen(5)                    # 监听连接请求

print('启动socket服务，等待客户端连接...')

while True:     # 一个死循环，不断的接受客户端发来的连接请求
    conn, address = sk.accept()  # 等待连接，此处自动阻塞
    # 每当有新的连接过来，自动创建一个新的线程，
    # 并将连接对象和访问者的ip信息作为参数传递给线程的执行函数
    t = threading.Thread(target=link_handler, args=(conn, address))
    t.start()

# -*- coding:utf-8 -*-
#########################
# 客户端
#########################
'''
1.创建套接字，连接服务器地址：socket.socket(socket.AF_INET,socket.SOCK_STREAM) , s.connect()
2.连接后发送数据和接收数据：s.sendall(), s.recv()
3.传输完毕后，关闭套接字：s.close()
'''

import socket

ip_port = ('127.0.0.1', 9999)

s = socket.socket()  # 创建套接字

s.connect(ip_port)  # 连接服务器

while True:  # 通过一个死循环不断接收用户输入，并发送给服务器
    inp = input("请输入要发送的信息： ").strip()
    if not inp:  # 防止输入空信息，导致异常退出
        continue
    s.sendall(inp.encode())

    if inp == "exit":  # 如果输入的是‘exit’，表示断开连接
        print("结束通信！")
        break

    server_reply = s.recv(1024).decode()
    print(server_reply)

s.close()  # 关闭连接
