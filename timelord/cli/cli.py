import os
import socket
import sys

from timelord import lib

server_connection = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

try:
    server_connection.connect(os.path.expanduser(lib.socket_address))
except socket.error as message:
    print(message)
    sys.exit(1)
