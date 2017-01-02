from tkinter import *
from tkinter import messagebox
window=Tk()
window.title('This is a title')
window.geometry('500x500+500+500')

def one():
    b=a.get()
    if b == 'Thomas':
         labela=Label(text='Welcome back Admin').pack()
    else:
         labelb=Label(text='Welcome back '+b).pack()
def two():
    messagebox.showinfo(title='Save',message='File has been saved')

def three():
    mes=messagebox.askyesno(title='Quit',message='Are you sure you want to quit')
    if mes == 1:
        window.destroy()

a=StringVar()
label1=Label(text='This is a label').pack()
button1=Button(text='This is a button',command=one).pack()
text=Entry(textvariable=a).pack()


menu1=Menu()
list1=Menu()
list2=Menu()

menu1.add_cascade(label='File',menu=list1)
menu1.add_cascade(label='Edit',menu=list2)

list1.add_command(label='Save File',command=two)
list1.add_command(label='Quit',command=three)

list1.add_checkbutton(label='Safe Mode')

list2.add_command(label='Undo')
list2.add_command(label='Redo')

window.config(menu=menu1)





window.mainloop()   