# Tuples are immutable datatypes. They are sequencial datatypes.
# Elements in tuple are enclosed in parenthesis"()"

# Creating an empty tuple
a=tuple()
print(a)   # empty tuple

a=()
print(a)  #empty tuple


# Creating non empty tuple
a=(1,2,3)
print(a)

a=tuple([1,2,3])
print(a)

a=([1,2],1,'a',{'b':2},{2,3})
print(a)


a=1
print(type(a)) #int
a=(1)
print(type(a))  #int
a=1,2,
print(a)  # (1,2)
print(type(a))  #tuple