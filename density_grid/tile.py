from pygame import Rect
import numpy as np
import math
from typing import TYPE_CHECKING, Tuple

if TYPE_CHECKING:
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
        self.average_direction: Tuple[int, int] = (0, 0)
        self.neighbours: List[Tile] = []

    def update_average_direction(self):
        combined_direction = (0, 0)
        for person in self.people_in_tile:
            curr_direction = (person.x - person.previous_x, person.y - person.previous_y)
            combined_direction = tuple(map(lambda i, j: i + j, combined_direction, curr_direction))
        
        x = combined_direction[0]
        y = combined_direction[1]
        hyp = math.hypot(x, y)
        if hyp < 1:
            hyp = 1 # This is just a hack, what does it mean if hyp = 0  and how should we handle /0 ?
        unit_vector_x = 3*(x)/(hyp)
        unit_vector_y = 3*(y)/(hyp)
        self.average_direction = (unit_vector_x, unit_vector_y)





        return

