from client.tcp_client import TCPClient


class DayTimeTCPClient(TCPClient):
    def __init__(self, ip, port):
        super().__init__(ip, port)


if __name__ == "__main__":
    client = DayTimeTCPClient('127.0.0.1', 5000)
    client.server_ip = '127.0.0.1'
    client.server_port = 5022

    client.connect_to_server()
    client.send_data_to_server(bytes('Time?', encoding='utf-8'))
