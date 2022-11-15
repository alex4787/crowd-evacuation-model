from __future__ import annotations
from typing import Tuple, List
from pygame import Rect
from behaviours import Behaviour, MoveToExit, DontMove, MoveToDensity, MoveWithCrowd, FollowTheLeader
from game_objects import Exit, Fire
from density_grid import Tile
import math

class People(Rect):
    def __init__(self, x: int, y: int, id: int, behaviour: Behaviour) -> None:
        self.color: Tuple[int, int, int] = (0, 255, 0)
        self.height: int = 10
        self.width: int = 10
        self.x: int = x
        self.y: int = y
        self.previous_x: int = x 
        self.previous_y: int = y
        self.id: int = id
        self._behaviour: Behaviour = behaviour

    def __hash__(self):
        return self.id

    @property
    def behaviour(self) -> Behaviour:
        return self._behaviour

    @behaviour.setter
    def behaviour(self, behaviour: Behaviour) -> None:
        self._behaviour = behaviour

    def tile_has_changed(self) -> bool:
        return self.x//100 != self.previous_x//100 or self.y//100 != self.previous_y//100

    def is_me(self: People, other: People) -> bool:
        if self.id == other.id:
            return True
        return False

    def distance(self, seg):
        return math.sqrt((seg[0][0] - seg[1][0])**2 + (seg[0][1] - seg[1][1])**2)

    def is_other_in_the_way(self, other: People, line: Tuple[Tuple[int, int], Tuple[int, int]]) -> bool:
        seg = other.clipline(line)
        if seg == () or self.distance(seg) < (math.sqrt(2))*self.width/2:
            return False
        return True

    def is_valid_line_of_sight(self, line: Tuple[Tuple[int, int], Tuple[int, int]], people: List[People]) -> bool:
        is_valid = True
        for other in people: 
            if not self.is_me(other) and self.is_other_in_the_way(other, line):
                is_valid = False
                break
        return is_valid

    def exits_in_sight(self, people: List[People], exits: List[Exit]) -> List[Exit]:
        exits_in_sight = []
        for exit in exits:
            line = ((self.centerx, self.centery), (exit.centerx, exit.centery))
            if self.is_valid_line_of_sight(line, people):
                exits_in_sight.append(exit)  
        return exits_in_sight

    def move(
            self,
            people: List[People],
            exits: List[Exit],
            fires: List[Fire],
            aptitude: float,
            current_tile: Tile,
            previous_tile: Tile,
            width: int,
            height: int
            ) -> None:

        # temp vals for current position
        temp_x = self.x
        temp_y = self.y

        # Execute proper movement strategy
        availible_exits = self.exits_in_sight(people, exits=exits)
        if availible_exits:
            if not isinstance(self._behaviour, MoveToExit):
                self._behaviour = MoveToExit()

            self._behaviour.go(
                exits=availible_exits,
                fires=fires,
                aptitude=aptitude,
                person=self,
                current_tile=None,
                width=width,
                height=height
                )

        else:
            if not isinstance(self._behaviour, FollowTheLeader):
                self._behaviour = FollowTheLeader()

            self._behaviour.go(
                exits=availible_exits,
                fires=fires,
                aptitude=aptitude,
                person=self,
                current_tile=current_tile,
                width=width,
                height=height,
                previous_tile=previous_tile
                )
        
        #is this the right place to update previous position?
        self.previous_x = temp_x
        self.previous_y = temp_y