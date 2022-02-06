import socket
import os


# Define socket host and port
HOST = '127.0.0.1'
PORT = 8000

# Create socket
sserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sserver.bind((HOST, PORT))
sserver.listen(1)
print('Listening on port %s ...' % PORT)

while True:
    client_connection, client_address = sserver.accept()

    request = client_connection.recv(1024).decode()
    # print(request)
    get_path = request.split('/r/n')[0].split()[1]
    print(get_path)

    if os.path.isfile(get_path[1:]):
        with open(get_path[1:], 'r') as f:
            data = f.read()
        response = f'HTTP/1.0 200 OK\n\n{data}'
        client_connection.sendall(response.encode())
        client_connection.close()
    elif get_path == '/':
        response = 'HTTP/1.0 200 OK\n\nPROG-AV'
        client_connection.sendall(response.encode())
        client_connection.close()
    else:
        response = 'HTTP/1.0 200 OK\n\nWrong Path'
        client_connection.sendall(response.encode())
        client_connection.close()

# Close socket
sserver.close()