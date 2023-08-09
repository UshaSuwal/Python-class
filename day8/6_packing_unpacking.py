# Tuples in python can be packed and unpacked


# Packing of Tuple
a=1,2,3,4,'a'
print(a)  #(1,2,3,4)

# Unpacking of Tuple
a,b=1,2 
print(a)    # 1
print(b)    # 2

a,b=(1,2)
print(a)   # 1
print(b)   # 2


# Possible errors in packing and unpacking

# a,b,c=1,2   Not enough value to unpack
# a,b=1,2,3   Too many vslue to unpack
