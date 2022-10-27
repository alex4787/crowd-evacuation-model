from .plants import Plants
from .prey import Prey
from random import randint

class BoardState:
    def __init__(self, width, height):
        self.plants = []
        self.preys = []
        for plant in range(20):
            self.plants.append(Plants("bassic", (0, 255, 0), 4, 100, randint(0, width), randint(0, height)))
        for prey in range(10):
            self.preys.append(Prey("bassic", (0, 0, 255), 6, 300, 1000, randint(0, width), randint(0, height)))

    def update(self):
        for plant in self.plants:
            plant.grow()
        for prey in self.preys:
            if prey.current_energy_level < 0:
                self.preys.remove(prey)
            #if prey.spawning_time < 0:

