# Dictionary are the mutable datatypes in python in key-value pair format

# Creating an empty dictionary
a=dict()
print(a)  # empty dictionary
a={}
print(a)  # empty dictionary


# Creating non empty dictionary
student={"name":"Ram","age":5,"address":"ktm","mark":[1,2,4],"total":{2,3,4},"mark1":(1,2,5)}
print(student)

student=dict(name="john",age=23,address="ktm")
print(student)   # {"name":"john","age":23,"address":"ktm"}

data={"phone number":999999}
data=dict(phone_number=99999)

data=({"name":"Ram","age":5,"address":"ktm"})