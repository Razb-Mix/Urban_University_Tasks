# Домашнее задание по уроку "Try и Except".
# Задание "Программистам всё можно":

def add_everything_up(num_1, num_2):
    try:
        sum = round(num_1 + num_2, 3)

    except TypeError:
        #sum = str(num_1) + str(num_2) # решение в лоб
        sum = ''.join([str(num_1), str(num_2)]) # Опробуем метод join

    return sum

# Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
