from mvc import Collections
from statboard import StatBoard


class Controller:
    def __init__(self, collections: Collections, width: int, height: int, stats: StatBoard) -> None:
        self.collections: Collections = collections
        self.stats: StatBoard = stats
        self.width: int = width
        self.height: int = height
        self.tick: int = 0

    def update_exit_distance_maps(self):
        for exit in self.collections.exits:
            for row in self.collections.grid.tiles:
                for tile in row:
                    tile.exit_distance_map[exit.id] = None

            exit_tile = self.collections.grid.tiles[exit.y//50][exit.x//50]
            frontier = [exit_tile]
            explored_tiles = set()
            distance = 0

            while (frontier):
                new_frontier = set()
                for tile in frontier:
                    explored_tiles.add(tile)
                    tile.exit_distance_map[exit.id] = distance
                    for neighbour in tile.neighbours.values():
                        if not neighbour.is_fire and not neighbour.is_obstacle and neighbour not in explored_tiles:
                            new_frontier.add(neighbour)
                distance += 1            
                frontier = list(new_frontier)
            # get current tile of exit
            # iterate and set tiles' mappings values


    def update(self):
        if self.tick == 0:
            self.update_exit_distance_maps()

        self.tick += 1
        if self.collections.grid.update_fires():
            self.update_exit_distance_maps()


        for row in range(20):
            for col in range(20):
                self.collections.grid.tiles[row][col].update_average_direction()
                self.collections.grid.tiles[row][col].update_density()
                self.collections.grid.tiles[row][col].update_heatmap()


        for person in self.collections.people:
            if person.is_dead:
                continue
            #check if they are dead
            if self.collections.maps.person_to_tiles[person].current.is_fire:
                person.color = (0, 0, 0)
                person.is_dead = True
                self.stats.death_count += 1
                self.stats.remaining_count -= 1
                continue
            for exit in self.collections.exits:
                if person.colliderect(exit):
                    self.stats.escape_count += 1
                    self.stats.remaining_count -= 1
                    self.collections.people.remove(person)
            
            person.move(
                self.collections.people,
                self.collections.exits,
                obstacles = self.collections.grid.obstacles,
                fires = self.collections.grid.fires,
                aptitude=0.9,
                current_tile=self.collections.maps.person_to_tiles[person].current,
                previous_tile=self.collections.maps.person_to_tiles[person].previous,
                traversed_tiles=self.collections.maps.person_to_tiles[person].traversed_tiles,
                width = self.width,
                height = self.height
            )

            # switch the logical tile if needed
            if person.tile_has_changed():
                previous_tile = self.collections.maps.person_to_tiles[person].current
                previous_tile.remove_person(person)
                self.collections.maps.person_to_tiles[person].previous = previous_tile

                # person.traversed_tiles.add(previous_tile)
                
                current_tile = self.collections.grid.tiles[person.y//50][person.x//50]
                current_tile.add_person(person)
                self.collections.maps.person_to_tiles[person].current = current_tile

                self.collections.maps.person_to_tiles[person].traversed_tiles.append(current_tile)
                


        
