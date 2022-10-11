# Список
# В цикле попросите пользователя вводить названия городов, каждый раз добавляя их в список.
# Когда пользователь введёт 0, то нужно выйти из цикла.
# Используя созданный список, выведите его с помощью Listbox в окно программы.

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

arr = []
i = 0
while i <= len(arr):
    town = input("Веедите название города (для окончания ввода введите 0): ")
    if town == "0":
        break
    arr.append(town)
    i+=1

list = Listbox(root, font="Tahoma 20", width=20, height=4, selectmode=SINGLE)

for t in arr:
    list.insert(END, t)

list.pack()
root.mainloop()