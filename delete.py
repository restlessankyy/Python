import MySQLdb
HOST='127.0.0.1'
USER='root'
PASSWORD='root'
DATABASE='mysql'
db = MySQLdb.connect(HOST,USER,PASSWORD,DATABASE)
cursor = db.cursor()
sql="Delete from emp where city = 'India'"

cursor.execute(sql)
db.commit()

db.close()

