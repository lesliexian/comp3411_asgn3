#!/usr/bin/python3

# utils.py

from enum import Enum

class Direction(Enum):
    NORTH = 0
    WEST = 1
    SOUTH = 2
    EAST = 3

class TileType(Enum):
    LAND = 0
    WATER = 1
    WALL = 2
    TREE = 3
    DOOR = 4

    KEY = 5
    AXE = 6
    STONE = 7

    GOLD = 8
    SPAWN = 9

def normalize_view(view, direction):
    '''
    normalize view received by agent to views with north being up.

    return normalized view
    '''

    if direction == Direction.NORTH:
        return view

    if direction == Direction.WEST:
        return [[ view[j][i] for j in range(4,-1,-1) ] for i in range(0,5)]

    if direction == Direction.SOUTH:
        return [[ view[i][j] for j in range(4,-1,-1) ] for i in range(4,-1,-1) ]

    if direction == Direction.EAST:
        return [[ view[i][j] for i in range(0,5) ] for j in range(4,-1,-1)]

