import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)  #设置成非阻塞
    sel.register(conn, selectors.EVENT_READ, read) #conn绑定的是read

def read(conn, mask):
    try:
        data = conn.recv(1024)  # Should be ready
        if not data:
            raise Exception
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    except Exception as e:
        print('closing', conn)
        sel.unregister(conn)  #解除注册
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 8090))
sock.listen(100)
sock.setblocking(False)
#注册
sel.register(sock, selectors.EVENT_READ, accept)
print("server....")

while True:
    events = sel.select() #监听[sock,conn1,conn2]
    print("events",events)
    #拿到2个元素，一个key,一个mask
    for key, mask in events:
        # print("key",key)
        # print("mask",mask)
        callback = key.data  #绑定的是read函数
        # print("callback",callback)
        callback(key.fileobj, mask)  #key.fileobj=sock,conn1,conn2