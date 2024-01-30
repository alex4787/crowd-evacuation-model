from behaviours import Behaviour
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_objects import People

import numpy as np
import math
from math import pi
import random
import pygame

from config import *

class MapPath(Behaviour):  
    def __init__(self):
        self.neighbour_cur_following = None

    def undo_motion(self, person, x: int, y: int):
        person.x -= x
        person.y -= y

    def choose_neighbour_to_follow(self, person, current_tile, traversed_tiles):
        neighbour_to_follow = None

        neighbours_to_consider = list(current_tile.neighbours.values())
        neighbours_to_consider = [neighbour for neighbour in neighbours_to_consider if neighbour.is_open_tile()]
        random.shuffle(neighbours_to_consider)

        # Find prefered tile based on map paths if possible (player must have exits inb memory)
        if person.exits_in_memory:
            for neighbour in neighbours_to_consider:
                if not self.should_ignore_density and neighbour.density >= MAX_DENSITY:
                    continue # although, if fire on our ass
                if neighbour.is_danger:
                    continue # we need to allow them to walk on these, but my brain is dying
                if all(x == None for x in neighbour.exit_distance_map.values()):
                    continue
                if not neighbour_to_follow:
                    neighbour_to_follow = neighbour
                    person.color = (pygame.color.Color("blue"))
                    continue

                neighbour_min_distance = min([v for k, v in neighbour.exit_distance_map.items() if k in person.exits_in_memory.keys() and v != None], default=0)
                neighbour_to_follow_min_distance = min([v for k, v in neighbour_to_follow.exit_distance_map.items() if k in person.exits_in_memory.keys() and v != None], default=0)
                if neighbour_min_distance < neighbour_to_follow_min_distance:
                    neighbour_to_follow = neighbour
                    person.color = (pygame.color.Color("blue"))

                # for exit_id in person.exits_in_memory.keys():
                #     if neighbour.exit_distance_map[exit_id] != None:
                #         if neighbour.exit_distance_map[exit_id] < min(x for x in neighbour_to_follow.exit_distance_map.values() if x != None):
                #             neighbour_to_follow = neighbour
                #             person.color = (pygame.color.Color("lightblue"))

        # If no desirable tiles, 
        cur_highest_heatmap = -1
        
        if not neighbour_to_follow:
            # if all neighbours are traversed, then ignore the traversed check
            all_neighbours_traversed = all(n in traversed_tiles or n.is_danger or (not self.should_ignore_density and n.density >= MAX_DENSITY) for n in neighbours_to_consider)
            for neighbour in neighbours_to_consider:
                # consider own as an option? because they're forced to move the other way if 
                # never do opposite of heatmap, do next best
                heat = sum(neighbour.heatmap)
                if neighbour.is_danger:
                    continue
                if not self.should_ignore_density and neighbour.density >= MAX_DENSITY:
                    continue
                if not all_neighbours_traversed and neighbour in traversed_tiles:
                    continue
                if heat > cur_highest_heatmap:
                    cur_highest_heatmap = heat
                    person.color = (pygame.color.Color("pink"))
                    neighbour_to_follow = neighbour

        # If still no tiles are desireable, stay put.
        if not neighbour_to_follow:
            neighbour_to_follow = current_tile
            person.color = (pygame.color.Color("yellow"))

        return neighbour_to_follow

    def go(self, person, exits, aptitude, current_tile, width, height, previous_tile, traversed_tiles):
        neighbour_to_follow = None
        self.should_ignore_density = random.random() < PANIC

        # If in danger, Move away from the fire
        if current_tile.is_danger:
            best_safe_tile = None
            best_danger_tile = None
            for tile in current_tile.neighbours.values():
                if tile.is_obstacle or tile.is_barrier:
                    continue
                if not tile.is_danger and not tile.is_fire:
                    best_safe_tile = tile
                elif tile.is_danger:
                    best_danger_tile = tile

            neighbour_to_follow = best_safe_tile or best_danger_tile or current_tile
        
        # If not in danger, but not currentyl following anyone, pick a new tile
        elif not self.neighbour_cur_following:
            neighbour_to_follow = self.choose_neighbour_to_follow(person, current_tile, traversed_tiles)
            self.neighbour_cur_following = neighbour_to_follow

        # If you are in the tile you were trying to get to, pick a new tile
        elif self.neighbour_cur_following == current_tile:
            neighbour_to_follow = self.choose_neighbour_to_follow(person, current_tile, traversed_tiles)
            self.neighbour_cur_following = neighbour_to_follow

        # If the target tile becomes to dense, pick a new one
        elif not self.should_ignore_density and self.neighbour_cur_following.density >= MAX_DENSITY:
            neighbour_to_follow = self.choose_neighbour_to_follow(person, current_tile, traversed_tiles)
            self.neighbour_cur_following = neighbour_to_follow

        # if the previous target is now fire or danger, select a new one.
        elif self.neighbour_cur_following.is_danger or self.neighbour_cur_following.is_fire:
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
        unit_vector_x = person.speed*(x - person.x)/(hyp)
        unit_vector_y = person.speed*(y - person.y)/(hyp)
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
