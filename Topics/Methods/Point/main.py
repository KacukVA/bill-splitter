import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, obj):
        return math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2)