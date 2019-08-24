from server.server import Server


class TCPServer(Server):
    def __init__(self, ip, port, queue_connections):
        super().__init__(ip, port)
        self.queue_connections = queue_connections
        self._start_server()

    def _start_server(self):
        self.socket.listen(self.queue_connections)

    def handle_connection(self):
        raise NotImplementedError
