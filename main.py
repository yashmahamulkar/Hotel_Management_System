#Hotel Management System
#Made by-Yash Mahamulkar 12 S3 
#       -Yashil B Ayyar 
#       - Arun

import mysql.connector
from datetime import date
conn = mysql.connector.connect(host='localhost', user='root', password='yash',autocommit=True)
cursor=conn.cursor()
cursor.execute('Create Database IF NOT EXISTS Hotel')
cursor.execute('Use Hotel')
cursor.execute('Create Table IF NOT EXISTS Room(Room_No int NOT NULL  ,DateofEntry Date,Name varchar(25),PhoneNO bigint ,AddharNo int(10),Room_Type varchar(15),DateofEXIT Date,RoomExpenditure int(6),OtherExpenditure int(5),Primary key(Room_No))')
cursor.execute('Create Table IF NOT EXISTS temp(Room_No int NOT NULL  ,DateofEntry Date,Name varchar(25),PhoneNO bigint ,AddharNo int(10),Room_Type varchar(15),DateofEXIT Date,RoomExpenditure int(6),OtherExpenditure int(5))')

cursor.execute('Create Table IF NOT EXISTS Roomstatus(Room_No int NOT NULL,Room_Type varchar(15),Room_Status varchar(15),Primary key(Room_No))')
arg='insert IGNORE into roomstatus(Room_No,Room_Type,Room_Status) values(%s,%s,%s)'
para=[[1,'Delux','Vacant'],[2,'Delux','Vacant'],[3,'Delux','Vacant'],[4,'Delux','Vacant'],[5,'Delux','Vacant'],[6,'SuperDelux','Vacant'],[7,'SuperDelux','Vacant'],[8,'SuperDelux','Vacant'],[9,'SuperDelux','Vacant'],[10,'SuperDelux','Vacant'],[11,'King Special','Vacant'],[12,'King Special','Vacant'],[13,'King Special','Vacant'],[14,'King Special','Vacant'],[15,'King Special','Vacant']]
cursor.executemany(arg,para)
cursor.execute('Create Table IF NOT EXISTS Food (Item_No int NOT NULL, Food_Item varchar(15),Food_cost int,Primary key(Item_No))')
a='insert IGNORE into Food (Item_No,Food_Item,Food_cost) values(%s,%s,%s)'
para=[[1,'Dal fry',100],[2,'steam rice',90],[3,'chapati',100],[4,'biryani',120],[5,'pao bhaji',130],[6,'gulab jamun',95]]
cursor.executemany(a,(para))

val=[]
rno=0
def space():
    print('\n'*10)
def singleline():
    print('-'*124)
    
def line():
    print('='*120)

def booking():
    while True:
        ans=input("Want To Enter Record(y/n):")
        if ans.lower()=='y':
            rno=int(input("Enter Room Number to book :"))
            x='select Room_Status from roomstatus where Room_No=%s'
            cursor.execute(x,(rno,))
            z=cursor.fetchone()
            for i in z:
                if i=='Vacant':
                    name=input("Enter Name              :")
                    Dateed=int(input('Date of Entry (dd)      :'))
                    Dateem=int(input('Date of Entry (mm)      :'))
                    Dateey=int(input('Date of Entry (yyyy)    :'))
                    Addr=int(input("Enter AddharCard No.      :"))
                    Phone=int(input("Enter PhoneNo.           :"))
                    Dateexd=int(input('Date of Exit (dd)      :'))
                    Dateexm=int(input('Date of Exit (mm)      :'))
                    Dateexy=int(input('Date of Exit(yyyy)     :'))
                    Roomtype=''
                    RoomEx=0
                    sql='select room_type from roomstatus where room_no=%s'
                    cursor.execute(sql,(rno,))
                    x=cursor.fetchone()
                             
                    for i in range(len(x)):
                        print(x[i])
                        
                        if x[i]=="Delux":
                            Roomtype='Dulex'
                            RoomEx=5000
                        elif x[i]=="SuperDelux":
                            Roomtype="SuperDelux"
                            RoomEx=7000
                        elif x[i]=='King Special':
                            Roomtype="KingSpecial"
                            RoomEx=10000
                    val.append(rno)
                    val.append(date(Dateey,Dateem,Dateed))
                    val.append(name)
                    val.append(Phone)
                    val.append(Addr)
                    val.append(Roomtype)
                    val.append(RoomEx)
                    val.append(date(Dateexy,Dateexm,Dateexd))
                    sql="Insert into Room(Room_No,DateofEntry,Name,PhoneNo,AddharNO,Room_Type,RoomExpenditure,DateofExit)values(%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.executemany(sql,(val,))
                    m='UPDATE Roomstatus set Room_Status="Occupied" where room_no=%s'
                    cursor.execute(m,(rno,))
                    print('Room booked Successfully')

                
                
                elif i=='Occupied':
                    space()
                    print("Room is already booked")
                    space()
                    continue                    
        elif ans.lower()=='n':
            break
        else:
            print('Invalid Input')
            print('Enter again!')
            continue



def display():
    singleline()
    print('Room_No | DateofEntry |Name              |PhoneNO      |AddharNo       |Room_Type     |DateofEXIT   |RoomExpense |Other    |')
    singleline()
    sql2='select * from room'
    cursor.execute(sql2)
    rec=cursor.fetchall()
    for i in rec :
        print(i[0],' '*(6-(len(str(i[0])))),'|',i[1],' '*(1-(len(str(i[1])))),'|',i[2],
              ' '*(15-(len(str(i[2])))),'|',i[3],' '*(10-(len(str(i[3])))),'|',i[4],' '*(12-(len(str(i[4])))),
              '|',i[5],' '*(11-(len(str(i[5])))),'|',i[6],' '*(10-(len(str(i[6])))),'|',i[7],' '*(9-(len(str(i[7])))),'|',i[8],' '*(6-(len(str(i[8])))),'|')
    singleline()

def temp():
    cursor.execute('Create Table IF NOT EXISTS temp(Room_No int NOT NULL  ,DateofEntry Date,Name varchar(15),PhoneNO bigint ,AddharNo int(10),Room_Type varchar(15),DateofEXIT Date,RoomExpenditure int(6),OtherExpenditure int(5))')
    print('+--------------------------------------------------------------------------------------------------------------------------+')
    print('|Room_No  | DateofEntry |Name              |PhoneNO      |AddharNo     |Room_Type     |DateofEXIT   |RoomExpenses |Other   |')
    print('+--------------------------------------------------------------------------------------------------------------------------+')
    sql2='select * from temp'
    cursor.execute(sql2)
    rec=cursor.fetchall()
    for i in rec :
        print('|',i[0],' '*(6-(len(str(i[0])))),'|',i[1],' '*(1-(len(str(i[1])))),'|',i[2],
              ' '*(15-(len(str(i[2])))),'|',i[3],' '*(10-(len(str(i[3])))),'|',i[4],' '*(10-(len(str(i[4])))),
              '|',i[5],' '*(11-(len(str(i[5])))),'|',i[6],' '*(10-(len(str(i[6])))),'|',i[7],' '*(10-(len(str(i[7])))),'|',i[8],' '*(5-(len(str(i[8])))),'|')
    print('+--------------------------------------------------------------------------------------------------------------------------+')
      


def roomstatus():
    print('\t'*6,"RoomStuts")
    print('\t'*4,'-'*39)
    print('\t'*4,'|RoomNo|RoomType          |RoomStatus |')
    sql2='select * from roomstatus'
    cursor.execute(sql2)
    rec=cursor.fetchall()
    print('\t'*4,'-'*39)
    for i in rec :
        print('\t'*4,'|',i[0],' '*(3-(len(str(i[0])))),'|',i[1],' '*(15-(len(str(i[1])))),'|',i[2],' '*(8-(len(str(i[2])))),'|')
    print('\t'*4,'-'*39)
    space()
def FoodCount():
    rno=input("Enter Room No.")
    print("\t\t\t\t\t  ~*Menu*~")
    print()
    cursor.execute('Select * from food')
    f=cursor.fetchall()
    
    print(' '*30,'+---------------------------------+')
    print(' '*30,"| No   | Item             | Rate  |")
    print(' '*30,'+---------------------------------+')
    for i in f :
        print(" "*30,'|',i[0],' '*(3-(len(str(i[0])))),'|',i[1],' '*(15-(len(str(i[1])))),'|',i[2]," "*(4-(len(str(i[2])))),'|')
    print(' '*30,'+---------------------------------+')
    sql='Select OtherExpenditure from room where Room_No=%s'
    cursor.execute(sql,(rno,))
    d=cursor.fetchone()
    sums=0
    for i in d:
        z=int(0 if i is None else i)
        sums+=z
        
    
    
    while True:
        o=input("Do u want to Enter More(y/n):")
        if o=='y':
            print()
            s=int(input("Enter Item No."))-1
            qty=int(input("Enter Quantity"))
            
            x=f[s]
            sums+=x[2]*qty
            print("Item ",x[1]," Ordered Succesfully!!")
        elif o=='n':
            break
        else:
         print("Invalid Input")
         print()
         continue

    x="UPDATE Room set OtherExpenditure=%s where room_no=%s"
    val=[]
    val.append(sums)
    val.append(rno)
    cursor.executemany(x,(val,))
    
#FoodCount()


#space()

def days():
    global rno
    x="select DateofEntry from room_no=%s"
    cursor.execute(x,(rno,))
    de=cursor.fetchone()
    x="select DateofExit from room_no=%s"
    cursor.execute(x,(rno,))
    dx=de=cursor.fetchone()
    d=de-dx
    print(d.days)

def bill():
    rno=int(input("Enter Room Number to find bill :"))
    x="select DateofEntry from room where room_no=%s"
    cursor.execute(x,(rno,))
    r=(cursor.fetchone())
    de,dx,roomexp,othexp,totalexp=0,0,0,0,0
    for i in r:
        de=i
    x="select DateofExit from room where room_no=%s"
    cursor.execute(x,(rno,))
    r=cursor.fetchone()
    for i in r:
        dx=i
    
        
    d=dx-de
    d=d.days
    o="select RoomExpenditure,OtherExpenditure  from room where room_no=%s"
    cursor.execute(o,(rno,))
    t=cursor.fetchall()
    roomexp=t[0][0]
    othexp=t[0][1]
    othexp=int(0 if othexp is None else othexp)
    d=int(1 if d==0 else d)
    totalexp=(roomexp*(d)+othexp)
    o='select *  from room where room_no=%s'
    cursor.execute(o,(rno,))
    t=cursor.fetchall()
    
    singleline()
    print("\t\t\t\t\t\t*Bill*")
    singleline()
    for i in t: 
        print("Room Number     :",i[0],end='\t'*6)
        print('Room Type       :',i[5])
        print("Name            :",i[2])
        print("Phone Number    :",i[3],end='\t'*5)
        print("Addhar Number   :",i[4])
        print("Date of Entry   :",i[1],end='\t'*5)
        print("Date of Exit    :",i[6])
        print()
        singleline()
        print("Room Expenditure:",i[7],'\t'*6,'Number of days  :',d)
        print("OtherExpenditure:",i[8])
        singleline()
        print("Total           :",totalexp)
        singleline()
        space()
    
    
def staff():
     
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
    





def exitb():
    rno=int(input("Enter Room Number to exit :"))
    
    x="Insert into temp(select * from room where room.room_no=%s)"
    cursor.execute(x,(rno,))
    
    bill()
    print("\t\t\t\t!!!Thank you for Honouring us by your visit !!!  ")
    s="Delete from room where room_no=%s"
    cursor.execute(s,(rno,))
    print("\n\nRoom",rno,"disallocated Successfully!!")
    m='UPDATE Roomstatus set Room_Status="Vacant" where room_no=%s'
    cursor.execute(m,(rno,))
    
    

def modify1():
    
    o='y'
    while o=='y':
        
        print('\t'*7,"*Menu of Modification*")
        print('\t'*6,'--------------------------------------')
        print('\t'*6,'1 -> Modification of Customer details')
        print('\t'*6,'2 -> Modification of Staff details')
        print('\t'*6,'3 -> Modification of Food Menu')
        print('\t'*6,'4 -> Exit')
        print('\t'*6,'------------------------------------')
        u=int(input("Enter Choice:"))
        if u==1:
            print('\t'*6,'------------------------------------')
            print('\t'*6,"1 -> Change Name")
            print('\t'*6,"2 -> Change Addhar Card number")
            print('\t'*6,"3 -> Change Phone number")
            print('\t'*6,"4 -> Change Date of Entry")
            print('\t'*6,"5 -> Change Date of Exit")
            print('\t'*6,"6 -> Exit")
            print('\t'*6,'------------------------------------')
            p=int(input("Enter Choice:"))
            
            val=[]
            if p==1:
                rno=int(input("Enter Room Number to Change Details :"))
                name=input("Enter New Name              :")          
                val.append(name)
                val.append(rno)
                m='UPDATE Room set Name=%s where room_no=%s'
                cursor.executemany(m,(val,))
            elif p==2:
                rno=int(input("Enter Room Number to Change Details :"))
                adno=int(input("Enter Addharcard Number:"))
                val.append(adno)
                val.append(rno)
                m='UPDATE Room set addharno=%s where room_no=%s'
                cursor.executemany(m,(val,))
            elif p==3:
                rno=int(input("Enter Room Number to Change Details :"))
                phno=int(input("Enter New Phone Number:"))
                val.append(phno)
                val.append(rno)
                m='UPDATE Room set PhoneNo=%s where room_no=%s'
                cursor.executemany(m,(val,))
            elif p==4:
                rno=int(input("Enter Room Number to Change Details :"))
                Dateed=int(input('Date of Entry (dd)      :'))
                Dateem=int(input('Date of Entry (mm)      :'))
                Dateey=int(input('Date of Entry(yyyy)    :'))
                m='UPDATE Room set DateofEntry=%s where room_no=%s'
                val=[]
                val.append(date(Dateey,Dateem,Dateed))
                val.append(rno)
                cursor.executemany(m,(val,))
    
            elif p==5:
                rno=int(input("Enter Room Number to Change Details :"))
                Dateed=int(input('Date of Exit (dd)      :'))
                Dateem=int(input('Date of Exit (mm)      :'))
                Dateey=int(input('Date of Exit (yyyy)    :'))
                m='UPDATE Room set DateofEXIT=%s where room_no=%s'
                val=[]
                val.append(date(Dateey,Dateem,Dateed))
                val.append(rno)
                cursor.executemany(m,(val,))
            else :
                print("\t\t\t\t!!Invalid Input!!")
                print('\n'*6)
                continue
        elif u==2:
            print('\t'*6,'------------------------------------')
            print('\t'*6,"1 -> Change Name")
            print('\t'*6,"2 -> Change Designtion")
            print('\t'*6,"3 -> Add New Employee")
            print('\t'*6,"4 -> Delete Employee Details")
            print('\t'*6,"5 -> Exit")
            print('\t'*6,'------------------------------------')
            p=int(input("Enter Choice:"))
            val=[]
            if p==1:
                rno=int(input("Enter Employee Number :"))
                name=input("Enter New Name:")
                val.append(name)
                val.append(rno)
                m='UPDATE Staff set Name=%s where Employee_Number=%s'
                cursor.executemany(m,(val,))
            elif p==2:
                rno=int(input("Enter Employee Number :"))
                d=input("Enter Designation")
                val.append(d)
                val.append(rno)
                cursor.executemany(m,(val,))
            elif p==3:
                rno=int(input("Enter Employee Number :"))
                name=input("Enter Employeee Name:")
                d=input("Enter Designation")
                val.append(rno)
                val.append(name)
                val.append(d)
                m="Insert into staff(Employee_Number,Name,Designation) values (%s,%s,%s)"
                cursor.executemany(m,(val,))
            elif p==4:
                rno=int(input("Enter Employee Number :"))
                m="Delete from staff where Employee_Number=%s"
                val.append(rno)
                cursor.executemany(m,(val,))
        elif u==3:
            print('--------------------------------------------')
            print('\t'*6,'1 -> Add Food Item')
            print('\t'*6,'2 -> Delete Food Item')
            print('\t'*6,"3 -> Change Food Item's rate")
            print('\t'*6,'4 -> Exit')
            p=int(input("Enter Choice:"))
            val=[]
            if p==1:
                no=int(input("Enter Item Number"))
                name=input("Enter Item Name:")
                rate=int(input("Enter Item Rate"))
                val.append(no)
                val.append(name)
                val.append(rate)
                m="Insert into food(Item_No,Food_Item,Food_cost) values(%s,%s,%s)"
                cursor.executemany(m,(val,))
            elif p==2:
                no=int(input("Enter Item Number"))
                m="Delete from food where Item_No=%s"
                val.append(no)
                cursor.executemany(m,(val,))
            elif p==3:
                no=int(input("Enter Item Number"))
                rate=int(input("Enter Item Rate"))
                val.append(rate)
                val.append(no)
                m='UPDATE Food set Food_cost=%s where Item_no=%s'
                cursor.executemany(m,(val,))
        elif u==4:
            break
    


def mainmenu():
   while True:

    print("\t"*5," *Hotel*")
    print()
    print("\t"*5,"~Main Menu~")
    print("\t"*4,'-----------------------------')
    print("\t"*4,'1 -> New Reservation')
    print("\t"*4,'2 -> Show Reservations')
    print("\t"*4,'3 -> Show Room Status')
    print("\t"*4,'4 -> Modify Record')
    print("\t"*4,'5 -> Food Service')
    print("\t"*4,'6 -> Billing')
    print("\t"*4,'7 -> Room Deallocation')
    print("\t"*4,'8 -> Staff')
    print("\t"*4,'9 -> Previous Reservations')
    print("\t"*4,'10-> Exit')
    print("\t"*4,'-----------------------------')
    print('\n'*5)
    p=int(input('\t Enter Choice(Number):'))
    if p==1:
        booking()
    elif p==2:
        display()
    elif p==3:
        roomstatus()
    elif p==4:
        modify1()
    elif p==5:
        FoodCount()   
    elif p==6:
        bill()
    elif p==7:
        exitb()
    elif p==8:
        staff()
    elif p==9:
        temp()
    elif p==10:
        break
    else:
        print("\t\t\t\t!!Invalid Input!!")
        print('\n'*6)
        continue
 


    print('\n'*6)
    


mainmenu()
