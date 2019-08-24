import socket

from server.server import Server


class UDPServer(Server):
    def __init__(self, ip, port):
        super().__init__(ip, port)
        self.create_server()

    def create_server(self):
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.bind((self.ip, self.port))

    def handle_connection(self):
        raise NotImplementedError
