from pygame import Rect
from game_objects import People
from typing import List

class Tile(Rect):
    def __init__(self, x: int, y: int) -> None:
        self.height: int = 100
        self.width: int = 100 
        self.x: int = x
        self.y: int = y
        self.people_in_tile: List[People] = []
        self.density: int = len(self.people_in_tile)
        self.average_direction = 0 # What type will this be ?
        self.neighbours: List[Tile] = []
