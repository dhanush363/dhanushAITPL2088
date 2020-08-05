n=int(input("enter  number of elements: "))
a=list(int,input("\nenter the numbers: ").strip().split())[:n]
a.sort()
print(a)
print("2nd largre number is {0},fourth largest number{1}",formate(a[2],a[4]))

