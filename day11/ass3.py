#write a python program to check whether the input number is prime or not
n=int(input("enter a number: "))
c=0
for i in range(n):
    a=i+1
    if n%a==0:
        c+=1
if(c>2):
    print("it is not prime number")
else:
    print("it is prime number")
