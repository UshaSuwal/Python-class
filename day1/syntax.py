
###IDENTIFIER###
 #-Any name of variable, function or class provided by user is identifier
 #-Rules of naming identifier:
#  1. identifier are case sensitive.ie a=1 and A=1 are different
#  2. identifier cant be python keywords.
#  3. identifier name can have A-Z, a-z 0-9 and _
#  4. BUT cant start with digit(0-9) and cant use any special symbols(@,$,#)

import keyword
name="usha"
print(keyword.iskeyword("name"))     #to check if it is keyword or not
print("name".isidentifier())         #to check if it is identifier or not

#Python statement
#-each line in a python code is an statement
#- we can separate multiple statement in same line using ';'
#- we can also use "\" for line continuation

message="hello world"
msg1="hello"; msg2="world"
mess="hello\
world"
print(message, msg1, mess)



###INDENTATION###
#it is imp for code representation
#IN C:
   #if(a=1){
   # print("a=1")
   # }

# IN python
a=1
b=2
if(a==2):
    print("this is a")
    if(b==2):
        print("this is b")
    print("this is outside the b")
print("this is outside")
