from behaviours import Behaviour
import numpy as np
import math

class MoveToDensity(Behaviour):  
    def __init__(self):
        return

    def go(self, person, exits, fires, aptitude, current_tile, width, height):
        person.color = (0, 0, 200)
        neighbour_w_highest_density = current_tile.neighbours[0]
        for neighbour in current_tile.neighbours:
            if neighbour.density > neighbour_w_highest_density.density:
                neighbour_w_highest_density = neighbour
        
        x = neighbour_w_highest_density.centerx
        y = neighbour_w_highest_density.centery
        hyp = math.hypot(x - person.x, y)
        if hyp == 0:
            return
        unit_vector_x = 3*(x - person.x)/(hyp)
        unit_vector_y = 3*(y - person.y)/(hyp)

        x_motion = (np.random.choice([unit_vector_x, -unit_vector_x], 1, p=[aptitude, 1-aptitude]))[0]
        y_motion = (np.random.choice([unit_vector_y, -unit_vector_y], 1, p=[aptitude, 1-aptitude]))[0]
        person.x += x_motion
        person.y += y_motion
        if self.out_of_bounds(person.x, person.y, width, height):
            person.x -= x_motion
            person.y -= y_motion
        return
      