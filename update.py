import MySQLdb
HOST='localhost'
USER='root'
PASSWORD='root'
DATABASE='mysql'
db = MySQLdb.connect(HOST,USER,PASSWORD,DATABASE)
cursor = db.cursor()
sql="update emp set emp = 154, name = 'Ankit' where City = 'UK'"

cursor.execute(sql)
db.commit()

db.close()

