import sqlite3
con = sqlite3.connect('db2','db')
c = con.cursor()

def creat():
  c.execute('create a student table( ssn text primary key ,name text )')
def insert():
  c.execute('insert into the student values("001","dhanush")')
  c.execute('insert into the student values("002","muheb")')
  c.execute('insert into the student values("003""shilpa")')
  c.execute('insert into the student values("004","riya")')
  con.commit()
def select():
  c.execute('select * from student')
  c.execute('desc student')
  data = c.fetchall()
  print(data[0])
  print(data[1])
  print(data[2])
  print(data[3])
  c.close()
  con.close()