import time
from threading import Thread

from server.udp_server import UDPServer


class EchoUDPServer(UDPServer):
    def __init__(self, ip, port):
        super().__init__(ip, port)
        self.client_data = {}
        self.client_thread_pool = {}

    def handle_connection(self):
        while True:
            data, client_address = self.socket.recvfrom(100)
            client_address_string = self.convert_address_to_string(client_address)
            self.client_data[client_address_string] = data.decode()
            print(self.client_data)
            self._create_client_thread(client_address_string)
            time.sleep(1)
            self._destroy_thread(client_address_string)
            del self.client_data[client_address_string]

    def _create_client_thread(self, client_address_string):
        self.client_thread_pool[client_address_string] = Thread(target=self._handle_current_connection, args=(client_address_string,))
        self.client_thread_pool[client_address_string].start()
        self.client_thread_pool[client_address_string].join()

    def _handle_current_connection(self, client_address_string):
        data_from_client = self.client_data[client_address_string]
        message_from_server = 'From server: {}, data is: {}'.format(self.convert_address_to_string((self.ip, self.port)), data_from_client)
        self.socket.sendto(bytes(message_from_server, encoding='utf-8'), self.convert_string_to_address(client_address_string))

    def _destroy_thread(self, client_address_string):
        del self.client_thread_pool[client_address_string]


if __name__ == "__main__":
    server = EchoUDPServer('127.0.0.1', 5001)
    try:
        server.handle_connection()
    finally:
        server.destroy_server()
