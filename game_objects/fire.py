from pygame import Rect
from typing import Tuple

class Fire(Rect):
    def __init__(self, x: int, y: int) -> None:
        self.color: Tuple[int, int, int] = (226, 38, 84)
        self.width: int = 3
        self.height: int = 3
        self.x: int = x
        self.y: int = y

    def update(self) -> None:
        self.width += 2
        self.height += 2
        self.x -= 1
        self.y -=1