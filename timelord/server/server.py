import logging
import os
import socket

from timelord import lib


def create_socket(address):
    _socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    logging.info("Starting server on {}".format(address))
    _socket.bind(address)
    _socket.listen()
    return _socket


def run(_socket: socket.socket):
    running = True
    while running:
        logging.info("Waiting for connection")
        connection, client_address = _socket.accept()
        try:
            logging.info("Connection from {}".format(client_address))
            reading = True
            while reading:
                data = connection.recv(16)
                logging.info("Received {!r}".format(data))
                if data:
                    logging.info("Responding to client.")
                    connection.sendall("1: Pong")
                else:
                    logging.info("No data from {}".format(client_address))
                    reading = False
        finally:
            connection.close()


def start_server():
    logging.basicConfig(level=logging.INFO)
    unlink_socket(lib.socket_address)
    _socket = create_socket(lib.socket_address)
    run(_socket)


def unlink_socket(address):
    try:
        logging.info("Destroying socket.")
        os.unlink(address)
    except OSError:
        if os.path.exists(address):
            raise


if __name__ == "__main__":
    start_server()
