from mvc import Collections


class Controller:
    def __init__(self, collections: Collections, width: int, height: int) -> None:
        self.collections: Collections = collections
        self.width: int = width
        self.height: int = height
        self.tick: int = 0

    def update(self):
        self.tick += 1

        # instead of recalculating this every time, is there a way to update it on the go?
        for row in range(10): # 10 or 9 ?
            for col in range(10): # 10 or 9 ?
                self.collections.grid.tiles[row][col].update_average_direction()

        for person in self.collections.people:
            for exit in self.collections.exits:
                if person.colliderect(exit):
                    self.collections.people.remove(person)

            current_tile = self.collections.grid.tiles[person.x//100][person.y//100]
            
            person.move(
                self.collections.people,
                self.collections.exits,
                fires=None,
                aptitude=0.9,
                current_tile=current_tile,
                width = self.width,
                height = self.height
            )

            # switch the logical tile if needed
            if person.tile_has_changed():
                self.collections.grid.tiles[person.previous_y//100][person.previous_x//100].people_in_tile.remove(person)
                self.collections.grid.tiles[person.y//100][person.x//100].people_in_tile.append(person)
                


        
