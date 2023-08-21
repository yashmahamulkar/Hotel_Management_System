import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', password='yash',autocommit=True)
#cursor=conn.cursor()
cursor = conn.cursor()
##cursor.execute('Create Database IF NOT EXISTS Booking')
cursor.execute('Use Booking')
##cursor.execute('Create Table IF NOT EXISTS Roomstatus(Room_No int NOT NULL,Room_Type varchar(15),Room_Status varchar(15),Primary key(Room_No))')
##arg='insert into roomstatus(Room_No,Room_Type,Room_Status) values(%s,%s,%s)'
##para=[[1,'Delux','Vacant'],[2,'Delux','Vacant'],[3,'Delux','Vacant'],[4,'Delux','Vacant'],[5,'Delux','Vacant'],[6,'SuperDelux','Vacant'],[7,'SuperDelux','Vacant'],[8,'SuperDelux','Vacant'],[9,'SuperDelux','Vacant'],[10,'SuperDelux','Vacant'],[11,'King Special','Vacant'],[12,'King Special','Vacant'],[13,'King Special','Vacant'],[14,'King Special','Vacant'],[15,'King Special','Vacant']]
##cursor.executemany(arg,para)
##x='select * from room '
##cursor.execute(x)
##r=cursor.fetchall()
##for i in r:
##        print(i)
##
##
##no=int(input("Enter Room No. to book:"))
##m='UPDATE Roomstatus set Room_Status="Occupied" where room_no=%s'
##
##try:
##        cursor.execute(m,(no,))    
##
##except EOFError:
##        print()

cnx={}


cursor.execute('Select * from food')
f=cursor.fetchall()
#f=list(f.values())
print(f)
s=int(input("Enter Item No."))-1

x=list(f[s])
print(x)
sums=x[2]
print(sums)
#for i in range (len(f[s].values())):
#        print(i[)


