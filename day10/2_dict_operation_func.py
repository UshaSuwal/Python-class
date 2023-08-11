# Membership Operation
#=> Dictionary membership is checked in keys and not in values
#key ma check garne
student={"name":"jon","age":25}
print("jon" in student)  # False
print("age" in student)  # True
print("name" not in student) # False


######### Built-In Functions ############
student={"name":"jon","age":25}

# len()
print(len(student))   # 2

# sorted()
#=> key lai sort garxa. output in form of list.
result= sorted(student)
print(result)     # ["age","name"]

#str()
result=str(result)
print(result)   # "{"name":"jon","age":25}"
#=>  string banaidinxa dictionary lai

# all(sequence)
# all() function takes only one parameter and that should be iterable.
# all the element inside the iterable must be truthy for all() to return true.
data_list=[1,"hello",[1,2]]
result=all(data_list)
print(result)  # True because all element in data_list are truthy

result=all([1,2,0])
print(result)  # False   because 0 is falsy

# But there is one exception in all()
result=all([])
print(result)   #True


#any(sequence)
# any( ) function also takes only one parameter and that should be iterable
# any one element inside the iterable must be truthy for all() to return true.
data_list=[0,"hello",[1,2]]
result=any(data_list)
print(result)    # True

result=any([1,0, False])
print(result) # True

result=any([],0)
print(result)  #False
