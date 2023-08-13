# Loops are used to execute certain blocks of code repeatedly.
# They are used to reduce manual efforts in the algorithm.

# For loops in python with different datatypes.
vowels=['a','e','i','o','u']
for i in vowels:
    print(i)
else:
    print("this is executed if the main loop is compeletely iterated")


# Looping is simialr to list, tuple and set.

# Let's see how is it done in a dictionary
student={'name':"jane","age":25,"address":"ktm"}

# looping in dictionary keys
print(student.keys())  # Dict_keys=(['name','age','address'])
for key in student.keys():
    print(key)

# looping in dictionary values
print(student.values())   # Dict_values=["jane",25,"ktm"]
for values in student.values():
    print(values) 

#looping through both dictionary keys and values
print(student.items())  # Dict_items= ([("name","jane"),("age",25),()"address","ktm)"])
for key,value in student.items():   #key,value->unpacking gareko tuple lai
    print(key)
    print(value)
