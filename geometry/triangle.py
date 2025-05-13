import math

from .shape import Shape


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("triangle sides must be gt 0")

        if a + b < c or a + c < b or b + c < a:
            raise ValueError("triangle inequality check failed")
        self.a = a
        self.b = b
        self.c = c

    def square(self) -> float:
        s = 0.5 * (self.a + self.b + self.c)
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_sqare(self) -> bool:
        g = max(self.a, self.b , self.c)
        return self.a * self.a + self.b * self.b + self.c * self.c - g*g == g*g


