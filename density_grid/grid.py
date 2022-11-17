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
                
                #Adding top left, top right, top center, as neighbours. 
                if row != 0:
                    tile.neighbours['N'] = self.tiles[row-1][col]
                    if col != 0:
                        tile.neighbours['NW'] = self.tiles[row-1][col-1]
                    if col != 9: 
                        tile.neighbours['NE'] = self.tiles[row-1][col+1]
                
                #Adding bottom left, bottom right, bottom center
                if row != 9:
                    tile.neighbours['S'] = self.tiles[row+1][col]
                    if col != 0:
                        tile.neighbours['SW'] = self.tiles[row+1][col-1]
                    if col != 9: 
                        tile.neighbours['SE'] = self.tiles[row+1][col+1]
                
                #Adding left
                if col != 0:
                    tile.neighbours['W'] = self.tiles[row][col-1]
                
                #Adding right
                if col != 9:
                    tile.neighbours['E'] = self.tiles[row][col+1]
