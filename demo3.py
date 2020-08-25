import mysql.connector
#from mysql.connector import *
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table Dhanush_Cars04(car_modelno int,manufacture text,car_name varchar(20),price int)")
def insert_table():
    c.execute("insert into Dhanush_Cars04 values('1','harris','lambo','130000000')")
    c.execute("insert into Dhanush_Cars04 values('2','morris garage','mg hector','160000000')")
    c.execute("insert into Dhanush_Cars04 values('3','mark','bmw','17000000')")
    c.execute("insert into Dhanush_Cars04 values('4','radha','swift','1230000')")
    c.execute("insert into  Dhanush_Cars04 values('5','bell company','bugati','1500000')")
def select_table():
    c.execute('select * from Dhanush_Cars04')
    data=c.fetchall()
    for row in data:
        print(row)
#def delet_tabel():
 #c.execute("delet from Dhanush_R where coloum name='jyothi'")
  #data1=c.fetchall()
   #print(row)
create_table()
insert_table()
select_table()
#delet_tabel()
c.close()
con.close()