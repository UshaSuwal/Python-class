####OPERATORS####
#operators are symbol in pyhton or in any programming language that carry out arithmetic and logical operations
#the python operators are :
#1. Arithmetic operators
#2. Relational operators
#3. Logical operators
#4. membership operators
#5. idientity operators
#6. assignment operators

###ARITHMETIC###
a=6
b=2
print(a+b)  #here + is arithmetic addition operator
print(a-b) 
print(a*b)
print(a/b)
print(a%b)  # % (modulus operator gives remainder of division operation)
print(a**2)  # **(power)

# Floor division
#this operator omits the decimal vslues from the decimal operation and gives floor value
print(3//2) #outout: 1
print(-3//2) #output: -2



###RELATIONAL OR COMPARION###
# ==, <, >, >=, <=, != are the relational operators.
#it gives boolean result ie either TRUE or FALSE
print(a==b)
print(a>b)
print(a<=b)
print(a!=b)



###LOGICAL OPERATOR###
# and, or, not are the logical operators
print(a>b or b!=a)
c=5
print(not c)   #(all empty and non zero are true). concept of truthy and falsy



###ASSIGNMENT OPERATOR###
# =(is equals to)
a=2+3  #sum is assigned to a 
a+=1   # += also first sum and then assign. similarly for all operators like -=, /=, *=, %=.



###MEMBERSHIP OPERATOR###
# in , not in are membership operator
#sequence dataset ma xa ki xaina herxa
#we can use membership operator in sequence datatypes
print(2 in [1,2,3])  # output:TRUE        []-list   -> mutable(change garna milxa)
print(3 not in (1,2,3))  # output: False  ()-tuple  -> immutable(change garna mildaina)
print('p' in "python")    #output: True



###IDENTITY OPERATOR###      (memory)
# is, is not are identity operator
# variable le eutai object refer garira xa vane true aauxa
# eutai memory location ma  xa or xaina herxa
a=[1,2,3]
b=a
print(a is b) #output=true  here a and b both refer the same memory location
print(id(a)==id(b)) #output=True  id le memory location dekhauxa

c=a.copy()
print(a is c)  #output=false  here a and c have same value but are not in same memory location



                          ####PRECEDENCE AND ASSOCIATIVITY####
#if an operation has multiple operators then precedence define the order of operator
# if multiple operator have same precedence then it apply associativity.
#Normally all operator have left-right associativity except power(**)
print(2*3/3) # * and / have same precedence. so through associativity it operates from left to right ie first * then /
print(2**3**2) #power(**) so associativity is from right-left

