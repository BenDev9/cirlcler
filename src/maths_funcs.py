import math


def sin(degs: float):
    """A function wrapper for the `math.sin()` function that converts from degress to radians"""
    return math.sin(math.radians(degs))


def cos(degs: float):
    """A function wrapper for the `math.cos()` function that converts from degress to radians"""
    return math.cos(math.radians(degs))


def get_point(degs: float, rad: float):
    """Calculates the coordinates of a point on a circle given it's radius and the angle"""
    return (int(sin(degs) * rad), int(cos(degs) * rad))
