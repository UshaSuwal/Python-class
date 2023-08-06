# True and False are boolean datatype in python. Keywords "True" and "False" are used to represent true and false state respectively.

###Operations that give Boolean type##
#1 Comparison Operation
a=5
b=3
print(a>b)
print(a>=b)
print(a==b)
print(a<b)
print(a<=b)
print(a!=b)

#2 Logical Operation
a=5
b=3
print(a>b and b!=a)
print(a>b or a!=b)
print(not True)
print(not False)
print(not a)


#3 Membership Operation
print(1 in [1,2,3])
print(3 not in [1,2,3])


# Identity Operation
a=1
b=1
print("here",a is b)
print(id(a) == id(b))
print(a is not b)
print(id(a)!=id(b))

#####Concept of Truthy and falsy#####
a=5
print(not a)  # false
# any non empty or non zero datatype including True itself is Truthy datatype
#egs:5,1,-1,[1,2],{2,3,'a'},{"a":3}, True  -> TRUTHY DATA TYPES

# all empty datatypes,zero,none, including False are Falsy datatypes
#egs: 0,[],{}, set(),(),'',None, False   -> FALSY DATA TYPES

#How can we verify data is Truthy or Falsy?

#check for TRUTHY
a=5
b=1
c=-1
d=[1,2]
e={2,3,'a'}
f={"a":1}
g="hello"
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print(bool(g))

#Applying not operation to any truthy value results False
print(not a)

# check for Falsy
a=0
b=[]
c=()
d={}
e=set()
f=None
g=False
h=''
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(e))
print(bool(f))
print(bool(g))
print(bool(h))
print(bool())       # null bool is also falsy

#Applying not operation to any Falsy value results True
print(not f)



####Python Boolean is sub-class of Integer####
#True is integer 1
#False is integer 0
print(True+1)  #2
print(70*False) #0
print(True+True) #2