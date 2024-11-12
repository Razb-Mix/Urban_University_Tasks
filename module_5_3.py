# Задача "Нужно больше этажей":

class House:
    def __init__(self, name: str, numbers_of_floors: int):
        self.name = name # имя
        self.numbers_of_floors = numbers_of_floors # кол-во этажей

    def __len__(self):
        return self.numbers_of_floors # должен возвращать кол-во этажей здания

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numbers_of_floors}' # должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

    def __eq__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors == other.numbers_of_floors # возвращать True, если количество этажей одинаковое у self и у other.
        else:
            return f'Ошибка! "{other}" - неверный тип данных.'

    def __lt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors < other.numbers_of_floors
        else:
            return f'Ошибка! "{other}" - неверный тип данных.'

    def __le__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors <= other.numbers_of_floors
        else:
            return f'Ошибка! "{other}" - неверный тип данных.'

    def __gt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors > other.numbers_of_floors
        else:
            return f'Ошибка! "{other}" - неверный тип данных.'

    def __ge__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors >= other.numbers_of_floors
        else:
            return f'Ошибка! "{other}" - неверный тип данных.'

    def __ne__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floors != other.numbers_of_floors
        else:
            return f'Ошибка! "{other}" - неверный тип данных.'

    def __add__(self, value):
        if isinstance(value, int):
            self.numbers_of_floors += value
            return self
        else:
            return f'Ошибка! "{value}" - неверный тип данных.'

    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)
        else:
            return f'Ошибка! "{value}" - неверный тип данных.'

    def __iadd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)
        else:
            return f'Ошибка! "{value}" - неверный тип данных.'

    def __sub__(self, value):
        if isinstance(value, int):
            #x, y = self.numbers_of_floors, value
            #return x - y
            return self.numbers_of_floors - value
        else:
            return f'Ошибка! "{value}" - неверный тип данных.'


    def go_to(self, new_floor: int):
            if 1 <= new_floor <= self.numbers_of_floors:
                for i in range(1, new_floor + 1):
                    print(i)
            else:
                print("Такого этажа не существует.")

sweet_home = House("Ломоносов", 4)

print("Отладка:")
sweet_home = sweet_home + 30
print(sweet_home)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print()
print("Проверка из условия задачи:")
print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)

print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

sweet_home = sweet_home.__sub__(3)
print(sweet_home)