from abc import ABC, abstractmethod

from push.observer import Observer


class Observable(ABC):
    @abstractmethod
    def subscribe(self, subscriber: Observer):
        pass
