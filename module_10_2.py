# Цель: научиться создавать классы наследованные от класса Thread.
# Задача "За честь и отвагу!":
import threading
from time import sleep

# Пункты задачи:
# Создайте класс Knight с соответствующими описанию свойствами.
class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self) # наследованный от Thread
        self.name = name # - имя рыцаря. (str)
        self.power = power # - сила рыцаря. (int)

    def run(self):
        # рыцарь будет сражаться с врагами:
        # При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
        print(f"{self.name}, на нас напали!")

        # Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
        qty_of_enemies: int = 100
        qty_of_days: int = 0 # сохраняем в переменную кол-во дней боевых действий
        while qty_of_enemies:
            # В процессе сражения количество врагов уменьшается на power текущего рыцаря.
            qty_of_enemies -= self.power
            qty_of_days += 1
            sleep(1) # По прошествию 1 дня сражения (1 секунды)
            # выводится строка "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
            print(f"{self.name} сражается {qty_of_days} день(дня)..., осталось {qty_of_enemies} воинов.")

        # После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
        # Вывод строки об окончании сражения
        print(f"{self.name} одержал победу спустя {qty_of_days} дней(дня)!")


# Создайте и запустите 2 потока на основе класса Knight.
# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
sleep(0.1) # задержка перед запуском второго потока, чтобы выводы в консоли двух потоков не записывались в одну строку
second_knight.start()

# и остановка текущего
first_knight.join()
second_knight.join()

# Выведите на экран строку об окончании битв.
print('Все битвы закончились!')
