from game_objects.people import People
from density_grid import Grid, Tile
from behaviours import MoveToExit
from density_grid import Maps, Tiles
from config import *

from typing import List, Tuple
from random import randint

class Collections:
    def __init__(self) -> None:
        self.grid: Grid = Grid()
        self.people: List[People] = []
        self.maps: Maps = Maps()
        
        self.next_people_id: int = 1
        self.next_exit_id: int = 1

        for _ in range(AGENT_COUNT):
            x, y = self.gen_valid_coordinate(SPAWN_DIMENSIONS, self.grid.obstacles, self.grid.fires)
            person = People(x, y, self.next_people_id, behaviour=None, speed=AGENT_SPEED)
            self.people.append(person)
            self.next_people_id+=1
            tile = self.grid.tiles[person.y//FLOOR][person.x//FLOOR]
            tile.add_person(person)
            self.maps.person_to_tiles[person] = Tiles(None, tile)


    def gen_valid_coordinate(self, wh: Tuple[int, int], obstacles: List[Tile], fires: List[Tile]):
        width, height = wh[0], wh[1]
        while True:
            x, y = randint(0, width-1), randint(0, height-1)
            in_the_clear = True
            for obstacle in obstacles:
                if (obstacle.x//FLOOR, obstacle.y//FLOOR) == (x//FLOOR, y//FLOOR):
                    in_the_clear = False
                    break
            for fire in fires:
                if (fire.x//FLOOR, fire.y//FLOOR) == (x//FLOOR, y//FLOOR):
                    in_the_clear = False
                    break
            if in_the_clear:
                return x, y

        
