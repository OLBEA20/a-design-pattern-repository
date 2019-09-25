from push.observer import Observer
from push.obersvable import Observable

class Player(Observable):
    def __init__(self, health: int):
        self._health = health
        self.observers = []
    
    def take_damage(self, damage: int) -> None:
        self.health = self.health - damage
    
    def recover(self, health: int) -> None:
        self.health = self.health + health
    
    def subscribe(self, subscriber: Observer) -> None:
        self.observers.append(subscriber)
    
    @property
    def health(self) -> int:
        return self._health
    
    @health.setter
    def health(self, new_health: int) -> None:
        self._health = new_health
        self.notify_observers()

    
    def notify_observers(self):
        for observer in self.observers:
            observer.notify()

