from behaviours import Behaviour
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_objects import People

import numpy as np
import math
from math import pi
import random

MAX_DENSITY = 4

class MapPath(Behaviour):  
    def __init__(self):
        self.neighbour_cur_following = None

    def undo_motion(self, person, x: int, y: int):
        person.x -= x
        person.y -= y

    def choose_neighbour_to_follow(self, person, current_tile, traversed_tiles):
        neighbour_to_follow = None
        person.color = (0, 0, 200) if person.exits_in_memory else (255, 100, 255)

        # Find prefered tile based on map paths if possible
        for neighbour in current_tile.neighbours.values():
            if neighbour.density >= MAX_DENSITY:
                continue # although, if fire on our ass
            for exit_id in person.exits_in_memory.keys():
                if neighbour_to_follow:
                    if neighbour.exit_distance_map[exit_id] < min(neighbour_to_follow.exit_distance_map.values()):
                        if not neighbour.is_danger:
                            neighbour_to_follow = neighbour
                        else:
                            continue

        # If no desirable tiles, 
        cur_highest_heatmap = 0
        if not neighbour_to_follow:
            for neighbour in current_tile.neighbours.values():
                heat = sum(neighbour.heatmap)
                if neighbour.is_danger or neighbour.is_fire:
                    continue
                if neighbour.density >= MAX_DENSITY:
                    continue
                if neighbour.is_obstacle:
                    continue
                if heat > cur_highest_heatmap:
                    cur_highest_heatmap = heat
                    neighbour_to_follow = neighbour

        # If still no tiles are desireable, stay put.
        if not neighbour_to_follow:
            neighbour_to_follow == current_tile
            person.color = (200, 200, 0)

        return neighbour_to_follow

    def go(self, person, exits, aptitude, current_tile, width, height, previous_tile, traversed_tiles):
        # If in danger, Move away from the fire
        if current_tile.is_danger:
            best_safe_tile = None
            best_danger_tile = None
            for tile in current_tile.neighbours.values():
                if not tile.is_danger and not tile.is_fire:
                    best_safe_tile = tile
                elif tile.is_danger:
                    best_danger_tile = tile
            neighbour_to_follow = best_safe_tile or best_danger_tile or current_tile
        
        # IF safe, but not currently headed anywhere, or desired tile not availble, find a new tile to head to
        elif (not self.neighbour_cur_following or self.neighbour_cur_following == current_tile) or (self.neighbour_cur_following.density >= MAX_DENSITY):
            neighbour_to_follow = self.choose_neighbour_to_follow(person, current_tile, traversed_tiles)
            self.neighbour_cur_following = neighbour_to_follow

        # IF safe, and you can continue in your desired direction.
        else:
            neighbour_to_follow = self.neighbour_cur_following

        # Get random coordinate inside neighbour_to_follow, make unit vector in that direction
        x = np.random.choice(neighbour_to_follow.width) + neighbour_to_follow.x
        y = np.random.choice(neighbour_to_follow.height) + neighbour_to_follow.y
        hyp = math.hypot(x - person.x, y - person.y)
        if hyp == 0:
            return
        unit_vector_x = 5*(x - person.x)/(hyp)
        unit_vector_y = 5*(y - person.y)/(hyp)
        person.x += unit_vector_x
        person.y += unit_vector_y

        # undo movement if you colided with another person.
        if neighbour_to_follow == current_tile:
            for other in current_tile.people_in_tile:
                if other.colliderect(person) and not person.is_me(other):
                    self.undo_motion(person, unit_vector_x, unit_vector_y)
                    return

        # undo your motion if you get pushed off the map
        if self.out_of_bounds(person.x, person.y, width, height):
            self.undo_motion(person, unit_vector_x, unit_vector_y)
