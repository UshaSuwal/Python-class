# range()
# range() function can take upto 3 parameters.
# syntax: range(start,end,step_size)
# "end" parameter is always exclusive.  ie. last < ma aauxa

data=range(6)
print(data)  # 0,1,2,3,4,5
print(list(data))  #[0,1,2,3,4,5]

print(list(range(0,6)))   # [0,1,2,3,4,5]

data=range(2,7)
print(list(data))  #[2,3,4,5,6]

data=range(1,10,2)    # 2 is kati le jump garne.
print(list(data))   #[1,2,4,6,8]

#enumerate()
#in c or c++ looping is done in index of an array
# unlike c or c++, looping is done in the elements of list/array.
# But in python, we can use "enumerate" to get the index in each iteration
vowels=['a','e','i','o','u']
print(enumerate(vowels))   #<enumerate_object
print(list(enumerate(vowels)))   # [(0, 'a'), (1, 'e'), (2, 'i'), (3, 'o'), (4, 'u')]

for index,value in enumerate(vowels):  #tuple vakole unpacking gareko ->index,value
    print(index)  #0,1,2,3,4
    print(value)  #a,e,i,o,u

for index,value in enumerate(vowels, start=2):  #tuple vakole unpacking gareko ->index,value
    print(index)   #2,3,4,5
    print(value)   #e,i,o,u



