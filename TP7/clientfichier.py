import socket
import sys

HOST = '127.0.0.1'
PORT = 6667

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(sys.argv[1].encode())

m = s.recv(1024)
data = m.decode()
with open(f'write/{sys.argv[1]}', 'w') as f:
    f.write(data)
print(data)
s.close()

