# Задача "Магические здания":

class House:
    def __init__(self, name: str, numbers_of_floors: int):
        self.name = name # имя
        self.numbers_of_floors = numbers_of_floors # кол-во этажей

    def __len__(self):
        return self.numbers_of_floors # должен возвращать кол-во этажей здания

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numbers_of_floors}' # должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

    def go_to(self, new_floor: int):
            if 1 <= new_floor <= self.numbers_of_floors:
                for i in range(1, new_floor + 1):
                    print(i)
            else:
                print("Такого этажа не существует.")

sweet_home = House("Ломоносов", 4)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(sweet_home)
print(h1)
print(h2)

# __len__
print(len(sweet_home))
print(len(h1))
print(len(h2))