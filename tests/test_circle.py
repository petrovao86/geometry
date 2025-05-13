import math

import pytest

from geometry import Circle


@pytest.mark.parametrize(
    "radius, is_valid",
    [
        (-1, False),
        (0, False),
        (1, True),
    ]
)
def test_circle_validation(radius: float, is_valid: bool):
    if is_valid:
        Circle(radius)
    else:
        with pytest.raises(Exception):
            Circle(radius)


@pytest.mark.parametrize(
    "radius, square",
    [
        (1, math.pi),
        (2, 4 * math.pi),
        (3, 9 * math.pi),
    ]
)
def test_circle_square(radius: float, square: float):
    assert Circle(radius).square() == square
