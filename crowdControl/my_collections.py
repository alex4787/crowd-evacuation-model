from game_objects.people import People
from behaviours.move_to_exit import MoveToExit
from game_objects.exit import Exit
from game_objects.fire import Fire
from density_grid.grid import Grid
from random import randint

class Collections:
    def __init__(self, width, height):
        self.grid = Grid()

        #populations
        self.people = []
        self.next_people_id = 1

        self.exits = []
        self.next_exit_id = 1

        self.fires = []

        self.exits.append(Exit(0, 0, 1))
        self.exits.append(Exit(0, 800, 2))

        for i in range(100):
            person = People(randint(0, width-1), randint(0, height-1), self.next_people_id, MoveToExit())
            self.people.append(person)
            self.next_people_id+=1
            self.grid.tiles[person.y//100][person.x//100].people_in_tile.append(person)

        # self.fires.append(Fire(460, 60))