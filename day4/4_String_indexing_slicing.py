#4_String_indexing_slicing.py

#String indexing and slicing is similar to that of list
#forward indexing starts from 0 and reverse indexing starts from -1
message="hello world"
print(message[0]) #h
print(message[3]) #l
print(message[5]) #<space>
print(message[-1]) #d
print(message[-7]) #o
print(message[20]) #index error


#String SLicing
message="hello world"
print(message[:5])  #hello
print(message[0:5])  #hello
print(message[3:])  #lo world
print(message[2:7])  #llo w
print(message[7:2])  # " "
print(message[:-3])  # hello wo
print(message[0:-3])  # hello wo
print(message[-4:])  # orld
print(message[-2:-7])
print(message[-7:-2]) # o wor
print(message[7:-8])  #" "
print(message[-8:7])   #lo w


message="Hello World"
#message[2]='A'  it raises error because we cant change string because stirng is immutable

del message # it delete the message. del can be used for other objects too

del message[2] #only euta euta ni delete garna mildaina

#iterating in string
message="hello world"
for i in message:
    print(i) 
# string comprehension chai hudaina list ma jasto

for i in message[2,-2]:
    print(i)     # range ma ni traverse garna milxa. 

