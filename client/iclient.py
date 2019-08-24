class IClient(object):
    def connect_to_server(self):
        raise NotImplementedError

    def send_data_to_server(self, data):
        raise NotImplementedError
