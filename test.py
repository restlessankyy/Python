def create():
import MySQLdb
HOST='127.0.0.1'
USER='root'
PASSWORD='root'
DATABASE='mysql'
db = MySQLdb.connect(HOST,USER,PASSWORD,DATABASE)
cursor = db.cursor()
sql="create table Google (emp_id int(5),name varchar(25),City varchar(25))"
cursor.execute(sql)


db.close()

