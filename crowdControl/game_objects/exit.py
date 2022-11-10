from pygame import Rect

class Exit(Rect):
    def __init__(self, x, y, id):
        self.color = (255, 223, 0)
        self.height = 20
        self.width = 20
        self.x = x
        self.y = y
        self.id = id