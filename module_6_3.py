# Задача "Ошибка эволюции":
import random

# Animal - класс описывающий животных
class Animal:
    # Класс обладает следующими атрибутами:
    live = True
    sound = None # - звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0 # - степень опасности существа

    # Объект этого класса обладает следующими атрибутами:
    def __init__(self, speed: int):
        self.cords = _cords = [0, 0, 0] # - координаты в пространстве.
        self.speed = speed # - скорость передвижения существа (определяется при создании объекта)

    # И методами:
    def move(self, x: int, y: int, z: int):
        if z < 0: # Если при попытке изменения координаты z в _cords значение будет меньше 0,
            print("It's too deep, i can't dive :()") # то выводить сообщение,
            return # при этом изменения не вносятся.
        else:
            #  который должен менять соответствующие координаты в _cords на dx, dy и dz в том же порядке, где множителем будет являться speed.

            # Решение в лоб. Просто, но работает.
            # self.cords[0] = x * self.speed
            # self.cords[1] = y * self.speed
            # self.cords[2] = z * self.speed

            # Решение через цикл for. Красиво, но не понятно есть ли в чём то выйгрыш, так как всё равно три строки.
            params = [x, y, z]
            for i in range(len(self.cords)):
                self.cords[i] = params[i] * self.speed

    def get_cords(self):
        # который выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
        print(f'X: {self.cords[0]} Y: {self.cords[1]} Z: {self.cords[2]}')

    def attack(self):
        # который выводит,
        if self._DEGREE_OF_DANGER < 5:
            # если степень опасности меньше 5:
            print("Sorry, i'm peaceful :)")
        else:
            # если равно или больше:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        # выводит строку со звуком sound.
        print(self.sound)


# Bird - класс описывающий птиц. Наследуется от Animal.
class Bird(Animal):
    # Должен обладать атрибутом:
    beak = True # - наличие клюва

    # И методом:
    def lay_eggs(self):
        # выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')


# AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal.
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    # Должен обладать методом:
    def dive_in(self, z):
        # где dz изменение координаты z в _cords.
        # Этот метод должен всегда уменьшать координату z в _coords.
        # Чтобы сделать dz положительным, берите его значение по модулю (функция abs).
        # Скорость движения при нырянии должна уменьшаться в 2 раза, в отличии от обычного движения. (speed / 2)
        self.cords[2] -= abs(int((self.speed / 2)) * z)


# PoisonousAnimal - класс описывающий ядовитых животных. Наследуется от Animal.
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8.
    def __init__(self, speed: int):
        super().__init__(speed)

# Duckbill - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal.
class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def __init__(self, speed: int):
        super().__init__(speed)
        # Объект этого класса должен обладать одним дополнительным атрибутом:
        self.sound = "Click-click-click" # - звук, который издаёт утконос


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()