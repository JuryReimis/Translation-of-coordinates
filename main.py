from math import sin, cos


class Point:
    def __init__(self, x, y, z, flag):         #flag показывает, в какой системе дана точка
        if flag == "cartesian":
            self.x = x
            self.y = y
            self.z = z
        elif flag == "spherical":
            self.radius = x
            self.polar = y
            self.azimuth = z
        else:
            print("Система координат не распознана\nПроверьте правильность ввода")

    def converse(self):


