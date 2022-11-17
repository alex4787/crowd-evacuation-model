from game_objects import People, Exit, Fire
from density_grid import Grid
from behaviours import MoveToExit
from density_grid import Maps, Tiles

from typing import List
from random import randint

class Collections:
    def __init__(self, width: int, height: int) -> None:
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

        for i in range(250):
            person = People(randint(0, width-1), randint(0, height-1), self.next_people_id, behaviour=None)
            self.people.append(person)
            self.next_people_id+=1
            tile = self.grid.tiles[person.y//100][person.x//100]
            tile.add_person(person)
            self.maps.person_to_tiles[person] = Tiles(None, tile)

        # self.fires.append(Fire(460, 60))
