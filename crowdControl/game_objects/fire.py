from pygame import Rect

class Fire(Rect):
    def __init__(self, x, y):
        self.color = (226, 38, 84)
        self.width = 3
        self.height = 3
        self.x = x
        self.y = y

    def update(self):
        self.width += 2
        self.height += 2
        self.x -= 1
        self.y -=1