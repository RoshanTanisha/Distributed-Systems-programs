import socket

from server.server import Server


class TCPServer(Server):
    def __init__(self, ip, port, queue_connections):
        self.queue_connections = queue_connections
        super().__init__(ip, port)
        self.create_server()

    def create_server(self):
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.port))
        self._start_server()

    def _start_server(self):
        self.socket.listen(self.queue_connections)

    def handle_connection(self):
        raise NotImplementedError
