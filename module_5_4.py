# Задача "История строительства":

class House:
    houses_history = [] # создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
    def __new__(cls, *args):
        cls.houses_history.append(args[0]) # Название объекта добавлялось в список cls.houses_history
        return super().__new__(cls)

    def __init__(self, name: str, numbers_of_floors: int):
        self.name = name # имя
        self.numbers_of_floors = numbers_of_floors # кол-во этажей

    def __del__(self): # Также переопределите метод __del__(self)
        print(f'{self.name} снесён, но он останется в истории')

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
        elif isinstance(value, House):
            self.numbers_of_floors += value.numbers_of_floors
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


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)