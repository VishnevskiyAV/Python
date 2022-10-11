# Текстовые поля
# Создайте текстовое поле.
# Попросите пользователя ввести в консоли произвольную строку.
# Выведите эту строку в текстовом поле окна.
# Примечание: запрос строки и её вывод в текстовом поле должны происходить до mainloop().

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

text = str(input("Enter a few words: "))

entry = Entry(root, font="Tahoma 20", bg="black", fg="white", bd=4)
entry.insert(END, text)

entry.pack()
root.mainloop()