import socket

from client.client import Client


class TCPClient(Client):

    def __init__(self, ip, port):
        super().__init__(ip, port)

        self._create_client()

    def _create_client(self):
        self.client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    def connect_to_server(self):
        return_value = self.client_socket.connect((self.server_ip, self.server_port))
        print(return_value)
        print('Connected to {}:{}'.format(self.server_ip, self.server_port))

    def send_data_to_server(self, data):
        while True:
            return_value = self.client_socket.send(data)
            print('return_value = ', return_value)
            received_data = self.client_socket.recv(100).decode()
            if received_data == 'EOF':
                self.close_connection()
                break
            print('Data from server : ', received_data)

    def close_connection(self):
        self.client_socket.send(bytes('EOF', encoding='utf-8'))
        self.server_ip = None
        self.server_port = None
