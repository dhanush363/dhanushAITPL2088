from tkinter import *
a=Tk()

def hello():
    c=Label(text='you have pressed enter',fg='orange',bg='white',font=50).pack()
def delet():
    c=Button(text='you have pressed delet',fg='orange',bg='white',font=50).pack()

a.title('notepad')
a.geometry('1366x768+0+0')
l=Label(text='label1',fg='orange',bg='white',font=50).pack()
button1=Button(text='entry',fg='orange',bg='white',command=hello,font=50).pack()
button2=Button(text='delet',fg='red',bg='white',command=delet,font=50).pack()

m1=Menu()
l1=Menu()
l1.add_command(label='new')
l1.add_command(label='new window')
l1.add_command(label='open')
l1.add_command(label='save')
l1.add_command(label='save as')
l1.add_command(label='exit')
l2=Menu()

l2.add_command(label='undo')
l2.add_command(label='cut')
l2.add_command(label='paste')
l2.add_command(label='delet')
l2.add_command(label='go_to')

l3=Menu()
l3.add_command(label='wordwrap')
l3.add_command(label='font...')

l4=Menu()
l4.add_command(label='zoom')
l4.add_command(label='status bar')

l5=Menu()
l5.add_command(label='view help')
l5.add_command(label='send feedback')
l5.add_command(label='about notepad')

m1.add_cascade(label='file',menu=l1)
m1.add_cascade(label='edit',menu=l2)
m1.add_cascade(label='formate',menu=l3)
m1.add_cascade(label='view',menu=l4)
m1.add_cascade(label='help',menu=l5)
a.configure(menu=m1)
a.mainloop()
