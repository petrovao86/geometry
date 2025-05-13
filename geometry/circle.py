import math

from .shape import Shape


class Circle(Shape):
    def __init__(self, r: float):
        if r <= 0:
            raise ValueError("circle radius must be gt 0")
        self.r = r

    def square(self) -> float:
        return math.pi * self.r * self.r
