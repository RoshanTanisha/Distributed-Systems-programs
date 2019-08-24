import socket

from client.iclient import IClient


class Client(IClient):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server_ip = None
        self.server_port = None

    @property
    def server_ip(self):
        return self._server_ip

    @server_ip.setter
    def server_ip(self, server_ip):
        self._server_ip = server_ip

    @property
    def server_port(self):
        return self._server_port

    @server_port.setter
    def server_port(self, server_port):
        self._server_port = server_port

    def create_connection(self):
        raise NotImplementedError

    def send_data_to_server(self, data):
        raise NotImplementedError
