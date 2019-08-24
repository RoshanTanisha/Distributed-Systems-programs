import time

from server.tcp_server import TCPServer
from threading import Thread


class DayTimeTCPServer(TCPServer):
    def __init__(self, ip, port, queue_connection):
        super().__init__(ip, port, queue_connection)
        self.client_thread_pool = {}
        self.client_connections = {}

    def handle_connection(self):
        while True:
            client_socket, ip_address = self.socket.accept()
            client_address = self.convert_address_to_string(ip_address)
            self.client_connections[client_address] = client_socket
            self._create_client_thread(client_address)
            time.sleep(1)
            self._destroy_thread(client_address)
            del self.client_connections[client_address]

    def _create_client_thread(self, client_address):
        self.client_thread_pool[client_address] = Thread(target=self._handle_current_connection, args=(client_address,))
        self.client_thread_pool[client_address].start()
        self.client_thread_pool[client_address].join()

    def _handle_current_connection(self, client_address):
        current_client = self.client_connections[client_address]
        current_time = time.strftime('%d/%m/%y %H:%M:%S')
        data_from_client = current_client.recv(100).decode()
        if 'time' in data_from_client.lower():
            message_from_server = bytes("From Server : {}, data is {}".format('{}:{}'.format(self.ip, self.port), current_time), encoding='utf-8')
            current_client.send(message_from_server)
        time.sleep(1)
        current_client.send(bytes('EOF', encoding='utf-8'))
        print('From client {} message is {} '.format(client_address, current_client.recv(100).decode()))
        print(self.client_thread_pool)

    def _destroy_thread(self, client_address):
        del self.client_thread_pool[client_address]


if __name__ == "__main__":
    server = DayTimeTCPServer('127.0.0.1', 5022, 10)
    try:
        server.handle_connection()
    finally:
        server.destroy_server()
