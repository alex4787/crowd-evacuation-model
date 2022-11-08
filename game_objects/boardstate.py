from .plants import Plants
from .prey import Prey
from .graph import Graph
from random import randint

class BoardState:
    def __init__(self, width, height):
        #populations
        self.plants = []
        self.next_plant_id = 1
        self.preys = []

        #game parameters
        self.tick = 0
        self.width = width
        self.height = height

        #setting up a plot of population sizes
        self.graph = Graph()

        #initial populations
        for plant in range(20):
            self.plants.append(Plants("bassic", (0, 255, 0), 4, 100, randint(0, width), randint(0, height), self.next_plant_id))
            self.next_plant_id+=1
        for prey in range(10):
            self.preys.append(Prey("bassic", (0, 0, 255), 6, 300, 500, randint(0, width), randint(0, height)))



    def update(self):
        self.tick+=1

        #grow the plants
        for plant in self.plants:
            plant.grow()

        #spawn new plants every so often
        if self.tick%100 == 0:
            for plant in range(5):
                self.plants.append(Plants("bassic", (0, 255, 0), 4, 100, randint(0, self.width), randint(0, self.height), self.next_plant_id))
                self.next_plant_id+=1

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
                        prey.spawning_time -= 10*plant.size
                        break

            # spawn a new prey, if any have outlasted their spawn timer
            if prey.spawning_time < 0:
                prey.spawning_time = 500
                self.preys.append(Prey("bassic", (0, 0, 255), 6, 300, 500, prey.x, prey.y))


        # update the graph (pyplot population logging)
        if self.tick%10 == 0:  
            #Calculate plant SA
            plantSA = 0
            for plant in self.plants:
                plantSA += plant.size
            # update graph
            self.graph.update(self.tick, len(self.preys), plantSA)
