# Dictionary key has a restrictions that they must be immutable datatype.
# There is no such restriction in dictionary values.

d={'name':"jon",'age':25}  #valid
d={1:"hello",2:"world"}    #valid
e={2.45:1,2.3:3}           #valid
e={(1,2):"hello",(3,2):"world"} #valid

#f={[1,2]:1,[3,2]:4}  # invalid
#f={([1,2],4):5,"name":jon} #invalid