# Радиокнопки
# Создайте список из 5-ти значений с названиями городов.
# Выведите радиокнопки с этими названиями городов, используя цикл по списку.
# Примечание: для параметра value создайте отдельную переменную и её значением должен быть индекс списка.
    # То есть, если в списке город «Москва» имеется индекс 3, то и value при создании радио-кнопки должен быть равен 3.

from tkinter import *

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

label = Label(root, text="Выберите город", font="Tahoma 20")
label.pack()

arr = ["Moscow", "St.Petersburg", "Kazan", "Samara", "Pskov"]
choice = IntVar()
for i in arr:
    r = Radiobutton(root, text=i,font="Tahoma 20", variable=choice, value=arr.index(i))
    choice.set(0)
    r.pack()




root.mainloop()