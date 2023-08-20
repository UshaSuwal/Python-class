# Decorators are the function that add extra functionality to existing function.

def decorate_me(func):
    def inner_func():
        print("i am the extra functionality")
        return func()
    return inner_func


def message():
    print("Hello world")
result=decorate_me(message)  # result=inner_func
result() # it calls inner_func()

#using decorator:
@decorate_me
def message():
    print("Hello world")
message()



