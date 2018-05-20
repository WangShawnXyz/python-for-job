

import socket
import select
import time


port = 12345

def _message():
    time.sleep(5)
    return str(time.time())

def _addr():
    global port
    port += 1
    return ("127.0.0.1", port)

sks = [socket.socket() for x in range(10)]
# sks = [sk.bind(_addr()) for sk in sks]
# [sk.listen() for sk in sks]
for sk in sks:
    sk.connect(_addr())

while True:
    # msg = input(">>").strip()
    for sk in sks:
        sk.send(_message().encode("utf8"))
        data = sk.recv(1024)
        print(data.decode("utf8"))