# Задача "Распаковка":
#
# 1.Функция с параметрами по умолчанию:
#
# Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями
# по умолчанию (например сейчас это: 1, 'строка', True).
def print_params(a = 1, b = "строка", c = True):
    print(a, b, c) # Функция должна выводить эти параметры.

# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print("1.Функция с параметрами по умолчанию:")
print_params()
print_params(58, "How do you do?", False)
print_params("egwseg", 5, 5)
print_params(1, 6)

# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b = 25) # Работает!
print_params(c = [1, 2, 3]) # Работает!


# 2.Распаковка параметров:
# добавил команд print для разделения вывода результатов в консоли
print()
print()
print('2.Распаковка параметров:')
# Создайте список values_list с тремя элементами разных типов.
value_list = ["I do wanna feel something you call real...", 254, False]

# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
values_dict = {'a' : 587, "b" : "sega mega drive", "c" : True}

# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(*value_list)
print_params(**values_dict)


# 3.Распаковка + отдельные параметры:
# добавил команд print для разделения вывода результатов в консоли
print()
print()
print("3.Распаковка + отдельные параметры:")
# Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = ["High", 12432.288]
# Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42) # Работает!