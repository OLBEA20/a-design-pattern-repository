from generic.obersvable import Observable
from generic.observer import Observer

class GraphicalHealthStatus(Observer[int]):
    def __init__(self, initial_health: int):
        self.inital_health = initial_health

    def notify(self, health: int) -> None:
        print(f"[{health * 'x'}{(self.inital_health - health) * ' '}]")
        