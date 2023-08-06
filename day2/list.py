#python list are mutable datatype and are sequencial(also an iterable)
#list are created enclosing data in big brackets[] or using built-in function list()
# (list and array are different. array must have homogeneous data)

# Creating empty list
a=[]
b=list()

# Creating non empty list
a=[1,2,3,4]
vowels=['a','e','i','o','u']
    # these are list with homogeneous data

a=[1,2.3,['a','e'],('i',4),{5,6,7},{'a':1,'b':2}]
    # these are list with heterogeneous data


# Accessing list item
#list item can be accessed using indexing and slicing


# INDEXING:
#indexing in list starts from 0 for forward traverse and -1 for reverse traverse
vowels=['a','e','i','o','u']
print(vowels[0])
print(vowels[4])
print(vowels[-1])
print(vowels[-5])
# print(vowels[10])  : indexerror: list index out of range

#item assignment is possible in list as it is mutable
vowels[3]='r'
print(vowels)




#SLICING:
#range always goes from left to right
a=['a','b','c','d','e','f','g','h','i']
print(a[0:5])   #0 to <5  
print(a[:5])    #agadi dekhi <5   a[0:5] = a[:5]
print(a[2:])    #2 dekhi paxadi sammai
print(a[2:7])   #2 to <7
print(a[7,2])   #output: []  empty

print(a[0:-2])  # a dekhi g samma aauxa as h is in index -2 (negatice indexing ma)
print(a[:-2])   # same as a[0:-2]
print(a[-5:])   # e dekhi right ko sabai
print(a[-7:-2]) #



# LIST OPERATION:

#1. Concatenation
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)  #output: [1,2,3,4,5,6]

#2. Membership operation
   #boolean output
print(2 in [1,2,3])   #O= True
print(3 not in [1,2,3])  #O= False


#typecasting tuple to list
z=(1,2,3)
print(list(z))    #this change tuple into list. Built-in list() is frequently used for typecasting


#SLICING
