from pygame import Rect
from typing import Tuple

class Exit(Rect):
    def __init__(self, x: int, y: int, id: int) -> None:
        self.color: Tuple[int, int, int] = (255, 223, 0)
        self.height: int = 20
        self.width: int = 20
        self.x: int = x
        self.y: int = y
        self.id: int = id