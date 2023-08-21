import mysql.connector
from datetime import date


def clear():
  for _ in range(65):
     print()

def room_booking():
  conn = mysql.connector.connect(host='localhost', database='hotel', user='root', password='yash',autocommit=True)
  cursor = conn.cursor()
  stmt='CREATE TABLE IF NOT EXISTS `customer` (`id` int(20) NOT NULL AUTO_INCREMENT Primary key,Name varchar(50) DEFAULT NULL,Address varchar(50) DEFAULT NULL,Phone int(10) DEFAULT NULL, Email varchar(80) DEFAULT NULL, Id_proof varchar(20) DEFAULT NULL, Id_proof_no varchar(25) DEFAULT NULL,Males int(2) DEFAULT NULL,Females int(2) DEFAULT NULL ,Children int(2) DEFAULT NULL,Date_of_Entry Date,Date_of_Exit Date)'
  cursor.execute(stmt)
  clear()
  print('Add New Customer - Screen')
  name = input('\n Enter Customer Name :')
  address = input('\n Enter Customer Address:')
  phone = input('\n Enter Customer Phone NO :')
  email = input('\n Enter Customer Email ID :')
  id_proof = input('\n Enter Customer ID(Aadhar/Passport/DL/VoterID)  :')
  id_proof_no = input('\n Enter Customer ID proof NO :')
  males = input('\n Enter Total Males :')
  females = input('\n Enter Total Females :')
  children = input('\n Enter Total Childeren :')
  dateentry=input('\nEnter Date of Entry(yyyy-mm-dd):')
  
  

  sql = 'insert into customer(name,address,phone,email,id_proof,id_proof_no,males,females,children) values \
        ("'+name+'","' + address.upper()+'","'+phone+'","'+email.upper()+'","'+id_proof.upper()+'","'+id_proof_no.upper()+'",'+males+','+females+','+children+');'

  cursor.execute(sql)
  print('\n\n\nCustomer Added success fully ...............')
  conn.close()
  wait = input('\n\n\n Press any key to continue....')

    cursor = conn.cursor()
    room_id =input('Enter room no to book :')
    cust_id = input('Enter customer ID :')
    date_of_occ = input('Enter date of occupancy (yyyy-mm-dd) :')
    advance = input('Enter advance amount :')
    sql1 = 'update rooms set status = "occupied" where id ='+room_id +';'
    sql2 = 'insert into booking(room_id,cust_id,doo,advance) values ('+room_id+','+cust_id+',"'+date_of_occ+'",'+advance+');'
    #print(sql2)
    #print(sql1)
    result = room_exist(room_id)
    result1 = customer_exist(cust_id)

    if result[5]=='free' and result1 is not None: 
      cursor.execute(sql1)
      cursor.execute(sql2)
      print('\n\n\nRoom no ', room_id, 'booked for', cust_id)
    
    if result[5] !='free':
       print('\n Room is not available for booking. Right now it is :',result[5])
    if result1 is None:
       print('Customer does not exist....Please add customer first in our database')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

