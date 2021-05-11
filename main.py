from math import sin, cos, sqrt, atan, acos, radians


class Point:
    def __init__(self, x=None, y=None, z=None):
        self.error = False    #маркер ошибки при получении данных
        self.write = True     #необходимо вывести координаты точки или нет
        if x is None:
            self.flag = input("Введите в какой системе будут представлены координаты Декартовы(d)/Сферические(s): ")
            if self.flag.lower() == "d":
                self.x = int(input("Введите координату X: "))
                self.y = int(input("Введите координату Y: "))
                self.z = int(input("Введите координату Z: "))
                self.flag = "cartesian"
            elif self.flag.lower() == "s":
                self.radius = int(input("Введите расстояние до начала координат r: "))
                self.polar = radians(int(input("Введите полярный угол θ: ")))
                self.azimuth = radians(int(input("Введите азимутальный угол φ: ")))
                self.flag = "spherical"
            else:
                print("Неправильно введена система, перезапустите программу!")
                self.error = True
        else:
            self.x = x
            self.y = y
            self.z = z
            self.flag = "cartesian"
            self.write = False
        if not self.error:
            self.converse(self.flag)
            if self.write:
                print(
                    f"Заданная точка в системах координат: Декартова: {(self.x, self.y, self.z)} Сферическая: {(self.radius, self.polar, self.azimuth)}")

    def converse(self, f):
        if f == "cartesian":
            self.radius = sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
            if self.z != 0:
                self.polar = atan(sqrt(self.x ** 2 + self.y ** 2) / self.z)
            else:
                self.polar = acos(0)
            self.azimuth = atan(self.y / self.x)
        elif f == "spherical":
            self.x = self.radius * sin(self.polar) * cos(self.azimuth)
            self.y = self.radius * sin(self.polar) * sin(self.azimuth)
            self.z = self.radius * cos(self.polar)


class Distance:
    def __init__(self, point_1: Point, point_2: Point):
        self.__distance = sqrt(
            (point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2 + (point_1.z - point_2.z) ** 2)

    def distance(self):
        print(f"Расстояние между точками с введенными координатами равно {self.__distance}")


class Slant:
    def __init__(self, point_1: Point, point_2: Point):
        self.__x = point_2.x - point_1.x
        self.__y = point_2.y - point_1.y
        self.__z = point_2.z - point_1.z
        self.slant_point = Point(self.__x, self.__y, self.__z)
        self.angle = self.slant_point.polar


if __name__ == "__main__":
    point_1 = Point()
    state = input("Вы хотите ввести координату второй точки? (y/n): ")
    if state == "y":
        point_2 = Point()
        state = input("Вы хотите посчитать расстояние между точками? (y/n): ")
        if state == "y":
            dist = Distance(point_1, point_2)
            dist.distance()
        state = input("Вы хотите посчитать угол наклона отрезка Point_1-Point_2? (y/n): ")
        if state == "y":
            slant = Slant(point_1, point_2)
            print("Угол наклона заданного отрезка равен: ", slant.angle)
    print("Программа завершена. Спасибо!")
