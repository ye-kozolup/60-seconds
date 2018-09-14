from tkinter import *
import random
import threading

res=0

def pos_oval():
    global pos2_1, pos2_2, oval_x1, oval_x2, oval_y1, oval_y2
    pos2_1=random.randint(0, 9)
    pos2_2=random.randint(0, 9)
    oval_x1=8+30*pos2_1
    oval_y1=8+30*pos2_2
    oval_x2=oval_x1+14
    oval_y2=oval_y1+14

def check():
    if pos1_1==pos2_1 and pos1_2==pos2_2:
        global res
        res=res+1
        pos_oval()
        canv.coords(oval,oval_x1,oval_y1,oval_x2,oval_y2)

def finish():
    global win1
    r=res
    win1=Tk()
    win1.title("Результат")
    win1.geometry("250x60+500+320")
    win1.resizable(False, False)
    Label(win1, text="Ваш результат: "+str(r), font="Times 13").place(x=60, y=17)
    win1.focus_force()
    canv.delete(rec)
    canv.delete(oval)
    win1.mainloop()
    win.destroy()
    win.quit()
    
def start(event):
    win2.destroy()
    win2.quit()

    global pos1_1, pos1_2, rec_x1, rec_y1, rec_x2, rec_y2, canv, oval, rec, win
    win=Tk()
    win.title("60 секунд")
    win["bg"]="light green"
    win.geometry("300x300+470+190")
    win.resizable(False, False)

    canv=Canvas(win, width=302, height=302)
    canv.place(x=-2, y=-2)
    x1=30
    y1_1=0
    y1_2=300
    for i in range(9):
        canv.create_line([x1, y1_1],[x1, y1_2])
        x1=x1+30
    y2=30
    x1_1=0
    x1_2=300
    for i in range(9):
        canv.create_line([x1_1, y2],[x1_2, y2])
        y2=y2+30
    
    pos_oval()
    oval=canv.create_oval([oval_x1, oval_y1],[oval_x2, oval_y2], fill="red")
    pos1_1=random.randint(0, 9)
    pos1_2=random.randint(0, 9)
    rec_x1=5+30*pos1_1
    rec_y1=5+30*pos1_2
    rec_x2=rec_x1+20
    rec_y2=rec_y1+20
    win.focus_force()
    rec=canv.create_rectangle([rec_x1, rec_y1],[rec_x2, rec_y2], fill="blue")
    t = threading.Timer(62.0, finish)
    t.start()
    
    win.bind("<KeyPress-Up>", up)
    win.bind("<KeyPress-Down>", down)
    win.bind("<KeyPress-Right>", right)
    win.bind("<KeyPress-Left>", left)
    
    win.mainloop()
        

def up(event):
    global pos1_2
    pos1_2=pos1_2-1
    if pos1_2==-1:
        canv.move(rec, 0, 270)
        pos1_2=9
    else:
        canv.move(rec, 0, -30)
    check()
def down(event):
    global pos1_2
    pos1_2=pos1_2+1
    if pos1_2==10:
        canv.move(rec, 0, -270)
        pos1_2=0
    else:
        canv.move(rec, 0, 30)
    check()
def right(event):
    global pos1_1
    pos1_1=pos1_1+1
    if pos1_1==10:
        canv.move(rec, -270, 0)
        pos1_1=0
    else:
        canv.move(rec, 30, 0)
    check()
def left(event):
    global pos1_1
    pos1_1=pos1_1-1
    if pos1_1==-1:
        canv.move(rec, 270, 0)
        pos1_1=9
    else:
        canv.move(rec, -30, 0)
    check()
    
win2=Tk()
win2.title("Стартове вікно")
win2.geometry("200x110+550+330")
win2.resizable(False, False)
Label(win2, text="Для того, щоб розпочати \n натисніть Enter", font="Times 12").place(x=16, y=30)
win2.bind("<KeyPress>", start)
win2.mainloop()