from tkinter import *

root = Tk()
root.title("A@di's calculator")

e = Entry(root, width=40)
# we can also add colour as we use in button
e.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

lst = []


def clear():
    global lst
    lst = []
    e.delete(0, END)


def dell():
    a = e.get()
    e.delete(0, END)
    e.insert(0, a[:-1])


def click(x):
    a = e.get()
    e.delete(0, END)
    if a == '0' or a == '00':
        e.insert(0, x)
    else:
        e.insert(0, a+x)


def operator(op):
    global lst
    lst.append(e.get())
    lst.append(op)
    e.delete(0, END)


def equal():
    global lst
    lst.append(e.get())
    e.delete(0, END)
    equation = ""
    for val in lst:
        equation += val
    e.insert(0, eval(equation))
    lst = []


Button(root, text=" 1 ", padx=20, pady=20, command=lambda: click('1')).grid(row=3, column=0, padx=5, pady=5)
Button(root, text=" 2 ", padx=20, pady=20, command=lambda: click('2')).grid(row=3, column=1, padx=5, pady=5)
Button(root, text=" 3 ", padx=20, pady=20, command=lambda: click('3')).grid(row=3, column=2, padx=5, pady=5)

Button(root, text=" 4 ", padx=20, pady=20, command=lambda: click('4')).grid(row=2, column=0, padx=5, pady=5)
Button(root, text=" 5 ", padx=20, pady=20, command=lambda: click('5')).grid(row=2, column=1, padx=5, pady=5)
Button(root, text=" 6 ", padx=20, pady=20, command=lambda: click('6')).grid(row=2, column=2, padx=5, pady=5)

Button(root, text=" 7 ", padx=20, pady=20, command=lambda: click('7')).grid(row=1, column=0, padx=5, pady=5)
Button(root, text=" 8 ", padx=20, pady=20, command=lambda: click('8')).grid(row=1, column=1, padx=5, pady=5)
Button(root, text=" 9 ", padx=20, pady=20, command=lambda: click('9')).grid(row=1, column=2, padx=5, pady=5)

Button(root, text=" . ", padx=20, pady=20, command=lambda: click(".")).grid(row=4, column=0, padx=5, pady=5)
Button(root, text=" 0 ", padx=20, pady=20, command=lambda: click('0')).grid(row=4, column=1, padx=5, pady=5)
Button(root, text=" 00 ", padx=20, pady=20, command=lambda: click("00")).grid(row=4, column=2, padx=5, pady=5)

Button(root, text=" + ", padx=20, pady=20, command=lambda: operator("+")).grid(row=1, column=3, padx=5, pady=5)
Button(root, text=" - ", padx=20, pady=20, command=lambda: operator("-")).grid(row=2, column=3, padx=5, pady=5)
Button(root, text=" * ", padx=20, pady=20, command=lambda: operator("*")).grid(row=3, column=3, padx=5, pady=5)
Button(root, text=" / ", padx=20, pady=20, command=lambda: operator("/")).grid(row=4, column=3, padx=5, pady=5)

Button(root, text=" = ", padx=45, pady=20, command=equal, fg="green").grid(row=5, column=0, columnspan=2, padx=5, pady=5)
Button(root, text=" clear ", padx=20, pady=20, fg="red", command=clear).grid(row=5, column=2, padx=5, pady=5)
Button(root, text=" <-- ", padx=20, pady=20, fg="red", command=dell).grid(row=5, column=3, padx=5, pady=5)

root.mainloop()
