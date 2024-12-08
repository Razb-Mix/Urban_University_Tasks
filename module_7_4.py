# Домашнее задание по теме "Файлы в операционной системе" из Модуля 7. Работа с файлами и форматированный вывод.
import os
import time

def get_files_info(directory: str):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            filetime = os.path.getmtime(file)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(file)
            parent_dir = os.path.dirname(filepath)
            print(
                f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
                f'Родительская директория: {parent_dir}')

'---------------------------------------Исполняемый код----------------------------------------------------------------'
# Так как в разных операционных системах разная схема расположения папок, тестировать проще всего в папке
# проекта (directory = “.”)
directory: str = "."
get_files_info(directory)