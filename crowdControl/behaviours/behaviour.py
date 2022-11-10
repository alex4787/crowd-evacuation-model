from __future__ import annotations
from abc import ABC, abstractmethod

class Behaviour(ABC):
    @abstractmethod
    def go(self, person, exits, fires, aptitude):
        pass