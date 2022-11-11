from .. import Collections


class Controller:
    def __init__(self, collections: Collections, width: int, height: int) -> None:
        self.collections: Collections = collections
        self.width: int = width
        self.height: int = height
        self.tick: int = 0

    def update(self):
        self.tick += 1

        # for fire in self.collections.fires:
        #     fire.update()

        for person in self.collections.people:
            for exit in self.collections.exits:
                if person.colliderect(exit):
                    print(f'Player {person.id} Escaped')
                    self.collections.people.remove(person)

            previous_x = person.x
            previous_y = person.y

            person.move(self.collections.people, self.collections.exits, fires=None, aptitude=0.9)

            # switch the logical tile if needed
            if person.tile_has_changed(previous_x, previous_y):
                self.collections.grid.tiles[previous_y//100][previous_x//100].people_in_tile.remove(person)
                self.collections.grid.tiles[person.y//100][person.x//100].people_in_tile.append(person)
                


        
