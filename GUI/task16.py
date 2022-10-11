# Обработка событий
# Создайте список из 3-х элементов, где значениями будут 3 различных цвета.
# При наведении курсора мыши на окно программы (именно на окно) цвет его фона должен меняться на случайный элемент из списка, 
    # созданного в предыдущем пункте.
# При уводе курсора мыши с окна программы цвет его фона должен возвращаться на цвет по умолчанию.

from tkinter import *
from random import choice

def setwindow(root):
    root.title("The title")
    root.resizable(False, False)

    w = 1000
    h = 500
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y)) 

def handlerenter(event):
    
    color = ["red", "yellow", "green"]
    color = choice(color)
    event.widget.config(bg = color)

def handlerleave(event):
    event.widget.config(bg = "black")


root = Tk()
root.configure(bg="black")
setwindow(root)

root.bind("<Enter>", handlerenter)
root.bind("<Leave>", handlerleave)

root.mainloop()