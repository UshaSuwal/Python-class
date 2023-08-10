# Tuple are immutable so we dont have methods like append(), pop(), insert() etc.
# The only methods in tuples are count() and index()


vowels=('a','e','i','o','u','a','u','i')
result=vowels.count("a")
print(result)  #2


result=vowels.index("a")
print(result)   # 0

result=vowels.index("a",2,7)
print(result)   # 5



# Some function that can be used with tuple

# sum()
result=sum((1,2,3,4,5))   #sequential datatype dina milxa sum ma
print(result)   # 15 

#max()
print(max(13,5,6,99))    # 99

# min()
print(min(1,2,3,4))   # 1

# sorted()   =>list banauxa
a=(99,5,1,-1,55)
result=sorted(a)
print(result)
print(sorted(a))    # [-1,1,5,55,99]

a=(99,5,1,-1,55)
print(sorted(a, reverse=True))  #[99,55,5,1,-1]


# reversed()
a=(1,2,3,10,20,11,3)
print(reversed(a))   # Output= <reversed object>
print(a)             (3,11,20,10,3,2,1)
result=reversed(a)
print(list(result))  #typecast

