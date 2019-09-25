from abc import ABC, abstractmethod

from pull.observer import Observer


class Observable(ABC):
    @abstractmethod
    def subscribe(self, subscriber: Observer):
        pass

    @abstractmethod
    def get_health(eslf) -> int:
        pass
