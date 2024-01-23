from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkmacosx import Button
from operator import itemgetter
import random
import openpyxl
from colorama import *

book = openpyxl.load_workbook("/Users/my_pc/Library/Mobile Documents/com~apple~CloudDocs/iCloud Drive/work/programming/github/python/frontend/final/data.xlsx")

sheets=book.worksheets
sheet = book.worksheets[0]
sheet_2=book.worksheets[1]
sheet_3=book.worksheets[2] 


global names
global points
global ac
global questions
global index
global answers


def close():
    if messagebox.askokcancel("Exit", "Do you want quit?"):
        book = openpyxl.load_workbook("/Users/my_pc/Library/Mobile Documents/com~apple~CloudDocs/iCloud Drive/work/programming/github/python/frontend/final/data.xlsx")
        sheets=book.worksheets
        sheet = book.worksheets[0]
        sheet_2=book.worksheets[1]
        sheet_3=book.worksheets[2] 
        for i in range(len(points)):
            if points[i]<5:
                results_lost[names[i]]=points[i]
            elif points[i]>=4:
                results_wins[names[i]]=points[i]
        sorted_results_lost=dict(sorted(results_lost.items(), key=itemgetter(1)))
        sorted_results_wins=dict(sorted(results_wins.items(), key=itemgetter(1)))
        row=1
        row2=1
        for ai in sorted_results_lost:
            sheet_3[row][0].value=ai
            row+=1
        for aiq in sorted_results_wins:
            sheet_2[row2][0].value=aiq
            row2+=1
        print(Fore.RED+f"Losers are: {sorted_results_lost}")
        Style.RESET_ALL
        print(Fore.CYAN+f"Winners are: {sorted_results_wins}")
        Style.RESET_ALL
        book.save("/Users/my_pc/Library/Mobile Documents/com~apple~CloudDocs/iCloud Drive/work/programming/github/python/frontend/final/data.xlsx")
        book.close
        root.destroy()


def close2(exit_window):
    if messagebox.askokcancel("Exit", "Do you want finish exam?"):
        lbl["text"]="Please, enter your name"
        lbl["foreground"]="grey"
        exit_window.destroy()



def start():
    a = "Please, enter the name and press OK to start"
    abq='+-/*!&$#?=@<>123456789'
    abc="Name must contain ONLY letters"
    abcd="Field can't be empty"
    abcde="Please, enter your name"
    c = lbl.cget("text")
    ca=entr.get()
    if c not in a and c not in abq and c not in abc and c not in abcd and c not in abcde:
        names.append(ca)
        entr.delete(0, 'end')
        def send():
            a = entr_answ.get() 
            if len(points_inside)==5:
                if a != answers2[index_list[0]]:
                    points_inside.append(0)
                    abca=sum(points_inside)
                    points.append(abca)
                    lbl["text"]="Please, enter your name"
                    lbl["foreground"]="grey"
                    new_window.destroy()
                elif a == answers2[index_list[0]]:
                    points_inside.append(1)
                    abca=sum(points_inside)
                    points.append(abca)
                    new_window.destroy()
            elif a != answers2[index_list[0]]:
                points_inside.append(0)
            elif a == answers2[index_list[0]]:
                points_inside.append(1)
            questions2.pop(index_list[0])
            answers2.pop(index_list[0])
            ab = random.randint(0, len(questions2)-1)
            index_list.pop(0)
            index_list.append(ab)
            lbl2["text"]= names[index] + ", could you say " + " " + questions2[index_list[0]]
            entr_answ.delete(0, END)
        new_window=Toplevel()
        new_window.title("EXAM")
        new_window.geometry("600x200+700+400")
        new_window.protocol("WM_DELETE_WINDOW", lambda exit_window=new_window: close2(exit_window))
        new_window.resizable(width=False, height=False)
        lbl["text"] = ""
        btn_send=Button(new_window, font="Arial 20", text="SEND", foreground="white", background="grey", width=300, command=send)
        btn_send.place(x=150, y=165)
        entr_answ=Entry(new_window, font="Arial 20", foreground="white", background="grey", justify=CENTER, width=30)
        entr_answ.place(x=110, y=110)
        lbl2=Label(new_window, text="", foreground="green", font="Arial 15")
        lbl2.place(x=105, y=80)
        img3 = Image.open("/Users/my_pc/Library/Mobile Documents/com~apple~CloudDocs/iCloud Drive/work/programming/github/python/frontend/final/1.png")
        img3 = img3.resize((170, 90), Image.LANCZOS)
        img3 = ImageTk.PhotoImage(img3)
        img3_label=Label(new_window, image=img3)
        img3_label.image=img3
        img3_label.place(x=210, y=-15)
        questions2=questions.copy()
        answers2=answers.copy()
        points_inside=[0]
        aqa=random.randint(0, len(questions2)-1)
        index_list=[aqa]
        lbl2["text"]= names[index] + ", could you say " + " " + questions2[index_list[0]]
        new_window.mainloop()
    else:
        lbl["text"] = "Please, enter the name and press OK to start"
        lbl["foreground"] = 'red'


def entr_name():
    a=""
    get = entr.get()
    if get.isalpha():
        a = "Welcome "
        lbl["foreground"] = 'green'
        lbl["text"] = a + get
    elif get == a:
        lbl["text"] = "Field can't be empty"
        lbl["foreground"] = 'red'
        entr.delete(0, 'end')
    else:
        lbl["text"] = "Name must contain ONLY letters"
        lbl["foreground"] = 'red'
        entr.delete(0, 'end')


root=Tk()

root.protocol("WM_DELETE_WINDOW", close)
root.title("SOFTWARE DEVELOPER EXAM")
root.geometry("600x200+700+400")
root.resizable(width=False, height=False)
img = Image.open("/Users/my_pc/Library/Mobile Documents/com~apple~CloudDocs/iCloud Drive/work/programming/github/python/frontend/final/clipart4343754.png")
img = img.resize((100, 100), Image.LANCZOS)
img = ImageTk.PhotoImage(img)
img_label=Label(image=img)
img_label.image=img
img_label.place(x=10, y=10)

img2 = Image.open("/Users/my_pc/Library/Mobile Documents/com~apple~CloudDocs/iCloud Drive/work/programming/github/python/frontend/final/pngwing.com (1).png")
img2 = img2.resize((100, 89), Image.LANCZOS)
img2 = ImageTk.PhotoImage(img2)
img2_label=Label(image=img2)
img2_label.image=img2
img2_label.place(x=490, y=10)




questions =[]
answers = []
names=[]
points=[]
results_wins={}
results_lost={}
index = len(names)-1
for row in range(1,10):
    ap=sheet[row][0].value
    questions.append(ap)

for row in range(1,10):
    ap=sheet[row][1].value
    ap=str(ap)
    answers.append(ap)



entr=Entry(
    root,
    font="Arial 20",
    foreground="white",
    background="grey",
    justify=CENTER,
    width=20
)
entr.place(x=175, y=100)


btn_ok=Button(
    root,
    text="OK",
    font="Arial 20",
    foreground="white",
    background="grey",
    width=300,
    command=entr_name,
)
btn_ok.place(x=150, y=165)

lbl=Label(
    root,
    text="Please, enter your name",
    font="Arial 20",
    foreground="grey",
    width=34 
)
lbl.place(x=95, y=130)

btn_start=Button(
    root,
    text="START",
    font="Arial 20",
    foreground="white",
    background="grey",
    command=start
)
btn_start.place(x=470, y=165)


book.save("/Users/my_pc/Library/Mobile Documents/com~apple~CloudDocs/iCloud Drive/work/programming/github/python/frontend/final/data.xlsx")
book.close
root.mainloop()