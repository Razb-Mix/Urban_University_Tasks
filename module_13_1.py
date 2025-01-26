# Задача "Асинхронные силачи":
import asyncio

# Напишите асинхронную функцию start_strongman(name, power), где name - имя силача, power - его подъёмная мощность.
async def start_strongman(name: str, power: int):
    # В начале работы должна выводиться строка - 'Силач <имя силача> начал соревнования.'
    print('Силач', name, 'начал соревнования.')

    for num_ball in range(1, 6): # Для каждого участника количество шаров одинаковое - 5.
        await asyncio.sleep(2 / power) # с задержкой обратно пропорциональной его силе power.
        # После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>'
        print('Силач', name, 'поднял', num_ball, 'шар')
    else:
        # В конце поднятия всех шаров должна выводится строка 'Силач <имя силача> закончил соревнования.'
        print('Силач', name, 'закончил соревнования.')

# Также напишите асинхронную функцию start_tournament, в которой создаются 3 задачи для функций start_strongman.
async def start_tournament():
    # Имена(name) и силу(power) для вызовов функции start_strongman можете выбрать самостоятельно.
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))

    # После поставьте каждую задачу в ожидание (await).
    await task_1
    await task_2
    await task_3


# Запустите асинхронную функцию start_tournament методом run.
asyncio.run(start_tournament())
