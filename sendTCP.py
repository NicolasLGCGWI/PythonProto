import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 5000))
sock.sendall(b"Hello Emulateur en TCP!")
sock.close()