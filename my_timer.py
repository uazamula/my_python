from tkinter import *

window = Tk()
window.geometry('400x400')


def update():
    global timer
    global i
    global limit
    if i < limit:
        window['bg'] = colors[i]
        timer = window.after(1000, update)
    else:
        window.after_cancel(timer)
    i += 1


colors = ['yellow', 'blue', 'red', window['bg']]
limit = len(colors)
i = 0
timer = window.after(1000, update)
window.mainloop()
