# Домашнее задание по теме "Декораторы"
def is_prime(func):
    def wrapper(num_1, num_2, num_3):
        result_of_sum = func(num_1, num_2, num_3)
        if result_of_sum > 1:  # Число подходит под признаки "простого" - больше 1
            for j in range(2, result_of_sum):  # Запускаем цикл на подбор делителей (j) для проверяемого result_of_sum
                if result_of_sum % j == 0:  # Проверяем равен ли 0 остаток от деления result_of_sum на j, если да, то
                    print("Составное") # распечатывает "Составное", если результат 1ой функции будет не простым числом
                    return result_of_sum # Прервать цикл, так как дальнейший перебор не имеет смысла
            print("Простое") # распечатывает "Простое", если результат 1ой функции будет простым числом
            return result_of_sum
        else:
            print("Сумма меньше или равна единице")
            return result_of_sum
    return wrapper

@is_prime
def sum_three(num_1, num_2, num_3):
    return num_1 + num_2 + num_3

result = sum_three(2, 3, 6)
print(result)