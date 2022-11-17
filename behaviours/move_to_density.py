from behaviours import Behaviour
import numpy as np
import math

MAX_DENSITY = 5

class MoveToDensity(Behaviour):  
    def __init__(self):
        return

    def go(self, person, exits, fires, aptitude, current_tile, width, height):
        person.color = (0, 0, 200)

        # find high density neighbour tiles, if tie, draw randomly from tiers
        tied_tile_densities = []
        curr_highest_density = 0
        for neighbour in current_tile.neighbours.values():
            if neighbour.density > MAX_DENSITY:
                continue
            if neighbour.density > curr_highest_density:
                curr_highest_density = neighbour.density
                tied_tile_densities = [neighbour]
            elif neighbour.density == curr_highest_density:
                tied_tile_densities.append(neighbour)
 
        if not tied_tile_densities:
            neighbour_to_follow = current_tile
        else:
            neighbour_to_follow = tied_tile_densities[np.random.choice(len(tied_tile_densities))]
        
        x = np.random.choice(neighbour_to_follow.width) + neighbour_to_follow.x
        y = np.random.choice(neighbour_to_follow.height) + neighbour_to_follow.y

        hyp = math.hypot(x - person.x, y - person.y)
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