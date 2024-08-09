# Калькулятор
# Для создания .exe
# pip install auto-py-to-exe
# auto-py-to-exe

import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


def dif():
    num1, num2 = get_values()
    res = num1 / num2
    if res == int(res):
        insert_values(int(res))
    else:
        insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('300x300')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=4, height=3, command=add)
button_add.place(x=55, y=150)
button_sub = tk.Button(window, text='-', width=4, height=3, command=sub)
button_sub.place(x=105, y=150)
button_mul = tk.Button(window, text='*', width=4, height=3, command=mul)
button_mul.place(x=155, y=150)
button_dif = tk.Button(window, text=' / ', width=4, height=3, command=dif)
button_dif.place(x=205, y=150)
number1_entry = tk.Entry(window, width=31)
number1_entry.place(x=55, y=75)
number2_entry = tk.Entry(window, width=31)
number2_entry.place(x=55, y=125)
answer_entry = tk.Entry(window, width=31)
answer_entry.place(x=55, y=250)
number1 = tk.Label(window, text='Введите первое число:')
number1.place(x=55, y=50)
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=55, y=100)
answer1 = tk.Label(window, text='Итого:')
answer1.place(x=55, y=225)
window.mainloop()
