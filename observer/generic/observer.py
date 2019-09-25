from abc import ABC, abstractmethod
from typing import TypeVar, Generic

S = TypeVar("S")

class Observer(Generic[S]):
    @abstractmethod
    def notify(self, state: S):
        pass