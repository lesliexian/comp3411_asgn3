import socket

class GameAgent(object):
    def __init__(self, port):
        self.socket_ = self.new_socket(port)
        self.view = None
        self.action = None

    def new_socket(self,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', port))
        return s

    def recv_view(self):
        data_str = self.socket_.recv(1024).decode('ascii')
        if data_str == '':
            raise RuntimeError('socket connection lost')

        # in case the packet get fragmentated
        while len(data_str) < 24:
            data_str += self.socket_.recv(1024).decode('ascii')

        # converts str to nested list
        view_str = data_str[:12:] + '^' + data_str[12::]
        self.view = [view_str[x:x+5] for x in range(0,25,5)]

    def send_action(self, action=None):
        if self.action is not None:
            action = self.action
        sent = self.socket_.send(action.encode('ascii'))
        if sent == 0:
            raise RuntimeError('socket connection lost')

    def print_view(self):
        print('+-----+')
        for row in self.view:
            print('|' + ''.join(row) + '|')
        print('+-----+')

    def test_run(self):
        while True:
            self.recv_view()
            self.print_view()
            action = input('action? ')
            self.send_action(action=action)


if __name__ == '__main__':
    GameAgent(9999).test_run()