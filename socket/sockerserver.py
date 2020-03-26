#!/usr/bin/env python
# -*- coding:utf-8 -*-
#######################
#服务器端
#######################
import socketserver
'''
使用ThreadingTCPServer的要点:
1.创建一个继承自socketserver.BaseRequestHandler的类；
2.这个类中必须定义一个名字为handle的方法，不能是别的名字！
3.将这个类，连同服务器的ip和端口，作为参数传递给ThreadingTCPServer()构造器
4.手动启动ThreadingTCPServer。
'''

'''
服务器端的代码核心要点:
1.连接数据封装在self.request中！调用send()和recv()方法都是通过self.request对象。
2.handle()方法是整个通信的处理核心，一旦它运行结束，当前连接也就断开了（但其他的线程和客户端还正常），因此一般在此设置一个无限循环。
3.注意server = socketServer.ThreadingTCPServer((‘127.0.0.1’,8009),MyServer)中参数传递的方法。
4.server.serve_forever()表示该服务器在正常情况下将永远运行。
'''

class MyServer(socketserver.BaseRequestHandler):
    '''必须继承socketserver.BaseRequestHandler类'''
    def handle(self):
        """
        必须实现这个方法！
        :return:
        """
        conn = self.request         # request里封装了所有请求的数据
        conn.sendall('欢迎访问socketserver服务器！'.encode())
        while True:
            data = conn.recv(1024).decode()
            if data == "exit":
                print("断开与%s的连接！" % (self.client_address,))
                break
            print("来自%s的客户端向你发来信息：%s" % (self.client_address, data))
            conn.sendall(('已收到你的消息<%s>' % data).encode())

if __name__ == '__main__':
    # 创建一个多线程TCP服务器
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    print("启动socketserver服务器！")
    # 启动服务器，服务器将一直保持运行状态
    server.serve_forever()


###########################
#客户端
###########################
"""
客户端依然使用socket模块就可以了，不需要导入socketserver模块
"""

import socket

ip_port = ('127.0.0.1', 9999)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)
data = sk.recv(1024).decode()
print('服务器:', data)
while True:
    inp = input('你:').strip()
    if not inp:
        continue

    sk.sendall(inp.encode())

    if inp == 'exit':
        print("谢谢使用，再见！")
        break
    data = sk.recv(1024).decode()
    print('服务器:', data)
sk.close()