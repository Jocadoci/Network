HOST = 'localhost'
PORT = 1337
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST , PORT))
s.send("MESASGE")
