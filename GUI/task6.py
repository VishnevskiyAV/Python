# Чекбокс
# Выведите чекбокс, который при каждом запуске программы случайным образом должен быть либо включенным, либо выключенным.

from tkinter import *
import random

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

choice = IntVar()
check = Checkbutton(root, bd=20, text="Согласие на обработку данных", variable=choice, onvalue=1, offvalue=0)

# Another variant of realization
#arr = [0, 1]             
#choice.set(random.choice(arr))

choice.set(random.randint(0, 1))
print(choice.get())

check.pack()
root.mainloop()



