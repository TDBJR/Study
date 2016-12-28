
from tkinter import *

window=Tk()
window.title('title')

def one():
    print(var1.get(),var2.get(),var3.get(),var4.get())

var1 = IntVar()
Checkbutton(window,text='checkbutton1',variable=var1).grid(row=0,sticky=W)
var2= IntVar()
Checkbutton(window,text='checkbutton2',variable=var2).grid(row=1,sticky=W)
var3 = IntVar()
Checkbutton(window,text='checkbutton3',variable=var3).grid(row=2,sticky=W)
var4 = IntVar()
Checkbutton(window,text='checkbutton4',variable=var4).grid(row=3,sticky=W)

Button(window,text='get values',command=one,width=25).grid(row=4,sticky=W)
Button(window,text='quit',command=window.destroy,width=25).grid(row=5,sticky=W)
window.mainloop