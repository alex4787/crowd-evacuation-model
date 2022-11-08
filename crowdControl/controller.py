class Controller:
    def __init__(self, collections, width, height):
        self.collections = collections
        self.width = width
        self.height = height

        self.tick = 0

    def update(self):
        self.tick += 1

        for people in self.collections.people:
            people.move(self.collections.exits, 0.9)
