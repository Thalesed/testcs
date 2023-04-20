import graphic
from tkinter import *

g = graphic.Graphic()

win = Tk()
win.title("Função")
win.geometry('310x100')
box = Entry(win, width=50, borderwidth=5)
box.grid(row=0, column=0, columnspan=4)

btn = Button(win, text='Enter', bg='blue', command=g.start)
btn.grid(row=1, column=0)


