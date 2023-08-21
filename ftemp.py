def FoodCount():
    rno=int(input("Enter Room No.:"))
    Rate= {'Dalfry':100,'Steamrice':90,'Chapati':12,'Mixveg':120,'Chicken69':130,'Gulabjamun':95,'Paneer420':100}
    lst1= list(Rate.keys())
    
    GST= 0.15
    sums=0
    while True:
        print('Dalfry:100\nsteamrice:90\nchapati:12\nmixveg:120\nchicken69:130\ngulabjamun:95\npaneer420:100')
        print('press done to exit')
        order= input('enter your order: ')
        if order in lst1:
          sums= sums + Rate[order]
        elif order== 'done':
            break
    print(sums)
    x="UPDATE Room set OtherExpenditure=%s where room_no=%s"
    val=[]
    val.append(sums)
    val.append(rno)
    cursor.executemany(x,(val,))
    display()
