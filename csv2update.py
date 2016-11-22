import MySQLdb
import csv
HOST='127.0.0.1'
USER='root'
PASSWORD='root'
DATABASE='mysql'
db = MySQLdb.connect(HOST,USER,PASSWORD,DATABASE)
cursor = db.cursor()
#sql="insert into emp values(14, 'Ankit','India')"

#cursor.execute(sql)

with open('names.csv','w') as csvfile:
    fieldnames = ['name','age']
    writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({'name' :'Rhea','age' : 23})
    writer.writerow({'name': 'Ankit','age' : 23})

#readers = csv.reader(open("rhea.csv",'r'))
#for emp_id,name,City  in readers:
    #sql="insert into emp values (%d,'%s','%s')"%(int(emp_id),name,City)
    #cursor.execute(sql)
    
    
db.commit()

db.close()
