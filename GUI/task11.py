# Компоновщик pack
# Сделайте 4 элемента Label, задав у них одинаковые параметры width и height.
# Выведите первый Label вверху по центру, второй и третий слева и справа соответственно под первым элементом, 
    # а четвёртый по центру снизу.

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

label1 = Label(root, text="Важная форма", font="Tahoma 10", bg="White", width=18, height=2)
label2 = Label(root, text="Важная форма", font="Tahoma 10", bg="green", width=18, height=2)
label3 = Label(root, text="Важная форма", font="Tahoma 10", bg="blue", width=18, height=2)
label4 = Label(root, text="Важная форма", font="Tahoma 10", bg="red", width=18, height=2)

label1.pack(side='top')
label2.pack(side='left')
label3.pack(side='right')
label4.pack(side='bottom')

root.mainloop()