# Обработка событий
# Сделайте кнопку с текстом «Сгенерировать случайное число».
# При клике по кнопке под ней должно появляться случайное целое число от 1 до 100.
# Примечание: для вывода сгенерированного числа используйте Label.


from tkinter import *
from random import random

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

def handlerclick1(event):
    num = int(random()*100)
    Label(root, text=num, font="Tahoma 10", bg="White", width=18, height=2).pack()    

root = Tk()
setwindow(root)

button = Button(root, text="Сгенерировать случайное число", font="Tahoma 20")
button.bind("<Button-1>", handlerclick1)

button.pack()
root.mainloop()