# Create a decorator which checks the password provided by user. if the password matches "1234"
# then the user can access the function else show message "your password is invalid"

def login_required(func):
    def inner_func(*args,**kwargs):
        password=input("enter your password ")
        if password=="1234":
            return func(*args,*kwargs)
        else:
            return "invalid password"
    return inner_func

@login_required
def addition(a,b):
    return a+b
print(addition(2,3))

