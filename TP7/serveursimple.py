import socket
import time
import threading

stop = False

HOST = '127.0.0.1'
PORT = 6667


def fonction_service(s, a):
    print(f"Service avec {a}")
    m = s.recv(1024)
    chaine = m.decode()
    chaine_up = chaine.upper()
    print(chaine)

    sservice.send(chaine_up.encode())
    time.sleep(2)
    sservice.close()


sserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sserver.bind((HOST, PORT))
sserver.listen()

print("ok server")
while not stop:
    print("waiting connection")
    (sservice, id_client) = sserver.accept()
    # t = threading.Thread(target=fonction_service, args=(sservice, id_client))
    # t.start()
    fonction_service(sservice,id_client)


sserver.close()
