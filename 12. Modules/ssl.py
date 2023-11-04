# The _ssl module provides classes and functions for implementing secure sockets.

import _ssl


# Create a secure socket
socket = _ssl.SSLContext().wrap_socket(socket.socket())

# Connect to a server
socket.connect(("example.com", 443))

# Send data to the server
socket.sendall("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n".encode())

# Receive data from the server
response = socket.recv(1024)