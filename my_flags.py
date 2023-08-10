from tkinter import *

w = Tk()
w.title('Форма')
w.geometry('400x500')
label = Label(text='xfn')
label.grid(column=0, row=0, sticky=W, padx=50)

labelTop = Label(text='Виберіть пристрої введення')
labelTop.grid(column=1, row=1, sticky=W)

choice1 = BooleanVar()
flag1 = Checkbutton(text='Клавіатура', variable=choice1)
flag1.grid(column=1, row=2, sticky=W)

choice2 = BooleanVar()
flag2 = Checkbutton(text='Монітор', variable=choice2)
flag2.grid(column=1, row=3, sticky=W)

choice3 = BooleanVar()
flag3 = Checkbutton(text='Миша', variable=choice3)
flag3.grid(column=1, row=4, sticky=W)

choice4 = BooleanVar()
flag4 = Checkbutton(text='Динаміки', variable=choice4)
flag4.grid(column=1, row=5, sticky=W)


def click():
    isTrue = choice1.get() and choice3.get() and not choice2.get() and not choice4.get()

    if isTrue:
        labelResult['text'] = 'Правильно!'
    else:
        labelResult['text'] = 'Спробуй ще'


button = Button(text='Перевірити', command=click)
button.grid(column=1, row=6, sticky=W)

labelResult = Label(text='Результат')
labelResult.grid(column=1, row=7, sticky=W)
mainloop()
