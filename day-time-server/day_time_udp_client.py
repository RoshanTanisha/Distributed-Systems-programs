from client.udp_client import UDPClient


class DayTimeUDPClient(UDPClient):
    def __init__(self, ip, port):
        super().__init__(ip, port)

    def send_data_to_server(self, data):
        self.client_socket.sendto(bytes(data, encoding='utf-8'), (self.server_ip, self.server_port))
        data, address = self.client_socket.recvfrom(100)
        print('Address: ', address)
        print('Data: ', data.decode())


if __name__ == "__main__":
    client = DayTimeUDPClient('127.0.0.1', 5004)
    client.server_ip = '127.0.0.1'
    client.server_port = 5001
    client.send_data_to_server('Time?')
