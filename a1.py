
from tkinter import *

def rect():
    can.delete('del')
    can.create_rectangle(100,100,200,200,tag='del',outline='#000000')

def oval():
    can.delete('del')
    can.create_oval(100,100,200,200,tag='del',outline='#000000')

def romb():
    can.delete('del')
    can.create_polygon(100,150,150,200,200,150,150,100,tag='del',outline='#000000',fill='#ffffff')

def word():
    can.delete('del')
    can.create_text(100,100, text='Май',tag='del', font='arial 14')
root=Tk()
root.title('15_8')
root.geometry('800x800+0+0')



var=IntVar()
frame1=Frame(root,width=100,heigh=100,bd=5)
can=Canvas(frame1,width=800, height=800,bg='#ffffff')
can.pack()

rbutton1=Radiobutton(root,text='Раз',
                     variable=var,value=1, command = rect)
rbutton2=Radiobutton(root,text='Два',
                     variable=var,value=2, command = oval)
rbutton3=Radiobutton(root,text='Три',
                     variable=var,value=3, command = romb)
rbutton4=Radiobutton(root,text='Четыре',
                     variable=var,value=4, command = word)

rbutton1.pack()
rbutton2.pack()
rbutton3.pack()
rbutton4.pack()
frame1.pack()
root.mainloop()

