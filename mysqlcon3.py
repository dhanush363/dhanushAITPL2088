import mysql.connector
#from mysql.connector import *
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()

def create_tabel():
    c.execute("create tabel  employee1(empid varchar(10),name varchar(20))")
def insert_tabel():
    c.execute("insert into employee1 values('ATPIL001','vishnu')")
    c.execute("insert into employee1 values('ATPIL002','nitya')")
    c.execute("insert into employee1 values('ATPIL003','jyothi')")
    c.execute("insert into employee1 values('ATPIL004','swetha')")
    c.execute("insert into employee1 values('ATPIL005','vamshi')")
con.commit()
def select_tabel():
    c.execcute("select * from employee1")
    data=c.fetchall()
    for row in data():
        print(row)
def delet_tabel():
 c.execute("delet from dhanush employee empid='004'")
  data1=c.fetchall()

create_tabel()
insert_tabel()
select_tabel()
#delet_tabel()
c.close()
con.close()
