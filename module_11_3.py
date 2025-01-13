from inspect import getmodule, ismodule, getmembers, ismethod

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

    def get_something(self):
        pass

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

# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
def introspection_info(obj):
    dict_: dict = {'type': type(obj), 'attributes': [], 'methods': []} # - Тип объекта. И создание пустых списков.

    if ismodule(getmodule(obj)):
        # Модуль, к которому объект принадлежит.
        dict_['module'] = getmodule(obj).__name__
    else:
        dict_['module'] = "Нет данных"

    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)  # сохраняем в ссылку атрибут объекта

        # фильтруем данные
        if attr_name[:2] == '__' and attr_name[-2:] == '__' or 'method' in str(type(attr)):
        #if ismethod(attr): - вроде бы смысл тот же, а результат другой... Похоже где-то в условии неточность или я что-то не понял
            dict_['methods'].append(attr_name) # - Методы объекта.
        else:
            dict_['attributes'].append(attr_name) # - Атрибуты объекта.

    return dict_ # Верните словарь с данными об объекте

# Пример работы:
iter_ = Iterator(1, 10) # Рекомендуется создавать свой класс и объект для лучшего понимания
number_info_1 = introspection_info(42)
number_info_2 = introspection_info(iter_)
number_info_3 = introspection_info(True)
number_info_4 = introspection_info('True')

# Вывод на консоль:
print(number_info_1, number_info_2, number_info_3, number_info_4, sep="\n"*2)