# A function that takes another function as an argument is called higher order function
# sorted(),map(),filter(),reduce(),decorators,etc. are the higher order function in python.


# map(function,iterable)
# map takes function as first parameter and iterable as second parameter.
# it maps every elements of the iterable to some other form.
# the length of initial iterable and final result is same in map. 

data=[1,2,3,4]
def cubed(elem):
    return elem**3

result=map(cubed,data)
print(result) #<map_object> which is an iterator and can be looped. but to see its element we need to
              #convert it to some other datatype.

print(list(result))
for i in result:
    print(i)

print(list(result))    #ietrable le garda khali aauxa yeta tala print garyo vane.



# filter()
#it also takes function and iterable as arguments.
#it picks certain elements from the initial iterable.
#but the size of initial iterable and final result may not be same in case of filter

data=[1,2,3,4,5,6,7,8,9,10]
def even(elem):
    if elem%2==0:
        return True
    else:
        return False
result=filter(even,data)
print(result)  #<filter_object>
print(list(result))   #[2,4,6,8,10]

#if return truthy then it pick and if return falsy then wont pick

#using lambda:
filter(lambda elem:elem%2==0,data)




# reduce()
#it also takes function and iterable arguments
#it does operation based on the given function and return a single value
from functools import reduce
data=[1,2,3,4,5]
def mul(x,y):
    return x*y
result=reduce(mul,data)
print(result) #15
#1+2=3 then 3+3=6 then 6+4=10 then 10+5=15

#using lambda:
reduce(lambda x,y:x*y,data)
 
