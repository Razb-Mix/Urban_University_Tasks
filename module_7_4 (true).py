# История: соперничество двух команд - Мастера кода и Волшебники данных.
# Пример входных данных
from random import random

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Использование %:
# Переменные: количество участников первой команды (team1_num).
print("В команде Мастера кода участников: %d !" % team1_num)

# Переменные: количество участников в обеих командах (team1_num, team2_num).
print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))


# Использование format():
# Переменные: количество задач решённых командой 2 (score_2).
print("Команда Волшебники данных решила задач: {:d} !".format(score_2))

# Переменные: время за которое команда 2 решила задачи (team2_time).
print("Волшебники данных решили задачи за {:.1f} с !".format(team2_time))


# Использование f-строк:
# Переменные: количество решённых задач по командам: score_1, score_2
print(f'Команды решили {score_1} и {score_2} задач.')

# Переменные: исход соревнования (challenge_result).
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(f'Результат битвы: {result}')

# Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!')