import socket

sk = socket.socket()

sk.connect(("127.0.0.1", 8080))

while True:
    data = sk.recv(1024)
    print(data.decode("utf8"))
    sk.send("Hello server".encode("utf8"))

