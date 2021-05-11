from math import sin, cos, sqrt, atan


class Point:
    def __init__(self, x, y, z, flag):  # flag показывает, в какой системе дана точка
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
            self.error = True
        if not self.error:
            self.converse(flag)

    def converse(self, flag):
        if flag == "cartesian":
            self.radius = sqrt(self.x**2+self.y**2+self.z**2)
            self.polar = atan(sqrt(self.x**2+self.y**2)/self.z)
            self.azimuth = atan(self.y/self.x)
        elif flag == "spherical":
            self.x = self.radius * sin(self.polar) * cos(self.azimuth)
            self.y = self.radius * sin(self.polar) * sin(self.azimuth)
            self.z = self.radius * cos(self.polar)
