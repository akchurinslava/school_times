from tkinter import *
from tkinter import ttk
k=0
def clicker(event):
    global k
    k+=1
    lbl.configure(text=k)


def clicker1(event):
    global k
    if k > 0:
        k-=1
    lbl.configure(text=k)


def entry_to_label(event):
    text = ent.get()
    lbl.configure(text=text)
    ent.delete(0, END)


def choose():
    text = var.get()
    ent.insert(END, text)



def new_window(ind:int):
    def tab_choose(ind:int):
        newwindow.title(texts[ind])
    newwindow = Toplevel()
    tabs = ttk.Notebook(newwindow)
    texts=['First', 'Second', 'Third', 'Fourth']
    img=["123.gif", "123.gif", "123.gif", "123.gif"]
    tab=[]
    cann=[]
    for i in range(len(texts)):
        #windows
        tab.append('tab'+str(i))
        tab[i]=Frame(tabs)
        tabs.add(tab[i], text=texts[i])
        #inside windows
        tab[i].bind('<Button-1>', tab_choose(i))
        cann.append("cann"+str(i))
        cann[i]=Canvas(tab[i], height=200, width=200, bg="gold")
        img[i]=PhotoImage(file=img[i]).subsample(1, 1)
        cann[i].create_image(0, 0, image=img, ANCHOR=NW)
        cann[i].pack()
    tabs.grid(row=0, column=0)
    tabs.select(ind)
    newwindow.title(texts[ind])
    newwindow.mainloop()



root =Tk()

root.title('My first window')
root.geometry('600x200')
m = Menu(root)
root.config(menu=m)
m1 = Menu(m)
m.add_cascade(label='Tabs', menu=m1)
m1.add_command(label='1.Tab', accelerator='Command+A', command=lambda:new_window(0))
m1.add_command(label='2.Tab', accelerator='Command+A', command=lambda:new_window(1))
m1.add_command(label='3.Tab', accelerator='Command+A', command=lambda:new_window(2))
m1.add_command(label='4.Tab', accelerator='Command+A', command=lambda:new_window(3))


lbl = Label(root,
    text='...',
    font='Arial 20')

btn = Button(
    root,
    text='CLICK',
    font='Aril 20',
    foreground='blue',
    background='black',
    width=30,
    height=5,
    relief=GROOVE #SUNKEN, RAISED
)

ent=Entry(
    root,
    fg='blue',
    bg='black',
    width=30,
    justify=CENTER
)

var=IntVar() #StringVar

r1 = Radiobutton(
    root,
    text='First',
    width=20,
    font='Arial 20',
    variable=var,
    value=1,
    command=choose
)

r2 = Radiobutton(
    root,
    text='Second',
    width=20,
    font='Arial 20',
    variable=var,
    value=2,
    command=choose
)

btn.bind('<Button-1>', clicker)#lkm
btn.bind('<Button-2>', clicker1)#pkm
ent.bind('<Return>', entry_to_label)#enter
btn.pack()
lbl.pack()
ent.pack()
r1.pack(side=LEFT)
r2.pack(side=LEFT)
root.mainloop()