from pull.obersvable import Observable
from pull.observer import Observer


class TextHealthStatus(Observer):
    def __init__(self, observable: Observable):
        self.observable = observable

    def notify(self) -> None:
        print(f"Health: {self.observable.get_health()}")
