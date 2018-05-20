

import socket
import select

port = 12345

def _addr():
    global port
    port += 1
    return ("127.0.0.1", port)

sks = [socket.socket() for x in range(10)]
# sks = [sk.bind(_addr()) for sk in sks]
# [sk.listen() for sk in sks]
for sk in sks:
    sk.bind(_addr())
    sk.listen()

while True:
    r, w, e = select.select(sks, [], [], 5)

    for i in r:
        conn, addr = i.accept()
        print(conn)
        # print("")
    print(">>>>>>>>>>")


# 一终止server就会有输出  hhh