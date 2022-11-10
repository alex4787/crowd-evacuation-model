from __future__ import annotations
import numpy as np
import math
from behaviours.behaviour import Behaviour
from behaviours.move_to_exit import MoveToExit
from behaviours.dont_move import DontMove
from pygame import Rect

class People(Rect):
    def __init__(self, x, y, id, behaviour: Behaviour):
        self.color = (0, 255, 0)
        self.height = 5
        self.width = 5
        self.x = x
        self.y = y
        self.id = id
        self._behaviour = behaviour

    @property
    def behaviour(self) -> Behaviour:
        return self._behaviour

    @behaviour.setter
    def behaviour(self, behaviour: Behaviour) -> None:
        self._behaviour = behaviour

    def tile_has_changed(self, previous_x, previous_y):
        return self.x//100 != previous_x//100 or self.y//100 != previous_y//100

    def exits_in_sight(self, people, exits):
        exits_in_sight = exits
        for exit in exits:
            line = ((self.x, self.y), (exit.x, exit.y))
            for other in people:
                if other.clipline(line):
                    exits_in_sight.remove(exit)
                    break
        return exits_in_sight

    def move(self, people, exits, fires, aptitude):
        availible_exits = self.exits_in_sight(people, exits=exits)
        if availible_exits:
            self._behaviour = MoveToExit()
            self._behaviour.go(exits=exits, fires=fires, aptitude=aptitude, person=self)
        else:
            self._behaviour = DontMove()
            self._behaviour.go(exits=exits, fires=fires, aptitude=aptitude, person=self)