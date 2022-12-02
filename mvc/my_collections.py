from game_objects import People, Exit
from density_grid import Grid, Tile
from behaviours import MoveToExit
from density_grid import Maps, Tiles

from typing import List
from random import randint

class Collections:
    def __init__(self, width: int, height: int, floor: int, player_count: int) -> None:
        self.grid: Grid = Grid()
        self.people: List[People] = []
        self.exits: List[Exit] = []
        self.maps: Maps = Maps()
        
        self.next_people_id: int = 1
        self.next_exit_id: int = 1

        self.exits.append(Exit(0, 980, 1))
        self.exits.append(Exit(980, 980, 2))

        for _ in range(player_count):
            x, y = self.gen_valid_coordinate(width, height//3, self.grid.obstacles, self.grid.fires, floor)
            person = People(x, y, self.next_people_id, behaviour=None)
            self.people.append(person)
            self.next_people_id+=1
            tile = self.grid.tiles[person.y//floor][person.x//floor]
            tile.add_person(person)

            # ARE THESE EVEN USED ANYMORE ?
            self.maps.person_to_tiles[person] = Tiles(None, tile) ##### IS THIS NEEDED?
            self.maps.person_to_tiles[person].traversed_tiles.append(tile) ##### IS THIS NEEDED?


    def gen_valid_coordinate(self, width: int, height: int, obstacles: List[Tile], fires: List[Tile], floor: int):
        while True:
            x, y = randint(0, width-1), randint(0, height-1)
            in_the_clear = True
            for obstacle in obstacles:
                if (obstacle.x//floor, obstacle.y//floor) == (x//floor, y//floor):
                    in_the_clear = False
                    break
            for fire in fires:
                if (fire.x//floor, fire.y//floor) == (x//floor, y//floor):
                    in_the_clear = False
                    break
            if in_the_clear:
                return x, y

        
