import mysql.connector
#from mysql.connector import *
con=mysql.connector.connect(host='18.219.99.141',database='db1',user="root",password='India12345')
c=con.cursor()
#def create_tabel():
    #c.execute("create tabel dhanush(regno varchar(10),name varchar(20)")

con.commit()
c.execute("insert into dhanush values('AITPL2088','dhanush')")
c.execute("select * from dhanush")
data=c.fetchall()
for row in data:
    print(row)
c.close()
con.close()
