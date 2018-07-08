# GUI
from tkinter import *

# create the window
root = Tk()

root.title("#")
root.geometry("200x200")

var = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()
var9 = StringVar()
# l = Label(root, textvariable=var, bg='white', font=('Arial', 12), width=5, height=2)
# l = Label(root, text='OMG! this is TK!', bg='green', font=('Arial', 12), width=15, height=2)
# l.pack()


on_hit = 0
on_hit2 = 0
on_hit3 = 0
on_hit4 = 0
on_hit5 = 0
on_hit6 = 0
on_hit7 = 0
on_hit8 = 0
on_hit9 = 0
def hit_me():
    global on_hit

    if on_hit == 0:
        on_hit = 1
        var.set('x')
    elif on_hit == 1:
        on_hit = 2
        var.set('o')
    else:
        on_hit = 0
        var.set(' ')


def hit_me2():
    global on_hit2

    if on_hit2 == 0:
        on_hit2 = 1
        var2.set('x')
    elif on_hit2 == 1:
        on_hit2 = 2
        var2.set('o')
    else:
        on_hit2 = 0
        var2.set(' ')


def hit_me3():
    global on_hit3

    if on_hit3 == 0:
        on_hit3 = 1
        var3.set('x')
    elif on_hit3 == 1:
        on_hit3 = 2
        var3.set('o')
    else:
        on_hit3 = 0
        var3.set(' ')


def hit_me4():
    global on_hit4

    if on_hit4 == 0:
        on_hit4 = 1
        var4.set('x')
    elif on_hit4 == 1:
        on_hit4 = 2
        var4.set('o')
    else:
        on_hit4 = 0
        var4.set(' ')


def hit_me5():
    global on_hit5

    if on_hit5 == 0:
        on_hit5 = 1
        var5.set('x')
    elif on_hit5 == 1:
        on_hit5 = 2
        var5.set('o')
    else:
        on_hit5 = 0
        var5.set(' ')


def hit_me6():
    global on_hit6

    if on_hit6 == 0:
        on_hit6 = 1
        var6.set('x')
    elif on_hit6 == 1:
        on_hit6 = 2
        var6.set('o')
    else:
        on_hit6 = 0
        var6.set(' ')


def hit_me7():
    global on_hit7

    if on_hit7 == 0:
        on_hit7 = 1
        var7.set('x')
    elif on_hit7 == 1:
        on_hit7 = 2
        var7.set('o')
    else:
        on_hit7 = 0
        var7.set(' ')


def hit_me8():
    global on_hit8

    if on_hit8 == 0:
        on_hit8 = 1
        var8.set('x')
    elif on_hit8 == 1:
        on_hit8 = 2
        var8.set('o')
    else:
        on_hit8 = 0
        var8.set(' ')


def hit_me9():
    global on_hit9

    if on_hit9 == 0:
        on_hit9 = 1
        var9.set('x')
    elif on_hit9 == 1:
        on_hit9 = 2
        var9.set('o')
    else:
        on_hit9 = 0
        var9.set(' ')


b = Button(root, textvariable=var, width=2, font=('Arial', 22), height=1, command=hit_me)
b.place(bordermode=OUTSIDE, height=65, width=65, anchor=NW, x=1, y=1)

b2 = Button(root, textvariable=var2, width=2, font=('Arial', 22), height=1, command=hit_me2)
b2.place(bordermode=OUTSIDE, height=65, width=65, anchor=NW, x=68, y=1)

b3 = Button(root, textvariable=var3, width=2, font=('Arial', 22), height=1, command=hit_me3)
b3.place(bordermode=OUTSIDE, height=65, width=65, anchor=NW, x=135, y=1)

b4 = Button(root, textvariable=var4, width=2, font=('Arial', 22), height=1, command=hit_me4)
b4.place(bordermode=OUTSIDE, height=65, width=65, anchor=NW, x=1, y=68)

b5 = Button(root, textvariable=var5, width=2, font=('Arial', 22), height=1, command=hit_me5)
b5.place(bordermode=OUTSIDE, height=65, width=65, anchor=NW, x=68, y=68)

b6 = Button(root, textvariable=var6, width=2, font=('Arial', 22), height=1, command=hit_me6)
b6.place(bordermode=OUTSIDE, height=65, width=65, anchor=NW, x=135, y=68)

b7 = Button(root, textvariable=var7, width=2, font=('Arial', 22), height=1, command=hit_me7)
b7.place(bordermode=OUTSIDE, height=65, width=65, anchor=NW, x=1, y=135)

b8 = Button(root, textvariable=var8, width=2, font=('Arial', 22), height=1, command=hit_me8)
b8.place(bordermode=OUTSIDE, height=65, width=65, anchor=NW, x=68, y=135)

b9 = Button(root, textvariable=var9, width=2, font=('Arial', 22), height=1, command=hit_me9)
b9.place(bordermode=OUTSIDE, height=65, width=65, anchor=NW, x=135, y=135)

# kick off the event loop
root.mainloop()


