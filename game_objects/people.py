from __future__ import annotations
from typing import Tuple, List, Set, Deque, Dict
from pygame import Rect
from behaviours import Behaviour, MoveToExit, DontMove, MoveToDensity, MoveWithCrowd, FollowTheLeader, BestOption
from behaviours.map_path import MapPath
from game_objects import Exit
from density_grid import Tile, Grid
import math

class People(Rect):
    def __init__(self, x: int, y: int, id: int, behaviour: Behaviour) -> None:
        self.color: Tuple[int, int, int] = (0, 255, 0)
        self.is_dead: bool = False
        self.height: int = 10
        self.width: int = 10
        self.x: int = x
        self.y: int = y
        self.previous_x: int = x 
        self.previous_y: int = y
        self.id: int = id
        self._behaviour: Behaviour = behaviour
        self.best_option: Exit = None
        # self.traversed_tiles: Set = set()
        self.exits_in_memory: Dict[int, int] = dict()

    def __hash__(self):
        return self.id

    @property
    def behaviour(self) -> Behaviour:
        return self._behaviour

    @behaviour.setter
    def behaviour(self, behaviour: Behaviour) -> None:
        self._behaviour = behaviour

    def tile_has_changed(self) -> bool:
        return self.x//50 != self.previous_x//50 or self.y//50 != self.previous_y//50

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

    def is_valid_line_of_sight(self, line: Tuple[Tuple[int, int], Tuple[int, int]], people: List[People], obstacles: List[Tile], fires :List[Tile]) -> bool:
        for other in people: 
            if not self.is_me(other) and self.is_other_in_the_way(other, line):
                return False
        for obstacle in obstacles:
            if self.is_other_in_the_way(obstacle, line):
                return False
        for fire in fires:
            if self.is_other_in_the_way(fire, line):
                return False
        return True

    def exits_in_sight(self, people: List[People], exits: List[Exit], obstacles: List[Tile], fires: List[Tile]) -> List[Exit]:
        exits_in_sight = []
        for exit in exits:
            line = ((self.centerx, self.centery), (exit.centerx, exit.centery))
            if self.is_valid_line_of_sight(line, people, obstacles, fires):
                exits_in_sight.append(exit)  
        return exits_in_sight

    def move(
            self,
            people: List[People],
            exits: List[Exit],
            obstacles: List[Tile],
            fires: List[Tile],
            aptitude: float,
            current_tile: Tile,
            previous_tile: Tile,
            traversed_tiles: Deque[Tile],
            width: int,
            height: int
            ) -> None:

        # temp vals for current position
        temp_x = self.x
        temp_y = self.y

        #this is the movement based on path length, consider deleting logic after this
        availible_exits = self.exits_in_sight(people, exits=exits, obstacles=obstacles, fires=fires) # do we want to be blocked by fire?
        for exit in availible_exits:
            self.exits_in_memory[exit.id] = 100 # tninker with this value
        for exit_id, counter in self.exits_in_memory.items():
            if counter == 0:
                del(self.exits_in_memory[exit_id])
            else:
                counter-=1

        # Update best option
        availible_exits = self.exits_in_sight(people, exits=exits, obstacles=obstacles, fires=fires)
        if not self.best_option and availible_exits:
            self.best_option = availible_exits[0]

        best_option_distance = self.distance([[self.x, self.y], [self.best_option.x, self.best_option.y]]) if self.best_option else None
        for exit in availible_exits:
            exit_distance = self.distance([[self.x, self.y], [exit.x, exit.y]])
            if exit_distance < best_option_distance:
                self.best_option = exit
                best_option_distance = exit_distance

        # execute behaviour
        if self.best_option in availible_exits:
            if not isinstance(self._behaviour, MoveToExit):
                self._behaviour = MoveToExit(best_option=self.best_option)
            else:
                self._behaviour.best_option = self.best_option

            self._behaviour.go(
                exits=availible_exits,
                aptitude=aptitude,
                person=self,
                current_tile=None,
                width=width,
                height=height
                )

        # else:
        #     if not isinstance(self._behaviour, BestOption):
        #         self._behaviour = BestOption(best_option=self.best_option)
        #     else:
        #         self._behaviour.best_option = self.best_option

        #     self._behaviour.go(
        #         exits=availible_exits,
        #         aptitude=aptitude,
        #         person=self,
        #         current_tile=current_tile,
        #         width=width,
        #         height=height,
        #         previous_tile=previous_tile,
        #         traversed_tiles=traversed_tiles,
        #         )
        else:
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
        
        #is this the right place to update previous position?
        self.previous_x = temp_x
        self.previous_y = temp_y
