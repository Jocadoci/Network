HOST = 'localhost'
PORT = 1337
import socket
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn , addr = s.accept()
conn.recv(1024)
