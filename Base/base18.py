# Выполнение команд
# Откройте командную строку в своей системе.
# Узнайте, с помощью какой команды можно получить текущую дату, используя команду help, либо документацию к своей ОС.
# Напишите программу, которая выполняет эту команду и выводит результат с помощью функции print().

import subprocess
import io

sp = subprocess.Popen(['date'], stdout=subprocess.PIPE, shell=True)
out = io.TextIOWrapper(sp.stdout, encoding = 'CP866')
s = ' '
while s:
    s = out.readline()
    print(s)

