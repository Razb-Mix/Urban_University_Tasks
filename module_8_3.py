# Задача "Некорректность":

class Car:
    def __init__(self, model: str, vin_number, car_number):

        self.model = model # Атрибут объекта model - название автомобиля (строка).
        # ВАЖНО!
        # Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта
        # (в __init__ при объявлении атрибутов __vin и __numbers).
        if Car.__is_valid_vin(vin_number):
            self.__vin = vin_number # Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
        if Car.__is_valid_numbers(car_number):
            self.__numbers = car_number # Атрибут __numbers - номера автомобиля (строка).

    def __is_valid_vin(vin_number):
        # принимает vin_number и проверяет его на корректность.
        if not isinstance(vin_number, int):
            # Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
            # если передано не целое число. (тип данных можно проверить функцией isinstance).
            raise  IncorrectVinNumber("Некорректный тип vin номер")
        else:
            if not 1000000 <= vin_number <= 9999999:
                # Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
                # если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
                raise IncorrectVinNumber("Неверный диапазон для vin номера")
            else:
                # Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
                return True

    def __is_valid_numbers(car_number):
        # Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
        if not isinstance(car_number, str):
            # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
            # если передана не строка. (тип данных можно проверить функцией isinstance)
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        else:
            # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
            # переданная строка должна состоять ровно из 6 символов.
            if not len(car_number) == 6:
                raise IncorrectCarNumbers('Неверная длина номера')
            else:
                # Возвращает True, если исключения не были выброшены.
                return True


class IncorrectVinNumber(Exception):
    def __init__(self, message: str):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message: str):
        self.message = message

# Пример результата выполнения программы:
# Пример выполняемого кода:

try:
   first = Car('Model1', 1000000, 'f123dj')

except IncorrectVinNumber as exc:
   print(exc.message)

except IncorrectCarNumbers as exc:
   print(exc.message)

else:
   print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')

except IncorrectVinNumber as exc:
  print(exc.message)

except IncorrectCarNumbers as exc:
  print(exc.message)

else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')

except IncorrectVinNumber as exc:
  print(exc.message)

except IncorrectCarNumbers as exc:
  print(exc.message)

else:
  print(f'{third.model} успешно создан')