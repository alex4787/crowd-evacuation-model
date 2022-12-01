from pygame import Rect

from density_grid.tile import Tile
from typing import List
import random

# tile_obstacles = [(10, 11), (10, 14), (10,10), (11,10), (12,10), (13,10), (14, 10), (15, 10), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15), (15, 11), (15, 12), (15, 13), (15, 14)]
#tile_obstacles = [(x,y) for x in range(1,5) for y in range(1,5)]
tile_obstacles = [(10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7)]

tile_fires = [(5, 5)]

class Grid():
    def __init__(self) -> None:
        self.tiles: List[List[Tile]] = []
        self.obstacles: List[Tile] = []
        self.fires: List[Tile] = []

        for row in range(20):
            self.tiles.append([]) 
            for col in range(20):
                self.tiles[row].append(Tile(col*50, row*50))

        for row, col in tile_obstacles:
            self.tiles[row][col].is_obstacle = True
            self.obstacles.append(self.tiles[row][col])

        for row, col in tile_fires:
            self.tiles[row][col].is_fire = True
            self.fires.append(self.tiles[row][col])

        for row in range(20):
            for col in range(20):
                tile = self.tiles[row][col]
                
                #Adding top left, top right, top center, as neighbours. 
                if row != 0:
                    tile.neighbours['N'] = self.tiles[row-1][col]
                    # if col != 0:
                    #     tile.neighbours['NW'] = self.tiles[row-1][col-1]
                    # if col != 19: 
                    #     tile.neighbours['NE'] = self.tiles[row-1][col+1]
                
                #Adding bottom left, bottom right, bottom center
                if row != 19:
                    tile.neighbours['S'] = self.tiles[row+1][col]
                    # if col != 0:
                    #     tile.neighbours['SW'] = self.tiles[row+1][col-1]
                    # if col != 19: 
                    #     tile.neighbours['SE'] = self.tiles[row+1][col+1]
                
                #Adding left
                if col != 0:
                    tile.neighbours['W'] = self.tiles[row][col-1]
                
                #Adding right
                if col != 19:
                    tile.neighbours['E'] = self.tiles[row][col+1]

    
    def update_fires(self):
        did_fire_spread = False
        for fire in self.fires:
            for adj in fire.neighbours.values():
                if not adj.is_obstacle and not adj.is_fire:
                    prob_catch_on_fire = random.random()
                    if prob_catch_on_fire <= 0.01:
                        adj.is_fire = True
                        adj.is_danger = False
                        self.fires.append(adj)
                        did_fire_spread = True
                    else:
                        adj.is_danger = True
        return did_fire_spread
