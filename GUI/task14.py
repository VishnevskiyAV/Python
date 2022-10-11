# Работа с изображениями
# Попросите пользователя ввести путь к картинке.
# Следующим шагом попросите его указать, с каким масштабом выводить изображение.
# Выведите его в окно программы с указанным пользователем масштабированием, используя Label.
# Примечание: нужно учесть, что, если пользователь вводит значения меньше 1, значит, он хочет его сжать,
    # и для этого потребуется функция subsample, а также перевод, например, 0.2 в число 5 (1 / 0.2).

from tkinter import *

def setwindow(root):
    root.title("The title")
    root.resizable(False, False)

    w = 1000
    h = 500
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y)) 

def img(scale):
    if scale >= 1:
        scale = int(scale)
        fs = photo.zoom(scale, scale) 
        return fs
    elif scale < 1:
        scale = 1 / scale
        scale = int(scale)
        fs = photo.subsample(scale, scale)
        return fs

path = input("Please enter the PATH to the picture: ")
scale = float(input("Enter the scale of image: "))

root = Tk()
setwindow(root)

photo = PhotoImage(file=path)

q = img(scale)
bl = Label(root, image=q)

bl.place(x=0, y=0, relwidth=1, relheight=1)
root.mainloop()