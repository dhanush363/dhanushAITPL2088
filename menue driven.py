def add(x,y):
    return(x+y)
def mul(x,y):
    return(x*y)
def sub(x,y):
    return(x-y)
def div(x,y):
    return(x/y)
def mod(x,y):
    return(x%y)
print("1.addition")
print("2.multiplication")
print("3.subraction")
print("4.division")
print("5.modlues")
choice=int(input("enter your choice: "))
a=int(input("enter first number: "))
b=int(input("enter second number: "))
if choice==1:
    print(a,"+",b"=",add,(a,b))
    print("do you continue yes/no:")
if choice==2:
    print(a,"*",b"=",mul(a,b))
    print("do you continue yes/no:")
if choice==3:
    print(a,"-",b"=",sub(a,b))
    print("do you continue yes/no:")
if choice==4:
    print(a,"/",b"=",div(a,b))
    print("do you continue yes/no:")
if choice==5:
    print(a,"%",b"=",mod(a,b))
    print("do you continue yes/no:")
if choice==6:
    print("invalid choice")


