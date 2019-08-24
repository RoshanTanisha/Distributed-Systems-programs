import time

from server.TCPServer import TCPServer
from threading import Thread


class EchoTCPServer(TCPServer):
    def __init__(self, ip, port, queue_connection):
        super().__init__(ip, port, queue_connection)
        self.client_thread_pool = {}
        self.client_connections = {}

    def _get_address_of_client(self, ip_address):
        return '{}:{}'.format(ip_address[0], ip_address[1])

    def _get_ip_port_from_address_str(self, client_string):
        ip, port = client_string.split(':')
        return ip, int(port)

    def handle_connection(self):
        while True:
            client_socket, ip_address = self.socket.accept()
            client_address = self._get_address_of_client(ip_address)
            self.client_connections[client_address] = client_socket
            self._create_client_thread(client_address)

    def _create_client_thread(self, client_address):
        self.client_thread_pool[client_address] = Thread(target=self._handle_current_connection, args=(client_address,))
        self.client_thread_pool[client_address].start()
        self.client_thread_pool[client_address].join()

    def _handle_current_connection(self, client_address):
        client_address_tuple = self._get_ip_port_from_address_str(client_address)
        current_client = self.client_connections[client_address]
        data_from_client = current_client.recv(100).decode()
        message_from_server = bytes("From Server : {}, data is {}".format('{}:{}'.format(self.ip, self.port), data_from_client), encoding='utf-8')
        current_client.send(message_from_server)
        time.sleep(1)
        current_client.send(bytes('EOF', encoding='utf-8'))
        print('From client {} message is {} '.format(client_address, current_client.recv(100).decode()))
        print(self.client_thread_pool)
        self._destroy_thread(client_address)

    def _destroy_thread(self, client_address):
        del self.client_thread_pool[client_address]

    def destroy_server(self):
        print('Closing connection:')
        self.socket.close()


if __name__ == "__main__":
    server = EchoTCPServer('127.0.0.1', 5022, 10)
    try:
        server.handle_connection()
    finally:
        server.destroy_server()
