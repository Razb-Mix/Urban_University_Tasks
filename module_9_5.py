# Задача "Range - это просто":

# Создайте пользовательский класс исключения StepValueError, который наследуется от ValueError.
class StepValueError(ValueError):
    # Наследования достаточно, класс оставьте пустым при помощи оператора pass.
    pass


class Iterator:
    def __init__(self, start: int, stop: int, step: int=1):
        # принимающий значения старта и конца итерации, а также шага.
        # В этом методе в первую очередь проверяется step на равенство 0.
        if step == 0:
            # Если равно, то выбрасывается исключение
            raise StepValueError('шаг не может быть равен 0')
        else:
            self.step = step  # step - шаг, с которым совершается итерация.
            self.start = start # start - целое число, с которого начинается итерация.
            self.stop = stop # stop - целое число, на котором заканчивается итерация.
            self.pointer = start # pointer - указывает на текущее число в итерации (изначально start)
            self.i = 0 # счётчик итераций

    def __iter__(self):
        self.i = 0 # сбрасываем счётчик перед новым проходом
        self.pointer = self.start # сбрасывающий значение pointer на start
        return self # возвращающий сам объект итератора.

    def __next__(self):
        # __next__ - метод, увеличивающий атрибут pointer на step.
        # В зависимости от знака атрибута step итерация завершится
        self.i += 1
        if self.i == 1:
            # проверить возможна ли вторая итерация, так как в эталонном результате нет вывода первого прохода объекта iter5,
            # если я, конечно, правильно понял логику задания и в нём нет ошибки.
            if ((self.step > 0 and self.pointer + self.step > self.stop)
                    or (self.step < 0 and self.pointer + self.step < self.stop)):
                # если вторая итерация не возможна, то ничего не выводим
                raise StopIteration()
        elif self.i > 1 and self.start <= self.pointer + self.step -1 < self.stop and self.step > 0:
            # либо когда pointer станет больше stop
            self.pointer += self.step
        elif self.i > 1 and self.start >= self.pointer + self.step + 1 > self.stop and self.step < 0:
            # либо меньше stop.
            self.pointer += self.step
        else:
            raise StopIteration()

        return self.pointer

# Пример выполняемого кода:
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')

except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')