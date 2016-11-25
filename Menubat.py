from Tkinter import *
import tkMessageBox

def close():
    window1.destroy()
window1 = Tk()
window1.title="Example for Menu"
window1.geometry("450x450")

menubar=Menu(window1)
filemenu=Menu(menubar)
filemenu.add_command(label="New")
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As")
filemenu.add_command(label="Exit",command=close)

menubar.add_cascade(label="File",menu=filemenu)

helpmenu = Menu(menubar)
helpmenu.add_command(label="Help Docs")
helpmenu.add_command(label="About US")
helpmenu.add_command(label="Info")

menubar.add_cascade(label="Help",menu=helpmenu)
window1.config(menu=menubar)
window1.mainloop()



