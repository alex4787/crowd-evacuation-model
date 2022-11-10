import numpy as np
import math
from pygame import Rect

class People(Rect):
    def __init__(self, living, x, y, id):
        self.color = (0, 255, 0)
        self.height = 5
        self.width = 5
        self.x = x
        self.y = y
        self.id = id

    def find_closest_exit(self, exits):
        closest_exit = exits[0]
        min_hyp = math.hypot(closest_exit.x - self.x, closest_exit.y - self.y)
        for exit in exits:
            hyp = math.hypot(exit.x - self.x, exit.y - self.y)
            if hyp < min_hyp:
                closest_exit = exit
                min_hyp = hyp
        return (closest_exit.x, closest_exit.y, min_hyp)

    def move(self, exits, fires, aptitude):
        x, y, min_hyp = self.find_closest_exit(exits)

        if min_hyp == 0: # handle this differently.
            min_hyp = 1

        unit_vector_x = 3*(x - self.x)/(min_hyp)
        unit_vector_y = 3*(y - self.y)/(min_hyp)

        if not fires:
            self.x += (np.random.choice([unit_vector_x, -unit_vector_x], 1, p=[aptitude, 1-aptitude]))[0]
            self.y += (np.random.choice([unit_vector_y, -unit_vector_y], 1, p=[aptitude, 1-aptitude]))[0]
            return

        # for fire in fires:
        #     perimeter = Rect(fire.x -20, fire.y -20, fire.width + 40, fire.height + 40)
        #     # If I am touching, then dies, switch this logic for proper death logic eventually
        #     if self.colliderect(fire):
        #         self.color = (255, 255, 255)
        #     # If I am within a threshold, run from the fire
        #     elif self.colliderect(perimeter):
        #         # if i am under or over the fire, continue with horizontal motion
        #         if self.x in range(fire.left, fire.right):
        #             self.x += (np.random.choice([unit_vector_x, -unit_vector_x], 1, p=[aptitude, 1-aptitude]))[0]
        #             # if i am above, never go down.
        #             if self.y > fire.y:
        #                 self.y += 2
        #             else:
        #                 self.y -= 2
        #         # if i am left of the fire, run left, if right of the fire, run right. In either case, verticle as normal.
        #         if self.y in range(fire.top, fire.bottom):
        #             self.y += (np.random.choice([unit_vector_y, -unit_vector_y], 1, p=[aptitude, 1-aptitude]))[0]
        #             if self.x > fire.x:
        #                 self.x += 2
        #             else:
        #                 self.x -= 2

        #     # else move normally
        #     else:
        #         self.x += (np.random.choice([unit_vector_x, -unit_vector_x], 1, p=[aptitude, 1-aptitude]))[0]
        #         self.y += (np.random.choice([unit_vector_y, -unit_vector_y], 1, p=[aptitude, 1-aptitude]))[0]

