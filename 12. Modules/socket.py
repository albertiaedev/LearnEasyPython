# The _socket module provides classes and functions for working with sockets

import socket

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
sock.bind(("localhost", 8080))

# Listen for incoming connections
sock.listen(10)

# Accept an incoming connection
conn, addr = sock.accept()

# Receive data from the client
data = conn.recv(1024)

# Send data back to the client
conn.sendall(data)