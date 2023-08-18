#lambda are the elegant way of creating one-liner function
#lambda function do not have name. So they  are also called anonymous function
#one line function ko lagi better
#call garnu parne thau ma use nagarnu is better
#auto return hunxa

def squared(num):
    return num**2
print(squared())

#using lambda
#this is improper way
squared=lambda num:num**2
print(squared(4))  #16

#proper way:
lambda num:num**2

# map
data=[1,2,3,4]
result=map(lambda elem:elem**2,data)
print(list(result))
result=map(lambda elem:elem%2==0,data)
print(list(result))  #[False,True,False,True]


#filter
data=[1,2,3,4,0]
result=filter(lambda elem:elem%2==0,data)
print(list(result))
result=filter(lambda elem:elem**2,data)
print(list(result))   #[1,2,3,4] because elem**2 is truthy and 0**2 is falsy so no 0 in result

#reduce
from functools import reduce
data=[1,2,3,4,5]
result=reduce(lambda x,y:x*y,data)
print(result)

