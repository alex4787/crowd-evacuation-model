from pygame import Rect

from density_grid.tile import Tile
from density_grid.exit import Exit
from typing import List
import random

from config import *

class Grid():
    def __init__(self) -> None:
        self.tiles: List[List[Tile]] = []
        self.obstacles: List[Tile] = []
        self.barriers: List[Tile] = []
        self.fires: List[Tile] = []
        self.exits: List[Exit] = []

        for row in range(20):
            self.tiles.append([]) 
            for col in range(20):
                if self.is_exit(row, col):
                    exit = Exit(col*FLOOR, row*FLOOR, len(self.exits) + 1)
                    self.tiles[row].append(exit)
                    self.exits.append(exit)
                else:
                    self.tiles[row].append(Tile(col*FLOOR, row*FLOOR))

        for row, col in TILE_OBSTACLES:
            if self.is_exit(row, col):
                continue
            self.tiles[row][col].is_obstacle = True
            self.obstacles.append(self.tiles[row][col])

        for row, col in TILE_BARRIERS:
            if self.is_exit(row, col):
                continue
            self.tiles[row][col].is_barrier = True
            self.barriers.append(self.tiles[row][col])

        for row, col in TILE_FIRES:
            if self.is_exit(row, col):
                continue
            self.tiles[row][col].is_fire = True
            self.fires.append(self.tiles[row][col])

        for row in range(20):
            for col in range(20):
                tile = self.tiles[row][col]
                #Adding top 
                if row != 0:
                    tile.neighbours['N'] = self.tiles[row-1][col]
                #Adding bottom
                if row != 19:
                    tile.neighbours['S'] = self.tiles[row+1][col]
                #Adding left
                if col != 0:
                    tile.neighbours['W'] = self.tiles[row][col-1]
                #Adding right
                if col != 19:
                    tile.neighbours['E'] = self.tiles[row][col+1]

    def is_exit(self, row, col):
        for exit_row, exit_col in TILE_EXITS:
            if row == exit_row and col == exit_col:
                return True
        return False
    
    def update_fires(self):
        did_fire_spread = False
        for fire in self.fires:
            for adj in fire.neighbours.values():
                if adj.is_open_tile():
                    if random.random() <= FIRE_SPREAD_RATE:
                        adj.is_fire = True
                        adj.is_danger = False
                        self.fires.append(adj)
                        did_fire_spread = True
                    else:
                        adj.is_danger = True
        return did_fire_spread
