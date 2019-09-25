from abc import ABC, abstractmethod

class Obesrver(ABC):
    @abstractmethod
    def notify(self, health: int):
        pass