from pygame import Rect

from density_grid.tile import Tile

class Grid():
    def __init__(self):
        self.tiles = []

        for row in range(10):
            self.tiles.append([])
            for col in range(10):
                self.tiles[row].append(Tile(col*100, row*100))

        for row in range(10):
            for col in range(10):
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