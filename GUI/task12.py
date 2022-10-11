# Компоновщик place
#  Используя place, создайте форму входа со следующими элементами: метку с текстом «Авторизация», 
    # под ней 2 текстовых поля и метки слева от них («Логин:», «Пароль:»), а уже под этими элементами выведите кнопку («Войти»).
# Примечание: разумеется, форма должна выглядеть аккуратно, всё должно быть выравнено.

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

label1.place(relx=0.5, rely=0, anchor="n")
entry1.place(relx=0.5, rely=0.1, anchor="n")
entry2.place(relx=0.5, rely=0.2, anchor="n")
button.place(relx=0.5, rely=0.3, anchor="n")
root.mainloop()