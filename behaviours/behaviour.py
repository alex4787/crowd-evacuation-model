from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_objects import People, Exit, Fire
from typing import List, Tuple
from abc import ABC, abstractmethod

class Behaviour(ABC):
    @abstractmethod
    def go(self, person: People, exits: List[Exit], fires: List[Fire], aptitude: int) -> None:
        pass
