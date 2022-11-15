from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_objects import People, Exit, Fire
    from density_grid import Tile
from typing import List
from abc import ABC, abstractmethod

class Behaviour(ABC):
    @abstractmethod
    def go(
        self,
        person: People,
        fires: List[Fire],
        aptitude: int,
        width: int,
        height: int,
        current_tile: Tile,
        exits: List[Exit] = None,
        previous_tile: Tile = None,
        ) -> None:
        pass

    def out_of_bounds(self, new_x: int, new_y: int, width: int, height: int) -> bool:
        if (new_x < 0 or new_x >= width or new_y < 0 or new_y >= height):
            return True
        return False

