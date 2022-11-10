from game_objects.people import People
from game_objects.exit import Exit
from game_objects.fire import Fire
from random import randint

class Collections:
    def __init__(self, width, height):
        #populations
        self.people = []
        self.next_people_id = 1

        self.exits = []
        self.next_exit_id = 1

        self.fires = []

        for person in range(1000):
            self.people.append(People(True, randint(0, width), randint(0, height), self.next_people_id))
            self.next_people_id+=1

        self.exits.append(Exit(0, 0, 1))
        self.exits.append(Exit(0, 800, 2))

        # self.fires.append(Fire(460, 60))