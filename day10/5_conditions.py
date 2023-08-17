# Conditions are used for making decisions in a program
# There are four variables of conditions we can create.

#1. Simple if
#2. if...else condition
#3. if...elif...else ladder
#4. nested if

# In the if conditions, the statement after the "if" is checked. If the statement is truthy then the
# condition is satisfied and the block inside the "if" is executed. Otherwise it is not executed.

# Simple if
a=20
if a>15:
    print("the number is greater than 15")

a=20 
if a:   # a is truthy value so vitra run hunxa
    print(f"the number is {a}")   

#if...else
a=20
if a>15:
    print("the number is greater than 15")
else:
    print("The number is less than 15")


if a:   # a is truthy value so vitra run hunxa
    print(f"the number is {a}")
else:
    print("the number is 0")


# if..elif..else ladder
mark=76
if mark>=80:
    print("distinction")
elif mark>=65:
    print("first division")
elif mark>=55:
    print("second division")
elif mark>=40:
    print("third division")
else:
    print("fail")


# nested if
a=20
if a>10:
    if a>15:
        print(f"{a} is greater than 15")
    else:
        print(f"{a} is just greater than 10")
else:
    print(f"{a} is less than 10")


# ternary if
# one liner conditions are called ternary if
a=10
b=5

#simple if:
if a>b:
    print("a is greater")
else:
    print("b is greater")

#ternary if:
print("a is greater") if a>b else print("b is greater")
