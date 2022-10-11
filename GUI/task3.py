# Кнопки
# Посмотрите в справочнике, какие есть параметры у Button.
# Добавьте несколько кнопок с различными значениями атрибутов в окно.

from tkinter import *
from random import random

def setwindow(root):
    root.title("The title")
    root.resizable(False, False)

    w = 1000
    h = 500
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()
    print(ws, wh)

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y)) 

root = Tk()
setwindow(root)

button1 = Button(root, text="Button", width=15, height=4, font="Tahoma 18", bg="White", fg="Green")
button1.pack()
root.mainloop()