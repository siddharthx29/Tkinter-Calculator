from tkinter import *

window = Tk()
window.geometry('500x500')
window.title("My Calculator")
window.config(bg="lightblue")

def number(num):
    e.insert(END, num)

def add():
    n1 = e.get()
    global math
    global i

    math = "add"
    i = int(n1)

    e.delete(0, END)

def calculate():
    n2 = e.get()

    if math == "add":
        result = i + int(n2)

    e.delete(0, END)
    e.insert(0, result)

def clear():
    e.delete(0, END)

e = Entry(
    window,
    width=30,
    borderwidth=5,
    font=("Arial", 18)
)
e.place(x=65, y=30)

b1 = Button(window, text='1', width=10, height=2, command=lambda: number(1))
b1.place(x=50, y=100)

b2 = Button(window, text='2', width=10, height=2, command=lambda: number(2))
b2.place(x=150, y=100)

b3 = Button(window, text='3', width=10, height=2, command=lambda: number(3))
b3.place(x=250, y=100)

b4 = Button(window, text='4', width=10, height=2, command=lambda: number(4))
b4.place(x=50, y=160)

b5 = Button(window, text='5', width=10, height=2, command=lambda: number(5))
b5.place(x=150, y=160)

b6 = Button(window, text='6', width=10, height=2, command=lambda: number(6))
b6.place(x=250, y=160)

b7 = Button(window, text='7', width=10, height=2, command=lambda: number(7))
b7.place(x=50, y=220)

b8 = Button(window, text='8', width=10, height=2, command=lambda: number(8))
b8.place(x=150, y=220)

b9 = Button(window, text='9', width=10, height=2, command=lambda: number(9))
b9.place(x=250, y=220)

b0 = Button(window, text='0', width=10, height=2, command=lambda: number(0))
b0.place(x=150, y=280)

add_button = Button(window, text='+', width=10, height=2, command=add)
add_button.place(x=350, y=100)

equal_button = Button(window, text='=', width=10, height=2, command=calculate)
equal_button.place(x=350, y=160)

clear_button = Button(window, text='CLEAR', width=10, height=2, command=clear)
clear_button.place(x=350, y=220)

window.mainloop()
