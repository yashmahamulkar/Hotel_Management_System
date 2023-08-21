import mysql.connector
conn2=mysql.connector.connect(host='localhost', user='root', password='yash',autocommit=True)
cursor=conn2.cursor()

cursor.execute('use booking')
cursor.execute('Drop table IF EXISTS Food')
cursor.execute('Create Table Food (Item_No int NOT NULL, Food_Item varchar(15),Food_cost int)')
arg='insert into Food (Item_No,Food_Item,Food_cost) values(%s,%s,%s)'
para=[[1,'Dal fry',100],[2,'steam rice',90],[3,'chapati',100],[4,'biryani',120],[5,'pao bhaji',130],[6,'gulab jamun',95]]
cursor.executemany(arg,(para))

x='select * from Food'
cursor.execute(x)
r=cursor.fetchall()
for i in r:
        print(i)
