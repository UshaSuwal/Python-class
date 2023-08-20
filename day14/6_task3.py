import time
print(time.time())

#Create a decorator which calculates the amount of time that it took to execute a function.

def calculate(func):
    def inner_func(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"execution time={end-start}")
        return result
    return inner_func


@calculate
def message(txt):
    for i in range(100000000):
        continue
    return txt
print(message("hello"))









