import mysql.connector as connection

mydb = connection.connect(host="localhost", user="root", passwd="root", use_pure=True)

cursor=mydb.cursor()
cursor.execute("select * from laxman1.seno")
for i in cursor.fetchall():
    print(i)


