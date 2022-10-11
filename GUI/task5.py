# Текстовая область
# Создайте текстовый файл с произвольным текстом.
# Выведите текстовую область в окно, где должен быть выведен весь текст из файла, созданном в предыдущем пункте.
# Примечание: разумеется, надо воспользоваться функциями для работы с файлами.

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

handler = open('a.txt', 'w')
handler.write("abc 123\n890")
handler.close()

handler = open('a.txt', 'r')
r = handler.read()
handler.close()

text = Text(root, bd=2, font="Tahoma 20", bg="Yellow", fg="Green", width=10, height=4, padx=10, pady=20)
text.insert(END, r)

text.pack()
root.mainloop()





