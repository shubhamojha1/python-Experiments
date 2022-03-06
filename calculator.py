from tkinter import *

expression = " "


def press(num):
    global expression

    expression = expression + str(num)
    equation.set(expression)

def equalpress():

    try:
        global expression

        total = str(eval(expression))
        equation.set(total)

        expression = " "

    except:
        equation.set("!!ERROR!!")
        expression = " "

def clear():
    global expression
    expression = " "
    equation.set("")

color = "#17202a"
if __name__ == "__main__":
    tk = Tk()

    tk.configure(background=color)
    tk.title("CALCULATOR")
    tk.geometry("290x150")
    equation = StringVar()

    expression_field = Entry(tk, textvariable=equation, fg='white', bg=color)
    expression_field.grid(columnspan=4, ipadx=85)

    button_1 = Button(tk, text='1', fg='white',bg=color, command=lambda:press(1),height=1,width=7)
    button_1.grid(row=2,column=0)

    button_2 = Button(tk, text='2', fg='white',bg=color, command=lambda: press(2), height=1, width=7)
    button_2.grid(row=2, column=1)

    button_3 = Button(tk, text='3', fg='white',bg=color, command=lambda: press(3), height=1, width=7)
    button_3.grid(row=2, column=2)

    button_4 = Button(tk, text='4', fg='white',bg=color, command=lambda: press(4), height=1, width=7)
    button_4.grid(row=3, column=0)

    button_5 = Button(tk, text='5', fg='white',bg=color, command=lambda: press(5), height=1, width=7)
    button_5.grid(row=3, column=1)

    button_6 = Button(tk, text='6', fg='white',bg=color, command=lambda: press(6), height=1, width=7)
    button_6.grid(row=3, column=2)

    button_7 = Button(tk, text='7', fg='white',bg=color, command=lambda: press(7), height=1, width=7)
    button_7.grid(row=4, column=0)

    button_8 = Button(tk, text='8', fg='white',bg=color, command=lambda: press(8), height=1, width=7)
    button_8.grid(row=4, column=1)

    button_9 = Button(tk, text='9',fg='white',bg=color, command=lambda: press(9), height=1, width=7)
    button_9.grid(row=4, column=2)

    button_0 = Button(tk, text='0', fg='white',bg=color, command=lambda: press(0), height=1, width=7)
    button_0.grid(row=5, column=0)

    plus = Button(tk, text="+",fg='white',bg=color,command=lambda:press("+"),height=1, width=7)
    plus.grid(row=2,column=3)

    minus = Button(tk, text="-", fg='white',bg=color, command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(tk, text="*", fg='white',bg=color, command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(tk, text="/", fg='white',bg=color, command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(tk, text="=", fg='white',bg=color, command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(tk, text="CLR", fg='white',bg=color, command=clear, height=1, width=7)
    clear.grid(row=5, column=1)

    decimal = Button(tk, text=".",fg='white',bg=color, command=lambda: press("."),height=1, width=7)
    decimal.grid(row=6, column=0)



    tk.mainloop()