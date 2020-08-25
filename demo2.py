import mysql.connector
#from mysql.connector import *
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
def create_table():
    c.execute("create table Dhanush_R(coloumname varchar(10),adderss varchar(20),dob int,pannumber int)")
def insert_table():
    c.execute("insert into Dhanush_R values('dhanush','mulbagal',24-10-1999,'1234567')")
    c.execute("insert into Dhanush_R values('nitya','kalar',25-10-1999,'1234568')")
    c.execute("insert into Dhanush_R values('jyothi','vkota',27-10-1999,'12345679')")
    c.execute("insert into Dhanush_R values('swetha','banglore',29-10-1999,'12345672')")
    c.execute("insert into Dhanush_R values('vamshi','palamaner',27-10-1999,'12345674')")

def select_table():
    c.execute('select * from Dhanush_R  ')
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