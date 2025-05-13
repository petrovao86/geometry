import math

import pytest

from geometry import Triangle


@pytest.mark.parametrize(
    "a, b, c, is_valid",
    [
        (0, 0, 0, False),
        (0, 0, 1, False),
        (0, 1, 1, False),
        (1, 1, 1, True),
        (1, 1, 2, True),
        (1, 1, 3, False),
        (-1, 1, 2, False),
        (1, -1, 2, False),
        (1, 1, -2, False),
        (-1, -1, -2, False),
    ]
)
def test_triangle_validation(a: float, b: float, c: float, is_valid: bool):
    if is_valid:
        Triangle(a, b, c)
    else:
        with pytest.raises(Exception):
            Triangle(a, b, c)


@pytest.mark.parametrize(
    "a, b, c, square",
    [
        (0, 0, 0, 0),
        (0, 1, 1, 0),
        (1, 1, 1, math.sqrt(3)/4),
        (1, 1, 2, 0),
        (3, 4, 5, 6),
    ]
)
def test_triangle_square(a: float, b: float, c: float, square: float):
    assert Triangle(a, b, c).square() == square


@pytest.mark.parametrize(
    "a, b, c, is_square",
    [
        (1, 1, 1, False),
        (1, 1, 2, False),
        (3, 4, 5, True),
    ]
)
def test_triangle_square(a: float, b: float, c: float, is_square: bool):
    assert Triangle(a, b, c).is_sqare() is is_square
