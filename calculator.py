from tkinter import *


def clicked(num):
    global needClear
    if needClear:
        ce()
        needClear = False
    current = textField.get()
    textField.delete(0, END)
    textField.insert(0, str(current) + str(num))


def dot():
    if '.' not in textField.get():
        clicked(".")


def backspace():
    previous = textField.get()
    textField.delete(0, END)
    now = previous[0:-1]
    if len(now) == 0:
        ce()
    else:
        textField.insert(0, now)


def c():
    textField.delete(0, END)
    global needClear
    needClear = True
    global operation
    operation = ""
    global memory
    memory = ""


def ce():
    textField.delete(0, END)
    global needClear
    needClear = True


def negative():
    num = textField.get()
    if num[0] != "-":
        textField.insert(0, "-")
    else:
        textField.delete(0)


def add():
    global memory
    memory = textField.get()
    global operation
    operation = "add"
    global needClear
    needClear = True


def minus():
    global memory
    memory = textField.get()
    global operation
    operation = "minus"
    global needClear
    needClear = True


def times():
    global memory
    memory = textField.get()
    global operation
    operation = "times"
    global needClear
    needClear = True


def divide():
    global memory
    memory = textField.get()
    global operation
    operation = "divide"
    global needClear
    needClear = True


def equal():
    if operation == "add":
        secondNum = textField.get()
        textField.delete(0, END)
        textField.insert(0, float(memory) + float(secondNum))
    elif operation == "minus":
        secondNum = textField.get()
        textField.delete(0, END)
        textField.insert(0, float(memory) - float(secondNum))
    elif operation == "times":
        secondNum = textField.get()
        textField.delete(0, END)
        textField.insert(0, float(memory) * float(secondNum))
    elif operation == "divide":
        secondNum = textField.get()
        textField.delete(0, END)
        textField.insert(0, float(memory) / float(secondNum))


needClear = True
operation = ""
memory = ""

root = Tk()
root.title("calculator app")

textField = Entry(root, borderwidth=5, width=35)
textField.insert(0, "0")
textField.pack()

buttonsPanel = LabelFrame(root, padx=10, pady=10, text="Calculator ^_^")
buttonsPanel.pack()
btn_1 = Button(buttonsPanel, text="1", width=6, height=3, command=lambda: clicked(1))
btn_2 = Button(buttonsPanel, text="2", width=6, height=3, command=lambda: clicked(2))
btn_3 = Button(buttonsPanel, text="3", width=6, height=3, command=lambda: clicked(3))
btn_4 = Button(buttonsPanel, text="4", width=6, height=3, command=lambda: clicked(4))
btn_5 = Button(buttonsPanel, text="5", width=6, height=3, command=lambda: clicked(5))
btn_6 = Button(buttonsPanel, text="6", width=6, height=3, command=lambda: clicked(6))
btn_7 = Button(buttonsPanel, text="7", width=6, height=3, command=lambda: clicked(7))
btn_8 = Button(buttonsPanel, text="8", width=6, height=3, command=lambda: clicked(8))
btn_9 = Button(buttonsPanel, text="9", width=6, height=3, command=lambda: clicked(9))
btn_0 = Button(buttonsPanel, text="0", width=6, height=3, command=lambda: clicked(0))

cBtn = Button(buttonsPanel, text="C", width=6, height=3, command=c)
ceBtn = Button(buttonsPanel, text="CE", width=6, height=3, command=ce)
addBtn = Button(buttonsPanel, text="+", width=6, height=3, command=add)
minusBtn = Button(buttonsPanel, text="-", width=6, height=3, command=minus)
timesBtn = Button(buttonsPanel, text="x", width=6, height=3, command=times)
divideBtn = Button(buttonsPanel, text="÷", width=6, height=3, command=divide)
equalBtn = Button(buttonsPanel, text="=", width=6, height=3, command=equal)
negativeBtn = Button(buttonsPanel, text="+/-", width=6, height=3, command=negative)
smallBtn = Button(buttonsPanel, text=".", width=6, height=3, command=dot)
backspaceBtn = Button(buttonsPanel, text="<-", width=6, height=3, command=backspace)

ceBtn.grid(row=0, column=0)
cBtn.grid(row=0, column=1)
backspaceBtn.grid(row=0, column=2)
divideBtn.grid(row=0, column=3)

btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
timesBtn.grid(row=1, column=3)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
minusBtn.grid(row=2, column=3)

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
addBtn.grid(row=3, column=3)

negativeBtn.grid(row=4, column=0)
btn_0.grid(row=4, column=1)
smallBtn.grid(row=4, column=2)
equalBtn.grid(row=4, column=3)

root.mainloop()
