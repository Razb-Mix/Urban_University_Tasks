# Домашнее задание по уроку "Пространство имен"

def test_function():

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()
# inner_function() # Выдаётся ошибка, так как мы не можем снаружи из глобальной области зайти в область видимости inner_function