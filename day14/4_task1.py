# Create a function that takes a text message and simply return text message.
# Create a decorator which changes the text into the upper case text.

def to_upper_case(func):
    def inner_func(*args,**kwargs):
        result=(func(*args,**kwargs))
        if type(result)!=str:
            return result
        return result.upper()
    return inner_func

@to_upper_case
def message(txt):
    return txt
print(message("hello world"))
print(message(2))


