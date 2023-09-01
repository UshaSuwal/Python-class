#Wap to calculate fatorial of 5 in three way
# noraml loop
# reduce() function
# recursion function


# Normal loop
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)


# reduce()
from functools import reduce
result=reduce(lambda x,y:x*y,range(1,6))
print(result) 


# recursion
def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
print(fact(5))  #120

# 5*fact(4)   5*24=120
# 4*fact(3)   4*6=24
# 3*fact(2)   3*2=6
# 2*fact(1)   2*1=2
# 1*fact(0)   1*1=1