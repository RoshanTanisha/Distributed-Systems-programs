import socket

from server.iserver import IServer


class Server(IServer):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        self._create_server()

    def _create_server(self):
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.port))

    def handle_connection(self):
        raise NotImplementedError
