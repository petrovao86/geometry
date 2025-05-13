from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def square(self) -> float:
        raise NotImplementedError
