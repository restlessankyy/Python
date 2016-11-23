from Tkinter import *
import tkMessageBox
def submit():
   print"You First Name is %s"%(entry1.get())
def quit1():
    window1.destroy()
def error1():
    tkMessageBox.showerror(title="GUIError",message="No Such Entry")
window1 = Tk()
window1.title("First GUI APP")
window1.geometry("500x500")
#window1.geometry("500x400+100+100")
label1=Label(window1,text="FName").grid(row=0,column=0)
label2=Label(window1,text="LName").grid(row=1,column=0)

entry1=Entry(window1)
entry2=Entry(window1)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

button1=Button(window1,text="Submit",command=submit).grid(row=5,column=0)

button2=Button(window1,text="EXIT",command=quit1).grid(row=5,column=1)

button3=Button(window1,text="Error",command=error1).grid(row=10,column=1)

window1.mainloop()
