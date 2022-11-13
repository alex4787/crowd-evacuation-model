from __future__ import annotations
from typing import Tuple, List
from pygame import Rect

from behaviours import Behaviour, MoveToExit, DontMove
from game_objects import Exit, Fire

class People(Rect):
    def __init__(self, x: int, y: int, id: int, behaviour: Behaviour) -> None:
        self.color: Tuple[int, int, int] = (0, 255, 0)
        self.height: int = 5
        self.width: int = 5
        self.x: int = x
        self.y: int = y
        self.id: int = id
        self._behaviour: Behaviour = behaviour

    @property
    def behaviour(self) -> Behaviour:
        return self._behaviour

    @behaviour.setter
    def behaviour(self, behaviour: Behaviour) -> None:
        self._behaviour = behaviour

    def tile_has_changed(self, previous_x: int, previous_y: int) -> bool:
        return self.x//100 != previous_x//100 or self.y//100 != previous_y//100

    def is_valid_line_of_sight(self, line: Tuple[Tuple[int, int], Tuple[int, int]], people: List[People]) -> bool:
        is_valid = True
        for other in people: 
            if other.clipline(line): # can this clip the actor of interest? ie can you clip yourself ?
                is_valid = False
                break
        return is_valid

    def exits_in_sight(self, people: List[People], exits: List[Exit]) -> List[Exit]:
        exits_in_sight = []
        for exit in exits:
            line = ((self.x, self.y), (exit.x, exit.y))
            if self.is_valid_line_of_sight(line, people):
                exits_in_sight.append(exit)                 # Something funny is still going on here.
        return exits_in_sight

    def move(self, people: List[People], exits: List[Exit], fires: List[Fire], aptitude: float) -> None:
        availible_exits = self.exits_in_sight(people, exits=exits)
        if availible_exits:
            if self._behaviour != MoveToExit:
                self._behaviour = MoveToExit()
            self._behaviour.go(exits=availible_exits, fires=fires, aptitude=aptitude, person=self)
        else:
            if self._behaviour != DontMove:
                self._behaviour = DontMove()
            self._behaviour.go(exits=availible_exits, fires=fires, aptitude=aptitude, person=self)