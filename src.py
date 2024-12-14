import mysql.connector as sql
import random  
import datetime as dt
import time

#Connecting database
conn=sql.connect(host='localhost',user='root',passwd='root',database='project1')
print("succesfully connected") if conn.is_connected() else print("no")

c='YES'
V='YES'
c1=conn.cursor() 
def accno_searcher (customer_id):
     info4="select * from Customer where customer_id='{}'".format(customer_id) 
     c1.execute(info4)
     data1=c1.fetchall()
     accountno=data1[0][0]
     return  accountno
                                    
def cust(custo_id,custid):
            if custo_id in custid:
               custo_id=random.randint(14000,3000000)
            else:
                 return custo_id 
             
def match( username,password,confirmpasswd,custo_id):
    print("inside match")           
    if password==confirmpasswd:
                info1="insert into newuseradd values('{}','{}','{}','{}')".format(username,password,confirmpasswd,custo_id )
                c1.execute(info1)
                conn.commit()
                print()
                print('please customer update your details 1.update details so that you can pay your bill smoothly')
                x=input("do you want to continue?(yes or no)")
                c=x.upper()
    else:
         print('you have no longer access')
         c='YES'
    return c 
          

while c=='YES':
    try:
                print('====================WELCOME TO ELECTRICITY BILLING SYSTEM====================')

                print('1.NEW USER')
                print("2.USER ACCOUNT SETTINGS")
                print("3.VIEW CUSTOMER DETAILS")
                print('4.FACING ISSUE/TICKET STATUS')
                print('5.EXIT')
                custid=[]
                info='select customer_id from project1.newuseradd'
                c1.execute(info)
                custid= c1.fetchall()
                #Selecting choice
                #New user updating info
                choice1=int(input('ENTER YOUR CHOICE:'))
                if choice1==1:
                   try:
                       username=input("Enter your username:")
                       password=input("Enter your password:")
                       confirmpasswd=input("Confirm  your password:")
                       custo_id=random.randint(140000,3000000)
                       custo_id=cust(custo_id,custid) 
                       match(username,password,confirmpasswd,custo_id) 
                   except:
                       print('username already exist pls try with new username')
                       
                elif choice1==2:
                        
                        inp='SELECT accountno FROM project1.customer'
                        c1.execute(inp)
                        data_a=c1.fetchall()
                        print(data_a)
                        accountno=random.randrange(10000,100000)  
                        accountno=cust(accountno,data_a)
                    
                        
                     
                        print("your accountno is",accountno)
                        bankname=input('Enter your BANK NAME  :')
                        bankbranch=input('Enter your BANK BRANCH  :')
                        areacode=int(input('Enter your area PIN CODE  :'))
                        boxid=input("enter your mete box ID:")
                        phoneno=int(input('Enter your PHONE NUMBER  :'))
                        conn.commit() 
                        info2="insert into customer values('{}','{}','{}','{}','{}','{}','{}')".format(accountno,bankname,bankbranch,areacode,phoneno,customer_id,username)
                        c1.execute(info2)
                        conn.commit()
                        x=input("do you want to continue?(yes or no)")
                        V=x.upper()
                        if(V=='YES'):
                            continue 
                        else:
                            break
                
                                                    
 
                elif choice1==3:
                      accountno=accno_searcher(customer_id)
                      info4="select * from Customer where accountno=" + str(accountno)
                      c1.execute(info4)
                      data1=c1.fetchall()
                      if data1:
                          for row in data1:
                              print(" Account Number: ", row[0])
                              print("bankname:",row[1])
                              print("bankbranch:",row[2])
                              print("Person name:",row[3])
                              print("Your meter device ID=",row[6])
                              print("area code:",row[4])
                      else:
                          print("")
                                                        
                elif choice1==4:
                    accountno=accno_searcher(customer_id)
                    print('1.COMPLAINT REGISTRATION')
                    print('2.TICKET STATUS')
                    choiceb=int(input('enter your choice'))
                    try:
                        if choiceb==2:
                            info10="select * from ticketissue where accountno="+str(accountno)
                            c1.execute(info10)
                            data3=c1.fetchall() 
                            for i in data3:
                                ts=i[3]
                                print("your ticket status:",ts)
                                if choiceb==1:
                                    print("If you have any queries or grievances which needs to be addressed:")
                                    print("Type YES")
                                    print("If you don't have any queries or grievances which needs to be addressed")
                                    print("Type NO")
                                    a=str(input("Type YES or NO"))
                                    query=a.upper()
                                    print(query )
                                    if query=='YES':
                                        ticketno=random.randint(766534,855425)
                                        print("Your query or grievance has been notified to the customer care centre")
                                        time.sleep(2)
                                        print("Your ticket number is",ticketno)
                                        time.sleep(2)
                                        print("You will need this ticket number for future referene")
                                        time.sleep(2)
                                        print("When a representative from cuustomer call centre contacts you, tell them this ticket number for easy coordination")
                                        time.sleep(2)
                                        ticket=input('enter the query')
                                                                                
                                    elif query=='NO':
                                        print("I hope you are satisfied by our service")
                                        time.sleep(2)
                                        print("THANK YOU AND VISIT AGAIN")
                                    info3="insert into ticketissue values({},{},'{}')".format(accountno,ticketno,ticket)
                                    c1.execute(info3)
                                    conn.commit()
                    except:
                        print('invalid choice')
                        x=input("do you want to continue?(yes or no)")
                        V=x.upper()
                        if V=='YES':
                            continue
                        else:
                            break

                elif choice1==5:
                    print("==============THANK YOU=============")
                    C='no'
                    break        
                else:
                   print('invalid choice')
                   x=input("do you want to continue?(yes or no)")
                   V=x.upper()
                   if V=='YES':
                            continue
                   else:
                            break              
    except:
      print('invalid choice')
      
else:
    print('THANK YOU')
    
                  
