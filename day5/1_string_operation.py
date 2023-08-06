#concatenation
#we can concatenate string using + operator
m1="hello"
m2="world"
print(m1+m2)   #helloworld

# Repetition/ Broadcast operation
#broadcast in string in string is done using * operator
m="hello"
print(m*3)  #hellohellohello
print("m"*4)


# Membership Operation
print('m' in 'message')  #True
print('e' not in "message") # False


### Built- in Function ##

#1. len()
#it gives length (total number of element) of sequencial datatypes ie list, string, tuple etc
message="hello world"
print(len(message))

#2. type()
#it return the type of an object
print(type(message))

#3. slice()
#this function is similar to string and list slicing
message="hello world"
slice_data=slice(2,7)
print(message[slice_data])    # llo w


#4. map
#5. bool()