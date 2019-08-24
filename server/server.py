import socket

from server.iserver import IServer


class Server(IServer):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        self.create_server()

    def convert_address_to_string(self, ip_address):
        return '{}:{}'.format(ip_address[0], ip_address[1])

    def convert_string_to_address(self, ip_address_string):
        ip, port = ip_address_string.split(':')
        return ip, int(port)

    def create_server(self):
        raise NotImplementedError

    def handle_connection(self):
        raise NotImplementedError

    def destroy_server(self):
        print('Closing connection:')
        self.socket.close()
