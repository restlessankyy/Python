import MySQLdb
HOST='127.0.0.0.1'
USER='root'
PASSWORD='root'
DATABASE='mysql'
db = MySQLdb.connect(HOST,USER,PASSWORD,DATABASE)
cursor = db.cursor()
sql = "select * from emp"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
     print "\t Emp id   : ", row[0]
     print "\t Emp name : ", row[1]
     print "\t City     : ", row[2]
db.close()

