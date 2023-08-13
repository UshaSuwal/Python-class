# Wap to find greatest among 3 numbers

n1=int(input("enter a number n1 "))
n2=int(input("enter a number n2 "))
n3=int(input("enter a number n3 "))
if n1>n2 and n1>n3:
    print("n1 is greatest")
elif n2>n1 and n2>n3:
    print("n2 is greatest")
else:
    print("n3 is greatest")
