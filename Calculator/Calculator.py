from tkinter import *

root = Tk()
root.title("CSC426 Calculator")
root.geometry("350x500")

expression = ""

def press(value):
    global expression
    expression += str(value)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression.replace("^", "**")))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = StringVar()

entry = Entry(root, textvariable=equation, font=("Arial", 20), bd=10)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('%',4,1), ('^',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    Button(root,
           text=text,
           width=8,
           height=3,
           command=lambda t=text: press(t)
          ).grid(row=row, column=col)

Button(root, text='C', width=8, height=3, command=clear).grid(row=5, column=0)
Button(root, text='=', width=25, height=3, command=equal).grid(row=5, column=1, columnspan=3)

root.mainloop()
