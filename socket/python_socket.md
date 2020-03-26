![](res/socket.png)

在Python中，import socket后，用socket.socket()方法来创建套接字，语法格式如下：

sk = socket.socket([family[, type[, proto]]])

参数说明：

1.family: 套接字家族，可以使AF_UNIX或者AF_INET。

2.type: 套接字类型，根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM，也就是TCP和UDP的区别。

3.protocol: 一般不填默认为0。

|  socket类型   | 描述  |
|  ----  | ----  |
| socket.AF_UNIX  | 只能够用于单一的Unix系统进程间通信 |
| socket.AF_INET6 | IPv6 |
|socket.SOCK_STREAM	|流式socket , for TCP|
|socket.SOCK_DGRAM  |数据报式socket , for UDP|
|socket.SOCK_RAW	|原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；<br>其次，SOCK_RAW也可以处理特殊的IPv4报文；<br>此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头。|
|socket.SOCK_SEQPACKET	|可靠的连续数据包服务|
|创建TCP Socket：	|s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)|
|创建UDP Socket：	|s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)|

通过s = socket.socket()方法，我们可以获得一个socket对象s，也就是通常说的获取了一个“套接字”，该对象具有一下方法：

|方法	| 描述  |
|  ----  | ----  |
|服务器端方法|	
|s.bind()	|绑定地址（host,port）到套接字，在AF_INET下,以元组（host,port）的形式<br>表示地址。|
|s.listen(backlog)	|开始监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接<br>数量。该值至少为1，大部分应用程序设为5就可以了。|
|s.accept()	|被动接受客户端连接,(阻塞式)等待连接的到来，并返回（conn,address）<br>二元元组,其中conn是一个通信对象，可以用来接收和发送数据。address<br>是连接客户端的地址。|
|客户端方法	|
|s.connect(address)	|客户端向服务端发起连接。一般address的格式为元组<br>（hostname,port），如果连接出错，返回socket.error错误。|
|s.connect_ex()	|connect()函数的扩展版本,出错时返回出错码,而不是抛出异常|
|公共方法|	
|s.recv(bufsize)	|接收数据，数据以bytes类型返回，bufsize指定要接收的最大数据量。|
|s.send()	|发送数据。返回值是要发送的字节数量。|
|s.sendall()	|完整发送数据。将数据发送到连接的套接字，但在返回之前会尝试发送所有<br>数据。成功返回None，失败则抛出异常。|
|s.recvform()	|接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是<br>包含接收的数据，address是发送数据的套接字地址。|
|s.sendto(data,address)	|发送UDP数据，将数据data发送到套接字，address是形式为（ipaddr，<br>port）的元组，指定远程地址。返回值是发送的字节数。|
|s.close()	|关闭套接字，必须执行。|
|s.getpeername()	|返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。|
|s.getsockname()	|返回套接字自己的地址。通常是一个元组(ipaddr,port)|
|s.setsockopt(level,optname,value)	|设置给定套接字选项的值。|
|s.getsockopt(level,optname[.buflen])	|返回套接字选项的值。|
|s.settimeout(timeout)	|设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None<br>表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可<br>能用于连接的操作（如connect()）|
|s.gettimeout()	|返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。|
|s.fileno()	|返回套接字的文件描述符。|
|s.setblocking(flag)	|如果flag为0，则将套接字设为非阻塞模式<br>，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用recv()<br>没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。|
|s.makefile()	|创建一个与该套接字相关连的文件|

**注意事项**

1.Python3以后，socket传递的都是bytes类型的数据，字符串需要先转换一下，string.encode()即可；另一端接收到的bytes数据想转换成字符串，只要bytes.decode()一下就可以。

2.在正常通信时，accept()和recv()方法都是阻塞的。所谓的阻塞，指的是程序会暂停在那，一直等到有数据过来。

