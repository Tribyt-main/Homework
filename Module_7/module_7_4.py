team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = round((team1_time + team2_time) / (score_2 + score_1), 1)
if time_avg.is_integer():
    time_avg = int(time_avg)
challenge_result = 'Победа команды Волшебники данных!'
# Метода %s %
print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))
# Метод format()
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {}с !'.format(team2_time))
# Метод f''
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по {time_avg} секунды на задачу!.')
