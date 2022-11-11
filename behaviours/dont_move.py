from behaviours import Behaviour
import numpy as np
import math

class DontMove(Behaviour):  
    def __init__(self):
        return

    def go(self, person, exits, fires, aptitude):
        print(f'player {person.id} Can\'t See')
        person.color = (0, 0, 200)
        return