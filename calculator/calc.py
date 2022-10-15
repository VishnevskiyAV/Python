from tkinter import *

# Функция обработки кнопок (принимает текст от нажатия кнопок, обрабатываем через command)
start = True
lastcommand = '='
result = 0

def click(text):
    global start
    global lastcommand
    global display
    # разделяем нажатие на цифру и нажатие на знак
    if text.isdigit() or text == '.':
        if start:
            display.configure(text='')  # стерли с дисплея 0
            start = False
        if text != '.' or display.cget('text').find('.') == -1: # Игнорируем вторую точку
            display.configure(text=(display.cget('text') + text))  # Добавляем значения на дисплей
    else:
        if start:
            lastcommand = text  # Сохраняем на экране значение
        else: 
            calculate(float(display.cget('text'))) # вызываем функцию вычисления и передаем ей число с дисплея
            lastcommand = text
            start = True

# Функция для обработки операций вычисления (передаем число с дисплея)
def calculate(x):
    global lastcommand
    global result
    global display
    if lastcommand == '+':
        result += x
    elif lastcommand == '-':
        result -= x
    elif lastcommand == '*':
        result *= x
    elif lastcommand == '/':
        try:
            result /= x
        except ZeroDivisionError:
            pass
    elif lastcommand == '=':
        result = x
    display.configure(text=result)

# Создадим объект и заголовок
root = Tk()
root.title("Калькулятор")

# Добавим кнопки в виде кортежа
buttons = (('7', '8', '9', '/'),
          ('4', '5', '6', '*'),
          ('1', '2', '3', '-'),
          ('0', '.', '=', '+'))

# Добавим табло калькулятора и разместим в самом верху растянув на 4 столбца     
display = Label(root, text='0', font='Tahoma 20', bd=10)
display.grid(row=0, column=0, columnspan=4)

# Выведем кнопки с помощью цикла на таблицу grid
for row in range(4):
    for column in range(4):
        button = Button(root, text=buttons[row][column], font="Tahoma 20", command=lambda text=buttons[row][column]: click(text))
        button.grid(row=row+1, column=column, padx=5, pady=5, ipadx=20, ipady=20, sticky="nsew")

# Получим размер окна
w = root.winfo_reqwidth()
h = root.winfo_reqheight()

# Получим разрешение экрана пользователя
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# Вычислим центр экрана
x = int(ws / 2 - w / 2)
y = int(hs / 2 - h / 2)

# Зададим координаты расположения окна
root.geometry("+{0}+{1}".format(x, y))

root.mainloop()
