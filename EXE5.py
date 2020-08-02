#FIND PRIME NUMBER BETWEEN M AND N USING FOR LOOP
m = int(input("Enter prime range m: "))
n = int(input("Enter prime range n: "))

for num in range(m,n + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
          print(num)