#!/usr/bin/python3

# explorer.py

# explorers the map using various algorithm but does nothing else.
# interacts with game server.

from collections import namedtuple

from agent import GameAgentBaseClass
from utils import *

class ExplorerAgent(object):
    def __init__(self, port):
        super(ExplorerAgent, self).__init__(port)
        self.map = {(0,0) : TileType.SPAWN}
        self.inventory = namedtuple('Inventory', ['axe', 'key', 'raft', 'stone'])(
                                    False, False, False, 0)
        self.pois = namedtuple('Pois', ['axe', 'key', 'tree', 'door','stone'])(
                                        [], [], [], [], [])
        self.pos = namedtuple('Point', ['x', 'y'])(0,0)

    def goto(self, target):
        '''
        use astar algorithm to calculate AND navigate to target coordinate. the
        target should be reachable without using raft or stone. will shop down 
        tree if the player have axe, but will also tries to minimize the tree 
        chopped down by setting the cose to tree a large number(currently 1000).

        return string of actions, or false if target is unreachable.
        '''
        pass

    def DFS_search(self):
        '''
        explorers the map using basic dfs algorithm.

        DFS(P, start):
            Choose direction dir, so that reverse(dir) points to a blocked cell;
            ExploreCell(dir);
        ExploreCell(dir):
            // Left-Hand Rule:
            ExploreStep(ccw(dir));
            ExploreStep(dir);
            ExploreStep(cw(dir));
        ExploreStep(dir):
            if unexplored(dir) then
                move(dir);
                ExploreCell(dir);
                move((reverse(dir));
            end if
        '''


    def update_map(self):
        