__author__ = 'Python Object Oriented Programming - Modules'


from DistanceFormula import CoordinateGeometry

if __name__ == "__main__":
    D = CoordinateGeometry(5, 6, 7, 8)
    D.distance_calculation()
    print D.distance

    D1 = CoordinateGeometry(50, 60, 70, 80)
    D1.distance_calculation()
    print D1.distance
