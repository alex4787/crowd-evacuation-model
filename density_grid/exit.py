from density_grid.tile import Tile
from typing import Tuple

class Exit(Tile):
    def __init__(self, x: int, y: int, id: int) -> None:
        super().__init__(x, y)
        self.color: Tuple[int, int, int] = (255, 223, 0)
        self.id: int = id