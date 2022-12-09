from __future__ import annotations
from typing import Tuple, List, Set, Deque, Dict
from pygame import Rect
from behaviours import Behaviour, MapPath
from density_grid.exit import Exit
from density_grid import Tile, Grid
import math

from config import *

class People(Rect):
    def __init__(self, x: int, y: int, id: int, behaviour: Behaviour, speed: int) -> None:
        self.color: Tuple[int, int, int] = (0, 255, 0)
        self.is_dead: bool = False
        self.height: int = 15
        self.width: int = 15
        self.x: int = x
        self.y: int = y
        self.previous_x: int = x 
        self.previous_y: int = y
        self.id: int = id
        self._behaviour: Behaviour = behaviour
        self.best_option: Exit = None
        self.exits_in_memory: Dict[int, int] = dict()
        self.panic = 0
        self.speed = speed

    def __hash__(self):
        return self.id

    @property
    def behaviour(self) -> Behaviour:
        return self._behaviour

    @behaviour.setter
    def behaviour(self, behaviour: Behaviour) -> None:
        self._behaviour = behaviour

    def tile_has_changed(self) -> bool:
        return self.x//FLOOR != self.previous_x//FLOOR or self.y//FLOOR != self.previous_y//FLOOR

    def is_me(self: People, other: People) -> bool:
        if self.id == other.id:
            return True
        return False

    def distance(self, seg):
        return math.sqrt((seg[0][0] - seg[1][0])**2 + (seg[0][1] - seg[1][1])**2)

    def is_other_in_the_way(self, other: Rect, line: Tuple[Tuple[int, int], Tuple[int, int]]) -> bool:
        seg = other.clipline(line)
        if seg == () or self.distance(seg) < (math.sqrt(2))*self.width/2:
            return False
        return True

    def is_valid_line_of_sight(self, line: Tuple[Tuple[int, int], Tuple[int, int]], people: List[People], tiles: List[List[Tile]]) -> bool:
        for other in people: 
            if not self.is_me(other) and self.is_other_in_the_way(other, line):
                return False
        
        for row in tiles:
            for tile in row:
                if tile.is_fire or tile.is_obstacle:
                    if self.is_other_in_the_way(tile, line):
                        return False
        return True

    def exits_in_sight(self, people: List[People], exits: List[Exit], tiles: List[List[Tile]]) -> List[Exit]:
        exits_in_sight = []
        for exit in exits:
            line = ((self.centerx, self.centery), (exit.centerx, exit.centery))
            if self.is_valid_line_of_sight(line, people, tiles):
                exits_in_sight.append(exit)  
        return exits_in_sight

    def move(
            self,
            people: List[People],
            exits: List[Exit],
            grid: Grid,
            aptitude: float,
            current_tile: Tile,
            previous_tile: Tile,
            traversed_tiles: Deque[Tile],
            width: int,
            height: int
            ) -> None:

        self.panic = len(grid.fires) / (len(grid.tiles) * len(grid.tiles[0]))

        temp_x = self.x
        temp_y = self.y

        availible_exits = self.exits_in_sight(people, exits=exits, tiles=grid.tiles)
        for exit in availible_exits:
            self.exits_in_memory[exit.id] = 500 # tninker with this value
        exit_ids_to_delete = []
        for exit_id, counter in self.exits_in_memory.items():
            if counter == 0:
                exit_ids_to_delete.append(exit_id)
            else:
                self.exits_in_memory[exit_id]-=1
        for id in exit_ids_to_delete:
            del(self.exits_in_memory[id])

        # Update best option
        availible_exits = self.exits_in_sight(people, exits=exits, tiles=grid.tiles)
        if not self.best_option and availible_exits:
            self.best_option = availible_exits[0]

        best_option_distance = self.distance([[self.x, self.y], [self.best_option.x, self.best_option.y]]) if self.best_option else None
        for exit in availible_exits:
            exit_distance = self.distance([[self.x, self.y], [exit.x, exit.y]])
            if exit_distance < best_option_distance:
                self.best_option = exit
                best_option_distance = exit_distance
 
        if not isinstance(self._behaviour, MapPath):
            self._behaviour = MapPath()

        self._behaviour.go(
            exits=availible_exits,
            aptitude=aptitude,
            person=self,
            current_tile=current_tile,
            width=width,
            height=height,
            previous_tile=previous_tile,
            traversed_tiles=traversed_tiles,
            )
        
        self.previous_x = temp_x
        self.previous_y = temp_y
