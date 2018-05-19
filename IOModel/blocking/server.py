import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8080))

sk.listen(5)

while True:
    conn, addr = sk.accept()

    while True:
        conn.send("Hello, client".encode("utf8"))
        data = conn.recv(1024)
        print(data.decode("utf8"))