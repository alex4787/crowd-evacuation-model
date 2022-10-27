from .plants import Plants
from .prey import Prey
from random import randint

class BoardState:
    def __init__(self, width, height):
        self.plants = []
        next_plant_id = 1
        self.preys = []

        for plant in range(20):
            self.plants.append(Plants("bassic", (0, 255, 0), 4, 100, randint(0, width), randint(0, height), next_plant_id))
            next_plant_id+=1
        for prey in range(10):
            self.preys.append(Prey("bassic", (0, 0, 255), 6, 300, 500, randint(0, width), randint(0, height)))

    def update(self):
        for plant in self.plants:
            plant.grow()

        for prey in self.preys:
            prey.grow()
            # kill the prey if it runs out of energy
            if prey.current_energy_level < 0:
                self.preys.remove(prey)

            # move the prey, then check if it has collided with a plant
            prey.move(self.plants, 0.7)
            if prey.is_colliding:
                for plant in self.plants:
                    if plant.id == prey.closest_plant_id:
                        self.plants.remove(plant)
                prey.current_energy_level += 300
                
            # spawn a new prey, if any have outlasted their spawn timer
            if prey.spawning_time < 0:
                prey.spawning_time = 500
                self.preys.append(Prey("bassic", (0, 0, 255), 6, 300, 500, prey.x, prey.y))

            


