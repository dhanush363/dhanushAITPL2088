from tkinter import *
a=Tk()
def hello():
    c=Label(text='you have pressed enter',fg='yellow',bg='white',font=30).pack()
a.title("my first window")
a.geometry("1366x768+0+0")
l=Label(text='label1',fg='red',bg='white',font=30).pack()
#l1=Label(text='label2',fg='blue',bg='white',font=30).pack()
button1=Button(text='enter',command=hello(),fg='orange',bg='white',font=30).pack()
a.mainloop()