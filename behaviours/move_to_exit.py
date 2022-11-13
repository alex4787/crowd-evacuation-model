from behaviours import Behaviour
from typing import List, Tuple
import numpy as np
import math

class MoveToExit(Behaviour):  
    def __init__(self) -> None:
        return

    def find_closest_exit(self, person, exits) -> Tuple[int, int, int]:
        closest_exit = exits[0]
        min_hyp = math.hypot(closest_exit.x - person.x, closest_exit.y - person.y)
        for exit in exits:
            hyp = math.hypot(exit.x - person.x, exit.y - person.y)
            if hyp < min_hyp:
                closest_exit = exit
                min_hyp = hyp
        return (closest_exit.centerx, closest_exit.centery, min_hyp)

    def go(self, person, exits, fires, aptitude, current_tile, width, height):
        x, y, min_hyp = self.find_closest_exit(person, exits)

        if min_hyp == 0:
            return 

        unit_vector_x = 3*(x - person.x)/(min_hyp)
        unit_vector_y = 3*(y - person.y)/(min_hyp)

        person.color = (0, 255, 0)

        x_motion = (np.random.choice([unit_vector_x, -unit_vector_x], 1, p=[aptitude, 1-aptitude]))[0]
        y_motion = (np.random.choice([unit_vector_y, -unit_vector_y], 1, p=[aptitude, 1-aptitude]))[0]
        person.x += x_motion
        person.y += y_motion
        if self.out_of_bounds(person.x, person.y, width, height):
            person.x -= x_motion
            person.y -= y_motion