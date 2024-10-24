# Задача "Рекурсивное умножение цифр":

# Напишите функцию get_multiplied_digits и параметр number в ней.
def get_multiplied_digits(number):
    str_number = str(number) # Создайте переменную str_number и запишите строковое представление(str) числа number в неё.

    # Основной задачей будет отделение первой цифры в числе:
    first = int(str_number[0]) # создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).

    # 4 пункт можно выполнить только тогда, когда длина str_number больше 1,
    # т.к. в противном случае не получиться взять срез str_number[1:].
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:])) # Возвращайте значение first * get_multiplied_digits(int(str_number[1:])).
    else:
       # Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
       return first

result = get_multiplied_digits(40203)
print(result)

# Стек вызовов будет выглядеть следующим образом:
#
# get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3