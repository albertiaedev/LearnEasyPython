# The _ssl module provides classes and functions for implementing secure sockets.

import _ssl


# Create a secure socket
socket = _ssl.SSLContext().wrap_socket(socket.socket())