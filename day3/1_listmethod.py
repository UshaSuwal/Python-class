# append()
vowels=['a','e','i','o']
vowels.append('u')       # add garxa value
print(vowels)

# extend()
a=[1,2,3]
b=[4,5,6]
#result=a.extend(b)
#print(result)  #output=none. result ma store hudaina

a.extend(b)  #a ma b ko add gardinxa
print(a)

# insert(index,value)      # value  ghusaidinxa
vowels=['a','e','i','o','u']
vowels.insert(2,'s')   #sidai yo print garyo vane none aauxa 
print(vowels)

# remove(value)
b=[1,2,3]
b.remove(3)
print(b)
#b.remove(4)    4 not in list so error
#print(b)

# pop(index)
vowels=['a','e','i','o','u']
result=vowels.pop(1)    # 1 is index ie 'e'  
print(result)           # here result wont be none because pop method return the popped value so it is stored in result
print(vowels)           # o= a i o u

vowels=['a','e','i','o','u']
print(vowels.pop())     # it will default pop the last value ie u


#clear()
a=[1,2,3]
a.clear()     #it will clear all value of list but wont delete the list
print(a)     


#index(value,start,end)
vowels=['a','e','i','o','u']
result=vowels.index('u')             # give index of 'u'
print(result)           

vowels=['a','e','i','e','o','u']
print(vowels.index('e'))
print(vowels.index('e',1))
print(vowels.index('e',2,4))


#count()
a=[1,2,1,1,5,6,7]
print(a.count(1))    #kati ota 1 xa tyo count garxa


# sort(reverse=True,Key=function)    #reverse and key are optional parameter
a=[5,6,3,7,99,1]
a.sort()    #ascending
print(a)
a.sort(reverse=True)   #descending
print(a)



b=[(5,4),(3,2),(4,10),(12,1),(1,9)]   #every item in list are tuple
def get_second(data):
    return data[1]
b.sort(key=get_second)
print(b)


a=[(4,12,5),(6,1),(11,12),(6,7,8)]
def get_last(data):
    return data[-1]
a.sort(key=get_last)   #sort le aafai euta euta list ko element paramenter banayera pathauxa.
print(a)

a=[(4,12,5),(6,1),(11,12),(6,7,8)]
def get_last(data):
    return data[-1]
a.sort(reverse=True,key=get_last)   
print(a)


# reverse()
a=[1,8,9,2,5]
a.reverse()
print(a)





