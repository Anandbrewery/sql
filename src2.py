import uuid
import mysql.connector as sql
import random  
import datetime as dt
import time


def generate_unique_id(x):
    unique_id = f"{x}{str(uuid.uuid4()).split('-')[-1]}"
    return str(unique_id)


conn=sql.connect(host='localhost',user='root',passwd='root',database='project1')
print("succesfully connected") if conn.is_connected() else print("no")
cur=conn.cursor()

info="Select accountno from customer"



while True:
    cur.execute(info)
    accno=cur.fetchall()
    print(accno)
    print("="*20+"WELCOME TO ELECTRICITY BILLING SYSTEM"+"="*20)
    print('1.NEW USER')
    print("2.ACCOUNT DETAILS DISPLAY")
    print("3.VIEW CUSTOMER DETAILS")
    print('4.FACING ISSUE/TICKET STATUS')
    print('5.EXIT')

    ch=int(input('ENTER YOUR CHOICE:'))
    
    if(ch==1):
        passwd=None
        cpasswd=""
        username=input("Enter your username:")
        while(passwd!=cpasswd):
            passwd=input("Enter your password:")
            cpasswd=input("Confirm  your password:")
        accno=generate_unique_id(username[:3])
        bankname=input("Enter the bankname")
        areacode=input("Enter the areacode")
        phno=input("Enter the phone number")
        info="insert into customer values('{}','{}','{}','{}','{}','{}')".format(accno,bankname,areacode,phno,username,passwd)
        cur.execute(info)
        conn.commit()
        print("your accountno is{} and your details have been saved successful".format(accno))
        
        
    elif(ch==2):
        pswd=""
        usr=""
        while(usr not in accno):
            usr=input("Enter your account number:")
        pswd=input("enter the password: ")
        info="Select passwd from customer where accountno={}".format(usr);
        cur.execute(info);
        passwd=cur.fetchall();
        while(passwd!=pswd):
            print("Incorrect password for the username entered")
            c=input("Username is wrong type 0 else type 1")
            if(c==0):
                break
            else:
                pswd=input("enter the password: ")
        if(pswd==passwd):
            info="Select * from customer where accountno={}".format(usr);
            cur.execute(info)
            data=cur.fetchall()
            print("Account number:{}".format(data[0]))
            print("Username:{}".format(data[4]))
            print("Bank Name:{}".format(data[1]))
            print("Areacode:{}".format(data[2]))
            print("Phone Number:{}".format(data[3]))
        
    elif(ch==3):
        
        pass
    elif(ch==4):
        pass
    else:
        break
    