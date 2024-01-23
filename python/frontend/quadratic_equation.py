from tkinter import *
import math
from tkmacosx import Button


def calc():
    a=entr0.get()
    b=entr1.get()
    c=entr2.get()
    check='qwertyuiopasdfghjklzxcvbnm0,./;"''\][]'
    if a in check:
        entr0.configure(bg="red")
    elif a not in check:
        a=int(a)
        entr0.configure(bg="lightblue")
        if b in check:
           entr1.configure(bg="red")
        elif b not in check:
            b=int(b)
            entr1.configure(bg="lightblue")
            if c in check:
                entr2.configure(bg="red")
            elif c not in check:
                c=int(c)
                entr2.configure(bg="lightblue")
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        x1 = (-b + math.sqrt(disc)) / (2 * a)
        x1 = round(x1, 2)
        x2 = (-b - math.sqrt(disc)) / (2 * a)
        x2 = round(x2, 2)
        lbl2.configure(text=f'D={disc}\nx1={x1}\nx2={x2}', font="Arial 10")
    elif disc == 0:
        x = -b / (2 * a)
        x = round(x, 2)
        lbl2.configure(text=f'D={disc}\nx1={x}', font="Arial 10")
    else:
        lbl2.configure(text=f'D={disc}\nNo square roots', font="Arial 10")

    


root=Tk()
root.title("Quadratic equation")
root.geometry("600x120+700+500")
root.resizable(width=False, height=False)

lbl2=Label(
    root,
    text="Решение",
    font="Arial 20",
    foreground="black",
    background="yellow",
    width=25  
)


lbl=Label(
    root,
    text="Решение квадратного уравнения",
    font="Arial 20",
    foreground="green",
    background="lightblue"    
)

entr0 = Entry(
    root,
    font="Arial 20",
    foreground="green",
    background="lightblue",
    width=3,
)

msg = Message(
    root,
    text="x**2+",
    font="Arial 20",
    foreground="Green"
)

entr1 = Entry(
    root,
    font="Arial 20",
    foreground="green",
    background="lightblue",
    width=3,
)

msg1 = Message(
    root,
    text="x+",
    font="Arial 20",
    foreground="Green"
)

entr2 = Entry(
    root,
    font="Arial 20",
    foreground="green",
    background="lightblue",
    width=3,
)

msg2 = Message(
    root,
    text="=0",
    font="Arial 20",
    foreground="Green"
)

btn = Button(
    root,
    text="Решить",
    bg='green',
    fg='black',
    borderless=1,
    command=calc
)
lbl2.pack(side=BOTTOM)
lbl.pack()
entr0.pack(side=LEFT)
msg.pack(side=LEFT)
entr1.pack(side=LEFT)
msg1.pack(side=LEFT)
entr2.pack(side=LEFT)
msg2.pack(side=LEFT)
btn.pack(side=LEFT)

root.mainloop()