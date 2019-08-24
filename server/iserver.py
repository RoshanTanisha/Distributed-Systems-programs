class IServer(object):

    def create_server(self):
        raise NotImplementedError

    def handle_connection(self):
        raise NotImplementedError

    def destroy_server(self):
        raise NotImplementedError
