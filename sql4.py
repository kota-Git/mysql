import mysql.connector as connection
mydb = connection.connect(host="localhost", user="root", passwd="root", use_pure=True)

    # Check if the connection is successful
print(mydb.is_connected())

cursor=mydb.cursor()
#cursor.execute("create database senobank")         # database created onetime only otherwise getting error
#cursor.execute("show databases")
cursor.execute("use senobank")
#print(cursor.fetchall())
cursor.execute("create table if not exists Bank_details ( age  int(10), job   varchar(30),marital  varchar(30),education  varchar(30),`default`  varchar(30),balance  int(30),housing  varchar(30),loan   varchar(30),contact  varchar(30),`day`   int(10),`month`  varchar(30),duration   int(10),campaign  int(10),pdays  int(10),previous int(10),poutcome  varchar(30),y  varchar(30))")
#print(cursor.fetchall())
cursor.execute("select * from Bank_details")
for i in cursor.fetchall():
    print(i)