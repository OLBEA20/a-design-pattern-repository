from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from generic.observer import Observer

S = TypeVar("S")

class Observable(Generic[S]):
    def __init__(self):
        self.observers = []

    def subscribe(self, subscriber: Observer[S]):
        self.observers.append(subscriber)

    def notify_observers(self, state: S) -> None:
        for observer in self.observers:
            observer.notify(state)