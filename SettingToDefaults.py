__author__ = 'Python Object Oriented Programming - Setting Constructor Values'


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.Sum = 0

    def sum_of_digits(self):
        self.Sum = self.x + self.y

if __name__ == "__main__":
    p = Point()
    p.sum_of_digits()
    print p.Sum

    p1 = Point(10, 20)
    p1.sum_of_digits()
    print p1.Sum
