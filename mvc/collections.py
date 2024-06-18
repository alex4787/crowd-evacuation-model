from game_objects.people import People
from density_grid import Grid, Tile
from behaviours import MoveToExit
from density_grid import PersonToTileHistoryMap, TileHistory
from config import *

from typing import List, Tuple
import random


class Collections:
    def __init__(self, proportion) -> None:
        self.grid: Grid = Grid()
        self.people: List[People] = []
        self.maps: PersonToTileHistoryMap = PersonToTileHistoryMap()
        
        self.next_people_id: int = 1
        self.next_exit_id: int = 1

        self.proportion = proportion

        occupied = []

        for i in range(AGENT_COUNT):
            if ONE_AGENT_PER_TILE:
                x, y = self.gen_valid_coordinate(SPAWN_DIMENSIONS, self.grid.obstacles, self.grid.fires,
                                                 self.grid.barriers, occupied=occupied, center=True)
                if x is None and y is None:
                    break
            else:
                x, y = self.gen_valid_coordinate(SPAWN_DIMENSIONS, self.grid.obstacles, self.grid.fires, self.grid.barriers)
            if i < self.proportion*AGENT_COUNT:
                person = People(x, y, self.next_people_id, behaviour=None, speed=AGENT_SPEED_1)
            else:
                person = People(x, y, self.next_people_id, behaviour=None, speed=AGENT_SPEED_2)
            self.people.append(person)
            self.next_people_id+=1
            tile = self.grid.tiles[person.y//FLOOR][person.x//FLOOR]
            tile.add_person(person)
            self.maps.person_to_tiles[person] = TileHistory(None, tile)


    def gen_valid_coordinate(self, valid_tiles: List[Tuple[int, int]], obstacles: List[Tile], fires: List[Tile], barriers: List[Tile], occupied: List[Tuple[int, int]] = None, center: bool = False):
        if occupied is None:
            occupied = []

        invalid_tiles = obstacles + fires + barriers
        invalid_tile_coords = [(tile.x // FLOOR, tile.y // FLOOR) for tile in invalid_tiles]
        candidate_tiles = list(set(valid_tiles) - set(invalid_tile_coords) - set(occupied))

        if len(candidate_tiles) == 0:
            return None, None

        chosen = candidate_tiles[random.randint(0, len(candidate_tiles) - 1)]
        x_floor = chosen[0]
        y_floor = chosen[1]

        occupied.append((x_floor, y_floor))

        if center:
            x, y = x_floor * FLOOR + (FLOOR / 2), y_floor * FLOOR + (FLOOR / 2)
        else:
            x, y = random.randint(0, FLOOR - 1) + (x_floor * FLOOR), random.randint(0, FLOOR - 1) + (y_floor * FLOOR)
        return x, y
