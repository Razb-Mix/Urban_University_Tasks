def calculate_structure_sum(*args):
    sum_of_elements = 0

    for arg in args:
        if isinstance(arg, (list, tuple, set)):
            sum_of_elements += calculate_structure_sum(*arg)
        elif isinstance(arg,dict):
            sum_of_elements += calculate_structure_sum(*arg.items())
        elif isinstance(arg, str):
            sum_of_elements += len(arg)
        elif isinstance(arg, (int, float)):
            sum_of_elements += arg

    return sum_of_elements # конец работы функции

data_structure = [

[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])

]

result = calculate_structure_sum(data_structure)

print(result)
