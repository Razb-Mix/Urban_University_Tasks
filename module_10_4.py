# Задача "Потоки гостей в кафе":
# Необходимо имитировать ситуацию с посещением гостями кафе.
import threading
import queue
from random import randint
from time import sleep

# Создайте 3 класса: Table, Guest и Cafe.
# Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
class Guest(threading.Thread):
    # Должен наследоваться от класса Thread (быть потоком).
    def __init__(self, name: str):
        threading.Thread.__init__(self)
        self.name = name # - имя гостя.

    def run(self):
        # где происходит ожидание случайным образом от 3 до 10 секунд.
        sleep(randint(3, 10))

# Table - стол, хранит информацию о находящемся за ним гостем (Guest).
class Table:
    def __init__(self, number: int, guest: Guest = None):
        self.number = number # - номер стола
        self.guest = guest # - гость, который сидит за этим столом (по умолчанию None)

# Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival)
# и их обслуживания (discuss_guests).
class Cafe:
    def __init__(self, *tables):
        self.tables = tables # tables - столы в этом кафе (любая коллекция).
        self.queue = queue.Queue() # - очередь (объект класса Queue)
        self.qty_of_free_tables:int = len(self.tables) # количество не занятых столов

    # Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
    def guest_arrival(self, *guests):
        for guest in guests:
            if self.qty_of_free_tables:
                for table in self.tables:
                    if table.guest is None:
                        # если есть свободный стол,
                        table.guest = guest # то сажать гостя за стол (назначать столу guest)
                        guest.start() # запускать поток гостя
                        print(f"{guest.name} сел(-а) за стол номер {table.number}") # выводить на экран строку.
                        self.qty_of_free_tables -= 1 # убавляем кол-во свободных столов
                        break # Гостя посадили, задача выполнена, цикл прервать
            else:
                # Если же свободных столов для посадки не осталось,
                self.queue.put(guest) # то помещать гостя в очередь queue
                print(f"{guest.name} в очереди") # выводить сообщение.

    def discuss_guests(self):
        # Этот метод имитирует процесс обслуживания гостей.

        # Обслуживание должно происходить пока очередь не пустая (метод empty)
        # или хотя бы один стол занят.
        while not self.queue.empty() or self.qty_of_free_tables != len(self.tables):
            for table in self.tables:
                # Если за столом есть гость(поток)
                # и гость(поток) закончил приём пищи (поток завершил работу - метод is_alive),
                if not table.guest is None and not table.guest.is_alive():
                    # то вывести строки
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None # текущий стол освобождается
                    self.qty_of_free_tables += 1 # увеличить кол-во свободных столов

                # Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None),
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get() # то текущему столу присваивается гость взятый из очереди.
                    self.qty_of_free_tables -= 1  # убавляем кол-во свободных столов
                    # Далее выводится строка
                    print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    table.guest.start() # Далее запустить поток этого гостя (start)

# # Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()