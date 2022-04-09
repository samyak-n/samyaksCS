import math
import utility


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):  # this is what equalizes objects
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
