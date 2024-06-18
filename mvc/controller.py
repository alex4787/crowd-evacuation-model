from mvc import Collections
from statboard import StatBoard

from config import *


class Controller:
    def __init__(self, collections: Collections, width: int, height: int, stats: StatBoard) -> None:
        self.collections: Collections = collections
        self.stats: StatBoard = stats
        self.width: int = width
        self.height: int = height
        self.tick: int = 0

    def update_exit_distance_maps(self):
        for exit in self.collections.grid.exits:
            for row in self.collections.grid.tiles:
                for tile in row:
                    tile.exit_distance_map[exit.id] = None

            exit_tile = self.collections.grid.tiles[exit.y//FLOOR][exit.x//FLOOR]
            frontier = [exit_tile]
            explored_tiles = set()
            distance = 0

            while (frontier):
                new_frontier = set()
                for tile in frontier:
                    explored_tiles.add(tile)
                    tile.exit_distance_map[exit.id] = distance
                    for neighbour in tile.neighbours.values():
                        if neighbour.is_open_tile() and neighbour not in explored_tiles:
                            new_frontier.add(neighbour)
                distance += 1            
                frontier = list(new_frontier)

    def check_has_exited(self, person):
        for exit in self.collections.grid.exits:
            if person in exit.people_in_tile:
                if person.time_on_exit <= 0:
                    if person.speed == AGENT_SPEED_1:
                        self.stats.escape_count_t1 += 1
                    else:
                        self.stats.escape_count_t2 += 1
                    self.stats.remaining_count -= 1
                    self.collections.maps.person_to_tiles[person].current.remove_person(person)
                    self.collections.people.remove(person)
                    return True
                else:
                    person.time_on_exit -= 1
                    return True
        return False


    def update(self):
        if self.tick == 0:
            self.update_exit_distance_maps()

        self.tick += 1
        if self.collections.grid.update_fires():
            self.update_exit_distance_maps()

        for row in range(20):
            for col in range(20):
                self.collections.grid.tiles[row][col].update_heatmap()

        newly_entered_tiles = set()

        for person in self.collections.people:
            if person.is_dead:
                continue
            if self.collections.maps.person_to_tiles[person].current.is_fire:
                person.color = BLACK
                person.is_dead = True
                if person.speed == AGENT_SPEED_1:
                    self.stats.burn_count_t1 += 1
                else:
                    self.stats.burn_count_t2 += 1
                self.stats.remaining_count -= 1
                continue
            if self.check_has_exited(person):
                continue

            person.move(
                self.collections.people,
                self.collections.grid.exits,
                grid=self.collections.grid,
                aptitude=0.9,
                current_tile=self.collections.maps.person_to_tiles[person].current,
                previous_tile=self.collections.maps.person_to_tiles[person].previous,
                traversed_tiles=self.collections.maps.person_to_tiles[person].traversed_tiles,
                width = self.width,
                height = self.height
            )
            if person.tile_has_changed():
                previous_tile = self.collections.maps.person_to_tiles[person].current
                previous_tile.remove_person(person)
                self.collections.maps.person_to_tiles[person].previous = previous_tile

                current_tile = self.collections.grid.tiles[person.y//FLOOR][person.x//FLOOR]
                current_tile.add_person(person)
                self.collections.maps.person_to_tiles[person].current = current_tile
                self.collections.maps.person_to_tiles[person].traversed_tiles.append(current_tile)

                newly_entered_tiles.add(current_tile)


        for current_tile in newly_entered_tiles:
            victim = current_tile.murder_if_too_dense()
            if victim:
                if victim.speed == AGENT_SPEED_1:
                    self.stats.crush_count_t1 += 1
                else: 
                    self.stats.crush_count_t2 += 1
                self.stats.remaining_count -= 1



                


        
