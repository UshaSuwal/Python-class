# Exceptions in Python can be handled using try...except block

try:
    num=int(input("ENter a number"))
except:
    print("Something went wrong")

# We can specify the error type in the except statement to catch the specific type of error 
try:
    num=int(input("ENter a number"))
except ValueError:     #except paxi error statement rakhnu is good
    print("Please enter a valid number")

# We can catch multiple exception using the same except block
try:
    num=int(input("enter a number "))
except(ValueError,KeyError,TypeError):
    print("Please enter a valid number and perform your operation properly")


try:
    num=int(input("enter a number "))
except ValueError:
    print("Please enter a valid number")
except TypeError:
    print("Please check your operation")


# try...except else.. finally block
# else block is executed when no error occurs in the try block
# finally block is always executed no matter there is an error or not.
try:
    num1=int(input("Enter first number "))
    num2=int(input("Enter second number "))
except ValueError:
    print("Please enter a valid number")
else:
    add=num1+num2
    sub=num1-num2
    prod=num1*num2

# except run vo vane else run hudaina
# try block ma error aauna sakne code matra rakhne
# error aayena vane else block run hunxa

try:
    num1=int(input("Enter first number "))
    num2=int(input("Enter second number "))
except Exception as a:
    print(a)   # error nai print garauna
    print("Please enter a valid number")
else:
    add=num1+num2
    sub=num1-num2
    prod=num1*num2
finally:
    print("This block is always executed")   # error aayeni na aayeni run hunxa