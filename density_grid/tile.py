from pygame import Rect
import numpy as np
import random
import pygame.color
from typing import TYPE_CHECKING, Tuple
from typing import List
from config import *

if TYPE_CHECKING:
    from game_objects import People

class Tile(Rect):
    def __init__(self, x: int, y: int, is_obstacle: bool = False, is_fire: bool = False, is_danger: bool = False) -> None:
        self.is_obstacle: bool = is_obstacle
        self.is_fire: bool = is_fire
        self.is_danger: bool = is_danger
        self.color = (255, 255, 255)
        self.height: int = FLOOR
        self.width: int = FLOOR 
        self.x: int = x
        self.y: int = y
        self.people_in_tile: List[People] = []
        self.density: int = len(self.people_in_tile)
        self.neighbours: dict[str, Tile] = {}
        self.heatmap: List[int] = []
        self.exit_distance_map: dict[int, int] = {}

    def __hash__(self):
        return int(f"{self.x}{self.y}")

    def update_heatmap(self):
        new_heatmap = []
        for heat in self.heatmap:
            new_heat = heat - 1
            if new_heat > 0:
                new_heatmap.append(new_heat)

        self.heatmap = new_heatmap

    def murder_if_too_dense(self):
        density_difference = self.density - MAX_DENSITY
        if density_difference > 0:
            prob_murder = density_difference * MURDER_MODIFIER
            if (random.random() < prob_murder):
                living_people_in_tile = [person for person in self.people_in_tile if not person.is_dead]
                if living_people_in_tile:
                    victim = random.choice(living_people_in_tile)
                    victim.color = RED
                    victim.is_dead = True
                    return victim


    def add_person(self, person):
        self.people_in_tile.append(person)
        self.density += 1
        if person.best_option:
            self.heatmap.append(BLUE_MAN_HEAT_DROP)
        else:
            self.heatmap.append(PINK_MAN_HEAT_DROP)

    def remove_person(self, person):
        self.people_in_tile.remove(person)
        self.density -= 1

    def tileColor(self):
        if self.is_fire:
            return pygame.color.Color('darkorange')
        elif self.is_danger:
            return pygame.color.Color('orange')
        elif self.is_obstacle:
            return pygame.color.Color('purple')
        else:
            #rgb_value = self.density*255/4     # if you wanan see density
            rgb_value = sum(self.heatmap)       # if you wanna see heat map
            return (rgb_value, rgb_value, rgb_value) if rgb_value <= 255 else pygame.color.Color('lightcyan')

