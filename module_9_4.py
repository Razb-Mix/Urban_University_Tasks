# Задача "Функциональное разнообразие":

# Lambda-функция:
# Даны 2 строки:
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
# Здесь ? - место написания lambda-функции.
print(list(map(lambda x, y: x == y, first, second)))

"---------------------------------------------------------------------------------------------------------"

# Замыкание:
# Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
def get_advanced_writer(file_name: str):
    # Внутри этой функции, напишите ещё одну - write_everything(*data_set),
    # где *data_set - параметр принимающий неограниченное количество данных любого типа.
    def write_everything(*data_set):
        # Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
        with open(file_name, 'w', encoding= 'utf-8') as file:
            for line in data_set:
                file.write('%s\n' % str(line))

    # Функция get_advanced_writer возвращает функцию write_everything.
    return write_everything

# Данный код:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

"---------------------------------------------------------------------------------------------------------"

# Метод __call__:
from random import choice, random

# Создайте класс MysticBall
class MysticBall:
    def __init__(self, *words):
        # объекты которого обладают атрибутом words хранящий коллекцию строк.
        self.words = words

    def __call__(self):
        # который будет случайным образом выбирать слово из words и возвращать его.
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())