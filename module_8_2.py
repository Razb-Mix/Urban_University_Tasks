# Цель: понять как работают исключения внутри функций и как обрабатываются эти исключения на практике при помощи try-except.
# Задача "План перехват":

def personal_sum(numbers: tuple): # Должна принимать коллекцию numbers.
    result: float = 0
    incorrect_data: int = 0

    for number in numbers:
        try:
            result += number # Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
        except TypeError:
            # Если же при переборе встречается данное типа отличного от числового, то обработать исключение TypeError
            incorrect_data += 1 # , увеличив счётчик incorrect_data на 1.
            print(f'Некорректный тип данных для подсчёта суммы - {number}')

    # В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел, incorrect_data - кол-во некорректных данных.
    return result, incorrect_data

def calculate_average(numbers: tuple):
    # Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
    result: float = 0
    try:
        sum_nums, qty_incorrect_elem = personal_sum(numbers) # сохраняем результат функции "personal_sum", чтобы не было беды
        result = sum_nums / (len(numbers) - qty_incorrect_elem)

    except ZeroDivisionError:
        # Т.к. коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError при делении на 0 и верните 0.
        result = 0

    except TypeError:
        # Обработайте исключение TypeError выводя строку 'В numbers записан некорректный тип данных'.
        print(f'В numbers записан некорректный тип данных')
        result = None # В таком случае функция просто вернёт None.

    return result

# Пример выполнения программы:
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать