import mysql.connector as connection

mydb = connection.connect(host="localhost", user="root", passwd="root", use_pure=True)

cursor=mydb.cursor()
cursor.execute("insert into laxman.seno values (1, 'ravi' ,350000,6)")
mydb.commit()     # commit makes all inserting values are saving in database
cursor.execute("select * from laxman.seno")
for i in cursor.fetchall():
    print(i)