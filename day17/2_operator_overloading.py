# Each operator in Python has it's own magic method which is called when the operation is carried out.
# Magic methods in python are the special methods created by using double underdcore "__"
# __add__(), __mul__(), __sub__(), __gt__() etc are some example of maguc methods

a=1
b=2
result=a+b   # this + operator calls magic method ie __add__()
print(result) #3

result=a.__add__(b)  
print(result)  #3

# So, everytime an operation is carried out, a magic method is called.
# Magic methods are also called as dunder methods(double underscore)