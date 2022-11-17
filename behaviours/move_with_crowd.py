from behaviours import Behaviour
import numpy as np
import math

class MoveWithCrowd(Behaviour):  
    def __init__(self):
        return

    def go(self, person, exits, fires, aptitude, current_tile, width, height):
        person.color = (0, 0, 200)

        # we re-calculate this for every agent in the tile, maybe we could just calculate this once per tile per iteraiton?
        combined_direction = (0, 0)
        for neighbour in current_tile.neighbours.values():
            combined_direction = tuple(map(lambda i, j: i + j, combined_direction, neighbour.average_direction))
        
        x = combined_direction[0]
        y = combined_direction[1]
        hyp = math.hypot(x, y)
        if hyp == 0:
            return
        unit_vector_x = 3*(x)/(hyp)
        unit_vector_y = 3*(y)/(hyp)
        
        x_motion = (np.random.choice([unit_vector_x, -unit_vector_x], 1, p=[aptitude, 1-aptitude]))[0]
        y_motion = (np.random.choice([unit_vector_y, -unit_vector_y], 1, p=[aptitude, 1-aptitude]))[0]
        person.x += x_motion
        person.y += y_motion
        
        if self.out_of_bounds(person.x, person.y, width, height):
            person.x -= x_motion
            person.y -= y_motion