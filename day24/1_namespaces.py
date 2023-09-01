# Namespaces determine the scope of the veriable and objects in Python.
# There are 4 types of namespaces
#1. Local scope
#2. Enclosed scope
#3. Global scope
#4. Built-in scope


# Built-in scope
# If the scope of a package or object is all over the project then it is an object of built-in scope.
# Example: Python built-in libraries like math,json,os etc
#egs:  import math


# GLobal scope
# The scope of the variable or object is limited to one python  module then it has a global scope to that module
# a=12 , This "a" cant be used in next python file. it is limited to this python file only.


# Local scope
# If the variable scope is limited to a function then it has local scope.

a=12    # Global scope
def test_func():
    a=20      # Local scope
    print(a) #20
print(a)    # 12
test_func()
print(a)    #12



# Enclosed scope
# If the scope of the variable or object is limited to a nested function then it has an enclosed scope.

a=12
def outer_func():
    a=20
    def inner_func():
        a=30     # enclosed scope
        print(a)   #30     if a=30 vetena vane ek step baira janxa and take a=20 and a=20 ni vetena vane again ek step baira janxa and take a=12
    inner_func()
    print(a)     #20

print(a)   #12
outer_func()
print(a)   #12

# We have a "global" keyword which can define even a local variable as a global
a=20
def outer_func():
    global a
    a=40     # global a nai change gardeko
    def inner_func():
        a=30
        print(a)    #30
    inner_func()
    print(a)  #40

print(a) #20
outer_func()
print(a)  #40

# non-local keyword
a=20
def outer_func():
    a=40    
    def inner_func():
        nonlocal a     # non local means function tira locally used vayeko lai matra change gardinxa.
        a=30
        print(a)    #30
    inner_func()
    print(a)  #30     # so yeta 30 aayeko.    non-local le func vari ko lagi matra global banaidinxa.

print(a) #20
outer_func()
print(a)  # 20
