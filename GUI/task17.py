# Обработка событий
# Выведите, используя метку, в окне такую строку: «ax^2 + bx + c = 0».
# Добавьте 3 текстовых поля с метками «a:», «b:» и «c:».
# Добавьте кнопку «Вычислить корни уравнения».
# После вычисления их нужно вывести под кнопкой в формате: «x1 = …; x2 = …;».
# Если число под корнем отрицательное, то вывести в метке для результата строку: «Нет корней».

from tkinter import *
from math import sqrt

def setwindow(root):
    root.title("Окно программы")
    root.resizable(False, False)

    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

def handlerbutton(event = False):
    global en1
    global en2
    global en3
    global result
    if event:
        print(event)
    try:   # мне лень делать проверку на отрицательный квадратный корень (надо выносить его в отдельную переменную), я понимаю что по матамитечским правилам такое не допостимо, но ....
        x1 = ((float(en2.get()) * -1) + (sqrt(float(en2.get()) **2) - (4 * (float(en1.get())) * (float(en3.get()))))) / (float(en1.get()) * 2)
        x2 = ((float(en2.get()) * -1) - (sqrt(float(en2.get()) **2) - (4 * (float(en1.get())) * (float(en3.get()))))) / (float(en1.get()) * 2)
        result.config(text="x1 = " + str(x1) + "; " + "x2 = " + str(x2) + ";")
    except ZeroDivisionError:
        result.config(text="Нет корней")
    except ValueError:
        if not en1.get() or not en2.get() or not en3.get():
            result.config(text="Вы ничего не ввели!")
        else:
            result.config(text="Вы ввели не числа!")
    
root = Tk()
setwindow(root)

label = Label(root, text="ax^2 + bx + c = 0", font="Tahoma 20")

fr1 = Frame(root, bg="black", bd=0)
fr2 = Frame(root, bg="black", bd=0)
fr3 = Frame(root, bg="black", bd=0)
en1 = Entry(fr1, font="Tahoma 20")
en2 = Entry(fr2, font="Tahoma 20")
en3 = Entry(fr3, font="Tahoma 20")

Label(fr1, text="a:", font="Tahoma 20").pack(side="left")
Label(fr2, text="b:", font="Tahoma 20").pack(side="left")
Label(fr3, text="c:", font="Tahoma 20").pack(side="left")

button = Button(root, text="Вычислить корни уравнения", font="Tahoma 20", command=handlerbutton)

result = Label(root, font="Tahoma 20")

en1.bind("<Return>", handlerbutton)
en2.bind("<Return>", handlerbutton)
en3.bind("<Return>", handlerbutton)

label.place(relx=0.5, rely=0.01, anchor="n")
fr1.place(relx=0.5, rely=0.1, anchor="n")
fr2.place(relx=0.5, rely=0.2, anchor="n")
fr3.place(relx=0.5, rely=0.3, anchor="n")
en1.pack()
en2.pack()
en3.pack()
button.place(relx=0.5, rely=0.4, anchor="n")
result.place(relx=0.5, rely=0.5, anchor="n")
root.mainloop()