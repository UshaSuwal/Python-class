# Take two numbers as input and add those numbers. Handle the possible exceptions.
try:
    num1=int(input("Enter a first number "))
    num2=int(input("Enter a second number "))
except ValueError:
    print("Please enter valid number")
else:
    print(num1+num2)

# Take two numbers input and divide a number by another number. Handle the possible exceptions.
try:
    num1=int(input("Enter a first number "))
    num2=int(input("Enter a second number "))
    a=num1/num2
except ZeroDivisionError:
    print("Please enter valid number")
else:
    print(a)




