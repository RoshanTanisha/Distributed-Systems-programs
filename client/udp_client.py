import socket

from client.client import Client


class UDPClient(Client):

    def __init__(self, ip, port):
        super(Client, self).__init__(ip, port)

        self._create_client()

    def _create_client(self):
        self.client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    def send_data_to_server(self, data):
        return_value = self.client_socket.sendto(data, (self.server_ip, self.server_port))
        print(return_value)
        print('Data from Server : {}'.format(self.client_socket.recv(100).decode()))
