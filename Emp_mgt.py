from Tkinter import *
import tkMessageBox

def close():
    window1.destroy()

def insert():
    name="Thanks for the click" + yourName.get()
    labelText.set(name)
    msg="My Name is "+ yourName.get()
    yourName.delete(0,END)
    yourName.insert(0,msg)
 

def new():
    pass
     


def open1():
    pass
window1 = Tk()
window1.title="Example for Menu"
window1.geometry("450x450")

menubar=Menu(window1)
filemenu=Menu(menubar)
filemenu.add_command(label="New",command=new)
filemenu.add_command(label="Insert",command=insert)
filemenu.add_command(label="Open",command=open1)
filemenu.add_command(label="Exit",command=close)

menubar.add_cascade(label="File",menu=filemenu)

helpmenu = Menu(menubar)
helpmenu.add_command(label="Help Docs")
helpmenu.add_command(label="About US")
helpmenu.add_command(label="Info")

menubar.add_cascade(label="Help",menu=helpmenu)


custName = StringVar()
yourName = Entry(window1,textvariable=custName)
yourName.pack()
window1.config(menu=menubar)
window1.mainloop()



