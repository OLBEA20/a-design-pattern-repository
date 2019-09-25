from pull.obersvable import Observable
from pull.observer import Observer

class GraphicalHealthStatus(Observer):
    def __init__(self, observable: Observable):
        self.inital_health = observable.get_health()
        self.observable = observable

    def notify(self) -> None:
        print(f"[{self.observable.get_health() * 'x'}{(self.inital_health - self.observable.get_health()) * ' '}]")