from tkinter import *
a=Tk()
def hello():
    c=Label(text='you have pressed enter',fg='orange',bg='white',font=50).pack()
def delet():
    c=Button(text='you have pressed delet',fg='orange',bg='white',font=50).pack()
a.title('notepad')
a.geometry("1366x768+0+0")
l=Label(text='label1',fg='orange',bg='white',font=50).pack()
button1=Button(text='entry',fg='orange',bg='white',command=hello,font=50).pack()
button2=Button(text='delet',fg='red',bg='white',command=delet,font=50).pack()
a.mainloop()