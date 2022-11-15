from density_grid.tile import Tile
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_objects.people import People

class Tiles():
    def __init__(self, previous, current) -> None:
        self.previous: Tile = previous
        self.current: Tile = current

class Maps():
    def __init__(self) -> None:
        self.person_to_tiles: dict[People, Tiles] = {}
