import numpy as np
import math

class People:
    def __init__(self, living, x, y, id):
        self.color = (0, 255, 0)
        self.size = 5
        self.x = x
        self.y = y
        self.id = id

    def slope(self, x1, y1, x2, y2):
            slope = (y2 - y1) / (x2 - x1)
            return slope

    def find_closest_exit(self, exits):
        closest_exit = exits[0]
        min_hyp = math.hypot(closest_exit.x - self.x, closest_exit.y - self.y)
        for exit in exits:
            hyp = math.hypot(exit.x - self.x, exit.y - self.y)
            if hyp < min_hyp:
                closest_exit = exit
                min_hyp = hyp
        # self.closest_plant_id = min_distance_plant.id
        return (closest_exit.x, closest_exit.y, min_hyp)

    def move(self, exits, aptitude):
        x, y, min_hyp = self.find_closest_exit(exits)
        slope = self.slope(self.x, self.y, x, y)
        unit_vector_x = 3*(x - self.x)/(min_hyp)
        unit_vector_y = 3*(y - self.y)/(min_hyp)

        self.x += (np.random.choice([unit_vector_x, -unit_vector_x], 1, p=[aptitude, 1-aptitude]))[0]
        self.y += (np.random.choice([unit_vector_y, -unit_vector_y], 1, p=[aptitude, 1-aptitude]))[0]
        # we move in the correct direction aptitude % of the time
        # if x > self.x:
        #     self.x += (np.random.choice([1, -1], 1, p=[aptitude, 1-aptitude]))[0]
        # else:
        #     self.x += (np.random.choice([1, -1], 1, p=[1-aptitude, aptitude]))[0]
        # if y > self.y:
        #     self.y += (np.random.choice([1, -1], 1, p=[aptitude, 1-aptitude]))[0]
        # else:
        #     self.y += (np.random.choice([1, -1], 1, p=[1-aptitude, aptitude]))[0]