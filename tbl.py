#Table
import mysql.connector as sql

conn=sql.connect(host='localhost',user='root',passwd='root')
print("succesfully connected") if conn.is_connected() else print("no")


   
c2=conn.cursor()
c2.execute('create database project1')

conn = sql.connect(host='localhost',user='root',password='root',database='project1')
   
c1=conn.cursor()
#c1.execute(' create table admin( ID INT primary key , Phone_number varchar(10) , position varchar(10), password varchar(50) )')
#c1.execute('CREATE TABLE newuseradd (username varchar(100) NOT NULL, password varchar(100) DEFAULT NULL,confirmpasswd varchar(100) DEFAULT NULL,customer_id int DEFAULT NULL,PRIMARY KEY (username)) ')
c1.execute('CREATE TABLE customer (accountno varchar(100) NOT NULL,bankname varchar(200) DEFAULT NULL,areacode int DEFAULT NULL,phoneno int DEFAULT NULL,username varchar(100) DEFAULT NULL,passwd varchar(100), PRIMARY KEY (accountno))')
c1.execute('CREATE TABLE billing (accountno varchar(100) NOT NULL,unit varchar(12) DEFAULT NULL,totalamt varchar(100) DEFAULT NULL,duedate varchar(12) DEFAULT NULL,paid_on varchar(12) DEFAULT NULL, bill_payment_status varchar(8) DEFAULT NULL,bill_no varchar(20),PRIMARY KEY (accountno))')                
c1.execute('CREATE TABLE ticketissue(accountno varchar(100) NOT NULL,ticket_no int DEFAULT NULL,ticket varchar(100) DEFAULT  NULL,ticket_status varchar(10),PRIMARY KEY (accountno))')
#c1.execute("insert into admin values (2001,'8765456784','HEAD_ADMIN',56723)")
conn.commit()
print("table created")    

