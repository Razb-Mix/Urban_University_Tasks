# Задание "Они все так похожи":
import math

class Figure:
    sides_count = 0

    # Каждый объект класса Figure должен обладать следующими атрибутами:
    def __init__(self, color: tuple, sides, filled = False):
        # Атрибуты(инкапсулированные):
        self.__color = list(color) # __color(список цветов в формате RGB)
        self.__sides = sides # __sides (список сторон (целые числа)),

        # Атрибуты(публичные): filled(закрашенный, bool)
        self.filled = filled

    def get_color(self):
        # возвращает список RGB цветов.
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int):
        # принимает параметры r, g, b, затем проверяет корректность переданных значений перед установкой нового цвета.
        # Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            # print(f'Код RGB: {r}, {g}, {b} неверен.')
            return False

    def set_color(self, r: int, g: int, b: int):
        # принимает параметры r, g, b - числа
        # предварительно проверив их на корректность.
        if self.__is_valid_color(r, g, b):
            # и изменяет атрибут __color на соответствующие значения,
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b
            # Если введены некорректные данные, то цвет остаётся прежним.

    def __set_valid_sides(self, *sides):
        # принимает неограниченное кол-во сторон,
        list_of_sides = sides

        # возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим,
        if self.sides_count == len(list_of_sides) and min(list_of_sides) > 0:
            for element in list_of_sides:
                if not isinstance(element, int): # проверяем все ли элементы в кортеже целые числа
                    return False # False - во всех остальных случаях.
                else:
                    return True
        else:
            return False # False - во всех остальных случаях.

    def get_sides(self):
        # вернуть значения атрибута __sides.
        return self.__sides

    def __len__(self):
        if self.sides_count == 1:
            return self.__sides[0] # вычислить периметр круга
        elif self.sides_count == 3:
            return sum(self.__sides) # вычислить периметр треугольника
        elif self.sides_count == 12:
            return self.sides_count * self.__sides # вычислить периметр куба

    def set_sides(self, *new_sides):
        # должен принимать новые стороны
        if len(new_sides) == self.sides_count:
            # если их количество не равно sides_count, то не изменять, в противном случае - менять.
            self.__sides = list(new_sides)


class Circle(Figure):
    # Атрибуты класса Circle:
    sides_count = 1

    # Каждый объект класса Circle должен обладать следующими атрибутами и методами:
    def __init__(self, color: tuple, *sides, filled = False):
        # Проверка на количество переданных сторон, если сторон не ровно sides_count, то
        # создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
        if len(sides) != self.sides_count:
            self.__sides = 1
        elif len(sides) == 1:
            self.__sides = sides[0]

        # Все атрибуты и методы класса Figure
        super().__init__(color, self.__sides, filled = False)

        # Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
        self.__radius = self.__sides / (math.pi * 2)

    def get_square(self):
        # Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
        return math.pi * pow(self.__radius, 2)


class Triangle(Figure):
    # Атрибуты класса Triangle:
    sides_count = 3

    # Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
    def __init__(self, color: tuple, *sides, filled = False):
        # Проверка на количество переданных сторон, если сторон не ровно sides_count, то
        # создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        elif len(sides) == 3:
            self.__sides = list(*sides)
        # Все атрибуты и методы класса Figure
        super().__init__(color, self.__sides, filled = False)

    def get_square(self):
        # возвращает площадь треугольника. (можно рассчитать по формуле Герона)
        p = sum(self.__sides) / 2 # полупериметр
        return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))


class Cube(Figure):
    # Атрибуты класса Cube:
    sides_count = 12

    # Каждый объект класса Cube должен обладать следующими атрибутами и методами:
    def __init__(self, color: tuple, *sides, filled = False):
        # Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
        if len(sides) > 1:
            self.__sides = [1] * self.sides_count
        elif len(sides) == 1:
            self.__sides = [*sides] * self.sides_count
        # Все атрибуты и методы класса Figure.
        super().__init__(color, self.__sides, filled=False)

    def get_volume(self):
        # Метод get_volume, возвращает объём куба.
        return pow(self.__sides[0], 3)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
