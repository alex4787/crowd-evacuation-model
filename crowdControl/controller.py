class Controller:
    def __init__(self, collections, width, height):
        self.collections = collections
        self.width = width
        self.height = height

        self.tick = 0

    def update(self):
        self.tick += 1

        for fire in self.collections.fires:
            fire.update()

        for person in self.collections.people:
            escaped = person.move(self.collections.exits, self.collections.fires, 0.9)
            if escaped:
                print(f'Player {person.id} Escaped')
                self.collections.people.remove(person)
