from server.server import Server


class UDPServer(Server):
    def __init__(self, ip, port):
        super(Server, self).__init__(ip, port)

    def handle_connection(self):
        raise NotImplementedError
