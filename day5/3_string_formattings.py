# we do string formatting using f-string
PL="Python"
message=f"i am learning {PL}"   # i am learning Python
print(message)

a=input("enter a language ")   #a=java 
message=f"i am learning {a}"   # i am learning java
print(message)


name="jhon"
age=2
print(f"i am {name} and i am {age} years old")   # new way of formatting
print("i am %s and i am %d years old"%("john",23))  # purano tarika

name="jhon"
age=int(input("enter a age"))   # input lida string input linxa so int rakhnu parxa
print(f"i am {name} and i am {age} years old") 

print("i am this {} and i am {} year old".format(name,age))
print("i am this {1} year old and i am {0}".format(name,age))

