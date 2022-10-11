# Scrollbar
# Добавьте scrollbar к текстовой области из упражнения к уроку «Текстовая область».
# Примечание: при необходимости в текстовый файл надо добавить ещё текста, чтобы scrollbar стал активным.

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
handler.write("abc 123\n890\n1221\n23123\n5555\n6666\ndfsdf")
handler.close()

handler = open('a.txt', 'r')
r = handler.read()
handler.close()

text = Text(root, bd=2, font="Tahoma 20", bg="Yellow", fg="Green", width=40)
text.insert(END, r)

scrollbar = Scrollbar(root, command=text.yview, orient=VERTICAL)
text['yscrollcommand'] = scrollbar.set

text.pack(side='left')
scrollbar.pack(side='left', fill=Y)
root.mainloop()