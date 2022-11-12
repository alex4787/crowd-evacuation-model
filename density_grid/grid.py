from pygame import Rect

from density_grid.tile import Tile
from typing import List

class Grid():
    def __init__(self) -> None:
        self.tiles: List[List[Tile]] = [] # shoudl this start as [[]] ?

        for row in range(10): #therefore, should this only go to 9 ?
            self.tiles.append([]) 
            for col in range(10): #again, to 10 or 9 ?
                self.tiles[row].append(Tile(col*100, row*100))

        for row in range(10): # 10 or 9 ?
            for col in range(10): # 10 or 9 ?
                tile = self.tiles[row][col]
                
                #in the first row
                if row != 0:
                    tile.neighbours.append(self.tiles[row-1][col])
                
                #in ht elast row
                if row != 9:
                    tile.neighbours.append(self.tiles[row+1][col])
                
                #in the first column
                if col != 0:
                    tile.neighbours.append(self.tiles[row][col-1])
                
                #in the last column
                if col != 9:
                    tile.neighbours.append(self.tiles[row][col+1])
