from tkinter import *

window = Tk()
window.geometry('400x300')

seasons = ['зима', 'весна', 'літо', 'осінь']
default_value = 'Виберіть пору року'

choice = StringVar(window)
choice.set(default_value)

seasonsGenMap = {'зима': 'зиму', 'весна': 'весну', 'літо': 'літо',
                 'осінь': 'осінь'}


def click(event):
    label['text'] = f'Ви обрали {seasonsGenMap[choice.get()]}'


optionMenu = OptionMenu(window, choice, *seasons, command=click)
optionMenu.pack()

label = Label(text='Ви ще нічого не обрали')
label.pack()

window.mainloop()
