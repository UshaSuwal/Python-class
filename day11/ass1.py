#wap to accept an integer and compute the value n+nn+nnn+...
n=int(input("enter a number"))
total = 0
a = n
for i in range(n):
    total=total + a 
    print(a)       
    a = a * 10 + n  
print("sum=",total)



