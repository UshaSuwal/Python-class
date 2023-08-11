student={"name":"jon","age":25}
student1=student.copy()
print(student)     #{"name":"jon","age":25}
print(student1)    #{"name":"jon","age":25}

# get()
student={"name":"jon","age":25}
name=student.get("name")
print(name)  # jon

name=student("name")
print(name)    # jon

roll=student.get('roll')  # None
# roll=student['roll']    Error

roll=student.get('roll',5)
print(roll)   # 5

name=student.get("name","jane")
print(name)   # jon


# items()
student={"name":"jon","age":25}
print(student.items())   # dict_items[("name","jon"),("age",25)]  (list chai haina)

#keys()
student={"name":"jon","age":25}
print(student.keys())  #dict_keys(["name","age"])

# values()
student={"name":"jon","age":25}
print(student.values())  #dict_values(["jon",25])

