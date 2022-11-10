from pygame import Rect
from game_objects.people import People

class Tile(Rect):
    def __init__(self, x, y):
        self.height = 100
        self.width = 100 
        self.x = x
        self.y = y
        self.people_in_tile = []
        self.density = len(self.people_in_tile)
        self.average_direction = 0
        self.neighbours = []
