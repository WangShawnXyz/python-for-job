import socket

sk=socket.socket()

sk.connect(("127.0.0.1",8090))
while 1:
    inp=input(">>>")
    sk.send(inp.encode("utf8")) #发送内容
    data=sk.recv(1024)  #接收信息
    print(data.decode("utf8"))  #打印出来