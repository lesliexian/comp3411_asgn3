import socket
from collections import namedtuple

from utils import *


class GameAgentBaseClass(object):
    def __init__(self, port):
        self.socket_ = self.new_socket(port)
        self.view = None
        self.action = None
        # self.map = [['' for _ in range(160)] for _ in range(160)] #todo: change to dedicated Map class
        # self.current_pos = namedtuple('Point', ['x', 'y'])(0,0)
        # self.inventory = namedtuple('Inventory', 
        #                             ['axe', 'key', 'raft', 'stone'])(
        #                             False, False, False, 0)
        # self.direction = Direction.NORTH

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
        self.view = [list(view_str[x:x+5]) for x in range(0,25,5)]

    def send_action(self):
        if self.action is not None:
            sent = self.socket_.send(self.action.encode('ascii'))
            if sent == 0:
                raise RuntimeError('socket connection lost')
        else:
            raise RuntimeError('no actions to send')

    def print_view(self):
        print('+-----+')
        for row in self.view:
            print('|' + ''.join(row) + '|')
        print('+-----+')

    def test_run(self):
        while True:
            self.recv_view()
            self.print_view()
            self.action = input('action?')
            self.send_action()





if __name__ == '__main__':
    print('Agent started at port 31415')
    GameAgentBaseClass(31415).test_run()