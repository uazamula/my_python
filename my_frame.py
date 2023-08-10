from tkinter import *
from tkinter import messagebox

w = Tk()
w.geometry('400x300')

frame = Frame()
frame.pack(fill='x')
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=2)
frame.columnconfigure(2, weight=1)


def click():
    messagebox.showinfo('khkkk','==')


b1 = Button(frame, text='1', font=('Arial', 18), command=click())

b1.grid(row=0, column=0, sticky='N')

b2 = Button(frame, text='2', font=('Arial', 18), )
b2.grid(row=0, column=1, sticky='N')

b3 = Button(frame, text='3', font=('Arial', 18))
b3.grid(row=0, column=2, sticky='N')

b4 = Button(frame, text='4', font=('Arial', 18))
b4.grid(row=1, column=0, sticky='N')

b5 = Button(frame, text='5', font=('Arial', 18))
b5.grid(row=1, column=1, sticky='N')

b6 = Button(frame, text='6', font=('Arial', 18))
b6.grid(row=1, column=2, sticky='N')
print()
print()
mainloop()
