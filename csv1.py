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


readers = csv.reader(open("rhea.csv",'r'))
for emp_id,name,City  in readers:
    sql="insert into emp values (%d,'%s','%s')"%(int(emp_id),name,City)
    cursor.execute(sql)
    
    
db.commit()

db.close()
