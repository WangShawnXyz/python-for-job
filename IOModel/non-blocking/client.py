import socket
import time

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
i = 0
while True:
    sk.connect(("127.0.0.1", 8098))
    print("sending message")
    sk.sendall("Hello server!".encode("utf8"))
    time.sleep(2)
    i += 1
    if i > 20:
        break