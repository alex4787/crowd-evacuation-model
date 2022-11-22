from game_objects import People, Exit, Fire
from density_grid import Grid, Tile
from behaviours import MoveToExit
from density_grid import Maps, Tiles

from typing import List
from random import randint

def gen_valid_coordinate(width: int, height: int, obstacles: List[Tile], floor: int):
    while True:
        x, y = randint(0, width-1), randint(0, height-1)
        in_the_clear = True
        for obstacle in obstacles:
            if (obstacle.x//floor, obstacle.y//floor) == (x//floor, y//floor):
                in_the_clear = False
                break
        if in_the_clear:
            return x, y




class Collections:
    def __init__(self, width: int, height: int, player_count: int) -> None:
        self.grid: Grid = Grid()

        #populations
        self.people: List[People] = []
        self.next_people_id: int = 1

        self.exits: List[Exit] = []
        self.next_exit_id: int = 1

        self.fires: List[Fire] = []

        self.exits.append(Exit(0, 0, 1))
        self.exits.append(Exit(980, 980, 2))

        self.maps: Maps = Maps()

        for i in range(player_count):
            coordinate = gen_valid_coordinate(width, height, self.grid.obstacles, 50)
            person = People(coordinate[0], coordinate[1], self.next_people_id, behaviour=None)
            self.people.append(person)
            self.next_people_id+=1
            tile = self.grid.tiles[person.y//50][person.x//50]
            tile.add_person(person)
            self.maps.person_to_tiles[person] = Tiles(None, tile)

        # self.fires.append(Fire(460, 60))
