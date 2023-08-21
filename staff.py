import mysql.connector
cors = mysql.connector.connect(host='localhost', user='root', password='yash',autocommit=True)
cursor=cors.cursor()
cursor.execute('Create Database IF NOT EXISTS Staff ')
cors.close()
conn0=mysql.connector.connect(host='localhost', user='root',database='Staff', password='yash',autocommit=True)
cursor=conn0.cursor()
cursor.execute('Use Staff')
cursor.execute('Create Table IF NOT EXISTS Staff(Employee_Number int NOT NULL ,Name varchar(100),Designation varchar(100),Primary key(Employee_Number))')
arg1='insert IGNORE into Staff (Employee_Number,Name,Designation)values(%s,%s,%s)'
datg=[[1,'Sheetal','Receptionist'],[2,'Raman','Day Security'],[3,'Ashish','Night Security'],[4,'Ramu','Home Services'],[5,'Shyam','Home Services'],[6,'Himesh','Home Services'],[7,'Sunny','Home Services'],[8,'Salma','Parking Incharge'],[9,'Seeta','Records Incharge']]
cursor.executemany(arg1,datg)
print('+--------------------------------------------------------+')
print('|Employee_Number   |Name         |Designation            |')
print('+--------------------------------------------------------+')

sql2='select * from staff'
cursor.execute(sql2)
rec=cursor.fetchall()
for i in rec :
        print('|',i[0],' '*(15-(len(str(i[0])))),'|',i[1],' '*(10-(len(str(i[1])))),'|',i[2],' '*(20-(len(str(i[2])))),'|')	
print('+--------------------------------------------------------+')
conn0.close()
