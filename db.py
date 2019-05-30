#!/usr/bin/python
import pymysql
pymysql.install_as_MySQLdb() 

import MySQLdb
db = MySQLdb.connect(user="root",passwd="root",host="localhost",db="client")
cursor = db.cursor()

cursor.execute("select * from emp")

print(cursor.rowcount, "record inserted.")



data=cursor.fetchall()
for row in data :
    print (row)
db.close()