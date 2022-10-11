# Создание фреймов
# Создайте 3 элемента Frame.
# В первый Frame добавьте label с текстом «Важная форма».
# Во второй Frame добавьте 2 текстовых поля.
# В третий Frame добавьте кнопку «Отправить форму».
# Разместите все 3 элемента Frame в окне.

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

frame1 = Frame(root, bg="Red", bd=3)
frame2= Frame(root, bg="Green", bd=3)
frame3 = Frame(root, bg="Black", bd=3)

label = Label(frame1, text="Важная форма", font="Tahoma 20")

entry1 = Entry(frame2, font="Tahoma 20", bg="white", fg="white", bd=4)
entry2 = Entry(frame2, font="Tahoma 20", bg="white", fg="white", bd=4)


button = Button(frame3, text="Отправить форму", width=15, height=1, font="Tahoma 18")


label.pack()
entry1.pack()
entry2.pack()
button.pack()
frame1.pack()
frame2.pack()
frame3.pack()

root.mainloop()