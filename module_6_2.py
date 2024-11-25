# Задача "Изменять нельзя получать":

class Vehicle:
    # Атрибут класса:
    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white'] # список допустимых цветов для окрашивания.

    # Атрибуты объекта Vehicle:
    def __init__(self, owner: str, __model: str, __color: str, __engine_power: int):
        self.owner = owner # - владелец транспорта. (владелец может меняться)
        self.model = __model # - модель (марка) транспорта. (мы не можем менять название модели)
        self.engine_power = __engine_power # - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.color = __color # - название цвета. (мы не можем менять цвет автомобиля своими руками)

    # Каждый объект Vehicle должен содержать следующий методы:
    def get_model(self):
        return f'Модель: {self.model}' # возвращает строку: "Модель: <название модели транспорта>"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.engine_power}" # - возвращает строку: "Мощность двигателя: <мощность>"

    def get_color(self):
        return f'Цвет: {self.color}' # - возвращает строку: "Цвет: <цвет транспорта>"

    # Метод print_info - распечатывает результаты методов (в том же порядке):
    # get_model,
    # get_horsepower,
    # get_color; а так же владельца в конце в формате "Владелец: <имя>"
    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), f'Владелец: {self.owner}', sep = '\n')

    # Метод set_color - принимает аргумент new_color(str)
    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS: # если он есть в списке __COLOR_VARIANTS, то
            self.color = new_color                   # меняет цвет __color на new_color,
        else:                      # в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
            print(f'Нельзя сменить цвет на {new_color}')


# Класс Sedan наследуется от класса Vehicle
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 # Вместимость: в седан может поместиться только 5 пассажиров.


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()