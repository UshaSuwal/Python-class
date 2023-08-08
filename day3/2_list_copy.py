a=[1,2,3]
b=a
print(a)
print(b)
print(a is b)  # O= True   a and b refer same memory so a ma change garda b ma pani hunxa

c=a.copy()
print(a)
print(c)
print(a is c)  # O= False   a and c refer diff memory so a ma change garda c ma pani change hudaina
               # all element are immutable so change hudaina tara immutable element xa vane change hunxa ie shallow copy

#shallow copy
a=[[1,2,3],4,5]
b=a.copy()
a[0][1]=7
print(a)   #O=[[1,7,3]4,5]
print(b)   # same output as a
# even if 'b is copy of 'a', if we change any object inside 'a' then the change is also reflected in'b'.this is shallow copy

# deepcopy
from copy import deepcopy
a=[[1,2,3],4,5]
b=deepcopy(a)
a[0][1]=7
print(a)    #O=[[1,7,3],4,5]
print(b)    #O=[[1,2,3],4,5]    
# a ma change garda b ma  hudaina