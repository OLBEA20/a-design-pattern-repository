from generic.observer import Observer
from generic.obersvable import Observable

class Player(Observable[int]):
    def __init__(self, health: int):
        super().__init__()
        self._health = health
    
    def take_damage(self, damage: int) -> None:
        self.health = self.health - damage
    
    def recover(self, health: int) -> None:
        self.health = self.health + health
    
    @property
    def health(self) -> int:
        return self._health
    
    @health.setter
    def health(self, new_health: int) -> None:
        self._health = new_health
        self.notify_observers(new_health)
   