__author__ = 'Python Object Oriented programming'


import math


class CoordinateGeometry:
    """
    Calculate the distance between 2 points in 2-dimensional space
    """
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        """
        :param x1: integer
        :param y1: integer
        :param x2: integer
        :param y2: integer
        """
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.distance = 0

    def distance_calculation(self):
        """
        :return distance: integer
        """
        self.distance = math.sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)

if __name__ == "__main__":
    p = CoordinateGeometry(10, 20, 30, 40)
    p.distance_calculation()
    print p.distance
