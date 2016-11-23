from Tkinter import *
from tkMessageBox import *

def changeLabel():
    pass
def hasClicked():
   pass
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


#CreateInput
custName = StringVar()
yourName = Entry(window1,textvariable=custName)
yourName.pack()

#CreateRadio Option
relStatus= StringVar()
relStatus.set(None)
radio1=Radiobutton(window1, text="Single",value="Single",variable=relStatus, command=hasClicked)
radio2=Radiobutton(window1, text="Married",value="Married",variable=relStatus, command=hasClicked)
radio1.pack()
radio2.pack()



#createButton
button1=Button(window1,text="Click Here",width=20,command=changeLabel)
button1.pack(side="bottom")
window1.mainloop()
