# Accessing elements of dictionary is similar to that of list. In list, we put numbers for indexing
# and in dictionary we put "keys" for indexing

student={"name":"ram","age":23,"address":"ktm"}
name=student["name"]
print(name)                # ram
print(student["age"])      # 23
print(student["address"])  # ktm
#print(student["phone"])   keyError

# We can also access dictionary values using get() method
student={"name":"ram","age":23,"address":"ktm"}
name=student.get("name")
print(name)    # ram

print(student.get("phone"))   # None  Its doesn't raise error


# Adding a key-value pair in dictionary
student={"name":"ram","age":23,"address":"ktm"}
student["phone"]=98767777
print(student)    # {"name":"ram","age":23,"address":"ktm","phone":98767777}


other_info={"email":"a@.com","roll":13}
student.update(other_info)
print(student)   # {"name":"ram","age":23,"address":"ktm","phone":98767777,"email":"a@.com","roll":13}

student["name"]="jon"
print(student)   # {"name":"jon","age":23,"address":"ktm","phone":98767777,"email":"a@.com","roll":13}



# Removing Key-value pair from a dictionary
#pop()
student={"name":"jon","age":23,"address":"ktm","phone":98767777,"email":"a@.com","roll":13}
email=student.pop("email")
print(email)     # a@.com
print(student)   # {"name":"jon","age":23,"address":"ktm","phone":98767777,"roll":13}

#institution=student.pop("institution")  it raises KeyError
institution=student.pop("institution","Broadway")
print(institution)    #Broadway

#popitem()
# last item matra pop garxa
student={"name":"jon","age":23,"address":"ktm","phone":98767777,"email":"a@.com","roll":13}
result=student.popitem()
print(result)  # "roll":13
print(student) # {"name":"jon","age":23,"address":"ktm","phone":98767777,"email":"a@.com"}

#clear()
student.clear()
print(student)   # {}
