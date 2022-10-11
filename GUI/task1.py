# Создание окна
# Создайте окно размером 1000 на 500 пикселей.
# Расположите его в верхнем левом углу.
# Расположите его в правом верхнем углу.
# Примечание: в 3-ем задании не пишите конкретные значения координат расположения. Используйте встроенные функции,
    # позволяющие получить разрешение экрана у пользователя, и на их основе рассчитайте координаты местоположения, 
    # чтобы правый верхний угол Вашего окна располагался в правом верхнем углу экрана.

from tkinter import *

root = Tk()
root.resizable(False, False)
root.title("The title")

w = 1000
h = 500
ws = root.winfo_screenwidth()
wh = root.winfo_screenheight()
print(ws, wh)
x = int(ws - w)   # width of the screen - width of the window
y = int(wh - wh)  # 0 always on the top of the screen
# root.geometry("{0}x{1}+{2}+{3}".format(w, h, 0, 0)) # Расположите его в верхнем левом углу
root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y)) #Расположите его в правом верхнем углу

root.mainloop()