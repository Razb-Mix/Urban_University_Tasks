# Задача "Developer - не только разработчик":

class House:
    def __init__(self, name: str, numbers_of_floors: int):
        self.name = name # имя
        self.numbers_of_floors = numbers_of_floors # кол-во этажей

    def go_to(self, new_floor: int):
            if 1 <= new_floor <= self.numbers_of_floors:
                for i in range(1, new_floor + 1):
                    print(i)
            else:
                print("Такого этажа не существует.")

sweet_home = House("Ломоносов", 4)
sweet_home.go_to(2)

print()
print("Проверка из условия задачи")
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)