# Функции для работы с датой и временем
# Попросите пользователя ввести 3 числа: год, месяц и число рождения.
# Напишите ему, сколько секунд он уже живёт.
from datetime import *

y = int(input("Year of your birth: "))
m = int(input("Month of your birth: "))
d = int(input('Day of your birth: '))

now_time = datetime.today()
dt = datetime(y, m, d)
delta = (now_time-dt)
print('Seconds you live since birth:', delta.total_seconds())


