# order of the arguments is important to note.
# Arguments are the value passed during function call and parameters are the values taken 
# in function definition.


# Order of the Arguments.
#1. Positional/Compulsory arguments
#2. Default arguments
#3. Arbitary arguments

def addition(a,b):  # here a and b are positional arguments. a ra b ma value pathaunai parxa.
    return a+b

print(addition(2,3))

def add(a,b,c=10):  # here a and b are positional arguments and c is default argument.
    return a+b

print(add(2,3))    #print(add(2,3,5)) pathayo vaney c=5 nai linxa.

#print(add(2,3,5)) pathayo vaney c=5 nai linxa. here c=5 override c=10
#if we send value in the function call then the calue always gets override.

#print(add(a=2,b=3,c=5))   valid
#print(add(2,b=3,5))        invalid
##print(add(2,3,c=5))  here c is keyword argument


# Arbitary Arguments
# arbitary arguments can take random number of elements in the function call.
# They are like expandable bucket.
def addition(*args):
    print(args)
    print(type(args))
    return sum(args)


print(addition(1,2))    #(1,2)
print(addition(1,2,3,4)) #(1,2,3,4) ,they are function

def addition(**kwargs):
    print(kwargs)
    print(type(kwargs))
    return sum(kwargs.values())

print(addition(a=1,b=2,c=3))

#arbitary arguments also have their own order. *args should always come before than **kwargs
def addition(a,b,c,d=1,e=2,f=3,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(args)
    print(kwargs)
    return a+b+c+d+e+f+sum(args)+sum(kwargs.values())

print(addition(1,2,3,4,5,6,12,13,14,p=5,q=6))
    






