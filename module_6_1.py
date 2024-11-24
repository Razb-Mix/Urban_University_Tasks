# Задача "Съедобное, несъедобное":

class Animal:
    def __init__(self, name: str):
        self.alive = True # Для класса Animal атрибуты alive = True(живой)
        self.fed = False # False(накормленный)
        self.name = name # индивидуальное название каждого животного.

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
            return self.fed
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
            return self.alive

class Mammal(Animal):
    pass

class Predator(Animal):
    pass


class Plant:
    def __init__(self, name: str):
        self.edible = False # Для класса Plant атрибут edible = False(съедобность),
        self.name = name # name - индивидуальное название каждого растения

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name: str):
        super().__init__(name)
        self.edible = True # У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)
