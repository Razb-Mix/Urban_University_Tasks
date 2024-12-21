# Задача "Потоковая запись в файлы":
# Импорты необходимых модулей и функций
from time import sleep
import datetime
import threading

# Объявление функции write_words
def wite_words(word_count: int, file_name: str):
    # где word_count - количество записываемых слов,
    # file_name - название файла, куда будут записываться слова.
    with open(file_name, 'w', encoding='utf-8') as file:
        for num_row in range(1, word_count + 1):
            file.write(f"Какое-то слово № {num_row}\n") # Функция должна вести запись слов в соответствующий файл
            sleep(0.1) # c прерыванием после записи каждого на 0.1 секунду.

    print(f"Завершилась запись в файл {file_name}") # В конце работы функции вывести строку

# Взятие текущего времени
time_of_start = datetime.datetime.now()

# Запуск функций с аргументами из задачи
# После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
wite_words(10, 'example1.txt') # 10, example1.txt
wite_words(30, 'example2.txt') # 30, example2.txt
wite_words(200, 'example3.txt') # 200, example3.txt
wite_words(100, 'example4.txt') # 100, example4.txt

# Взятие текущего времени
time_of_end = datetime.datetime.now()

# Вывод разницы начала и конца работы функций
print(f'Работа потоков {time_of_end - time_of_start}')

# После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
# Взятие текущего времени
time_of_start = datetime.datetime.now()

# Создание и запуск потоков с аргументами из задачи
thread_1 = threading.Thread(target=wite_words, args=(10, 'example5.txt')) # 10, example5.txt
thread_2 = threading.Thread(target=wite_words, args=(30, 'example6.txt')) # 30, example6.txt
thread_3 = threading.Thread(target=wite_words, args=(200, 'example7.txt')) # 200, example7.txt
thread_4 = threading.Thread(target=wite_words, args=(100, 'example8.txt')) # 100, example8.txt

# Запустите эти потоки методом start
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

# не забыв, сделать остановку основного потока при помощи join.
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

# Также измерьте время затраченное на выполнение функций и потоков.
# Взятие текущего времени
time_of_end = datetime.datetime.now()

# Вывод разницы начала и конца работы потоков
print(f'Работа потоков {time_of_end - time_of_start}')