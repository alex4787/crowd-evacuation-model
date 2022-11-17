from behaviours import Behaviour
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_objects import People

import numpy as np
import math
from math import pi

angle_to_list_of_neighbours = [
    (-7*pi/8, ['NW', 'W', 'SW']),
    (-5*pi/8, ['S', 'W', 'SW']),
    (-3*pi/8, ['SW', 'S', 'SE']),
    (-1*pi/8, ['S', 'SE', 'E']),
    (1*pi/8, ['SE', 'E', 'NE']),
    (3*pi/8, ['E', 'NE', 'N']),
    (5*pi/8, ['NE', 'N', 'NW']),
    (7*pi/8, ['N', 'NW', 'W']),
    (pi, ['NW', 'W', 'SW']),
]

MAX_DENSITY = 4

class BestOption(Behaviour):  
    def __init__(self, best_option):
        self.best_option = best_option
        return

    def find_compass_from_angle(self, person):
        delta_x = self.best_option.x - person.x
        delta_y = -1*(self.best_option.y - person.y)
        angle = np.arctan2(delta_y, delta_x) # value from -PI to PI

        for upper_limit, neighbours in angle_to_list_of_neighbours:
            if angle <= upper_limit:
                return neighbours

    def convert_compass_to_neighbours(self, person, current_tile):
        compass = self.find_compass_from_angle(person)
        desired_neighbours = []
        for direction in compass:
            neighbour = current_tile.neighbours.get(direction)
            if neighbour:
                desired_neighbours.append(neighbour)
        
        return desired_neighbours

    def undo_motion(self, person, x: int, y: int):
        person.x -= x
        person.y -= y

    def go(self, person, exits, fires, aptitude, current_tile, width, height, previous_tile):
        person.color = (0, 0, 200)

        # find high density neighbour tiles, if tie, draw randomly from tiers
        
        tied_tile_densities = []
        curr_highest_density = 0
        desired_neighbours = self.convert_compass_to_neighbours(person, current_tile) if self.best_option else current_tile.neighbours.values()
        for neighbour in desired_neighbours:
            if neighbour.density >= MAX_DENSITY:
                continue
            if neighbour.density > curr_highest_density:
                curr_highest_density = sum(neighbour.heatmap)
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

        x_motion = (np.random.choice([unit_vector_x, -unit_vector_x], 1, p=[1, 0]))[0]
        y_motion = (np.random.choice([unit_vector_y, -unit_vector_y], 1, p=[1, 0]))[0]
        person.x += x_motion
        person.y += y_motion

        if not tied_tile_densities:
            # undo movement if you colided with another person.
            for other in current_tile.people_in_tile:
                if other.colliderect(person) and not person.is_me(other):
                    self.undo_motion(person, x_motion, y_motion)
                    return

        if self.out_of_bounds(person.x, person.y, width, height):
            self.undo_motion(person, x_motion, y_motion)