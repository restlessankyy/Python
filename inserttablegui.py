from Tkinter import *
import MySQLdb

def submit():
      db=MySQLdb.connect("127.0.0.1","root","root","mysql")
      cursor=db.cursor()
      sql="insert into emp(id,name,City) values("
      en1=entry1.get()
      en2=entry2.get()
      en3=entry3.get()
      sql=sql+en1+",'"
      sql=sql+en2+"','"
      sql=sql+en3+"')"
      print sql
      cursor.execute(sql)
      db.commit()
      db.close
def quit1():
    window1.destroy()


window1=Tk()
window1.title("Database")

window1.geometry("500x250+50+0")
label1=Label(window1,text="Id").grid(row=0,column=0)
label2=Label(window1,text="Name").grid(row=1,column=0)
label3=Label(window1,text="City").grid(row=2,column=0)
entry1=Entry(window1)
entry1.grid(row=0,column=1)
entry2=Entry(window1)
entry2.grid(row=1,column=1)
entry3=Entry(window1)
entry3.grid(row=2,column=1)

button1=Button(window1,text="Submit",command=submit).grid(row=5,column=0)
button1=Button(window1,text="Exit",command=quit1).grid(row=5,column=1)
window1.mainloop()



##email="sourav@gmail.com"
#is_valid=validate_email(email,verify=True)
#print is_valid
#print "sdfs"
