import mysql.connector
#from mysql.connector import *
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table dhanush_employee2(empid varchar(10),name varchar(20),salary int)")
def insert_table():
    c.execute("insert into dhanush_employee2 values('AITPL2088','dhanush','11500')")
    c.execute("insert into dhanush_employee2 values('ATPIL0024','nitya','15000')")
    c.execute("insert into dhanush_employee2 values('ATPIL0034','jyothi','14000')")
    c.execute("insert into dhanush_employee2 values('ATPIL0044','swetha','12000')")
    c.execute("insert into dhanush_employee2 values('ATPIL0054','vamshi','16000')")

def select_table():
    c.execute('select * from dhanush_employee2')
    data=c.fetchall()
    for row in data:
        print(row)
#def delet_tabel():
 #c.execute("delet from dhanush_employee2 empid='004'")
  #data1=c.fetchall()
   #print(row)
create_table()
insert_table()
select_table()
#delet_tabel()
c.close()
con.close()
