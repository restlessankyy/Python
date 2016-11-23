from Tkinter import *
from tkMessageBox import *

window1 = Tk()
window1.title("GUI Example")
window1.geometry("450x300+200+200")

#CreateLabel
labelText=StringVar()
labelText.set("Click Button")
label1 = Label(window1, textvariable=labelText, height=4)
label1.pack()

#CreateCheckBox
checkBoxVal = IntVar()
checkBox1 = Checkbutton(window1,variable=checkBoxVal,text="Happy?!!!")
checkBox1.pack()

window1.mainloop()
