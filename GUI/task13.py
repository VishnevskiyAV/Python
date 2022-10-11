# Компоновщик grid
# Сделайте предыдущее упражнение, но уже используя grid. 

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

label1 = Label(root, text="Авторизация", font="Tahoma 10", bg="White", width=18, height=2)

entry1 = Entry(root, font="Tahoma 20", bg="white", fg="white", bd=4)
entry1.insert(END, "Логин")
entry2 = Entry(root, font="Tahoma 20", bg="white", fg="white", bd=4)
entry2.insert(END, "Пароль")

button = Button(root, text="Войти", width=10, height=2, font="Tahoma 18")

label1.grid(row = 1, column=1)
entry1.grid(row = 2, column=1)
entry2.grid(row = 3, column=1)
button.grid(row = 4, column=1)
root.mainloop()