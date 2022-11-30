from behaviours import Behaviour
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_objects import People

import numpy as np
import math
from math import pi
import random

davinci_wheel = [
    (-3/4*pi, ['W', 'S', 'N', 'E']),
    (-1/2*pi, ['S', 'W', 'E', 'N']),
    (-1/4*pi, ['S', 'E', 'W', 'N']),
    (0, ['E', 'S', 'N', 'W']),
    (1/4*pi, ['E', 'N', 'S', 'W']),
    (1/2*pi, ['N', 'E', 'W', 'S']),
    (3/4*pi, ['N', 'W', 'E', 'S']),
    (pi, ['W', 'N', 'S', 'E']),
]

MAX_DENSITY = 4

class BestOption(Behaviour):  
    def __init__(self, best_option):
        self.best_option = best_option
        self.neighbour_cur_following = None

    def find_compass_from_angle(self, person):
        delta_x = self.best_option.x - person.x
        delta_y = -1*(self.best_option.y - person.y)
        angle = np.arctan2(delta_y, delta_x) # value from -PI to PI

        for upper_limit, compass in davinci_wheel:
            if angle <= upper_limit:
                return compass

    def convert_compass_to_neighbours(self, person, current_tile):
        compass = self.find_compass_from_angle(person)
        desired_neighbours = []
        for direction in compass:
            neighbour = current_tile.neighbours.get(direction)
            desired_neighbours.append(neighbour)

        return desired_neighbours

    def undo_motion(self, person, x: int, y: int):
        person.x -= x
        person.y -= y

    def choose_neighbour_to_follow(self, person, current_tile, traversed_tiles):
        # find high density neighbour tiles, if tie, draw randomly from tiers
        if self.best_option:
            prioritized_neighbours = self.convert_compass_to_neighbours(person, current_tile) #[Tile?, Tile?, Tile?, Tile?]
            neighbours_to_consider = prioritized_neighbours[0:2]
            random.shuffle(neighbours_to_consider)
            person.color = (0, 0, 200)
        else:
            neighbours_to_consider = list(current_tile.neighbours.values())
            random.shuffle(neighbours_to_consider)
            person.color = (255, 100, 255)

        neighbour_to_follow = None
        curr_highest_density = 0

        for neighbour in neighbours_to_consider:
            if not neighbour:
                continue
            heat = sum(neighbour.heatmap)
            if neighbour.density >= MAX_DENSITY:
                continue
            if neighbour.obstacle:
                continue
            if not self.best_option and neighbour in traversed_tiles:
                continue
            # if neighbour == previous_tile:
            #     continue
            if not neighbour_to_follow or heat > curr_highest_density:
                curr_highest_density = heat
                neighbour_to_follow = neighbour
 
        if not neighbour_to_follow and self.best_option:
            for neighbour in prioritized_neighbours[2:4]:
                if neighbour and neighbour.density < MAX_DENSITY and not neighbour.obstacle:
                    neighbour_to_follow = neighbour
        
        if not neighbour_to_follow:
            neighbour_to_follow = current_tile
            person.color = (200, 200, 0)

        return neighbour_to_follow


    def go(self, person, exits, fires, aptitude, current_tile, width, height, previous_tile, traversed_tiles):
        if not self.neighbour_cur_following or (self.neighbour_cur_following.density >= MAX_DENSITY or self.neighbour_cur_following == current_tile):
            neighbour_to_follow = self.choose_neighbour_to_follow(person, current_tile, traversed_tiles)
            self.neighbour_cur_following = neighbour_to_follow
        else:
            neighbour_to_follow = self.neighbour_cur_following

        # problem not down here
        x = np.random.choice(neighbour_to_follow.width) + neighbour_to_follow.x
        y = np.random.choice(neighbour_to_follow.height) + neighbour_to_follow.y

        hyp = math.hypot(x - person.x, y - person.y)
        if hyp == 0:
            return
        unit_vector_x = 5*(x - person.x)/(hyp)
        unit_vector_y = 5*(y - person.y)/(hyp)

        x_motion = (np.random.choice([unit_vector_x, -unit_vector_x], 1, p=[1, 0]))[0]
        y_motion = (np.random.choice([unit_vector_y, -unit_vector_y], 1, p=[1, 0]))[0]
        person.x += x_motion
        person.y += y_motion

        if neighbour_to_follow == current_tile:
            # undo movement if you colided with another person.
            for other in current_tile.people_in_tile:
                if other.colliderect(person) and not person.is_me(other):
                    self.undo_motion(person, x_motion, y_motion)
                    return

        if self.out_of_bounds(person.x, person.y, width, height):
            self.undo_motion(person, x_motion, y_motion)
