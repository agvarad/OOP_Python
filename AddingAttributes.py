__author__ = 'Object Oriented programming - 1'


class Point:
    """
    Sample Python Program to demonstrate a simple class with attributes
    """
    def __init__(self):
        pass

if __name__ == "__main__":
    p1 = Point()
    p2 = Point()

    p1.x = 3
    p1.y = 2
    p2.x = 4
    p2.y = 3

    print "Point 1: (" + str(p1.x) + "," + str(p1.y) + ")"
    print "Point 2: (" + str(p2.x) + "," + str(p2.y) + ")"
