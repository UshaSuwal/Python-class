#Strings are the immutable datatypes in Python
#THey are sequencial datatypes(iterable)

#Creating empty string
a=""
b=''
c="""
"""            # c and d are docstring or triple-quoted string
d='''
'''            
e=str()        #str is built-in function

#Quote characters
message=" i'm learning python "  #double quote outside and single quote inside
#message=' i'm learning python '  this raises error
message=' "He said, python is awesome" '  #single quote outside and double quote inside
#message=""He said, python is awesome"" this raises error

#but we have the feature of escspe sequence in python if we want to use single quote both inside outside
message=' I\'m learning python'
message="He said,\"python is awesome\""
print(message)

#escape sequence suprresses the usual meaning of character and gives new meaning
#\',\",\n,\t etc are escape sequence
print("hello\nworld")
print("hello\tworld")




##### Triple quoted String #####
# Triple quoted strings can be used as docstring. we can write doc for function and classes using triple quoted string
#it is also used for multi line comments
#it is also used to store variables like regular string

def addition(a,b):
    """
    This is a function to add two integer
    """
    return a+b
print("sum=",addition(2,5))
print(help(addition))    # display description 

a="""nekjcflskdnfs.kvn dse
ekmflksdnflsw
kwnfklwdfn
jnkjbj
"""
print(a)