from itertools import chain
import socket
import time

HOST = '127.0.0.1'
PORT = 6667


sserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sserver.bind((HOST, PORT))

sserver.listen()

stop = False
print('ok serveur')
while not stop:
    print('attend connection')
    (sserver, id_client) = sserver.accept()
    m = sserver.recv(1024)
    chaine = m.decode()
    print(chaine)
    if chaine == 'au revoir':
        stop = True
    time.sleep(2)
    sserver.close()