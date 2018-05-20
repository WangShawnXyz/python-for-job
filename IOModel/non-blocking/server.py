import socket
import time


sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(("127.0.0.1", 8098))
sk.listen(5)
sk.setblocking(False)

while True:
    try:
        print("waiting client connection ...")
        conn, addr = sk.accept()
        print(">>" + str(addr))
        message = conn.recv(1024)
        print(message.decode("utf8"))
        conn.close()
    except Exception as e:
        print(e)
        time.sleep(4)