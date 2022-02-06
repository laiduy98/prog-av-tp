import socket


# Define socket host and port
HOST = '0.0.0.0'
PORT = 6667

# Create socket
sserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sserver.bind((HOST, PORT))
sserver.listen(1)
print('Listening on port %s ...' % PORT)

while True:
    # Wait for client connections
    client_connection, client_address = sserver.accept()

    # Get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # Send HTTP response
    response = 'HTTP/1.0 200 OK\n\nPROG-AV'
    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
sserver.close()