from generic.obersvable import Observable
from generic.observer import Observer


class HealthAlert(Observer[int]):
    def __init__(self, threshold: int):
        self.threshold = threshold

    def notify(self, health: int) -> None:
        if health < 0:
            print("PLAYER IS DEAD!!!")
        elif health < self.threshold:
            print(f"HEALTH LOW!!!")

