# Метки
# Создайте окно с меткой, где должно выводиться случайное целое число от 1 до 1000.
# Примечание: то есть при каждом запуске программы там должно появляться случайное число.

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

label = Label(root, text=int(random()*1000)) 
label.pack()

root.mainloop()