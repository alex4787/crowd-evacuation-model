import math
import numpy as np

class Prey:
    def __init__(self, type, color, size, current_energy_level, spawning_time, x, y, is_colliding=False):
        self.type = type
        self.color = color
        self.size = size
        self.current_energy_level = current_energy_level
        self.spawning_time = spawning_time
        self.x = x
        self.y = y
        self.closest_plant_id = None
        self.is_colliding = is_colliding


    def __str__(self):
        return f"{self.type} : {self.color} : {self.size} : {self.current_energy_level} : {self.spawning_time} : ({self.x, self.y})"


    def grow(self):
        self.current_energy_level -= 1
        self.spawning_time -= 1


    def find_closest_plant(self, plants):
        min_distance_plant = plants[0]
        min_hyp = math.hypot(min_distance_plant.x - self.x, min_distance_plant.y - self.y)
        for plant in plants:
            hyp = math.hypot(plant.x - self.x, plant.y - self.y)
            if hyp < min_hyp:
                min_distance_plant = plant
                min_hyp = hyp
        self.closest_plant_id = min_distance_plant.id
        return (min_distance_plant.x, min_distance_plant.y, min_distance_plant.size)


    def has_it_collided_with_plant(self, x, y, size):
        self.is_colliding = True if (x <= self.x <= x+size) and (y <= self.y <= y+size) else False
            

    def move(self, plants, aptitude):
        if plants:
            x, y, size = self.find_closest_plant(plants)
            # we move in the correct direction aptitude % of the time
            if x > self.x:
                self.x += (np.random.choice([1, -1], 1, p=[aptitude, 1-aptitude]))[0]
            else:
                self.x += (np.random.choice([1, -1], 1, p=[1-aptitude, aptitude]))[0]
            if y > self.y:
                self.y += (np.random.choice([1, -1], 1, p=[aptitude, 1-aptitude]))[0]
            else:
                self.y += (np.random.choice([1, -1], 1, p=[1-aptitude, aptitude]))[0]

            self.has_it_collided_with_plant(x, y, size)
        else:
            return
            # stand still and die ?
            # eventually, we should "wander / flee enemies"

