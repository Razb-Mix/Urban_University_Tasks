# Домашнее задание по теме "Генераторные сборки":
# Задача:
# Дано 2 списка:

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Необходимо создать 2 генераторных сборки:

# 1. В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из списков
# first и second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.
# где s - строка из списка
first_result = (abs(len(s[0]) - len(s[1])) for s in list(zip(first, second)) if not len(s[0]) == len(s[1]))


# 2. В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк в
# одинаковых позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip.
# Используйте функции range и len.
# где i - индекс строки из списка first и second
if len(first) == len(second): second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))


# Пример выполнения кода:
print(list(first_result))
print(list(second_result))