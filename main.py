from math import sin, cos, sqrt, atan, radians


class Point:
    def __init__(self, x, y, z, flag=None):  # flag показывает, в какой системе дана точка
        self.error = False
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

    def converse(self, f):
        if f == "cartesian":
            self.radius = sqrt(self.x**2+self.y**2+self.z**2)
            self.polar = atan(sqrt(self.x**2+self.y**2)/self.z)
            self.azimuth = atan(self.y/self.x)
        elif f == "spherical":
            self.x = self.radius * sin(self.polar) * cos(self.azimuth)
            self.y = self.radius * sin(self.polar) * sin(self.azimuth)
            self.z = self.radius * cos(self.polar)


class Distance:
    def __init__(self, point_1: Point, point_2: Point):
        self.__distance = sqrt((point_1.x-point_2.x)**2+(point_1.y-point_2.y)**2+(point_1.z-point_2.z)**2)

    def distance(self):
        print(f"расстояние между точками с введенными координатами равно {self.__distance}")


class Slant:
    def __init__(self, point_1: Point, point_2: Point):
        self.__x = point_2.x - point_1.x
        self.__y = point_2.y - point_1.y
        self.__z = point_2.z - point_1.z
        self.point = Point(x=self.__x, y=self.__y, z=self.__z, flag="cartesian")
        self.angle = self.point.polar


if __name__ == "__main__":
    flag = input("Введите в какой системе будут представлены координаты Декартовы(d)/Сферические(s)")
    error = False
    if flag.lower() == "d":
        first = int(input("Введите координату X: "))
        second = int(input("Введите координату Y: "))
        third = int(input("Введите координату Z: "))
        flag = "cartesian"
    elif flag.lower() == "s":
        first = int(input("Введите расстояние до начала координат r: "))
        second = int(input("Введите полярный угол θ: "))
        third = int(input("Введите азимутальный угол φ: "))
        flag = "spherical"
    else:
        print("Неправильно введена система, перезапустите программу!")
        error = True
    if not error:
        point = Point(first, radians(second), radians(third), flag)
        print(f"Заданная точка в системах координат: Декартова: {(point.x, point.y, point.z)} Сферическая: {(point.radius, point.polar, point.azimuth)}")


