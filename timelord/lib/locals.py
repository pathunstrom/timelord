import os

home = os.path.expanduser("~")
directory = ".timelord"
socket_name = "tlsocket"

try:
    os.mkdir(os.path.join(home, directory))
except FileExistsError:
    pass

socket_address = os.path.join(home, directory, socket_name)