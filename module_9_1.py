# Задача "Вызов разом":
def apply_all_func(int_list, *functions):
    results: dict = {} # В функции apply_all_func создайте пустой словарь results.

    for function in functions:
        # Переберите все функции из *functions.
        # При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
        results[function.__name__] = function(int_list)

    # Возвращать словарь, где ключом будет название вызванной функции, а значением - её результат работы со списком int_list.
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))