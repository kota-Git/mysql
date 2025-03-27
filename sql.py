import mysql.connector as connection
mydb = connection.connect(host="localhost", user="root", passwd="root", use_pure=True)

    # Check if the connection is successful
print(mydb.is_connected())

cursor=mydb.cursor()
#cursor.execute("create database BCA_D")         # database created onetime only otherwise getting error
cursor.execute("show databases")
#cursor.execute("create table BCA_D.DS (student_id int(8),student_name varchar(20),course_fee int(10),duration_months int(2))")
print(cursor.fetchall())
#q1=cursor.execute("select * from BCA_D.DS")
#print(q1)


  