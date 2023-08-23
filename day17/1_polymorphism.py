# Polymorphism in Python refers to many forms of the same functions or objects.
# sum(), len(), max(), min(), etc are some of the examples which follows polymorphism.
# These built-in functions can take different datatypes and performs their respective tasks.
# There are two important aspects of Polymorphism:
#1. Function / Method overloading
#2. Operator overloading


# Function / method overloading

def addition(a,b):
    return a+b

def addition(a,b,c):
    return a+b+c

#result=addition(1,2)     3 ota parameter khojeko tara 2 ota pathayo vanera error aauxa
#print(result)
result=addition(1,2,3)
print(result)
# Though addition() is defined twice, only the latest definition is considered.
# So, Python does'nt support function overloading



# But we can give default argument so that we can pass both two and three arguments in function call
def addition(a,b,c=0):
    return a+b+c

result=addition(1,2)  
print(result)
result=addition(1,2,3)
print(result)


# same as for method in class
class Employee:
    salary=1200
    def description(self):
        return self.salary
    def description(self):
        return f"salary={self.salary}"
e=Employee()
print(e.description())   # The last definition is considered so the result is salary=1200