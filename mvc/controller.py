from mvc import Collections
from statboard import StatBoard


class Controller:
    def __init__(self, collections: Collections, width: int, height: int, stats: StatBoard) -> None:
        self.collections: Collections = collections
        self.stats: StatBoard = stats
        self.width: int = width
        self.height: int = height
        self.tick: int = 0

    def update(self):
        self.tick += 1

        # instead of recalculating this every time, is there a way to update it on the go?
        for row in range(20): # 10 or 9 ?
            for col in range(20): # 10 or 9 ?
                self.collections.grid.tiles[row][col].update_average_direction()
                self.collections.grid.tiles[row][col].update_density()


        for person in self.collections.people:
            for exit in self.collections.exits:
                if person.colliderect(exit):
                    self.stats.escape_count += 1
                    self.stats.remaining_count -= 1
                    self.collections.people.remove(person)
            
            person.move(
                self.collections.people,
                self.collections.exits,
                obstacles = self.collections.grid.obstacles,
                fires=None,
                aptitude=0.9,
                current_tile=self.collections.maps.person_to_tiles[person].current,
                previous_tile=self.collections.maps.person_to_tiles[person].previous,
                width = self.width,
                height = self.height
            )

            # switch the logical tile if needed
            if person.tile_has_changed():
                previous_tile = self.collections.maps.person_to_tiles[person].current
                previous_tile.remove_person(person)
                self.collections.maps.person_to_tiles[person].previous = previous_tile
                
                current_tile = self.collections.grid.tiles[person.y//50][person.x//50]
                current_tile.add_person(person)
                self.collections.maps.person_to_tiles[person].current = current_tile
                


        
