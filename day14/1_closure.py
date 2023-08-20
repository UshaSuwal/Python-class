# Closure is a concept in python which fulfills the following:
#1. There should be a nested function(a function inside another function)
#2. An inner function must reference the argument from outer function.
#3. Outer function should return the inner function.

def closure_func(msg):
    def inner_func():
        print(msg)
    return inner_func
result=closure_func("hello world")    # result=inner_func
result()  # it will call inner_func()

# The above function is the simplest closure that can be made in python. 
# Closure are the basis of decorators in python

