from typing import Deque
from collections import deque
from density_grid.tile import Tile
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game_objects.people import People

class TileHistory():
    def __init__(self, previous, current) -> None:
        self.previous: Tile = previous
        self.current: Tile = current
        self.traversed_tiles: Deque[Tile] = deque(maxlen=4)

class PersonToTileHistoryMap():
    def __init__(self) -> None:
        self.person_to_tiles: dict[People, TileHistory] = {}
