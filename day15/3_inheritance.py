# Inheritance is the process of accessing the attributes of Parent class by children classes
# Types of inheritance in python:
#1. Single inheritance
#2. Multiple inheritance
#3. Multilevel inheritance
#4. Hierarchical inheritance
#5. Hybrid inheritance

## Single Inheritance
class A:
    a=2
class B(A):   # here B is child which inheriting A
    pass
obj=B()
print(obj.a)  #2


## Multiple Inheritance
class A:
    a=3
class B:
    a=5
class C(A,B):   # child C is inheriting multiple class ie A and B
    pass
obj=C()
print(obj.a)  # 3


## Multilevel Inheritance
class A:
    a=5
class B(A):
    a=10
class C(B):
    pass


## Hierarchical Inheritance
class A:
    a=5
class B(A):
    pass
class C(A):
    pass


## Hybrid Inheritance
# it is the combination of multiple and hierarchical inheritance
class A:
    a=3
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
class E(D):
    pass

obj=E()
print(E.mro())

# MRO => It stands for Method Resolution Order. 
# It is the order in which attributes in an inheritance is accessed from the child class
